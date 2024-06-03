### Kompletní struktura projektu 
    
    main
    ├─ db.sqlite3
    ├─ manage.py
    ├─ requirements.txt
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
    ├─ common_data
    │  ├─ __init__.py
    │  ├─ base_view.py					   / Definice základní třídy BaseView, ze které dědí všechny ostatní pohledy.
    │  ├─ get_unique_value.py				   / Funkce pro ověření jedinečnosti dané hodnoty v rámci pole modelu.
    │  ├─ image_processing.py				   / Funkce na zpracování nového obrázku a nahrazení původního.
    │  └─ image_resize_and_crop.py				   / Funkce pro změnu velikosti a oříznutí obrázku.
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
    ├─ main
    │  ├─ __init__.py
    │  ├─ asgi.py
    │  ├─ settings.py
    │  ├─ urls.py
    │  └─ wsgi.py
    ├─ media
    │  ├─ 3130627.jpg					   / Záloha mého profilového obrázku.
    │  └─ images
    │	  ├─ articles
    │	  │	 ├─ no-image.jpg			   / Defaultní obrázek - použit při vytvoření článku, není-li definován vlastní.
    │	  │	 └─ main_picture			   / Složka pro 4 velikostní varianty hlavního obrázku článku:
    │	  │		├─ article-00000001-0150.jpg	   / 150px/150px - miniatura obrázku (použito na homepage).
    │	  │		├─ article-00000001-0440.jpg	   / 440px/330px - náhledová velikost (použito v náhledech článků).
    │	  │		├─ article-00000001-0800.jpg	   / Maximální šířka 800px - velikost pro článek (použito na stránce s článkem).
    │	  │		├─ article-00000001-1920.jpg	   / Maximální šířka 1920px - maximální velikost (použito při zvětšení obrázku na celou stránku).
    │	  │		├─ article-00000002-0150.jpg
    │	  │		├─ article-00000002-0440.jpg
    │	  │		├─ article-00000002-0800.jpg
    │	  │		├─ article-00000002-1920.jpg
    │	  │		├─ article-00000003-0150.jpg
    │	  │		├─ article-00000003-0440.jpg
    │	  │		├─ article-00000003-0800.jpg
    │	  │		├─ article-00000003-1920.jpg
    │	  │		├─ article-00000004-0150.jpg
    │	  │		├─ article-00000004-0440.jpg
    │	  │		├─ article-00000004-0800.jpg
    │	  │		├─ article-00000004-1920.jpg
    │	  │		├─ article-00000005-0150.jpg
    │	  │		├─ article-00000005-0440.jpg
    │	  │		├─ article-00000005-0800.jpg
    │	  │		├─ article-00000005-1920.jpg
    │	  │		├─ article-00000006-0150.jpg
    │	  │		├─ article-00000006-0440.jpg
    │	  │		├─ article-00000006-0800.jpg
    │	  │		├─ article-00000006-1920.jpg
    │	  │		├─ article-00000007-0150.jpg
    │	  │		├─ article-00000007-0440.jpg
    │	  │		├─ article-00000007-0800.jpg
    │	  │		├─ article-00000007-1920.jpg
    │	  │		├─ article-00000008-0150.jpg
    │	  │		├─ article-00000008-0440.jpg
    │	  │		├─ article-00000008-0800.jpg
    │	  │		├─ article-00000008-1920.jpg
    │	  │		├─ article-00000009-0150.jpg
    │	  │		├─ article-00000009-0440.jpg
    │	  │		├─ article-00000009-0800.jpg
    │	  │		├─ article-00000009-1920.jpg
    │	  │		├─ article-00000010-0150.jpg
    │	  │		├─ article-00000010-0440.jpg
    │	  │		├─ article-00000010-0800.jpg
    │	  │		├─ article-00000010-1920.jpg
    │	  │		├─ article-00000024-0150.jpg
    │	  │		├─ article-00000024-0440.jpg
    │	  │		├─ article-00000024-0800.jpg
    │	  │		└─ article-00000024-1920.jpg
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
    ├─ templates
    │  ├─ 0_base						   / Základní šablona pro všechny stránky projektu.
    │  │  ├─ 00__base__.html
    │  │  ├─ 01__head__.html
    │  │  ├─ 02__header__.html
    │  │  ├─ 03__messages__.html
    │  │  ├─ 04__footer__.html
    │  │  ├─ 05__body_scripts__.html
    │  │  ├─ _footer
    │  │  │  ├─ __content__.html
    │  │  │  ├─ __edit_section__.html
    │  │  │  ├─ __end_line_section__.html
    │  │  │  ├─ _content_data
    │  │  │	 │	├─ _address_and_social_.html
    │  │  │	 │	├─ _articles_.html
    │  │  │	 │	└─ _selected_links_.html
    │  │  │	 └─ _edit_data
    │  │  │		├─ _column_1_.html
    │  │  │		├─ _column_2_.html
    │  │  │		├─ _column_3_.html
    │  │  │		└─ _column_4_.html
    │  │  ├─ _head
    │  │  │  ├─ __links__.html
    │  │  │  ├─ __meta__.html
    │  │  │  └─ __scripts__.html
    │  │  └─ _header
    │  │	 ├─ __dropdown_display__.html
    │  │	 ├─ __navigation__.html
    │  │	 ├─ _dropdown_data
    │  │	 │	├─ __dropdown_menu__.html
    │  │	 │	├─ _button_.html
    │  │	 │	├─ _category_dropdown_.html
    │  │	 │	├─ _create_article_and_favorite_.html
    │  │	 │	├─ _homepage_articles_search_.html
    │  │	 │	├─ _profile_and_login_.html
    │  │	 │	├─ _show_sidebar_.html
    │  │	 │	└─ _special_offer_.html
    │  │	 └─ _navigation_data
    │  │		├─ _navigation_items_.html
    │  │		├─ _search_and_language_.html
    │  │		└─ _special_offer_.html
    │  ├─ 1_home						   / Šablona pro domácí stránku.
    │  │  ├─ 10__base__.html
    │  │  ├─ 11__hero__.html
    │  │  ├─ 12__intro__.html
    │  │  ├─ 13__featured_articles__.html
    │  │  ├─ 14__divider__.html
    │  │  ├─ 15__latest_articles__.html
    │  │  ├─ 16__newsletter__.html
    │  │  ├─ 17__gallery__.html
    │  │  ├─ _home_data
    │  │  │  ├─ __featured_articles__.html
    │  │  │  ├─ __latest_articles__.html
    │  │  │  ├─ _display_background_image_.html
    │  │  │  ├─ _display_div_text_.html
    │  │  │  ├─ _display_h1_text_.html
    │  │  │  ├─ _display_h2_text_.html
    │  │  │  ├─ _display_link_.html
    │  │  │  ├─ _edit_button_.html
    │  │  │  ├─ _gallery_articles_.html
    │  │  │  ├─ _input_email_field_.html
    │  │  │  ├─ _main_picture_.html
    │  │  │	 └─ _section_display_.html
    │  │  └─ _home_edit
    │  │	 ├─ __divider__.html
    │  │	 ├─ __featured__.html
    │  │	 ├─ __gallery__.html
    │  │	 ├─ __hero__.html
    │  │	 ├─ __intro__.html
    │  │	 ├─ __latest__.html
    │  │	 ├─ __newsletter__.html
    │  │	 └─ _edit_data
    │  │		├─ _edit_article_.html
    │  │		├─ _edit_background_image_.html
    │  │		├─ _edit_html_field_.html
    │  │		├─ _edit_link_.html
    │  │		└─ _submit_button_with_display_checkbox_.html
    │  ├─ 2_main						   / Šablona pro stránky zobrazující postranní panel.
    │  │  ├─ 20__base__.html
    │  │  ├─ 21__sidebar__.html
    │  │  ├─ 22__search__.html
    │  │  ├─ 23__profile_update__.html
    │  │  ├─ _search_data
    │  │  │  ├─ _form_.html
    │  │  │	 └─ _form_data
    │  │  │		├─ _autor_input_.html
    │  │  │		├─ _collapse_button_.html
    │  │  │		├─ _date_inputs_.html
    │  │  │		├─ _error_messages_.html
    │  │  │		├─ _check_box_inputs_.html
    │  │  │		├─ _input_field_.html
    │  │  │		└─ _submit_button_md_.html
    │  │  └─ _sidebars
    │  │	 ├─ __category__.html
    │  │	 ├─ __search__.html
    │  │	 ├─ __tags__.html
    │  │	 ├─ __user__.html
    │  │	 └─ _data
    │  │		├─ _author_dropdown_menu_.html
    │  │		├─ _search_options_items_.html
    │  │		├─ _sidebar_movement_buttons_.html
    │  │		└─ _user_dropdown_items_.html
    │  ├─ 3_articles					   / Šablona pro stránky zobrazující více článků.
    │  │  ├─ 30__base__.html
    │  │  ├─ 31__page_title__.html
    │  │  ├─ 32__page_navigation__.html
    │  │  ├─ 33__articles__.html
    │  │  ├─ 34__pagination__.html
    │  │  ├─ _articles_data
    │  │  │  ├─ _article_view_setup_.html
    │  │  │	 └─ _view_setup_data
    │  │  │		├─ _author_.html
    │  │  │		├─ _category_.html
    │  │  │		├─ _comment_count_.html
    │  │  │		├─ _main_picture_.html
    │  │  │		├─ _overview_.html
    │  │  │		├─ _published_ago_.html
    │  │  │		├─ _published_date_.html
    │  │  │		├─ _tags_.html
    │  │  │		└─ _title_.html
    │  │  └─ _page_navigation_data
    │  │	 ├─ _categories_.html
    │  │	 ├─ _my_articles_.html
    │  │	 ├─ _search_results_.html
    │  │	 ├─ _tags_.html
    │  │	 ├─ _search_result_data
    │  │	 │	├─ _tab_for_categories_.html
    │  │	 │	├─ _tab_for_results_and_similar_.html
    │  │	 │	├─ _tab_to_show_categories_.html
    │  │	 │	└─ _tab_to_show_results_and_similar_.html
    │  │	 └─ _tags_data
    │  │		├─ _tab_for_categories_.html
    │  │		├─ _tab_for_tag_and_similar_.html
    │  │		├─ _tab_to_show_categories_.html
    │  │		└─ _tab_to_show_tag_and_similar_.html
    │  ├─ 4_article						   / Šablona pro stránku zobrazující jeden článek.
    │  │  ├─ 40__base__.html
    │  │  ├─ 41__article__.html
    │  │  ├─ 42__previous_and_next__.html
    │  │  ├─ 43__display_comments__.html
    │  │  ├─ 44__add_comment__.html
    │  │  ├─ _article_data
    │  │  │  ├─ _content_.html
    │  │  │  ├─ _main_picture_.html
    │  │  │  ├─ _next_.html
    │  │  │  ├─ _overview_.html
    │  │  │  ├─ _previous_.html
    │  │  │  ├─ _tags_.html
    │  │  │  ├─ _title_.html
    │  │  │	 └─ _update_article_.html
    │  │  └─ _comment_data
    │  │	 ├─ _add_comment_header_.html
    │  │	 ├─ _comment_author_picture_.html
    │  │	 ├─ _comment_creation_.html
    │  │	 ├─ _comment_display_.html
    │  │	 └─ _title_and_comment_count_.html
    │  ├─ 5_create_article					   / Šablona pro vytvoření a úpravu článku.
    │  │  ├─ 50__base__.html
    │  │  ├─ 51__overview__.html
    │  │  ├─ 52__content__.html
    │  │  ├─ 53__settings__.html
    │  │  ├─ 54__confirm_leave__.html
    │  │  ├─ 55__confirm_delete__.html
    │  │  └─ _data
    │  │	 ├─ _buttons_both_.html
    │  │	 ├─ _input_category_.html
    │  │	 ├─ _input_next_article_.html
    │  │	 ├─ _input_previous_article_.html
    │  │	 ├─ _input_status_.html
    │  │	 ├─ _input_tags_.html
    │  │	 └─ _main_picture_view_.html
    │  ├─ account						   / Přepsání stránek AllAuth pro přihlášení a registraci.
    │  │  ├─ login.html
    │  │  ├─ signup.html
    │  │  ├─ _login
    │  │  │	 ├─ _email_input_.html
    │  │  │	 ├─ _help_links_.html
    │  │  │	 ├─ _login_with_google_.html
    │  │  │	 ├─ _or_separator_.html
    │  │  │	 ├─ _password_input_.html
    │  │  │	 ├─ _remember_me_.html
    │  │  │	 └─ _submit_button_.html
    │  │  ├─ _shared
    │  │  │  ├─ _base_.html
    │  │  │  ├─ _error_messages_.html
    │  │  │  ├─ _picture_.html
    │  │  │  ├─ _redirect_value_.html
    │  │  │	 └─ _script_for_showing_password_.html
    │  │  └─ _signup
    │  │	 ├─ _email_input_.html
    │  │	 ├─  _help_links_.html
    │  │	 ├─ _password_input1_.html
    │  │	 ├─ _password_input2_.html
    │  │	 ├─ _submit_button_.html
    │  └─ socialaccount					   / Přepsání stránek AllAuth pro přihlášení přes sociální sítě (zde Google).
    │	  └─ login.html
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
