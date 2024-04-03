print("### 03 main/main/settings.py")

"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 5.0.1.

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
SECRET_KEY = 'django-insecure-21%qw^cdm8+oeph%3+q8i1)rfdq8_%(_g+lg)2p13&ch+qul8o'

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
    'users',
    'articles',
    'tinymce',
    'widget_tweaks',
    'crispy_forms',
    'crispy_bootstrap5',
    'autoslug',
    'taggit',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'homepage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'users.anonymous_user_settings.AnonymousUserSettingsMiddleware',
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

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#############################################################################################
### Vlasní nastavení:
# Nastavení pro Session pro ukládání dat pro nepřihlášené uživatele

# Nastavení pro ukládání session dat do databáze
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Další SESSION související nastavení
SESSION_COOKIE_AGE = 3600  # Doba platnosti session cookie v sekundách (např. 1 hodina)
SESSION_SAVE_EVERY_REQUEST = True  # Ukládat session data na každý request

#############################################################################################

# Do INSTALLED_APPS zasat co je třeba
# Do TEMPLATES zapsat: 'DIRS': [BASE_DIR / 'templates'],

## Doplnění definice na různé konfigurační proměnné pro manipulaci s médii a statickými soubory:
MEDIA_URL = '/media/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR.parent / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

# Nastavení vlastní třídy uživaelů (pro users/models.py > CustomUser(AbstractUser))
AUTH_USER_MODEL = 'users.CustomUser'

#############################################################################################
# Nastavení Crispy forms na Bottstrap 5:
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
# Nastavení pro Tinymce
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

#############################################################################################
# Nastavení pro AllAuth:

# označení pořadí v site (v nové verzi AllAuth se již site nezobrazuje, tak je možné, že toto nastavení není již potřeba)
SITE_ID = 1

# Do MIDDLEWARE přidat řádek "allauth.account.middleware.AccountMiddleware",

# Definice backendů pro autentizaci
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Tato volba určuje, zda je povinné mít e-mail při vytváření uživatelského účtu:
# Nastavením na True vyžadujete, aby uživatel poskytl e-mail při registraci.
ACCOUNT_EMAIL_REQUIRED = True
# Tato volba určuje, zda je povinné mít uživatelské jméno při vytváření uživatelského účtu:
# Nastavením na False umožňujete uživatelům vytvářet účty bez uživatelského jména.
ACCOUNT_USERNAME_REQUIRED = False
# Tato volba nastavuje metodu autentizace pro uživatelský účet.
# V tomto případě je nastaveno na 'email', což znamená, že se uživatelé přihlašují pomocí své e-mailové adresy.
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# Tato volba určuje, kam bude uživatel přesměrován po úspěšném přihlášení.
# V tomto případě je uživatel přesměrován na domovskou stránku '/'.
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = 'auto'
ACCOUNT_LOGOUT_ON_GET = True
#Zakázání potvrzovacího pole pro přihlášení k soc. sítím
# SOCIALACCOUNT_LOGIN_ON_GET=True

# Nastavení pro vývoj:
ACCOUNT_EMAIL_VERIFICATION = "none"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Nastavení pro produkci:
# Tato volba určuje, zda je vyžadováno ověření e-mailu po registraci.
# Nastavením na 'optional' znamená, že ověření e-mailu je volitelné pro uživatele.
# Může být nastaveno i na 'mandatory' (povinné) nebo 'none' (žádné ověření).
#ACCOUNT_EMAIL_VERIFICATION = "mandatory"
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#+Dále je třeba nastavit další informace o SMTP serveru, jako jsou EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, atd. Podle konkrétního nastavení vašeho SMTP serveru.

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
'openid': Tato položka znamená, že vaše aplikace chce používat OpenID Connect pro autentizaci uživatele. Získáváním openid získáváte identifikátor uživatele, který můžete použít k jednoznačnému identifikování uživatele.
'email': Tato položka znamená, že žádáte o přístup k e-mailové adrese uživatele. Běžně je e-mailová adresa jednou z informací poskytovaných OpenID Connect.
'profile': Tato položka znamená, že žádáte o přístup k dalším profilovým informacím o uživateli. To může zahrnovat jméno, příjmení, obrázek profilu a další informace, které jsou veřejně dostupné.
'access_type': 'online': Určuje typ přístupu. V tomto případě je nastaveno na 'online', což znamená, že aplikace žádá o přístup online, a uživatel je přesměrován k přihlášení, pokud není přihlášen.
'''

#############################################################################################

# Nastavení pro taggit, aby nerozlišoval mezi malým a velkým písmem
TAGGIT_CASE_INSENSITIVE = True

#############################################################################################

# Nastavení cesty pro indexaci Whoosh
INDEX_DIRECTORY = BASE_DIR / 'articles' / 'article_index'