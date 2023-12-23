### Definuje formuláře (na webu) pro aplikaci.


from django import forms
from posts.models.post import Post
from posts.models.comment import Comment
from .tiny_mce_winget import TinyMCEWidget


class PostForm(forms.ModelForm):
    '''
    Definice formuláře pro model Post s použitím TinyMCEWidgetu

    Nápověda:
    models.CharField(): pole, které představuje textový řetězec v databázi
    widget=TinyMCEWidget(...): Specifikuje použití vlastního widgetu TinyMCEWidget pro pole content formuláře
    '''
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        '''
        Obsahuje informace o konkrétním chování formuláře vzhledem k modelu.

        Nápověda:
        model = Post: Specifikuje, který model bude tento formulář reprezentovat, v tomto případě Post.
        fields = ('title', 'overview', ...): Určuje, která pole z modelu budou zahrnuta ve formuláři.
        '''
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail',
        'categories', 'featured', 'previous_post', 'next_post')