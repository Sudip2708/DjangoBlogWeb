### Obsahuje nastavení pro váš Django projekt, včetně databázové konfigurace, klíčů API, nastavení jazyka a dalších


from pathlib import Path
'''
[from]
pathlib: balíček, který poskytuje objektové rozhraní pro manipulaci s cestami k souborům a adresářům
[import]
Path: třída, která slouží k manipulaci s cestami k souborům a adresářům
'''


# Definice kořenového adresáře:
BASE_DIR = Path(__file__).resolve().parent.parent


# Definice tajného klíče:
# (tajný klíč pro různé bezpečnostní operace včetně šifrování, generování CSRF (Cross-Site Request Forgery) tokenů, a dalších bezpečnostních mechanismů)
SECRET_KEY = 'django-insecure-sny#m+80^f!g6rj2w5ve%zdih6&bh(hvh=@p^+ga!s$s@(_5vr'


# Definice vývojového režimu pro ladění:
DEBUG = True


# Definice seznamu povolených domén:
ALLOWED_HOSTS = []


# Definice jednotlivých aplikací:
# (aplikace jsou samostatné komponenty, které mohou poskytovat určité funkce a mohou být znovu použity v různých projektech)
'''
'django.contrib.admin': aplikace, která poskytuje administrátorské rozhraní pro správu dat v aplikaci. Umožňuje administrátorům pohodlně spravovat modely (databázové tabulky), zobrazovat, filtrovat a editovat data.
'django.contrib.auth': aplikace, pro autentizaci a autorizaci uživatelů. Poskytuje modely pro uživatele, skupiny a oprávnění. Zahrnuje také několik pohledů a formulářů pro přihlašování, odhlašování a registraci.
'django.contrib.contenttypes': aplikace, která umožňuje definovat modely, které mohou být propojeny s jinými modely v aplikaci. Pomocí této aplikace můžete vytvářet obecné vztahy mezi objekty.
'django.contrib.sessions': aplikace, která poskytuje podporu pro ukládání a získávání dat relací uživatele. Může být použito pro uchování stavu relace mezi HTTP požadavky.
'django.contrib.messages': aplikace, která  podporuje systém zpráv, který umožňuje předávat krátké zprávy mezi pohledy a šablonami. Tyto zprávy jsou užitečné například pro zobrazování potvrzení po úspěšném provedení akce.
'django.contrib.staticfiles': aplikace, která slouží k správě statických souborů, jako jsou CSS, JavaScript, obrázky atd. Tato aplikace umožňuje jednoduché zpracování a poskytování statických souborů v aplikaci.
'tinymce': aplikace, která poskytuje možnosti formátování a editace obsahu pro webové stránky
'posts': aplikace, pro správu příspěvků
'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'posts',
    'marketing',
]


# Definice seznamu středníků:
# (pořadí středníků v seznamu je důležité, protože každý středník je volán v pořadí, v jakém je uveden)
'''
SecurityMiddleware: Zajišťuje bezpečnostní opatření, například nastavení HTTP hlaviček pro ochranu před útoky.
SessionMiddleware: Spravuje relace pro uživatele.
CommonMiddleware: Poskytuje několik standardních úprav pro HTTP požadavky a odpovědi.
CsrfViewMiddleware: Ochrana proti CSRF útokům (Cross-Site Request Forgery).
AuthenticationMiddleware: Zajišťuje autentizaci uživatelů.
MessageMiddleware: Poskytuje podporu pro systém zpráv.
XFrameOptionsMiddleware: Nastavuje HTTP hlavičku X-Frame-Options pro ochranu proti clickjacking útokům.
'''
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Definice hlavního URL konfigurátoru:
# (v tomto příkladu to znamená, že se bude očekávat soubor s názvem urls.py ve vaší aplikaci myapp)
ROOT_URLCONF = 'blog.urls'


# Definice šablon:
# (šablony jsou použity pro generování HTML obsahu v rámci vaší Django aplikace)
'''
'BACKEND': 'django.template.backends.django.DjangoTemplates': Specifikuje backend (úložiště) pro šablony. V tomto případě se jedná o Django vlastní šablonový backend.
'DIRS': []: Seznam adresářů, kde mohou být umístěny vlastní šablony pro vaši aplikaci. Prázdný seznam znamená, že se očekává, že šablony budou umístěny ve standardních adresářích aplikací.
'APP_DIRS': True: Určuje, zda se mají prohledávat adresáře jednotlivých aplikací v projektu (True). Pokud je True, Django bude prohledávat adresáře s názvem templates ve všech aplikacích ve vašem projektu.
'OPTIONS': { 'context_processors': [...] }: Nastavení pro možnosti šablon. Zde jsou zahrnuty kontextové procesory, které automaticky přidávají některé proměnné do každého kontextu šablony. Tyto proměnné mohou být následně použity ve šablonách. V tomto příkladě jsou zahrnuty kontextové procesory pro debugování, zpracování požadavků, autentizaci a zprávy.
'''
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


# Definice cesty k modulu WSGI (Web Server Gateway Interface) aplikace pro váš projekt)
# (tato aplikace pak bude použita webovým serverem (například Gunicorn nebo uWSGI), aby bylo možné obsluhovat HTTP požadavky pro váš Django projekt)
WSGI_APPLICATION = 'blog.wsgi.application'


# Definice databáze:
'''
'ENGINE': 'django.db.backends.sqlite3': Specifikuje, který databázový engine (dříve označován jako backend) se má použít. V tomto případě je použit SQLite engine.
'NAME': BASE_DIR / 'db.sqlite3': Určuje název databázového souboru nebo cesty k databázi. BASE_DIR je proměnná, která obvykle obsahuje cestu k adresáři, ve kterém se nachází soubor settings.py. Tímto způsobem je vytvořena cesta k souboru db.sqlite3 v kořenovém adresáři projektu.
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Definice sady pravidel pro ověření silného hesla uživatele
# (tyto pravidla určují minimální požadavky, které heslo uživatele musí splňovat, aby bylo považováno za bezpečné)
'''
'django.contrib.auth.password_validation.UserAttributeSimilarityValidator': Toto pravidlo kontroluje, zda heslo obsahuje příliš podobné atributy uživatelského jména nebo jiných uživatelských informací.
'django.contrib.auth.password_validation.MinimumLengthValidator': Toto pravidlo kontroluje minimální délku hesla.
'django.contrib.auth.password_validation.CommonPasswordValidator': Toto pravidlo kontroluje, zda heslo není příliš běžné a nejedná se o často používané heslo.
'django.contrib.auth.password_validation.NumericPasswordValidator': Toto pravidlo kontroluje, zda heslo obsahuje alespoň jednu číselnou hodnotu.
'''
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


