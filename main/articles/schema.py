print("### Schema: ArticleSchema")

import os
from whoosh.index import create_in, open_dir
from whoosh.fields import SchemaClass, TEXT, DATETIME, ID
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

        if not os.path.exists(settings.INDEX_DIRECTORY):
            os.makedirs(settings.INDEX_DIRECTORY)

        if not os.listdir(settings.INDEX_DIRECTORY):
            ix = create_in(settings.INDEX_DIRECTORY, self.get_schema())
        else:
            ix = open_dir(settings.INDEX_DIRECTORY)

        return ix

    def get_schema(self):
        """
        Vrací schéma pro indexování článků.

        Returns:
            whoosh.fields.Schema: Schéma pro indexování článků.
        """
        return SchemaClass(
            id=ID(stored=True, unique=True),  # Přidání pole 'id'
            title=TEXT(stored=True),
            overview=TEXT(stored=True),
            content=TEXT(stored=True),
            author=TEXT(stored=True),
            updated=DATETIME(stored=True)
        )

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
            content_text = soup.get_text(strip=True).lower()

            # Normalizace titulku, přehledu a autora na malá písmena
            normalized_title = article.title.lower()
            normalized_overview = article.overview.lower()
            normalized_author = article.author.author.lower()

            # Vložení aktualizovaného dokumentu
            writer.add_document(id=str(article.id),
                                title=normalized_title,
                                overview=normalized_overview,
                                content=content_text,
                                author=normalized_author,
                                updated=article.updated)

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
        normalized_author = article_instance.author.author.lower()

        # Převod HTML obsahu na čistý text a normalizace na malá písmena
        soup = BeautifulSoup(article_instance.content, 'html.parser')
        normalized_content = soup.get_text(strip=True).lower()

        # Vložení aktualizovaného dokumentu
        writer.add_document(
            id=str(article_instance.id),  # Přidání identifikátoru článku
            title=normalized_title,
            overview=normalized_overview,
            content=normalized_content,
            author=normalized_author,
            updated=article_instance.updated
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
