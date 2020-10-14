# Study Bank

## Development

- clone the git repo
- create `settings/secret.py` based on `settings/secret.sample`
- register an OAuth app with Ion for authentication (client-type = confidential, auth-grant-type = authorization-code)
- copy the client_id for SOCIAL_AUTH_ION_KEY and client_secret for SOCIAL_AUTH_ION_SECRET from Ion to `settings/secret.py`
- edit `settings/__init__.py` so that `MEDIA_ROOT` and `STATIC_ROOT` point to your desired directories (you also need to create these directories)
- uploaded documents will be stored in the media directory, and static files will be collected to the static directory
- django will not serve any files in either of these directories, so you need to make sure your web server will
