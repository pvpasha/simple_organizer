import os

from datetime import timedelta


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'O97L9FEPi8XuIoAE4xFT437zm06yXI0GwS8Gyme7YOzvqVQgFfsoNp09DKacQtcuIL8lS4gYAw9h6kMs6F9m'

DEBUG = True

ALLOWED_HOSTS = ['sp-lutsk.com', 'www.sp-lutsk.com', 'localhost', '46.101.125.168', '127.0.0.1']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_social_oauth2',     # oauth2
    'rest_social_auth',
    'social_django',
    'sorl.thumbnail',
    'oauth2_provider',                  # oauth2
    'corsheaders',

    'accounts',
    'budget',
    'contacts',
    'diary',
    'password',
    'task',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'accounts.OrganizerUser'
# SOCIAL_AUTH_USER_MODEL = 'accounts.SocUser'


# Facebook configuration developers.facebook.com
SOCIAL_AUTH_FACEBOOK_KEY = '1941904676136083'
SOCIAL_AUTH_FACEBOOK_SECRET = 'f3bfc8c5f7d125186a379cc733f41326'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'id, name, email'}

# Twitter configuration apps.twitter.com
SOCIAL_AUTH_TWITTER_KEY = 'tq328SxBckRKIabef8bAElWWn'
SOCIAL_AUTH_TWITTER_SECRET = 'yafk1bOOA18GkLabk7tY9WlruIKexVwvwSLRAdNBUcGIMYVDzr'
SOCIAL_AUTH_TWITTER_SCOPE = ['email']

# Google configuration console.developers.google.com
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '870374304466-mntnl7obbg1ok09jujq915e03q3q74en.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'T-82D89sXjiMYE2FhgPmPNI1'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]

# GitHUB configuration github.com/settings/developers
SOCIAL_AUTH_GITHUB_KEY = '4605b9332d9a03eca134'
SOCIAL_AUTH_GITHUB_SECRET = '883bbb40d1bd4082b867a4950783fe642eee1207'

# LinkedIn configuration linkedin.com/developer/apps
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '86upih6mvan2z2'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'WqOkSGrE3cR5zVID'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_SELECTORS = ['email-address', 'headline', 'industry']
SOCIAL_AUTH_LINKEDIN_OAUTH2_DATA = [('id', 'id'),
                                    ('firstName', 'first_name'),
                                    ('lastName', 'last_name'),
                                    ('emailAddress', 'email_address')]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)


WSGI_APPLICATION = 'wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'organizer.sqlite3')
        }
    # {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'organizer.sqlite3')
    # }
    # {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': os.environ['POSTGRES_DB'],
    #     'USER': os.environ['POSTGRES_USER'],
    #     'PASSWORD': os.environ['POSTGRES_PASSWORD'],
    #     'HOST': os.environ['POSTGRES_SERVICE'],
    #     'PORT': os.environ['POSTGRES_PORT']
    # }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

# DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_ROOT = os.path.join(BASE_DIR, 'files', 'media')
MEDIA_URL = '/media/'
AVATAR_DIR = os.path.join(MEDIA_ROOT, 'avatar')


STATIC_ROOT = os.path.join(BASE_DIR, 'files', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'accounts.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}


JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'accounts.views.jwt_response_handler_user',          # Handler that make token and response

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': timedelta(days=1),           # default seconds=300 (5min)
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': True,                              # /api-token-refresh/ True or False
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=1),      # default days=1

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,

}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# 'django.core.mail.backends.console.EmailBackend'
# EMAIL_FILE_PATH = '/tmp/app-messages' # for 'console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'organizer2018.new@gmail.com'
EMAIL_HOST_PASSWORD = 'adminadmin123!'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = 465
# EMAIL_TIMEOUT =

# SERVER_EMAIL = 'pv.pasha.pv@gmail.com'    # 'django@my-domain.com'

ADMINS = (
    ('Pasha M', 'pv.pasha.pv@gmail.com'),
)


CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = (
#     'google.com',
#     'hostname.example.com',
#     'localhost:8000',
#     '127.0.0.1:9000'
# )

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                      '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y/%m/%d %H:%M:%S",
        },
        'simple': {
            'format': '%(asctime)s: %(levelname)s >> %(message)s',
            'datefmt': "%m/%d %H:%M:%S",
        },
    },
    'filters': {
        'debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/log.txt',
            # 'maxBytes': 1024 * 1024 * 5,  # 5 MB
            # 'backupCount': 10,
            'formatter': 'simple',
            'filters': ['debug_true'],
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
            'filters': ['debug_true'],
        },
        'mail_admins': {
            'level': 'WARNING',
            'filters': ['debug_true'],
            'class': 'django.utils.log.AdminEmailHandler'
            # 'include_html': True,
            # 'email_backend': 'django.core.mail.backends.filebased.EmailBackend',
        },
    },
    'loggers': {
        'accounts': {
            'handlers': ['mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        '': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
