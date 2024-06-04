### Souborová struktura celého projektu 
    
###### Main
    main
    ├─ db.sqlite3
    ├─ manage.py
    ├─ requirements.txt

###### Articles
    ├─ articles
    │  ├─ __init__.py
    │  ├─ admin.py
    │  ├─ apps.py
    │  ├─ tests.py
    │  ├─ forms
    │  │  ├─ __init__.py
    │  │  ├─ article_content_form.py			   / Formulář ArticleContentForm - pro vytvoření a úpravu článku - pro záložku "Content".
    │  │  ├─ article_overview_form.py			   / Formulář ArticleOverviewForm - pro vytvoření a úpravu článku - pro záložku "Overview".
    │  │  ├─ article_settings_form.py			   / Formulář ArticleSettingsForm - pro vytvoření a úpravu článku - pro záložku "Settings".
    │  │  ├─ comment_form.py				   / Formulář ArticleCommentForm - pro přidání komentáře k článku.
    │  │  └─ search_form.py					   / Formulář ArticleSearchForm - pro vyhledávání článků.
    │  ├─ migrations
    │  │  ├─ __init__.py
    │  │  └─ 0001_initial.py
    │  ├─ models
    │  │  ├─ __init__.py
    │  │  ├─ article.py					   / Databázový model Article - pro uchování dat článku.
    │  │  ├─ article_author.py				   / Databázový model ArticleAuthor - pro uchování dat o autorovi článku.
    │  │  ├─ article_category.py				   / Databázový model ArticleCategory - pro uchování dat o kategoriích článku.
    │  │  ├─ article_comment.py				   / Databázový model ArticleComment - pro uchování dat o komentářích článku.
    │  │  ├─ article_view.py				   / Databázový model ArticleView - pro uchování dat o počtu zhlédnutí článku.
    │  │  ├─ article_data
    │  │  │  ├─ __init__.py
    │  │  │	 ├─ main_picture_processing.py			   / Metoda modelu Article - pro úpravu hlavního obrázku článku (ve 4 velikostech).
    │  │  │	 ├─ mixin_dates_and_status.py			   / Mixin modelu Article - pro přidání polí pro datum a stav.
    │  │  │	 ├─ mixin_foreign_key.py			   / Mixin modelu Article - pro přidání polí odkazujících na jiné tabulky.
    │  │  │	 └─ mixin_main_picture.py			   / Mixin modelu Article - pro přidání polí a správu hlavního obrázku.
    │  │  └─ article_author_data
    │  │     ├─ __init__.py
    │  │	 └─ profile_picture_processing.py		   / Metoda modelu ArticleAuthor - pro úpravu profilového obrázku (ve 2 velikostech).
    │  ├─ schema
    │  │  ├─ __init__.py
    │  │  ├─ article_schema.py				   / Definice třídy ArticleSchema - pro indexování článků v systému Whoosh.
    │  │  ├─ data
    │  │  │  ├─ __init__.py
    │  │  │  ├─ delete_article_from_index.py		   / Metoda třídy ArticleSchema - pro odstranění indexu článku.
    │  │  │  ├─ index_article.py				   / Metoda třídy ArticleSchema - pro zaindexování článku.
    │  │  │  ├─ print_indexed_articles.py			   / Metoda třídy ArticleSchema - pro vypsání názvů všech indexovaných článků.
    │  │  │  ├─ rebuild_schema.py				   / Funkce pro odstranění a opětovné vytvoření celého schématu.
    │  │  │  └─ update_field_in_index.py			   / Metoda třídy ArticleSchema - pro aktualizaci specifického pole v indexu.
    │  │  └─ article_index
    │  │     ├─ _MAIN_17.toc
    │  │     ├─ MAIN_f28cj67c6ri29vi8.seg
    │  │     ├─ MAIN_q59f8pk8e3q55cwe.seg
    │  │	 └─ MAIN_WRITELOCK
    │  ├─ signals
    │  │  ├─ __init__.py
    │  │  ├─ article_signals.py				   / Zachycení signálů spojených s modelem Article.
    │  │  ├─ article_author_signals.py			   / Zachycení signálů spojených s modelem ArticleAuthor.
    │  │  ├─ article_handlers
    │  │  │  ├─ __init__.py
    │  │  │  ├─ default_values_handler.py			   / Pre-save handler modelu Article - pro kontrolu výchozích hodnot.
    │  │  │  ├─ delete_article_handler.py			   / Pre-delete/post-delete handler modelu Article - pro smazání článku.
    │  │  │  ├─ delete_unused_tags_handler.py		   / Post-save handler modelu Article - pro kontrolu a případné smazání tagů.
    │  │  │  ├─ main_picture_handler.py			   / Post-save handler modelu Article - pro zpracování hlavního obrázku článku.
    │  │  │  └─ status_update_handler.py			   / Pre-save/post-save handler modelu Article - pro změnu statusu článku.
    │  │  └─ article_author_handlers
    │  │	 ├─ __init__.py
    │  │	 ├─ default_values_handler.py			   / Pre-save handler modelu ArticleAuthor - pro kontrolu výchozích hodnot.
    │  │	 └─ profile_picture_handler.py			   / Post-save handler modelu ArticleAuthor - pro zpracování profilového obrázku.
    │  ├─ urls
    │  │  ├─ __init__.py
    │  │  ├─ article.py					   / Definice URL adres začínajících s prefixem 'article/'.
    │  │  ├─ articles.py					   / Definice URL adres začínajících s prefixem 'articles/'.
    │  │  ├─ my_articles.py					   / Definice URL adres začínajících s prefixem 'my-articles/'.
    │  │  └─ search.py					   / Definice URL adres začínajících s prefixem 'search/'.
    │  └─ views
    │	  ├─ __init__.py
    │	  ├─ article_create.py				   / Pohled ArticleCreateView - pro vytvoření článku.
    │	  ├─ article_delete.py				   / Pohled ArticleDeleteView - pro smazání článku.
    │	  ├─ article_detail.py				   / Pohled ArticleDetailView - pro zobrazení jednoho článku.
    │	  ├─ article_list.py				   / Pohled ArticleListView - pro zobrazení více článků.
    │	  ├─ article_update.py				   / Pohled ArticleUpdateView - pro úpravu vytvořeného článku.
    │	  ├─ my_articles.py				   / Pohled MyArticlesView - pro zobrazení článků vytvořených přihlášeným uživatelem.
    │	  ├─ search.py					   / Pohled SearchView - pro zpracování zadaných parametrů pro vyhledávání v článcích.
    │	  ├─ search_input.py				   / Pohled SearchInputView - pro zadání parametrů pro vyhledávání v článcích.
    │	  ├─ article_create_data
    │	  │  ├─ __init__.py
    │	  │  ├─ get_context_data.py			   / Metoda pohledu ArticleCreateView - pro vytvoření kontextu.
    │	  │  ├─ get_form_class.py			   / Metoda pohledu ArticleCreateView - pro výběr formuláře dle záložky stránky.
    │	  │  ├─ get_or_create_author.py			   / Funkce pro získání instance autora na základě uživatelského jména.
    │	  │	 └─ get_success_url.py			   / Metoda pohledu ArticleCreateView - pro vytvoření návratové adresy.
    │	  ├─ article_list_data
    │	  │  ├─ __init__.py
    │	  │  ├─ get_context_data.py			   / Metoda pohledu ArticleListView - pro vytvoření kontextu.
    │	  │  ├─ get_queryset.py				   / Metoda pohledu ArticleListView - pro vytvoření seznamu článků zobrazených na stránce.
    │	  │	 └─ get_queryset_data
    │	  │		├─ __init__.py
    │	  │		├─ get_queryset_for_articles.py    / Metoda pohledu ArticleListView - pro vytvoření seznamu článků pro stránku se všemi články.
    │	  │		├─ get_queryset_for_categories.py  / Metoda pohledu ArticleListView - pro vytvoření seznamu článků pro vybranou kategorii.
    │	  │		├─ get_queryset_for_tags.py        / Metoda pohledu ArticleListView - pro vytvoření seznamu článků pro konkrétní tag a pro podobné články.
    │	  │		└─ get_tag_data.py                 / Metoda pohledu ArticleListView - pro vytvoření seznamu článků pro konkrétní tag.
    │	  ├─ common_data
    │	  │	 ├─ __init__.py
    │	  │	 ├─ get_category_data.py		   / Sdílená metoda - pro vytvoření seznamu článků pro konkrétní kategorii.
    │	  │	 ├─ get_paginate_by.py			   / Sdílená metoda - pro určení počtu článků na stránce při stránkování výsledků vyhledávání.
    │	  │	 └─ get_similar_data.py			   / Sdílená metoda - pro vytvoření atributů pro zobrazení podobných článků.
    │	  ├─ my_articles_data
    │	  │	 ├─ __init__.py
    │	  │	 ├─ get_context_data.py			   / Metoda pohledu MyArticlesView - pro vytvoření kontextu.
    │	  │	 └─ get_queryset.py			   / Metoda pohledu MyArticlesView - pro vytvoření seznamu článků zobrazených na stránce.
    │	  └─ search_data
    │		 ├─ __init__.py
    │		 ├─ get_article_ids.py			   / Funkce pro získání ID článků na základě zadaných parametrů hledání.
    │		 ├─ get_context_data.py			   / Metoda pohledu SearchView - pro vytvoření kontextu.
    │		 ├─ get_queryset.py			   / Metoda pohledu SearchView - pro vytvoření seznamu článků zobrazených na stránce.
    │		 ├─ get_search_parameters.py		   / Funkce pro zpracování očištěných dat získaných z formuláře.
    │		 └─ get_article_ids_data
    │			├─ __init__.py
    │			├─ search_in_author.py		   / Funkce pro vytvoření dotazu a popisného textu pro hledání článků podle autora.
    │			├─ search_in_date.py		   / Funkce pro vytvoření dotazu a popisného textu pro hledání článků podle data.
    │			└─ search_in_query.py		   / Funkce pro vytvoření dotazu a popisného textu pro hledání článků na základě zadaného dotazu.

