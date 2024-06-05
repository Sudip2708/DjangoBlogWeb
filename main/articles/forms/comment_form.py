from django import forms

from ..models.article_comment import ArticleComment


class ArticleCommentForm(forms.ModelForm):
    '''
    Form for defining and managing selected fields of the ArticleComment model.

    This form is used in the view:
    - ArticleDetailView: Display of a specific article.

    The form is used to enter a comment for the article.
    '''

    class Meta:
        '''
        Meta class is a special inner class for form configuration.

        The Meta class provides metadata and configuration for the main class,
        and here it defines the following attributes:
        - model: Specifies the model on which the form is based.
        - fields: Defines the fields to be included in the form.
        - widgets: Allows specifying custom widgets for individual form fields.

        Widgets used in this code:
        - forms.Textarea: Field for entering longer text (limited to 4 rows here).
        '''

        model = ArticleComment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type your comment here',
                'id': 'usercomment',
                'rows': '4'
            }),
        }
