from ...models.article_author import ArticleAuthor


def get_or_create_author(user):
    '''
    Function to retrieve an author instance based on the user's username.

    The function searches for an author instance in the ArticleAuthor model based on the user instance.
    If the user does not have an associated author account,
    it creates a new one using the 'get_or_create' method.

    The function returns the author instance.
    '''

    author, created = ArticleAuthor.objects.get_or_create(linked_user=user)
    return author
