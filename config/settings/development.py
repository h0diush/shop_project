import os

from .base import *

SECRET_KEY = env.str("SECRET_KEY")
ALLOWED_HOSTS = env.str("ALLOWED_HOSTS", default="").split(" ")
DEBUG = env.bool("DEBUG", default=False)

# CART_SESSION_ID = 'cart'

LOCAL_APPS = [
    'api.apps.ApiConfig',
    'cart.apps.CartConfig',
    'common.apps.CommonConfig',
    # 'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'shop.apps.ShopConfig',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

EMAIL_BACKEND = env.str('EMAIL_BACKEND')
EMAIL_HOST = env.str('EMAIL_HOST')
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": env.str("PG_DATABASE", "postgres"),
#         "USER": env.str("PG_USER", "postgres"),
#         "PASSWORD": env.str("PG_PASSWORD", "postgres"),
#         "HOST": env.str("DB_HOST", "localhost"),
#         "PORT": env.int("DB_PORT", 5432),
#     },
#     "extra": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     },
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
