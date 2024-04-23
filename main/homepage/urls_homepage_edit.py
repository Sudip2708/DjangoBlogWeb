print("### main/main/urls.py")

from django.urls import path

# Pohledy pro domácí stránku
from homepage.views.home_page_view_edit import HomePageEditView
from homepage.views.edit_hero_section import EditHeroSection
from homepage.views.edit_intro_section import EditIntroSection
from homepage.views.edit_featured_section import EditFeaturedArticlesSection
from homepage.views.edit_divider_section import EditDividerSection
from homepage.views.edit_latest_section import EditLatestArticlesSection
from homepage.views.edit_newsletter_section import EditNewsletterSection
from homepage.views.edit_gallery_section import EditGallerySection
from homepage.views.edit_footer_section import EditFooterSection


urlpatterns = [

    # Adresy začínající s 'edit/'
    # URL pro editaci domácí stránky
    path('', HomePageEditView.as_view(), name='home-page-edit'),
    # URL pro editaci sekce Hero
    path('hero/', EditHeroSection.as_view(), name='edit-hero-section'),
    # URL pro  sekce Intro
    path('intro/', EditIntroSection.as_view(), name='edit-intro-section'),
    # URL pro editaci sekce Featured
    path('featured/', EditFeaturedArticlesSection.as_view(), name='edit-featured-section'),
    # URL pro editaci sekce Divider
    path('divider/', EditDividerSection.as_view(), name='edit-divider-section'),
    # URL pro editaci sekce Latest
    path('latest/', EditLatestArticlesSection.as_view(), name='edit-latest-section'),
    # URL pro editaci sekce Newsletter
    path('newsletter/', EditNewsletterSection.as_view(), name='edit-newsletter-section'),
    # URL pro editaci sekce Gallery
    path('gallery/', EditGallerySection.as_view(), name='edit-gallery-section'),
    # URL pro editaci sekce Footer
    path('footer/', EditFooterSection.as_view(), name='edit-footer-section'),
]













