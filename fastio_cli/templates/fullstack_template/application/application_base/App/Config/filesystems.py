# Here you may specify the default filesystem disk that should be used
import os
from .app import settings

default = os.getenv('FILESYSTEM_DRIVER', 'local')

drivers = {
    'local': {
        'root': settings.STORAGE_PATH,
    },
    's3': {
        'driver': 's3',
        'key': os.getenv('AWS_ACCESS_KEY_ID'),
        'secret': os.getenv('AWS_SECRET_ACCESS_KEY'),
        'region': os.getenv('AWS_DEFAULT_REGION'),
        'bucket': os.getenv('AWS_BUCKET'),
        'url': os.getenv('AWS_URL'),
        'endpoint': os.getenv('AWS_ENDPOINT'),
    },
}

