"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)@+b)eh5_o*uo7)h@!@l9n-i7t&^zqw2hgxmor@gr-un#jf+rc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Definition of the custom user model
AUTH_USER_MODEL = 'users.CustomUser'

# Application definition
INSTALLED_APPS = [

    'users',
    'articles',
    'homepage',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'crispy_bootstrap5',
    'widget_tweaks',
    'tinymce',
    'taggit',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'allauth.account.middleware.AccountMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'users.models.anonymous_user_middleware.AnonymousUserMiddleware',
]


ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR.parent / 'static'

# Media files (CSS, JavaScript, Images)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#############################################################################################
# Settings for Session to store data for non-logged-in users

# Settings for storing session data in the database
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Additional SESSION related settings
SESSION_COOKIE_AGE = 3600  # Session cookie expiration time in seconds (e.g., 1 hour)
SESSION_SAVE_EVERY_REQUEST = True  # Save session data on every request

#############################################################################################

# Settings for taggit to be case insensitive
TAGGIT_CASE_INSENSITIVE = True

#############################################################################################

# Settings for Whoosh indexing path
INDEX_DIRECTORY = BASE_DIR / 'articles' / 'schema' / 'article_index'

#############################################################################################
# Settings for AllAuth:

# site order designation (in the new version of AllAuth, site is no longer displayed, so this setting may not be needed)
SITE_ID = 1

# Add the line "allauth.account.middleware.AccountMiddleware" to MIDDLEWARE

# Definition of authentication backends
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# This option specifies whether it is mandatory to have an email when creating a user account:
# Setting it to True requires the user to provide an email during registration.
ACCOUNT_EMAIL_REQUIRED = True
# This option specifies whether it is mandatory to have a username when creating a user account:
# Setting it to False allows users to create accounts without a username.
ACCOUNT_USERNAME_REQUIRED = False
# This option sets the authentication method for the user account.
# In this case, it is set to 'email', which means users log in using their email address.
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# This option specifies where the user will be redirected after successful login.
# In this case, the user is redirected to the home page '/'.
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = 'auto'
ACCOUNT_LOGOUT_ON_GET = True
# Disable confirmation field for social media login
# SOCIALACCOUNT_LOGIN_ON_GET=True

# Development settings:
ACCOUNT_EMAIL_VERIFICATION = "none"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Production settings:
# This option specifies whether email verification is required after registration.
# Setting it to 'optional' means email verification is optional for users.
# It can also be set to 'mandatory' or 'none'.
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Additionally, you need to set other SMTP server details like EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, etc. according to your SMTP server configuration.

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '493878433253-mrt023g89cufncgaked1bvelcc6h7csv.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
        'EMAIL_AUTHENTICATION': True,
        'SCOPE': [
            'openid',
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
'''
'openid': This item means that your application wants to use OpenID Connect to authenticate the user. By acquiring openid, you obtain the user's identifier, which you can use to uniquely identify the user.
'email': This item means that you are requesting access to the user's email address. The email address is usually one of the pieces of information provided by OpenID Connect.
'profile': This item means that you are requesting access to additional profile information about the user. This may include the first name, last name, profile picture, and other publicly available information.
'access_type': 'online': Specifies the type of access. In this case, it is set to 'online', which means the application requests online access, and the user is redirected to log in if not already logged in.
'''

#############################################################################################

# Settings for Crispy forms to use Bootstrap 5:
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = 'bootstrap5'
ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'allauth.account.forms.SignupForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
}

#############################################################################################
