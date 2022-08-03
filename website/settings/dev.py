from .base import *
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ddni5lfdkfi68p',                      
        'USER': 'coaltklgsrjxms',
        'PASSWORD': '08fe73356edf6ffd2ed80dabc51404faeee88b2a96de642b46155ea85f9a4c22',
        'HOST': 'ec2-54-208-104-27.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
