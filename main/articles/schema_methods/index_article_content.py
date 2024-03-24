from bs4 import BeautifulSoup
from articles.schema import ArticleSchema


def index_article_content(article_instance):
    '''
    Metoda pro indexaci obsahu jednoho článku.

    Tato metoda slouží k indexaci obsahu jednoho článku. Provádí následující kroky:
    - Odstraní existující dokument pro danou instanci článku pomocí ID.
    - Normalizuje titulek, přehled a autora na malá písmena.
    - Převede HTML obsah na čistý text a normalizuje na malá písmena.
    - Získá ID tagů článku.
    - Vloží aktualizovaný dokument do indexu.

    :param article_instance: Instance článku, který má být zaindexován.
    :return: None
    '''

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Načtení writeru
    writer = article_schema.ix.writer()

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

    # Vložení aktualizovaného dokumentu
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