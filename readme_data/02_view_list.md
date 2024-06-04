### Pohledy projetku

###### Vytvoření a úprava článku
    ArticleCreateView: Pohled pro vytvoření článku (pouze pro přihlášené uživatele).
    ArticleUpdateView: Pohled pro úpravu vytvořeného článku (pouze pro přihlášené uživatele).
    
        Pohled zpracovává následující URL:
        - article-create: Stránka pro vytvoření nového článku.
        - article-update: Stránka pro úpravu vytvořeného článku.
    
        Šablona pohledu se skládá z těchto částí:
        - Nadpis
        - Navigace
            - Overview: Hlavní obrázek, Nadpis, Popis článku.
            - Content: Hlavní obsah článku (vytváří se za pomocí editoru TinyMCE).
            - Settings: Status, Kategorie, Předchozí článek, Následující článek, Tagy.
        - Formulář
        - Potvrzení odchodu ze stránky při neuložených změnách (JS)
    
###### Smazání článku
    ArticleDeleteView: Pohled pro smazání článku (jen pro přihlášené uživatele).
    
        Pohled zpracovává následující URL:
        - article-delete: Stránka pro potvrzení smazání článku.
    
        Šablona pohledu se skládá z těchto částí:
        - Nadpis
        - Info text
        - Náhled článku, který má být smazán
        - Dotaz na potvrzení smazání
        - Tlačítko pro smazání
        - Tlačítko pro návrat na úpravu článku
    
###### Zobrazení celého článku
    ArticleDetailView: Pohled pro stránku s výpisem jednoho článku.
    
        Pohled zpracovává následující URL:
        - article-detail: Stránka zobrazující jeden vybraný článek.
    
        Šablona pohledu se skládá z těchto částí:
        - Článek
            - Hlavní obrázek
            - Kategorie
            - Nadpis
            - Odkaz na autora
            - Stáří článku
            - Počet komentářů
            - Odkaz na editaci článku (pouze pro autora)
            - Popis článku
            - Obsah článku
            - Tagy
        - Odkaz na předchozí a následující článek
        - Komentáře uživatelů
        - Formulář pro přidání komentáře

###### Zobrazení náhledů článků
    ArticleListView: Pohled pro stránku s výpisem článků.
    MyArticlesView: Pohled pro stránku s vlastními články uživatele (jen pro přihlášené uživatele).
    SearchView: Pohled pro zpracování vyhledávání v článcích.
    
        Pohled zpracovává následující URL:
        - article-list: Stránka zobrazující všechny publikované články.
        - article-category-list: Stránka zobrazující všechny publikované články roztříděné do kategorií.
        - article-tag-list: Stránka pro zobrazení článků pro daný tag.
        - article-tag-list-similar: Stránka pro zobrazení podobných článků pro daný tag.
        - article-tag-list-category: Stránka pro zobrazení kategorií pro články pro daný tag.
        - article-tag-list-similar-category: Stránka pro zobrazení kategorií pro podobné články pro daný tag.
        - my-articles: Stránka pro články od autora navázaného na uživatele.
        - article-search: Základní adresa sloužící k zadání a vyhodnocení parametrů hledání.
        - article-search-results: Stránka pro zobrazení výsledků vyhledávání.
        - article-search-similar: Stránka pro zobrazení podobných článků pro články z výsledku vyhledávání.
        - article-search-results-category: Stránka pro zobrazení kategorií pro vásledek vyhledávání.
        - article-search-similar-category: Stránka pro zobrazení kategorií pro podobné články.
    
        Šablona pohledu se skládá z těchto částí:
        - Nadpis
        - Info text (Pouze pro url které ho obsahují.)
        - Navigace (Viditelná pouze na zařízeních MD a větších.)
            - Kategorie
                - All: Pro stránku se všemi články (article-list).
                - Jméno kategorie: Pro články dané kategorie (article-category-list).
            - Tagy
                - Jméno tagu: Pro články které obsahují daný tag.
                - Podobné články: Pro články, jenž obsahují alespoň jeden tag obsažený v článcích pro daný tag, ale neobsahují daný tag.
                - Kategorie: Možnost zobrazení kategorií článků pro daný tag a pro podobné články.
            - Moje články
                - All: Všechny články autora.
                - Drafted: Články které jsou v přípravě.
                - Publish: Publikované články.
                - Archive: Archivované články.
            - Výsledek vyhledávání
                - Výsledek vyhledávání: Pro články které obsahují daný tag.
                - Podobné články: Pro články, jenž obsahují alespoň jeden tag obsažený ve vyhledaných článcích, ale nejsou součástí.
                - Kategorie: Možnost zobrazení kategorií článků pro výsledek vyhledávání a pro podobné články.
        - Zobrazení náhledů článků
            - Náhled článku se skládá z:
                - Hlavní obrázek
                - Datum publikování
                - Kategorie
                - Tagy
                - Nadpis
                - Popis článku
                - Odkaz na autora
                - Stáří článku
                - Počet komentářů
        - Stránkování
            - Počet článků na stránku bez postranního panelu, a s postranním panelem: 6/4
                - Případné zlepšení: Pro zobrazení na mobilních zařízeních namísto stránkování mít nekonečný seznam.

###### Vyhledávání v článcích
    SearchInputView: Pohled pro zobrazení stránky pro vyhledávání (a pro oznamování chyb ve vyhledávání).
    
        Pohled zpracovává následující URL:
        - article-search-input: Stránka pro zadání vyhledávání.
        - article-search-error: Stránka pro oznámení chyb vyhledávání.
    
        Šablona pohledu se skládá z těchto částí:
        - Nadpis
        - Oznam chyb
        - Formulář pro vyhledávání
            - Pole pro zadání hledaného textu (Fultextové hledání se provádí za pomoci whoosh indexu.)
            - Pole pro specifikaci polí: Nadpis, Popis, Obsah (Defaultně jsou vybrány všechny položky.)
            - Pole pro specifikaci datumu publikování:
                - Články před určitým datem.
                - Články po určitém datu.
                - Články mezi dvěma daty.
            - Pole pro specifikaci autora

