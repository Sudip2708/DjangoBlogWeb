from django import forms

from ..models.article_comment import ArticleComment


class ArticleCommentForm(forms.ModelForm):
    '''
    Formulář pro definování a správu vybraných polí modelu ArticleComment.

    Formulář je použit v pohledu:
    - ArticleDetailView: Zobrazení konkrétního článku.

    Formulář slouží pro zadání komentáře k článku.
    '''

    class Meta:
        '''
        Třída Meta je speciální vnitřní třída pro konfiguraci formuláře.

        Třída Meta poskytuje metadata a konfiguraci pro hlavní třídu,
        a zde definuje následující atributy:
        - model: Určuje model, na kterém je formulář založen.
        - fields: Definuje pole, která budou zahrnuta ve formuláři.
        - widgets: Umožňuje specifikovat vlastní widgety pro jednotlivá pole formuláře.

        Widgety použité v tomto kódu:
        - forms.Textarea: Pole pro zadání delšího textu (zde omezeno na 4 řádky).
        '''

        model = ArticleComment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type your comment',
                'id': 'usercomment',
                'rows': '4'
            }),
        }
