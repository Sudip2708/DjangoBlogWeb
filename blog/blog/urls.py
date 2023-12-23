### Definuje URL směrovač, který určuje, jak mají být zpracovány příchozí HTTP požadavky


# Import modulů:
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views.index import IndexView
from posts.views.post_create import PostCreateView
from posts.views.post_delete import PostDeleteView
from posts.views.post_detail import PostDetailView
from posts.views.post_list import PostListView
from posts.views.post_update import PostUpdateView
from posts.views.search import SearchView
from marketing.views import email_list_signup


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='home'),
    path('blog/', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search/', SearchView.as_view(), name='search'),
    path('email-signup/', email_list_signup, name='email-list-signup'),

    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
]


# Ověření vývojového režimu:
# (Význam této podmínky spočívá ve změně chování aplikace v závislosti na tom, zda je aktivní vývojový režim nebo ne)
# (V praxi to znamená, že při vývoji můžete přistupovat k těmto souborům přímo z webového prohlížeče, aniž byste je museli spravovat přes webserver. Ve výrobním prostředí by mělo být toto chování zakázáno, protože by mohlo představovat bezpečnostní rizika.)
'''
urlpatterns: seznam obsahující definice URL tras v Django. Tyto trasy určují, jak mají být zpracovávány různé URL požadavky ve vaší aplikaci.
settings.STATIC_URL: obsahuje URL pro statické soubory, například "/static/".
settings.STATIC_ROOT: obsahuje cestu k adresáři, ve kterém jsou statické soubory uloženy na serveru.
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT): přidává cestu pro servírování statických souborů.
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT): přidává cestu pro servírování mediálních souborů
'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)