# Definice mezinárodního nastavení
# (slouží k definování několika klíčových parametrů, které ovlivňují způsob, jakým se zpracovávají mezinárodní aspekty vaší webové aplikace)
'''
LANGUAGE_CODE: Určuje výchozí jazyk pro vaši aplikaci. V tomto příkladě je nastaven na angličtinu ('en-us'). Tento jazyk bude použit jako výchozí, pokud není žádný jiný jazyk explicitně specifikován.
TIME_ZONE: Určuje výchozí časové pásmo pro vaši aplikaci. V tomto příkladě je nastaveno na UTC (Koordinovaný světový čas). Toto časové pásmo bude použito pro všechny časové operace, pokud není specifikováno jiné časové pásmo.
USE_I18N: Boolean hodnota, která indikuje, zda se má používat mezinárodní zpracování. Pokud je True, Django bude podporovat mezinárodní zpracování, včetně možnosti překladu textů ve vaší aplikaci do různých jazyků.
USE_TZ: Boolean hodnota, která indikuje, zda se mají používat časová pásma. Pokud je True, Django bude používat časová pásma pro manipulaci s daty a časy.
'''
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Definice adresy pro statické soubory:
# (CSS, JavaScript, Images)
STATIC_URL = 'static/'

## Doplnění definice na různé konfigurační proměnné pro manipulaci s médii a statickými soubory:
'''
MEDIA_URL: Určuje URL adresu, přes kterou budou přístupné média (např. obrázky, videa) v rámci aplikace. V tomto případě je nastaveno na '/media/', což znamená, že média budou dostupná na URL adrese začínající http://example.com/media/ (předpokládejme, že váš web běží na doméně example.com).
STATICFILES_DIRS: Je seznam adresářů, ve kterých Django bude hledat statické soubory (např. CSS, JavaScript). V tomto případě je použit adresář BASE_DIR / 'static'. Adresáře uvedené zde jsou použity výhradně v režimu vývoje (při spuštění serveru v režimu DEBUG=True).
STATIC_ROOT: Je cesta k adresáři, kam budou statické soubory shromážděny před distribucí aplikace. Tato proměnná je relevantní především při nasazování aplikace, kdy chcete shromáždit všechny statické soubory na jednom místě. V tomto případě je použito BASE_DIR / 'static'.
MEDIA_ROOT: Je cesta k adresáři, kam budou ukládány nahrané mediální soubory (např. obrázky nahrané uživateli). Podobně jako STATIC_ROOT, je to cesta k adresáři, kde jsou fyzicky uložena média. V tomto případě je použito BASE_DIR / 'media'
'''
MEDIA_URL = '/media/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR.parent / 'static'
MEDIA_ROOT = BASE_DIR / 'media'


# Definice výchozího tipu primárního klíče:
# (nastavuje výchozí hodnotu pro automaticky generovaný primární klíč (auto-incrementing primary key) pro modely v databázi)
'''
BigAutoField je varianta AutoField, která používá datový typ BigIntegerField na pozadí (v databázi). BigIntegerField umožňuje ukládat velká celá čísla, což může být užitečné v případech, kdy se očekává velký počet záznamů v databázi a hrozí vyčerpání rozsahu standardního IntegerField.
'''
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
