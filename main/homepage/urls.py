### Definice URL patternů pro aplikaci

from django.urls import path
from .views.home_page import HomePageView
from .views.home_page_edit import HomePageEditView
from .views.edit_hero_section import EditHeroSection
from .views.edit_intro_section import EditIntroSection
from .views.edit_featured_section import EditFeaturedArticlesSection
from .views.edit_divider_section import EditDividerSection
from .views.edit_latest_section import EditLatestArticlesSection
from .views.edit_newsletter_section import EditNewsletterSection
from .views.edit_gallery_section import EditGallerySection
from .views.edit_footer_section import EditFooterSection

urlpatterns = [

    # URL pro domovskou stránku
    path('', HomePageView.as_view(), name='home'),
    path('edit/', HomePageEditView.as_view(), name='home-page-edit'),
    path('edit/hero/', EditHeroSection.as_view(), name='edit-hero-section'),
    path('edit/intro/', EditIntroSection.as_view(), name='edit-intro-section'),
    path('edit/featured/', EditFeaturedArticlesSection.as_view(), name='edit-featured-section'),
    path('edit/divider/', EditDividerSection.as_view(), name='edit-divider-section'),
    path('edit/latest/', EditLatestArticlesSection.as_view(), name='edit-latest-section'),
    path('edit/newsletter/', EditNewsletterSection.as_view(), name='edit-newsletter-section'),
    path('edit/gallery/', EditGallerySection.as_view(), name='edit-gallery-section'),
    path('edit/footer/', EditFooterSection.as_view(), name='edit-footer-section'),
]