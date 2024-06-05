### Project File Structure
    
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
    │  │  ├─ article_content_form.py			   / ArticleContentForm - form for creating and editing an article for the "Content" tab.
    │  │  ├─ article_overview_form.py			   / ArticleOverviewForm - form for creating and editing an article for the "Overview" tab.
    │  │  ├─ article_settings_form.py			   / ArticleSettingsForm - form for creating and editing an article for the "Settings" tab.
    │  │  ├─ comment_form.py				   / ArticleCommentForm - form for adding a comment to the article.
    │  │  └─ search_form.py					   / ArticleSearchForm - form for searching articles.
    │  ├─ migrations
    │  │  ├─ __init__.py
    │  │  └─ 0001_initial.py
    │  ├─ models
    │  │  ├─ __init__.py
    │  │  ├─ article.py					   / Article - database model for storing article data.
    │  │  ├─ article_author.py				   / ArticleAuthor - database model for storing data about the article's author.
    │  │  ├─ article_category.py				   / ArticleCategory - database model for storing data about article categories.
    │  │  ├─ article_comment.py				   / ArticleComment - database model for storing data about article comments.
    │  │  ├─ article_view.py				   / ArticleView - database model - for storing data about the number of views of the article.
    │  │  ├─ article_data
    │  │  │  ├─ __init__.py
    │  │  │	 ├─ main_picture_processing.py			   / Article model method for editing the main article image (in 4 sizes).
    │  │  │	 ├─ mixin_dates_and_status.py			   / DatesAndStatusMixin - Article model mixin for adding fields for date and status.
    │  │  │	 ├─ mixin_foreign_key.py			   / ForeignKeyMixin - Article model mixin for adding fields referencing other tables.
    │  │  │	 └─ mixin_main_picture.py			   / MainPictureMixin - Article model mixin for adding fields and managing the main image.
    │  │  └─ article_author_data
    │  │     ├─ __init__.py
    │  │	 └─ profile_picture_processing.py		   / ArticleAuthor model method for editing the profile image (in 2 sizes).
    │  ├─ schema
    │  │  ├─ __init__.py
    │  │  ├─ article_schema.py				   / ArticleSchema - class definition for indexing articles in the Whoosh system.
    │  │  ├─ data
    │  │  │  ├─ __init__.py
    │  │  │  ├─ delete_article_from_index.py		   / ArticleSchema class method for removing the article index.
    │  │  │  ├─ index_article.py				   / ArticleSchema class method for indexing an article.
    │  │  │  ├─ print_indexed_articles.py			   / ArticleSchema class method for listing names of all indexed articles.
    │  │  │  ├─ rebuild_schema.py				   / Function for removing and recreating the entire schema.
    │  │  │  └─ update_field_in_index.py			   / ArticleSchema class method for updating a specific field in the index.
    │  │  └─ article_index
    │  │     ├─ _MAIN_17.toc
    │  │     ├─ MAIN_f28cj67c6ri29vi8.seg
    │  │     ├─ MAIN_q59f8pk8e3q55cwe.seg
    │  │	 └─ MAIN_WRITELOCK
    │  ├─ signals
    │  │  ├─ __init__.py
    │  │  ├─ article_signals.py				   / Capturing signals related to the Article model.
    │  │  ├─ article_author_signals.py			   / Capturing signals related to the ArticleAuthor model.
    │  │  ├─ article_handlers
    │  │  │  ├─ __init__.py
    │  │  │  ├─ default_values_handler.py			   / Pre-save handler of the Article model for checking default values.
    │  │  │  ├─ delete_article_handler.py			   / Pre-delete/post-delete handler of the Article model for deleting an article.
    │  │  │  ├─ delete_unused_tags_handler.py		   / Post-save handler of the Article model for checking and potentially deleting tags.
    │  │  │  ├─ main_picture_handler.py			   / Post-save handler of the Article model for processing the main article image.
    │  │  │  └─ status_update_handler.py			   / Pre-save/post-save handler of the Article model for changing the status of an article.
    │  │  └─ article_author_handlers
    │  │	 ├─ __init__.py
    │  │	 ├─ default_values_handler.py			   / Pre-save handler of the ArticleAuthor model for checking default values.
    │  │	 └─ profile_picture_handler.py			   / Post-save handler of the ArticleAuthor model for processing the profile image.
    │  ├─ urls
    │  │  ├─ __init__.py
    │  │  ├─ article.py					   / URL addresses starting with the prefix 'article/'.
    │  │  ├─ articles.py					   / URL addresses starting with the prefix 'articles/'.
    │  │  ├─ my_articles.py					   / URL addresses starting with the prefix 'my-articles/'.
    │  │  └─ search.py					   / URL addresses starting with the prefix 'search/'.
    │  └─ views
    │	  ├─ __init__.py
    │	  ├─ article_create.py				   / ArticleCreateView - view for creating an article.
    │	  ├─ article_delete.py				   / ArticleDeleteView - view for deleting an article.
    │	  ├─ article_detail.py				   / ArticleDetailView - view for displaying a single article.
    │	  ├─ article_list.py				   / ArticleListView - view for displaying multiple articles.
    │	  ├─ article_update.py				   / ArticleUpdateView - view for editing a created article.
    │	  ├─ my_articles.py				   / MyArticlesView - view for displaying articles created by the logged-in user.
    │	  ├─ search.py					   / SearchView - view for processing the entered parameters for searching articles.
    │	  ├─ search_input.py				   / SearchInputView - view for entering parameters for searching articles.
    │	  ├─ article_create_data
    │	  │  ├─ __init__.py
    │	  │  ├─ get_context_data.py			   / Method of the ArticleCreateView for creating a context.
    │	  │  ├─ get_form_class.py			   / Method of the ArticleCreateView for selecting a form based on the page tab.
    │	  │  ├─ get_or_create_author.py			   / Function to get the author's instance based on the username.
    │	  │	 └─ get_success_url.py			   / Method of the ArticleCreateView for creating a return address.
    │	  ├─ article_list_data
    │	  │  ├─ __init__.py
    │	  │  ├─ get_context_data.py			   / Method of the ArticleListView for creating a context.
    │	  │  ├─ get_queryset.py				   / Method of the ArticleListView for creating a list of articles displayed on the page.
    │	  │	 └─ get_queryset_data
    │	  │		├─ __init__.py
    │	  │		├─ get_queryset_for_articles.py    / Method of the ArticleListView for creating a list of articles for the page with all articles.
    │	  │		├─ get_queryset_for_categories.py  / Method of the ArticleListView for creating a list of articles for the selected category.
    │	  │		├─ get_queryset_for_tags.py        / Method of the ArticleListView for creating a list of articles for a specific tag and similar articles.
    │	  │		└─ get_tag_data.py                 / Method of the ArticleListView for creating a list of articles for a specific tag.
    │	  ├─ common_data
    │	  │	 ├─ __init__.py
    │	  │	 ├─ get_category_data.py		   / Shared method for creating a list of articles for a specific category.
    │	  │	 ├─ get_paginate_by.py			   / Shared method to determine the number of articles per page when paginating search results.
    │	  │	 └─ get_similar_data.py			   / Shared method for creating attributes for displaying similar articles.
    │	  ├─ my_articles_data
    │	  │	 ├─ __init__.py
    │	  │	 ├─ get_context_data.py			   / Method of MyArticlesView for creating a context.
    │	  │	 └─ get_queryset.py			   / Method of MyArticlesView for creating a list of articles displayed on the page.
    │	  └─ search_data
    │		 ├─ __init__.py
    │		 ├─ get_article_ids.py			   / Function to get article IDs based on entered search parameters.
    │		 ├─ get_context_data.py			   / Method of SearchView for creating a context.
    │		 ├─ get_queryset.py			   / Method of SearchView for creating a list of articles displayed on the page.
    │		 ├─ get_search_parameters.py		   / Function for processing sanitized data obtained from the form.
    │		 └─ get_article_ids_data
    │			├─ __init__.py
    │			├─ search_in_author.py		   / Function to create a query and descriptive text for searching articles by author.
    │			├─ search_in_date.py		   / Function to create a query and descriptive text for searching articles by date.
    │			└─ search_in_query.py		   / Function to create a query and descriptive text for searching articles based on entered query.

