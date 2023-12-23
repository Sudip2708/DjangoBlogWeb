### Definuje formuláře (na webu) pro aplikaci.


from django import forms
from posts.models.comment import Comment


class CommentForm(forms.ModelForm):
    '''
    Definice formuláře pro komentáře

    Nápověda:
    models.CharField(): pole, které představuje textový řetězec v databázi
    widget=forms.Textarea(): specifikuje zobrazení pomocí víceřádkového textové pole (textarea)
    '''
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))

    class Meta:
        '''
        Obsahuje informace o konkrétním chování formuláře vzhledem k modelu.

        Nápověda:
        model = Comment: Specifikuje, který model bude tento formulář reprezentovat, v tomto případě Comment.
        fields = ('content'): Určuje, která pole z modelu budou zahrnuta ve formuláři.
        '''
        model = Comment
        fields = ('content', )