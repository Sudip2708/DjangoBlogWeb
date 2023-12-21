### Definuje formuláře (na webu) pro aplikaci.


from django import forms
from tinymce import TinyMCE
from .models import Post, Comment
'''
[from]
django: balíček, který obsahuje různé moduly a nástroje související s frameworkem Django
tinymce: balíček, který poskytuje nástroje pro integraci a používání WYSIWYG (What You See Is What You Get) editoru TinyMCE 
.models: balíček, který se nachází ve stejném adresáři a slouží k definici modelů databázových tabulek
[import]
forms: modul, který obsahuje různé třídy a nástroje pro práci s formuláři 
TinyMCE: třída, která reprezentuje konfiguraci a funkcionalitu TinyMCE editoru v kontextu webové aplikace
Post: třída, modelu databázové tabulky pro příspěvky
Comment: třída, modelu databázové tabulky pro komentáře
'''


class TinyMCEWidget(TinyMCE):
    '''
    Definice vlastního widgetu pro TinyMCE editor
    '''
    def use_required_attribute(self, *args):
        '''
        Metoda umožňuje ovlivnit chování povinných atributů pro pole widgetu
        :param args: funkce může přijmout libovolný počet argumentů a tyto argumenty budou předávány jako n-tice (tuple)
        :return:  Vrací False, což znamená, že nevyžaduje atribut required (povinné pole) pro toto pole. Tato metoda umožňuje ovlivnit chování povinných atributů pro pole widgetu.
        '''
        return False


class PostForm(forms.ModelForm):
    '''
    Definice formuláře pro model Post s použitím TinyMCEWidgetu

    Nápověda:
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