###### Common data
    ├─ common_data
    │  ├─ __init__.py
    │  ├─ base_view.py					   / Definice základní třídy BaseView, ze které dědí všechny ostatní pohledy.
    │  ├─ get_unique_value.py				   / Funkce pro ověření jedinečnosti dané hodnoty v rámci pole modelu.
    │  ├─ image_processing.py				   / Funkce na zpracování nového obrázku a nahrazení původního.
    │  └─ image_resize_and_crop.py				   / Funkce pro změnu velikosti a oříznutí obrázku.

###### Homepage
    ├─ homepage
    │  ├─ __init__.py
    │  ├─ admin.py
    │  ├─ apps.py
    │  ├─ forms
    │  │  ├─ __init__.py
    │  │  ├─ divider_section_form.py			   / Formulář DividerSectionForm - pro nastavení Divider sekce domácí stránky.
    │  │  ├─ featured_section_form.py			   / Formulář FeaturedArticlesForm - pro nastavení sekce Featured Articles na domácí stránce.
    │  │  ├─ footer_section_form.py				   / Formulář FooterSettingsForm - pro editaci nastavení patičky.
    │  │  ├─ gallery_section_form.py			   / Formulář GallerySectionForm - pro editaci nastavení Gallery sekce domácí stránky.
    │  │  ├─ hero_section_form.py				   / Formulář HeroSectionForm - pro nastavení Hero sekce domácí stránky.
    │  │  ├─ intro_section_form.py				   / Formulář IntroSectionForm - pro nastavení Intro sekce domácí stránky.
    │  │  ├─ latest_section_form.py				   / Formulář LatestArticlesForm - pro nastavení sekce Nejnovější články na domácí stránce.
    │  │  └─ newsletter_section_form.py			   / Formulář NewsletterSectionForm - pro nastavení sekce Novinek na domácí stránce.
    │  ├─ migrations
    │  │  ├─ __init__.py
    │  │  └─ 0001_initial.py
    │  ├─ models
    │  │  ├─ __init__.py
    │  │  ├─ divider_section.py				   / Databázový model HomePageDividerSection - pro data sekce.
    │  │  ├─ featured_section.py				   / Databázový model HomePageFeaturedArticles - pro data sekce.
    │  │  ├─ footer_section.py				   / Databázový model FooterSettings - pro data sekce.
    │  │  ├─ gallery_section.py				   / Databázový model HomePageGallerySection - pro data sekce.
    │  │  ├─ hero_section.py				   / Databázový model HomePageHeroSection - pro data sekce.
    │  │  ├─ intro_section.py				   / Databázový model HomePageIntroSection - pro data sekce.
    │  │  ├─ latest_section.py				   / Databázový model HomePageLatestArticles - pro data sekce.
    │  │  ├─ newsletter_section.py				   / Databázový model HomePageNewsletterSection - pro data sekce.
    │  │  ├─ newsletter_subscriber.py			   / Databázový model NewsletterSubscriber - pro správu emailů pro zasílání novinek.
    │  │  └─ data
    │  │	 ├─ __init__.py
    │  │	 ├─ footer_section_default.py			   / Výchozí hodnoty pro model FooterSettings - pro patičku stránky.
    │  │	 ├─ save_footer_data.py				   / Funkce pro uložení dat z formuláře do modelu FooterSettings.
    │  │	 └─ singleton_model.py				   / Základní abstraktní třída pro editační modely homepage - pro implementaci Singleton návrhového vzoru.
    │  ├─ tests.py
    │  ├─ urls
    │  │  ├─ __init__.py
    │  │  ├─ homepage.py					   / Definice URL adres - začínajících s prefixem ''.
    │  │  └─ homepage_edit.py				   / Definice URL adres - začínajících s prefixem 'edit/'.
    │  └─ views
    │	  ├─ __init__.py
    │	  ├─ edit_divider_section.py			   / Pohled EditDividerSection - pro správu sekce.
    │	  ├─ edit_featured_section.py			   / Pohled EditFeaturedArticlesSection - pro správu sekce.
    │	  ├─ edit_footer_section.py			   / Pohled EditFooterSection - pro správu sekce.
    │	  ├─ edit_gallery_section.py			   / Pohled EditGallerySection - pro správu sekce.
    │	  ├─ edit_hero_section.py			   / Pohled EditHeroSection - pro správu sekce.
    │	  ├─ edit_intro_section.py			   / Pohled EditIntroSection - pro správu sekce.
    │	  ├─ edit_latest_section.py			   / Pohled EditLatestArticlesSection - pro správu sekce.
    │	  ├─ edit_newsletter_section.py			   / Pohled EditNewsletterSection - pro správu sekce.
    │	  ├─ home_page_view.py				   / Pohled HomePageView - pro zobrazení obsahu domovské stránky.
    │	  └─ home_page_view_edit.py			   / Pohled HomePageEditView - pro úpravu obsahu domovské stránky.

