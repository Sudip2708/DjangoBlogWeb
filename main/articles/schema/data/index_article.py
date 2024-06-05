from whoosh.index import open_dir
from django.conf import settings
from bs4 import BeautifulSoup


def index_article(self, article):
    '''
    Method of the ArticleSchema class for indexing an article.

    This method expects an instance of the article to be indexed.
    First, it opens the index file and then loads the methods for writing.

    Then, it retrieves the content of the 'content' field, which is HTML content from TinyMCE,
    and converts the HTML text to normal text using the BeautifulSoup methods and get_text,
    and then removes whitespace characters at the beginning and end of the text.

    The method assigns all indexed fields to the index
    and saves the changes.
    '''

    # Open the index file for writing.
    ix = open_dir(settings.INDEX_DIRECTORY)
    writer = ix.writer()

    # Convert HTML content to text.
    html_content = article.content
    text_content = BeautifulSoup(html_content, 'html.parser').get_text(strip=True)

    # Update field values in the index and save the changes.
    writer.update_document(
        id=str(article.id),
        title=article.title,
        overview=article.overview,
        content=text_content,
        author=str(article.author.id),
        published=article.published,
    )

    writer.commit()
