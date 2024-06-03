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


# Definování adres začínajících s prefixem 'edit/' (editace domácí stránky superuživatelem)
urlpatterns = [

    # Editace domácí stránky.
    path('', HomePageEditView.as_view(), name='homepage-edit'),

    # Editace sekce Hero.
    path('hero/', EditHeroSection.as_view(), name='edit-hero-section'),

    # UEditace sekce Intro.
    path('intro/', EditIntroSection.as_view(), name='edit-intro-section'),

    # Editace sekce Featured.
    path('featured/', EditFeaturedArticlesSection.as_view(), name='edit-featured-section'),

    # Editace sekce Divider.
    path('divider/', EditDividerSection.as_view(), name='edit-divider-section'),

    # Editace sekce Latest.
    path('latest/', EditLatestArticlesSection.as_view(), name='edit-latest-section'),

    # Editace sekce Newsletter.
    path('newsletter/', EditNewsletterSection.as_view(), name='edit-newsletter-section'),

    # Editace sekce Gallery.
    path('gallery/', EditGallerySection.as_view(), name='edit-gallery-section'),

    # Editace sekce Footer.
    path('footer/', EditFooterSection.as_view(), name='edit-footer-section'),
]













