from django.core.management.base import BaseCommand, CommandError
import csv
from studyguides.apps.courses.models import Tag

class Command(BaseCommand):
    help = 'upload tags from csv'

    def add_arguments(self, parser):
        parser.add_argument('filename')
    
    def handle(self,*args,**kwargs):
        try:
            with open(kwargs['filename']) as tagfile:
                tag_reader = csv.reader(tagfile, delimiter=',')
                for row in tag_reader:
                    name = row[0].strip()
                    url = row[1].strip()
                    tag = Tag.objects.get_or_create(name=name,url=url)[0]
                    tag.save()
        except OSError as ex:
            raise CommandError(str(ex)) from ex
        
        