###### Main
    ├─ main
    │  ├─ __init__.py
    │  ├─ asgi.py
    │  ├─ settings.py
    │  ├─ urls.py
    │  └─ wsgi.py

###### Media
    ├─ media
    │  └─ images
    │	  ├─ articles
    │	  │	 ├─ no-image.jpg			   / Defaultní obrázek - použit při vytvoření článku, není-li definován vlastní.
    │	  │	 └─ main_picture			   / Složka pro 4 velikostní varianty hlavního obrázku článku:
    │	  │		├─ article-00000001-0150.jpg	   / 150px/150px - miniatura obrázku (použito na homepage).
    │	  │		├─ article-00000001-0440.jpg	   / 440px/330px - náhledová velikost (použito v náhledech článků).
    │	  │		├─ article-00000001-0800.jpg	   / Maximální šířka 800px - velikost pro článek (použito na stránce s článkem).
    │	  │		└─ article-00000001-1920.jpg	   / Maximální šířka 1920px - maximální velikost (použito při zvětšení obrázku na celou stránku).
    │	  ├─ homepage
    │	  │	 └─ default				   / Obrázky z původní šablony použité na stránce homepage.
    │	  │		├─ divider-bg.jpg
    │	  │		├─ featured-pic-1.jpeg
    │	  │		├─ featured-pic-2.jpeg
    │	  │		├─ featured-pic-3.jpeg
    │	  │		├─ gallery-1.jpg
    │	  │		├─ gallery-2.jpg
    │	  │		├─ gallery-3.jpg
    │	  │		├─ gallery-4.jpg
    │	  │		├─ hero.jpg
    │	  │		├─ hero-bg.jpg
    │	  │		├─ small-thumbnail-1.jpg
    │	  │		├─ small-thumbnail-2.jpg
    │	  │		└─ small-thumbnail-3.jpg
    │	  └─ profile_pictures
    │		 ├─ default.jpg				   / Defaultní obrázek pro uživatele bez vlastního profilového obrázku.
    │		 ├─ authors				   / Složka pro 2 velikostní varianty profilového obrázku autora:
    │		 │	├─ author-00000001-0150.jpg	   / 150px/150px - miniatura obrázku (pro běžné použití).
    │		 │	└─ author-00000001-0440.jpg	   / 440px/440px - náhledová velikost (použito na stránce správy účtu autora).
    │		 └─ users				   / Složka pro 2 velikostní varianty profilového obrázku uživatele:
    │			├─ user-00000001-0150.jpg	   / 150px/150px - miniatura obrázku (pro běžné použití).
    │			└─ user-00000001-0440.jpg	   / 440px/440px - náhledová velikost (použito na stránce správy účtu uživatele).

