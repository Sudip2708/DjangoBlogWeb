
def index_selected_articles_content(self, selected_articles):
    '''
    Metoda pro indexaci obsahu vybraných článků. (Vhodné pro hromadnou reindexaci)

    Tato metoda slouží k indexaci obsahu všech vybraných článků. Pro každý článek provede následující kroky:
    - Převede HTML obsah na čistý text a normalizuje na malá písmena.
    - Normalizuje titulek, přehled a autora na malá písmena.
    - Získá ID tagů článku.
    - Vloží aktualizovaný dokument do indexu.

    :param selected_articles: Seznam vybraných článků, které mají být zaindexovány.
    :return: None
    '''

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