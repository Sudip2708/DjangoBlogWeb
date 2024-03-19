print("### main/articles/views/article_list.py")

### Definice třídy pohledu pro výpis článků

from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django.urls import resolve
from django.db.models import Q

from articles.models.article import Article
from articles.models.article_category import ArticleCategory
from .article_common_contex_mixin import CommonContextMixin
from articles.schema import ArticleSchema


class ArticleListView(CommonContextMixin, ListView):
    # Použitý model pro seznam článků
    model = Article

    # Cesta k šabloně pro zobrazení seznamu článků
    template_name = '3_articles/30__base__.html'

    # Název objektu v kontextu (seznam článků)
    context_object_name = 'queryset'

    # Počet článků na stránku
    paginate_by = 4

    # Ověření, zda se jedná o stránku se všemi články a nebo o stránky s kategoriemi
    category_page = False

    # Ověření zda se jedná o zobrazení s navigací pro kategorie
    category_navigation = False

    # Název pro aktuální záložku kategorií
    current_category_tab = None

    # Ověření zda se jedná o stránku s tagy
    tag_page = False

    # Ověření zda se jedná o zobrazení s navigací pro tagy
    tag_navigation = False

    # Název pro aktuální záložku tagů
    current_tag = None

    # Kontrola zda jsme na záložce pro podobné články
    similar_tag_articles = False


    def get_queryset(self, *args, **kwargs):

        # Získání informací o vyřešené URL z aktuálního požadavku
        resolved_url = resolve(self.request.path_info)
        print("### resolved_url: ",resolved_url)

        # Získání přihlášeného uživatele
        user = self.request.user

        # Ověření, zda se jedná o stránku se všemi články a nebo o stránky s kategoriemi
        if resolved_url.route == 'articles/all' or self.kwargs.get('category_slug'):
            self.category_page = True


            # Ověření zda je uživatel přihlášen a má zaplé zobrazení navigace kategorií
            if user.is_authenticated and user.sidebar_category_navigation:
                self.category_navigation = True


            # Když jsme na stránce pro zobrazení všech článků
            if resolved_url.route == 'articles/all':
                print("### if route == 'articles/all'")

                self.current_category_tab = 'all'
                status = 'publish'
                article_ids = ArticleSchema().find_all_articles_by_status(status)

                queryset = Article.objects.filter(id__in=article_ids).order_by('-created')


            # Když jsme na stránce pro zobrazení článků pro danou kategorii
            elif self.kwargs.get('category_slug'):
                print("### elif self.kwargs.get('category_slug')")

                self.current_category_tab = self.kwargs.get('category_slug')
                category_id = ArticleCategory().get_category_id_by_slug(self.current_category_tab)
                article_ids = ArticleSchema().find_all_articles_by_category(str(category_id))

                queryset = Article.objects.filter(id__in=article_ids).order_by('-created')


        # Když jsme na stránce pro zobrazení článků pro daný tag
        elif self.kwargs.get('tag_slug'):
            print("### elif self.kwargs.get('tag_slug'):")

            self.tag_page = True

            # Ověření zda je uživatel přihlášen a má zaplé zobrazení navigace kategorií
            if user.is_authenticated and user.show_tab_for_similar:
                self.tag_navigation = True
                self.current_tag = self.kwargs.get('tag_slug')

            tag = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))
            article_ids = ArticleSchema().find_all_articles_by_tag(str(tag.id))

            if self.kwargs.get('similar'):
                print("similar")
                self.similar_tag_articles = True

                # Získání tagů článků na aktuální stránce
                current_article_tags = Tag.objects.filter(article__id__in=article_ids)

                # Filtrování článků podle podobných tagů
                similar_articles = Article.objects.filter(
                    ~Q(id__in=article_ids),  # Nezahrnuje články na aktuální stránce
                    tags__in=current_article_tags  # Zahrnuje články s alespoň jedním stejným tagem
                ).distinct().order_by('-created')

                queryset = similar_articles

            else:
                queryset = Article.objects.filter(id__in=article_ids).order_by('-created')


        return queryset


    def get_paginate_by(self, queryset):
        print("### def get_paginate_by(self, queryset):")

        # Získání přihlášeného uživatele
        user = self.request.user

        # Pokud je uživatel přihlášený a má pole sidebar nastavené na False, nastavte paginate_by na 6, jinak na 4
        if user.is_authenticated and not user.sidebar:
            return 6
        return 4


    def get_context_data(self, **kwargs):
        print("### def get_context_data(self, **kwargs):")

        # Získání kontextu od rodičovské třídy
        context = super().get_context_data(**kwargs)

        # Získání přihlášeného uživatele
        user = self.request.user

        # Kontext pro stránku se všemi články a nebo pro stránky s kategoriemi
        if self.category_page:

            # Získání kategorií pokud je zapnutá navigace pro kategorie
            if self.category_navigation:

                # Přidání množiny kategorií do kontextu
                categories = ArticleCategory.get_all_category_except_default()
                context['categories'] = categories

                # Přidání jména aktuální záložky
                context['current_tab'] = self.current_category_tab

            else:

                # Přidání jména aktuální záložky
                context['current_tab'] = self.current_category_tab

                # Přidání jména aktuální záložky
                category_title = ArticleCategory().get_category_title_by_slug(self.current_category_tab)
                context['current_tab_name'] = category_title

        elif self.tag_page:
            print("### elif self.tag_page:")

            if self.tag_navigation:
                print("### if self.tag_navigation:")
                print("### self.current_tag_tab", self.current_tag)
                context['current_tag_tab'] = self.current_tag
                context['similar_tag_articles'] = self.similar_tag_articles
            pass



        return context