###### Static
    ├─ static
    │  ├─ css
    │  │  ├─ github.css					   / CSS sloužící k úpravě vzhledu webových stránek, které jsou hostovány na platformě Github.
    │  │  ├─ my_custom.css					   / Vlastní CSS (definováno autorem projektu).
    │  │  ├─ style.default.css				   / Defaultní CSS (obdržené s šablonou stránky).
    │  │  ├─ style.default.min.css				   / Minifikovaná verze defaultního CSS (pro produkční prostředí).
    │  │  └─ style.default.min.css.map			   / Mapovací soubor pro minifikovaný CSS k původnímu nezminifikovanému defaultnímu CSS kódu.
    │  ├─ img
    │  │  ├─ default.jpg					   / Defaultní obrázek pro uživatele bez vlastního profilového obrázku (záloha).
    │  │  ├─ favicon.ico					   / Ikona pro zobrazení v záložce webu.
    │  │  ├─ hide_side_panel[150].jpg			   / Obrázek použitý pro schování bočního panelu.
    │  │  ├─ login_picture.svg				   / Obrázek použitý na stránce pro přihlášení.
    │  │  ├─ no-image.jpg					   / Defaultní obrázek - použit při vytvoření článku, není-li definován vlastní (záloha).
    │  │  └─ signup_picture.jpg				   / Obrázek použitý na stránce pro registraci.
    │  └─ js
    │	  ├─ _tagify_input.js				   / Skript pro našeptávač tagů Tagify - použito na stránce pro vytvoření a úpravu článku.
    │	  ├─ _tinymce_article_settings.js		   / Skript pro nastavení editoru TinyMCE - použito pro obsah článku.
    │	  ├─ _tinymce_mini_settings.js			   / Skript pro nastavení editoru TinyMCE - použito pro editaci některých položek z homepage.
    │	  └─ jquery-3.7.1.min.js			   / Skript pro implementaci jQuery - použito pro zasílání AJAX požadavků.

