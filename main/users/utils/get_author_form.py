from users.forms import AuthorProfileForm
from articles.models.article_author import ArticleAuthor


def get_author_form(request, user):
    '''
    Funkce pro načtení formulářových dat autora.

    :param user: Instance autora
    :param request: Požadavek o data
    :return: Formulář s daty autora, nebo None.
    '''

    # Ověření, zda uživatel má i účet autora
    if ArticleAuthor.user_is_author(user):

        # Načtení instance autora
        author_instance = ArticleAuthor.objects.get(user_id=user.id)

        # Ověření, zda se jedná o POST nebo GET požadavek
        if request.POST:

            # Návratová hodnota pro požadavek POST
            return AuthorProfileForm(request.POST, request.FILES, instance=author_instance)

        else:

            # Návratová hodnota pro požadavek GET
            return AuthorProfileForm(instance=author_instance)
    else:

        # Návratová hodnota když uživatel nemá účet autora
        return None