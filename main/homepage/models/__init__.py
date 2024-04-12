# Model pro Newsletter Subscriber (pro zběr emailů v Newsletter sekci)
from .newsletter_subscriber import NewsletterSubscriber

# Abstraktní Singleton třída z které dědí všechny dále uvedené modely
from .singleton_model import SingletonModel

# Model pro Hero sekci na domovské stránce
from .hero_section import HomePageHeroSection

# Model pro Intro sekci na domovské stránce
from .intro_section import HomePageIntroSection

# Model pro Featured sekci na domovské stránce
from .featured_section import HomePageFeaturedArticles

# Model pro Divider sekci na domovské stránce
from .divider_section import HomePageDividerSection

# Model pro Latest sekci na domovské stránce
from .latest_section import HomePageLatestArticles

# Model pro Newsletter sekci na domovské stránce
from .newsletter_section import HomePageNewsletterSection

# Model pro Gallery sekci na domovské stránce
from .gallery_section import HomePageGallerySection

# Defaultní hodnoty pro sekci Footer
from .footer_section_default import (
    DEFAULT_ADDRESS_VALUES,
    DEFAULT_SOCIAL_MEDIA,
    DEFAULT_SITE_LINKS,
    DEFAULT_ARTICLES,
    DEFAULT_END_LINE
)

# Model pro Footer sekci na domovské stránce
from .footer_section import FooterSettings










