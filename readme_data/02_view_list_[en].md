### Project Views

###### Article Creation and Editing
    ArticleCreateView: View for creating an article (only for logged-in users).
    ArticleUpdateView: View for editing a created article (only for logged-in users).
     
        URL:
        - article-create: Page for creating a new article.
        - article-update: Page for editing a created article.
        
        Template:
        - Header
        - Navigation
            - Overview: Main image, Title, Article description.
            - Content: Main article content (created using TinyMCE editor).
            - Settings: Status, Category, Previous article, Next article, Tags.
        - Form
        - Confirmation of leaving the page with unsaved changes (JS)
    
###### Article Deletion
    ArticleDeleteView: View for deleting an article (only for logged-in users).

        URL:
        - article-delete: Page for confirming article deletion.

        Template:
        - Header
        - Info text
        - Preview of the article to be deleted
        - Confirmation prompt
        - Delete button
        - Back to article editing button
    
###### Full Article View
    ArticleDetailView: View for the page with the listing of one article.
    
        URL:
        - article-detail: Page displaying one selected article.
    
        Template:
        - Article
            - Main image
            - Category
            - Title
            - Author link
            - Article age
            - Number of comments
            - Link to edit article (author only)
            - Article description
            - Article content
            - Tags
        - Link to previous and next article
        - User comments
        - Form for adding a comment
          ArticleDetailView: Pohled pro stránku s výpisem jednoho článku.

###### Article Preview Display

    ArticleListView: View for the article list page.
    MyArticlesView: View for the user's own articles page (only for logged-in users).
    SearchView: View for processing article searches.

    URLs:
    - article-list: Page displaying all published articles.
    - article-category-list: Page displaying all published articles categorized by category.
    - article-tag-list: Page for displaying articles for a given tag.
    - article-tag-list-similar: Page for displaying similar articles for a given tag.
    - article-tag-list-category: Page for displaying categories for articles for a given tag.
    - article-tag-list-similar-category: Page for displaying categories for similar articles for a given tag.
    - my-articles: Page for articles by the author associated with the user.
    - article-search: Base URL for entering and evaluating search parameters.
    - article-search-results: Page for displaying search results.
    - article-search-similar: Page for displaying similar articles for articles from the search results.
    - article-search-results-category: Page for displaying categories for the search result.
    - article-search-similar-category: Page for displaying categories for similar articles.
    
    The view template consists of the following parts:
    - Heading: The title of the page.
    - Info text: (Only for URLs that contain it.)
    - Navigation: (Visible only on MD and larger devices.)
        - Categories:
            - All: For the page with all articles (article-list).
            - Category name: For articles in a given category (article-category-list).
        - Tags:
            - Tag name: For articles that contain the given tag.
            - Similar articles: For articles that contain at least one tag contained in the articles for the given tag, but do not contain the given tag.
            - Categories: Option to display categories for articles for the given tag and for similar articles.
        - My articles:
            - All: All author's articles.
            - Drafted: Articles that are in draft.
            - Publish: Published articles.
            - Archive: Archived articles.
        - Search result:
            - Search result: For articles that contain the given tag.
            - Similar articles: For articles that contain at least one tag contained in the search results, but are not part of them.
            - Categories: Option to display categories for articles for the search result and for similar articles.
    - Article preview display:
        - The article preview consists of:
            - Main image: The main image of the article.
            - Publication date: The date the article was published.
            - Category: The category of the article.
            - Tags: The tags of the article.
            - Headline: The headline of the article.
            - Article description: A brief description of the article.
            - Link to author: A link to the author's profile.
            - Article age: The age of the article (how long ago it was published).
            - Number of comments: The number of comments on the article.
    - Pagination:
        - Number of articles per page without sidebar, and with sidebar: 6/4
            - Possible improvement: For mobile devices, have an infinite list instead of pagination.


