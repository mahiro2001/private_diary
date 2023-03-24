import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s#gkx$y2o9)9a^gz2igcweoeupzx=5hm=0vh)_(phr$5-&t%t@'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'private_diary',
        'USER':os.environ.get('DB_USER'),
        'PASSWORD':os.environ.get('DB_PASSWORD') ,
        'HOST':'',
        'PORT':'',
    }
}