###### Common data
    ├─ common_data
    │  ├─ __init__.py
    │  ├─ base_view.py					   / BaseView - definition of the base class from which all other views inherit.
    │  ├─ get_unique_value.py				   / Function to verify the uniqueness of a given value within a model field.
    │  ├─ image_processing.py				   / Function to process a new image and replace the original.
    │  └─ image_resize_and_crop.py				   / Function for resizing and cropping an image.

###### Homepage
    ├─ homepage
    │  ├─ __init__.py
    │  ├─ admin.py
    │  ├─ apps.py
    │  ├─ forms
    │  │  ├─ __init__.py
    │  │  ├─ divider_section_form.py			   / DividerSectionForm - form for setting up the Divider section of the homepage.
    │  │  ├─ featured_section_form.py			   / FeaturedArticlesForm - form for setting up the Featured Articles section on the homepage.
    │  │  ├─ footer_section_form.py				   / FooterSettingsForm - form for editing footer settings.
    │  │  ├─ gallery_section_form.py			   / GallerySectionForm - form for editing the Gallery section settings of the homepage.
    │  │  ├─ hero_section_form.py				   / HeroSectionForm - form for setting up the Hero section of the homepage.
    │  │  ├─ intro_section_form.py				   / IntroSectionForm - form for setting up the Intro section of the homepage.
    │  │  ├─ latest_section_form.py				   / LatestArticlesForm - form for setting up the Latest Articles section on the homepage.
    │  │  └─ newsletter_section_form.py			   / NewsletterSectionForm - form for setting up the Newsletter section on the homepage.
    │  ├─ migrations
    │  │  ├─ __init__.py
    │  │  └─ 0001_initial.py
    │  ├─ models
    │  │  ├─ __init__.py
    │  │  ├─ divider_section.py				   / HomePageDividerSection - database model for section data.
    │  │  ├─ featured_section.py				   / HomePageFeaturedArticles - database model for section data.
    │  │  ├─ footer_section.py				   / FooterSettings - database model for section data.
    │  │  ├─ gallery_section.py				   / HomePageGallerySection - database model for section data.
    │  │  ├─ hero_section.py				   / HomePageHeroSection - database model for section data.
    │  │  ├─ intro_section.py				   / HomePageIntroSection - database model for section data.
    │  │  ├─ latest_section.py				   / HomePageLatestArticles - database model for section data.
    │  │  ├─ newsletter_section.py				   / HomePageNewsletterSection - database model for section data.
    │  │  ├─ newsletter_subscriber.py			   / NewsletterSubscriber - database model for managing emails for newsletter distribution.
    │  │  └─ data
    │  │	 ├─ __init__.py
    │  │	 ├─ footer_section_default.py			   / Default values for the FooterSettings model for the website footer.
    │  │	 ├─ save_footer_data.py				   / Function to save form data into the FooterSettings model.
    │  │	 └─ singleton_model.py				   / Basic abstract class for homepage editing models for implementing the Singleton design pattern.
    │  ├─ tests.py
    │  ├─ urls
    │  │  ├─ __init__.py
    │  │  ├─ homepage.py					   / URL address definitions starting with the prefix '/'.
    │  │  └─ homepage_edit.py				   / URL address definitions starting with the prefix 'edit/'.
    │  └─ views
    │	  ├─ __init__.py
    │	  ├─ edit_divider_section.py			   / EditDividerSection - view for managing the section.
    │	  ├─ edit_featured_section.py			   / EditFeaturedArticlesSection - view for managing the section.
    │	  ├─ edit_footer_section.py			   / EditFooterSection - view for managing the section.
    │	  ├─ edit_gallery_section.py			   / EditGallerySection - view for managing the section.
    │	  ├─ edit_hero_section.py			   / EditHeroSection - view for managing the section.
    │	  ├─ edit_intro_section.py			   / EditIntroSection - view for managing the section.
    │	  ├─ edit_latest_section.py			   / EditLatestArticlesSection - view for managing the section.
    │	  ├─ edit_newsletter_section.py			   / EditNewsletterSection - view for managing the section.
    │	  ├─ home_page_view.py				   / HomePageView - view for displaying the homepage content.
    │	  └─ home_page_view_edit.py			   / HomePageEditView - view for editing the homepage content.

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
    │	  │	 ├─ no-image.jpg			   / Default image used when creating an article if a custom one is not defined.
    │	  │	 └─ main_picture			   / Folder for 4 size variations of the main article image:
    │	  │		├─ article-00000001-0150.jpg	   / 150px/150px - thumbnail image (used on the homepage).
    │	  │		├─ article-00000001-0440.jpg	   / 440px/330px - preview size (used in article previews).
    │	  │		├─ article-00000001-0800.jpg	   / Maximum width 800px - size for the article (used on the article page).
    │	  │		└─ article-00000001-1920.jpg	   / Maximum width 1920px - maximum size (used when enlarging the image to full page).
    │	  ├─ homepage
    │	  │	 └─ default				   / Images from the original template used on the homepage.
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
    │		 ├─ default.jpg				   / Default image for users without a custom profile picture.
    │		 ├─ authors				   / Folder for 2 size variations of the author's profile picture:
    │		 │	├─ author-00000001-0150.jpg	   / 150px/150px - thumbnail image (for general use).
    │		 │	└─ author-00000001-0440.jpg	   / 440px/440px - preview size (used on the author's account management page).
    │		 └─ users				   / Folder for 2 size variations of the user's profile picture:
    │			├─ user-00000001-0150.jpg	   / 150px/150px - thumbnail image (for general use).
    │			└─ user-00000001-0440.jpg	   / 440px/440px - preview size (used on the user's account management page).

###### Static
    ├─ static
    │  ├─ css
    │  │  ├─ github.css					   / CSS used to style the web pages hosted on the Github platform.
    │  │  ├─ my_custom.css					   / Custom CSS (defined by the project author).
    │  │  ├─ style.default.css				   / Default CSS (received with the page template).
    │  │  ├─ style.default.min.css				   / Minified version of the default CSS (for production environment).
    │  │  └─ style.default.min.css.map			   / Mapping file for the minified CSS to the original non-minified default CSS code.
    │  ├─ img
    │  │  ├─ default.jpg					   / Default image for users without a custom profile picture (backup).
    │  │  ├─ favicon.ico					   / Icon for displaying on the website tab.
    │  │  ├─ hide_side_panel[150].jpg			   / Image used to hide the sidebar panel.
    │  │  ├─ login_picture.svg				   / Image used on the login page.
    │  │  ├─ no-image.jpg					   / Default image - used when creating an article if a custom one is not defined (backup).
    │  │  └─ signup_picture.jpg				   / Image used on the registration page.
    │  └─ js
    │	  ├─ _tagify_input.js				   / Script for the Tagify tag suggestion tool used on the article creation and editing page.
    │	  ├─ _tinymce_article_settings.js		   / Script for configuring the TinyMCE editor used for article content.
    │	  ├─ _tinymce_mini_settings.js			   / Script for configuring the TinyMCE editor used for editing certain items on the homepage.
    │	  └─ jquery-3.7.1.min.js			   / Script for implementing jQuery used for sending AJAX requests.

###### Templates (due to their extensive nature, they are located in a separate file).
    ├─ templates
[>>> View the file structure of the templates.](05_tree_templates_[en].md)

###### Users
    └─ users
       ├─ __init__.py
       ├─ admin.py
       ├─ apps.py
       ├─ tests.py
       ├─ forms
       │  ├─ __init__.py
       │  ├─ author_profile_form.py				   / AuthorProfileForm - form for managing author account settings.
       │  └─ user_profile_form.py				   / UserProfileForm - form for managing user account settings.
       ├─ migrations
       │  ├─ __init__.py
       │  └─ 0001_initial.py
       ├─ models
       │  ├─ __init__.py
       │  ├─ anonymous_user_middleware.py			   / AnonymousUserMiddleware - middleware for handling anonymous users.
       │  ├─ custom_user.py					   / CustomUser - database model for user data.
       │  ├─ anonymous_user_data
       │  │	 ├─ __init__.py
       │  │	 ├─ anonymous_user_with_settings.py		   / AnonymousUserWithSettings - class for creating an instance for an anonymous user with sidebar settings.
       │  │	 └─ mixin_property.py				   / AnonynousPropertyMixin - mixin for the class AnonymousUserWithSettings adding properties to the class.
       │  ├─ common_data
       │  │	 ├─ __init__.py
       │  │	 ├─ default_setting_values.py			   / Default values for sidebar settings.
       │  │	 ├─ get_sorted_sidebar_panels.py		   / Shared method for creating a list of sorted panels with data needed for rendering.
       │  │	 ├─ change_bool_value.py			   / Function to change boolean values of dictionaries for user sidebar settings.
       │  │	 └─ change_sidebar_order.py			   / Function to change the order of sidebar panels.
       │  └─ custom_user_data
       │	 ├─ __init__.py
       │	 ├─ managers.py					   / CustomUserManager - class for changing user and superuser identification settings.
       │	 ├─ mixin_settings.py				   / UserSettingsMixin - mixin for the CustomUser class adding sidebar panel settings to the class.
       │	 ├─ profile_picture_processing.py		   / Method of the ArticleAuthor model to edit profile picture (2 sizes).
       │	 └─ setting_values_check.py			   / Function to check items for sidebar settings based on default values.
       ├─ signals
       │  ├─ __init__.py
       │  ├─ user_signals.py				   / Capturing signals related to the CustomUser model.
       │  └─ user_handlers
       │	 ├─ __init__.py
       │	 ├─ default_values_handler.py			   / Pre-save handler of the CustomUser model for checking default values.
       │	 └─ profile_picture_handler.py			   / Post-save handler of the ArticleAuthor model for processing the profile picture.
       ├─ urls
       │  ├─ __init__.py
       │  ├─ accounts.py					   / URL address definitions starting with the prefix 'accounts/'.
       │  ├─ profile.py					   / URL address definitions starting with the prefix 'profile/'.
       │  └─ sidebar_settings.py				   / URL address definitions starting with the prefix 'settings/'.
       └─ views
            ├─ __init__.py
            ├─ profile_update_author.py			   / AuthorProfileView - view for editing and setting author data.
            ├─ profile_update_user.py			   / UserProfileView - view for editing and setting user data.
            ├─ user_navigation_settings.py			   / user_navigation_settings - view for setting the visibility of navigation panels and sidebar.
            ├─ user_sidebar_appearance.py			   / user_sidebar_appearance - view for changing boolean values in the database for sidebar settings.
            └─ user_sidebar_movements.py			   / user_sidebar_movements - view for changing the order of sidebar panels.

[<<< Go to README page](README_[en].md)