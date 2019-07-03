#flake8: NOQA    #告诉PEP8这个文件不需要检测
from .base import *    #NOQA   告诉PEP8检测工具这个地方不需要检测

DEBUG=True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}