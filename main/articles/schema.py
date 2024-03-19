print("### Schema: ArticleSchema")

import os
from whoosh.index import create_in, open_dir
from whoosh.fields import SchemaClass, TEXT, DATETIME, ID, KEYWORD
from bs4 import BeautifulSoup
from django.conf import settings


class ArticleSchema:
    """Třída schématu pro indexování článků."""

    def __init__(self):
        """
        Inicializuje instanci schématu a vytváří Whoosh index.
        """

        # Vytvoření Whoosh indexu
        self.ix = self.create_index()

    def create_index(self):
        """
        Vytvoří index Whoosh v adresáři nastaveném v settings.

        Returns:
            whoosh.index.Index: Inicializovaný index Whoosh.
        """

        # Vytvoření složky
        if not os.path.exists(settings.INDEX_DIRECTORY):
            os.makedirs(settings.INDEX_DIRECTORY)

        # Načtení složky
        if not os.listdir(settings.INDEX_DIRECTORY):
            ix = create_in(settings.INDEX_DIRECTORY, self.get_schema())
        else:
            ix = open_dir(settings.INDEX_DIRECTORY)

        # Navrácení složky
        return ix


    def get_schema(self):
        """
        Vrací schéma pro indexování článků.

        Returns:
            whoosh.fields.Schema: Schéma pro indexování článků.
        """
        return SchemaClass(
            id=ID(stored=True, unique=True),
            slug=ID(stored=True),

            title=TEXT(stored=True),
            overview=TEXT(stored=True),
            content=TEXT(stored=True),

            author=ID(stored=True),

            created=DATETIME(stored=True),
            updated=DATETIME(stored=True),
            published=DATETIME(stored=True),

            tags=ID(stored=True),
            category=ID(stored=True),
            status=TEXT(stored=True)
        )


    def find_all_articles_by_status(self, status):
        """
        Vyhledá a vrátí seznam ID článků daného stavu seřazených podle data publikování.

        Args:
            status: Stav článků pro vyhledání (např. 'publish').

        Returns:
            List: Seznam ID článků.
        """
        print("### find_articles_by_status(self, status)")

        article_ids = []

        # Otevření searcheru
        with self.ix.searcher() as searcher:
            results = searcher.documents(status=status)

            # Procházení výsledků a přidání ID článků do seznamu
            for doc in results:
                article_ids.append(doc['id'])

        return article_ids


    def find_all_articles_by_category(self, category_ID):
        """
        Vyhledá a vrátí seznam ID článků daného stavu seřazených podle data publikování.

        Args:
            status: Stav článků pro vyhledání (např. 'publish').

        Returns:
            List: Seznam ID článků.
        """
        print("### find_all_articles_by_category(self, category_ID)")

        article_ids = []

        # Otevření searcheru
        with self.ix.searcher() as searcher:
            results = searcher.documents(category=category_ID)

            # Procházení výsledků a přidání ID článků do seznamu
            for doc in results:
                article_ids.append(doc['id'])

        return article_ids

    def find_all_articles_by_tag(self, tag_ID):
        """
        Vyhledá a vrátí seznam ID článků s daným tagem seřazených podle data publikování.

        Args:
            tag_ID: ID tagu pro vyhledání.

        Returns:
            List: Seznam ID článků.
        """
        print("### find_all_articles_by_tag(self, tag_ID)")

        article_ids = []

        # Otevření searcheru
        with self.ix.searcher() as searcher:
            results = searcher.documents(tags=tag_ID)

            # Procházení výsledků a přidání ID článků do seznamu
            for doc in results:
                article_ids.append(doc['id'])

        return article_ids

    def index_all_article_content(self, selected_articles):
        """
        Indexuje obsah všech článků pro full-text vyhledávání.
        """
        print("### index_all_articles(cls)")

        # Otevření writeru mimo cyklus
        writer = self.ix.writer()

        # Procházení všech článků a jejich indexace
        for article in selected_articles:
            # Převod HTML obsahu na čistý text a normalizace na malá písmena
            soup = BeautifulSoup(article.content, 'html.parser')
            normalized_content = soup.get_text(strip=True).lower()

            # Normalizace titulku, přehledu a autora na malá písmena
            normalized_title = article.title.lower()
            normalized_overview = article.overview.lower()

            # Získání ID tagů
            tag_ids = [str(tag.id) for tag in article.tags.all()]


            # Vložení aktualizovaného dokumentu
            writer.add_document(
                id=str(article.id),
                slug=article.slug,

                title=normalized_title,
                overview=normalized_overview,
                content=normalized_content,

                author=str(article.author.id),

                created=article.created,
                updated=article.updated,
                published=article.published,

                tags=tag_ids,
                category=str(article.category.id),
                status=article.status
            )

        # Uzavření writeru a commit změn mimo cyklus
        writer.commit()


    def index_article_content(self, article_instance):
        """
        Aktualizuje index obsahu článku pro full-text vyhledávání.
        """
        print("### index_article_content(cls, article_instance)")

        # Načtení writeru
        writer = self.ix.writer()

        # Odstranění existujícího dokumentu pro danou instanci článku pomocí ID
        article_id = article_instance.id
        writer.delete_by_term('id', str(article_id))

        # Normalizace titulku, přehledu a autora na malá písmena
        normalized_title = article_instance.title.lower()
        normalized_overview = article_instance.overview.lower()

        # Převod HTML obsahu na čistý text a normalizace na malá písmena
        soup = BeautifulSoup(article_instance.content, 'html.parser')
        normalized_content = soup.get_text(strip=True).lower()

        # Získání ID tagů
        tag_ids = [str(tag.id) for tag in article_instance.tags.all()]

        writer.add_document(
            id=str(article_instance.id),
            slug=article_instance.slug,

            title=normalized_title,
            overview=normalized_overview,
            content=normalized_content,

            author=str(article_instance.author.id),

            created=article_instance.created,
            updated=article_instance.updated,
            published=article_instance.published,

            tags=tag_ids,
            category=str(article_instance.category.id),
            status=article_instance.status
        )

        # Zapsání změn
        writer.commit()


    def print_all_index_articles_title(self):
        """
        Vytiskne názvy všech indexovaných článků.
        """
        print("### print_articles_titles(cls)")

        # Inicializace seznamu názvů článků
        article_titles = []

        # Procházení všech dokumentů v indexu
        with self.ix.searcher() as searcher:
            # Vytáhnutí všech dokumentů
            results = searcher.documents()

            # Pro každý dokument získání názvu článku a přidání do seznamu
            for doc in results:
                article_titles.append(doc['author'])

        # Vytisknutí seznamu názvů článků
        print("Indexované články:")
        for title in article_titles:
            print(title)


    def find_articles_by_author(self, author_name):
        """
        Vyhledá a vrátí seznam ID článků daného autora.

        Args:
            author_name: Jméno autora (string).

        Returns:
            List: Seznam ID článků.
        """
        print("### find_articles_by_author(self, author_name)")

        # Normalizace jména autora na malá písmena
        normalized_author_name = author_name.lower()
        print("### normalized_author_name:", normalized_author_name)

        article_id = []

        # Otevření searcheru
        with self.ix.searcher() as searcher:
            print("### with self.ix.searcher() as searcher")

            results = searcher.documents()

            # Pro každý dokument získání názvu článku a přidání do seznamu
            for doc in results:
                if doc['author'] == normalized_author_name:
                    article_id.append(doc['id'])

            print("### article_id:", article_id)

        return article_id


    def update_author_name(self, old_author_name, new_author_name):
        """
        Aktualizuje jméno autora v indexu Whoosh pro všechny jeho články.

        Args:
            old_author_name: Původní jméno autora (string).
            new_author_name: Nové jméno autora (string).
        """
        print("### update_author_name(self, old_author_name, new_author_name)")

        # Normalizace jmen
        normalized_old_author_name = old_author_name.lower()
        normalized_new_author_name = new_author_name.lower()

        # Načtení writeru
        writer = self.ix.writer()

        # Procházení všech dokumentů s daným jménem autora
        with self.ix.searcher() as searcher:
            results = searcher.documents(author=normalized_old_author_name)

            # Aktualizace jména autora v dokumentech
            for doc in results:
                writer.update_document(id=doc['id'], author=normalized_new_author_name)

        # Zapsání změn
        writer.commit()
