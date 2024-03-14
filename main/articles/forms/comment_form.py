print("### main/articles/forms/comment_form.py")

### Definuje formuláře (na webu) pro aplikaci.

from django import forms
from articles.models.article_comment import ArticleComment


class CommentForm(forms.ModelForm):
    # Pole pro obsah komentáře s vlastními atributy pro vzhled (CSS třídy, placeholder, id, atd.)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))

    class Meta:
        # Specifikace modelu, pro který je formulář vytvořen
        model = ArticleComment

        # Seznam polí, která budou zahrnuta ve formuláři
        fields = ('content',)