###### Article Search

    SearchInputView: A view for displaying the search page (and for reporting search errors).
    
        URLs:
        - article-search-input: The search input page.
        - article-search-error: The search error notification page.
        
        The view template consists of the following parts:
        
        - Heading
        - Error message
        - Search form
            - Search field (Full-text search is performed using the whoosh index.)
            - Field selection: Title, Description, Content (All items are selected by default.)
            - Publication date selection field:
                - Articles before a certain date.
                - Articles after a certain date.
                - Articles between two dates.
            - Author selection field

###### Homepage
    HomePageView: A view for displaying the homepage content.
    
        URL:
        - home-page: Displays the homepage.
    
        The view template consists of the following parts:
        - Hero Section: Page introduction section (Background image, Heading, Link)
        - Intro Section: Page introduction text (Heading, Text)
        - Featured articles: Three selected articles (Articles)
        - Divider Section: Divider section (Background image, Text, Link)
        - Latest articles: Three latest articles (Heading, Subheading, Articles)
        - Newsletter Section: Newsletter subscription (Heading, Subheading, Email input field)
        - Gallery Section: Four selected main article images (Images can be clicked to view full size.)
        - Footer Section: Page footer (I did not change anything here and left everything as it is in the original template.)

###### Homepage Settings

    HomePageEditView: A view for editing homepage content (for superusers only).

        URL:
        - home-page-edit: Edits the homepage.
    
        The view is then linked to these other views for processing requests for individual sections:
        - EditHeroSection: Processes form data for the Hero section of the Home Page. 
            (View processing URL: edit-hero-section)
        - EditIntroSection: Processes form data for the introduction section on the Home Page. 
            (View processing URL: edit-intro-section)
        - EditFeaturedArticlesSection: Processes form data for the featured articles section on the Home Page. 
            (View processing URL: edit-featured-section)
        - EditDividerSection: Processes form data for the Divider section on the Home Page. 
            (View processing URL: edit-divider-section)
        - EditLatestArticlesSection: Processes form data for the latest articles section on the Home Page. 
            (View processing URL: edit-latest-section)
        - EditNewsletterSection: Processes form data for the newsletter section on the Home Page. 
            (View processing URL: edit-newsletter-section)
        - EditGallerySection: Processes form data for the article gallery section on the Home Page. 
            (View processing URL: edit-gallery-section)
        - EditFooterSection: Processes form data for the footer section on the Home Page. 
            (View processing URL: edit-footer-section)

###### User Account Settings

    UserProfileView: A view for editing and configuring user data.
    AuthorProfileView: A view for editing and configuring author data.
    
        URLs:
        - profile-update-user: Page for editing a user account.
        - profile-update-author: Page for editing an author account.
    
        The view template consists of the following parts:
        - Heading
        - Navigation
            - User: For setting the profile picture, username, first name and last name
            - Author: For setting the author's profile picture and username (only displayed if the user is also an author)
        - Form

###### Sidebar Settings Views

    user_navigation_settings: A view for setting the visibility of navigation bars and the sidebar.
    user_sidebar_appearance: A view for changing boolean values in the database to configure the sidebar.
    user_sidebar_movements: A view for changing the order of sidebars.
    
        URLs:
        - user_navigation_settings: URL for setting the visibility of navigation bars and the sidebar.
            - show_sidebars: Sidebar visibility.
            - show_category_navigation: Category navigation visibility.
            - show_tab_for_similar: Navigation visibility for similar articles.
        
        - user_sidebar_appearance: URL for changing the visibility of inner sidebar menus (ajax).
            - show_search_sidebar: Search sidebar visibility.
            - show_search_options: Search menu visibility.
            - show_user_sidebar: User items sidebar visibility.
            - show_user_options: User items menu visibility.
            - show_author_options: Author items menu visibility.
            - show_category_sidebar: Category sidebar visibility.
            - show_category_options: Category menu visibility.
            - show_tags_sidebar: Tags sidebar visibility.
            - show_tags_options: Tags menu visibility. 
            (The view receives a request received via AJAX from the page script.)
        
        - user_sidebar_movements: URL for changing the order of sidebars.
            - search: Search sidebar position.
            - user: User items sidebar position.
            - category: Category sidebar position.
            - tags: Tags sidebar position.

[<<< Go to README page](README_[en].md)