###### Šablony (pro svou rozsáhlost jsou umístněné ve vlastním souboru)
    ├─ templates
[>>> Prohlédnout si souborovou strukturu templates.](readme_data/05_tree_templates.md)

###### Users
    └─ users
       ├─ __init__.py
       ├─ admin.py
       ├─ apps.py
       ├─ tests.py
       ├─ forms
       │  ├─ __init__.py
       │  ├─ author_profile_form.py				   / Formulář AuthorProfileForm - pro správu účtu autora.
       │  └─ user_profile_form.py				   / Formulář UserProfileForm - pro správu uživatelského účtu.
       ├─ migrations
       │  ├─ __init__.py
       │  └─ 0001_initial.py
       ├─ models
       │  ├─ __init__.py
       │  ├─ anonymous_user_middleware.py			   / Třída AnonymousUserMiddleware - middleware pro správu nepřihlášeného uživatele.
       │  ├─ custom_user.py					   / Databázový model CustomUser - pro data uživatele.
       │  ├─ anonymous_user_data
       │  │	 ├─ __init__.py
       │  │	 ├─ anonymous_user_with_settings.py		   / Třída AnonymousUserWithSettings - pro vytvoření instance pro nepřihlášeného uživatele s nastavením pro postranní panely.
       │  │	 └─ mixin_property.py				   / Mixin pro třídu AnonymousUserWithSettings - přidávající třídě property.
       │  ├─ common_data
       │  │	 ├─ __init__.py
       │  │	 ├─ default_setting_values.py			   / Výchozí hodnoty pro nastavení bočních panelů.
       │  │	 ├─ get_sorted_sidebar_panels.py		   / Sdílená metoda - pro vytvoření seznamu setříděných panelů s daty potřebnými pro jejich vykreslení.
       │  │	 ├─ change_bool_value.py			   / Funkce pro změnu boolean hodnot slovníků pro nastavení bočních panelů uživatele.
       │  │	 └─ change_sidebar_order.py			   / Funkce pro změnu pořadí postranních panelů.
       │  └─ custom_user_data
       │	 ├─ __init__.py
       │	 ├─ managers.py					   / Třída CustomUserManager - pro změnu nastavení identifikace uživatele a superuživatele.
       │	 ├─ mixin_settings.py				   / Mixin pro třídu CustomUser - přidávající třídě nastavení postranního panelu.
       │	 ├─ profile_picture_processing.py		   / Metoda modelu ArticleAuthor pro úpravu profilového obrázku (2 velikosti).
       │	 └─ setting_values_check.py			   / Funkce pro kontrolu položek pro nastavení bočních panelů dle defaultních hodnot.
       ├─ signals
       │  ├─ __init__.py
       │  ├─ user_signals.py				   / Zachycení signálů spojených s modelem CustomUser.
       │  └─ user_handlers
       │	 ├─ __init__.py
       │	 ├─ default_values_handler.py			   / Pre-save handler modelu CustomUser - pro kontrolu výchozích hodnot.
       │	 └─ profile_picture_handler.py			   / Post-save handler modelu ArticleAuthor - pro zpracování profilového obrázku.
       ├─ urls
       │  ├─ __init__.py
       │  ├─ accounts.py					   / Definice URL adres - začínajících s prefixem 'accounts/'
       │  ├─ profile.py					   / Definice URL adres - začínajících s prefixem 'profile/'
       │  └─ sidebar_settings.py				   / Definice URL adres - začínajících s prefixem 'settings/'
       └─ views
            ├─ __init__.py
            ├─ profile_update_author.py			   / Pohled AuthorProfileView - pro úpravu a nastavení dat autora.
            ├─ profile_update_user.py			   / Pohled UserProfileView - pro úpravu a nastavení dat uživatele.
            ├─ user_navigation_settings.py			   / Pohled user_navigation_settings - pro nastavení viditelnosti navigačních panelů a postranního panelu.
            ├─ user_sidebar_appearance.py			   / Pohled user_sidebar_appearance - pro změnu boolean hodnot v databázi pro nastavení bočního panelu.
            └─ user_sidebar_movements.py			   / Pohled user_sidebar_movements - pro změnu pořadí bočních panelů.

[<<< Přechod na stránku README.](README.md)