from django.contrib.auth.models import AbstractUser
from django.db import models

from social_django.utils import load_strategy

import requests
import logging

logger = logging.getLogger(__name__)

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key = True)
    full_name = models.CharField(max_length = 105)

    @property
    def short_name(self):
        return self.username
    def __str__(self):
        return self.full_name
    def empty_fields(self):
        list = []
        for field in User._meta.fields:
            list.append((field.value_from_object(self),field))
        return list
    def api_request(self, url, params={}, refresh=True):
        s = self.get_social_auth()
        params.update({"format": "json"})
        params.update({"access_token": s.access_token})
        r = requests.get(
            "https://ion.tjhsst.edu/api/{}".format(url),
            params = params,
        )
        if r.status_code == 401:
            if refresh:
                try:
                    self.get_social_auth().refresh_token(load_strategy())
                except BaseException as e:
                    logger.exception(str(e))
                return self.api_request(url, params, False)
            else:
                logger.error(
                    "Ion API Request Failure: {} {}".format(r.status_code,
                                                            r.json()))
        return r.json()

    def get_social_auth(self):
        return self.social_auth.get(provider = "ion")