###### Domácí stránky
    HomePageView: Pohled pro zobrazení obsahu domovské stránky.
    
        Pohled zpracovává následující URL:
        - home-page: Zobrazení domácí stránky.
    
        Šablona pohledu se skládá z těchto částí:
        - Hero Section: Úvodní sekce stránky (Obrázek pozadí, Nadpis, Odkaz)
        - Intro Section: Úvodní text stránky (Nadpis, Text)
        - Featured articles: Tři vybrané články (Články)
        - Divider Section: Oddělovací část (Obrázek pozadí, Text, Odkaz)
        - Latest articles: Tři nejnovější články (Nadpis, Podnadpis, Články)
        - Newsletter Section: Odběr novinek (Nadpis, Podnadpis, Pole pro zadání emailu)
        - Gallery Section: Čtyři vybrané hlavní obrázky článklů (Obrázky je možné rozkliknout do plného zobrazení.)
        - Footer Section: Patička stránky (Zde jsem nic neměnil a ponechal vše tak, jak je v původní šabloně.)

###### Nastavení domácí stránky
    HomePageEditView: Pohled pro úpravu obsahu domovské stránky (pouze pro superuživatele).

        Pohled zpracovává následující URL:
        - home-page-edit: Editace domácí stránky.
    
        Na pohled jsou pak navázené tyto další pohledy pro zpracování požadavků pro jednotlivé sekce:
            - EditHeroSection: Zpracování dat formuláře pro Hero sekci z Home Page.
                (URL pro zpracování pohledu: edit-hero-section)
            - EditIntroSection: Zpracování dat formuláře pro úvodní sekci na Home Page.
                (URL pro zpracování pohledu: edit-intro-section)
            - EditFeaturedArticlesSection: Zpracování dat formuláře pro sekci vybraných článků na Home Page.
                (URL pro zpracování pohledu: edit-featured-section)
            - EditDividerSection: Zpracování dat formuláře pro Divider sekci na Home Page.
                (URL pro zpracování pohledu: edit-divider-section)
            - EditLatestArticlesSection: Zpracování dat formuláře pro sekci nejnovějších článků na Home Page.
                (URL pro zpracování pohledu: edit-latest-section)
            - EditNewsletterSection: Zpracování dat formuláře pro sekci newsletteru na Home Page.
                (URL pro zpracování pohledu: edit-newsletter-section)
            - EditGallerySection: Zpracování dat formuláře pro sekci galerie článků na Home Page.
                (URL pro zpracování pohledu: edit-gallery-section)
            - EditFooterSection: Zpracování dat formuláře pro sekci patičky na Home Page.
                (URL pro zpracování pohledu: edit-footer-section)

###### Nastavení uživatelských účtů
    UserProfileView: Pohled pro úpravu a nastavení dat uživatele.
    AuthorProfileView: Pohled pro úpravu a nastavení dat autora.

        Pohled zpracovává následující URL:
        - profile-update-user: Stránka pro úpravu uživatelského účtu.
        - profile-update-author: Stránka pro úpravu autorského účtu.
    
        Šablona pohledu se skládá z těchto částí:
        - Nadpis
        - Navigace
            - User: Pro nastavení profilového obrázku, uživatelského jména, jména a příjmení
            - Author: Pro nastavení profilového obrázku a uživatelského jména autora (Zobrazí se pouze je-li uživatel i autor)
        - Formulář

###### Pohledy pro nastavení bočního panelu
    user_navigation_settings: Pohled pro nastavení viditelnosti navigačních panelů a postranního panelu.
    user_sidebar_appearance: Pohled pro změnu boolean hodnot v databázi pro nastavení bočního panelu.
    user_sidebar_movements: Pohled pro změnu pořadí bočních panelů.

        Pohled zpracovává následující URL:
    
        - user_navigation_settings: URL pro nastavení viditelnosti navigačních panelů a postranního panelu.
            - show_sidebars: Viditelnost bočních panelů.
            - show_category_navigation: Viditelnost navigace pro kategorie.
            - show_tab_for_similar: Viditelnost pro navigaci pro podobné články.
    
        - user_sidebar_appearance: URL pro změnu viditelnosti vnitřních nabídek postranních panelů (ajax).
            - show_search_sidebar: Viditelnost panelu pro vyhledávání.
            - show_search_options: Viditelnost vnitřní nabídky pro vyhledávání.
            - show_user_sidebar: Viditelnost panelu pro položky uživatele.
            - show_user_options: Viditelnost vnitřní nabídky pro položky uživatele.
            - show_author_options: Viditelnost vnitřní nabídky pro položky autora.
            - show_category_sidebar: Viditelnost panelu pro kategorie.
            - show_category_options: Viditelnost vnitřní nabídky pro kategorie.
            - show_tags_sidebar: Viditelnost panelu pro tagy.
            - show_tags_options: Viditelnost vnitřní nabídky pro tagy.
            (Pohled přijímá požadavek obdržený prostřednictvím AJAX ze scriptu stránky.)
    
        - user_sidebar_movements: URL pro změnu pořadí postranních panelů.
            - search: Pozice pabelu pro vyhledávání.
            - user: Pozice pabelu pro položky uživatele.
            - category: Pozice pabelu pro kategorie.
            - tags: Pozice pabelu pro tagy.

[<<< Přechod na stránku README.](../README.md)