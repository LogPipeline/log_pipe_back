from .common import * 


DEBUG = True # SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["http://0.0.0.0:8080", "http://127.0.0.1:8000", "http://0.0.0.0:8081"]



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_DATABASE'),
        'USER': os.getenv('DB_USERNAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': '3306'
    },
}

REST_FRAMEWORK={
    ###'NON_FIELD_ERRORS_KEY': 'error',###  요거 제외밑에부터       
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static")
# ]
STATIC_ROOT = os.path.join(BASE_DIR, "static")