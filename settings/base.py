import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'key034950kjhkjhkjhu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['myapp.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'social_django',
    'social.apps.django_app.default', # python-social-auth
    'oauth2_provider',
    'rest_framework',
    'rest_framework_social_oauth2',

    'accounts',
    'budget',
    'contacts',
    'diary',
    'password',
    'todo',
    'task',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
        'DIRS': [os.path.join(BASE_DIR, 'todo', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social.apps.django_app.context_processors.backends',       # python-social-auth
                'social.apps.django_app.context_processors.login_redirect', # python-social-auth

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (

    # Django
    'django.contrib.auth.backends.ModelBackend',

    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',

    'social_core.backends.github.GithubOAuth2',

    # # Facebook OAuth2
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',

    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',

)

# User model
AUTH_USER_MODEL = 'accounts.OrganizerUser'
SOCIAL_AUTH_USER_MODEL = 'accounts.OrganizerUser'

LOGIN_REDIRECT_URL = '/'        # Redirect path after Login
LOGIN_URL = '/acc/login/'
LOGOUT_URL = '/acc/logout/'     # Redirect path after Logout

# SOCIAL_AUTH configuration
SOCIAL_AUTH_LOGIN_ERROR_URL = '/accounts/login-error/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

# Facebook configuration developers.facebook.com
SOCIAL_AUTH_FACEBOOK_KEY = '1941904676136083'
SOCIAL_AUTH_FACEBOOK_SECRET = 'f3bfc8c5f7d125186a379cc733f41326'
# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from facebook.
# Email is not sent by default, to get it, you must request the email permission:
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'name, email'}

# Google configuration developers.google.com
SOCIAL_AUTH_GOOGLE_KEY = '870374304466-mntnl7obbg1ok09jujq915e03q3q74en.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_SECRET = 'T-82D89sXjiMYE2FhgPmPNI1'

# GitHUB configuration github.com/settings/developers
SOCIAL_AUTH_GITHUB_KEY = '4605b9332d9a03eca134'
SOCIAL_AUTH_GITHUB_SECRET = '883bbb40d1bd4082b867a4950783fe642eee1207'

# Twitter configuration apps.twitter.com
SOCIAL_AUTH_TWITTER_KEY = 'tq328SxBckRKIabef8bAElWWn'
SOCIAL_AUTH_TWITTER_SECRET = 'yafk1bOOA18GkLabk7tY9WlruIKexVwvwSLRAdNBUcGIMYVDzr'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# WSGI
WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'organizer.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
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

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'files', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'files', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# REST Settings
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'accounts.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
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
    )
}
