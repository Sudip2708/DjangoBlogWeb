### Obsahuje nastavení pro váš Django projekt, včetně databázové konfigurace, klíčů API, nastavení jazyka a dalších

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&!z)p7g7bu=-8%cxqs)ecg6%yh8f$e7=7_xci$o*kn#+lhbmir'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
    'marketing',
    'tinymce',
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'autoslug',
]

# Nastavení Crispy forms na Bottstrap 5:
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
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


## Doplnění definice na různé konfigurační proměnné pro manipulaci s médii a statickými soubory:
MEDIA_URL = '/media/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR.parent / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Tinymce
'''
theme: rčuje vzhled editoru. Například: 'silver', 'advanced', 'modern', 'simple', apod.
width a height: Určují výchozí šířku a výšku editoru.
plugins: Seznam pluginů, které chcete povolit. Například: 'advlist autolink lists link image charmap print preview anchor'.
toolbar: Definuje obsah panelu nástrojů. Můžete specifikovat seznam tlačítek, které se zobrazí v panelu nástrojů.
menubar: Nastavuje, které položky mají být zobrazeny v hlavním menu.
statusbar: Pokud je nastaven na True, zobrazí se stavový řádek editoru.
language: Nastavuje jazyk editoru. Například: 'en', 'es', atd.
file_browser_callback: Specifikuje funkci, která se má zavolat při výběru souboru. Může být použita k přizpůsobení chování pro výběr souborů.
image_dimensions: Povoluje nebo zakazuje možnost měnit rozměry obrázků při jejich vložení.
content_css: Specifikuje CSS soubory, které se mají použít pro formátování obsahu editoru.
extended_valid_elements: Definuje rozšířený seznam povolených HTML elementů.
'''
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 500,
    "image_dimensions": True,
    "menubar": "format insert table tools view help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table powerpaste advcode help wordcount spellchecker typography",
    "toolbar": "undo redo | "
               "insertfile image media pageembed template link anchor codesample | "
               "showcomments addcomment code typography | "
               "pagebreak | "
               "charmap emoticons | "
               "fontselect fontsizeselect formatselect | "
               "bold italic | "
               "forecolor backcolor casechange permanentpen formatpainter removeformat | "
               "alignleft aligncenter alignright alignjustify | "
               "outdent indent | "
               "numlist bullist checklist | "
               "fullscreen  preview save print",
}

# Definice backendů pro autentizaci
'''
AUTHENTICATION_BACKENDS určuje pořadí, ve kterém jsou backendy zkoušeny pro ověření uživatele. Pokud první backend nedokáže ověřit uživatele, bude použit další v seznamu
Tato konfigurace specifikuje, jaké backendy budou použity pro ověření identity uživatele
'django.contrib.auth.backends.ModelBackend': Standardní Django backend pro autentizaci založený na databázovém modelu. Používá databázový model User pro ukládání a ověřování uživatelů
'allauth.account.auth_backends.AuthenticationBackend': Backend poskytovaný frameworkem django-allauth. Tento backend rozšiřuje funkce autentizace a zahrnuje podporu pro různé metody přihlašování, včetně sociálního přihlašování
'''
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Dočasně pro sprovoznění
MAILCHIMP_API_KEY = ''
MAILCHIMP_DATA_CENTER = ''
MAILCHIMP_EMAIL_LIST_ID = ''