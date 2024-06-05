from django.urls import path

from ..views.home_page_view_edit import HomePageEditView
from ..views.edit_hero_section import EditHeroSection
from ..views.edit_intro_section import EditIntroSection
from ..views.edit_featured_section import EditFeaturedArticlesSection
from ..views.edit_divider_section import EditDividerSection
from ..views.edit_latest_section import EditLatestArticlesSection
from ..views.edit_newsletter_section import EditNewsletterSection
from ..views.edit_gallery_section import EditGallerySection
from ..views.edit_footer_section import EditFooterSection


# Defining URLs starting with prefix 'edit/' (homepage editing by superuser)
urlpatterns = [

    # Editing the homepage.
    path('', HomePageEditView.as_view(), name='homepage-edit'),

    # Editing the Hero section.
    path('hero/', EditHeroSection.as_view(), name='edit-hero-section'),

    # Editing the Intro section.
    path('intro/', EditIntroSection.as_view(), name='edit-intro-section'),

    # Editing the Featured section.
    path('featured/', EditFeaturedArticlesSection.as_view(), name='edit-featured-section'),

    # Editing the Divider section.
    path('divider/', EditDividerSection.as_view(), name='edit-divider-section'),

    # Editing the Latest section.
    path('latest/', EditLatestArticlesSection.as_view(), name='edit-latest-section'),

    # Editing the Newsletter section.
    path('newsletter/', EditNewsletterSection.as_view(), name='edit-newsletter-section'),

    # Editing the Gallery section.
    path('gallery/', EditGallerySection.as_view(), name='edit-gallery-section'),

    # Editing the Footer section.
    path('footer/', EditFooterSection.as_view(), name='edit-footer-section'),
]
