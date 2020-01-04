
import os, sys
import django
from django.db import models
from django.conf import settings
from django.core.management import call_command
INSTALLED_APPS = ['djangotest',]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '../../../output/db.sqlite3',
    }
}
settings.configure(
    DATABASES=DATABASES, 
    INSTALLED_APPS=INSTALLED_APPS,
    USE_I18N=True)
django.setup()
call_command('makemigrations', 'djangotest')
call_command('migrate', 'djangotest')

from djangotest.models import Password
p = Password(website='example.com', username='hello-01', pwd='12345678')
#p.save()
objs = Password.objects.all()
for obj in objs:
    print(obj)
    print(obj.id, obj.website, obj.username, obj.pwd)