from django import forms

from homepage.models.gallery_section import HomePageGallerySection


class GallerySectionForm(forms.ModelForm):
    '''
    Formulář pro editaci nastavení Gallery sekce domácí stránky.

    Tato třída formuláře slouží k vytvoření formuláře pro úpravu nastavení této sekce.
    Obsahuje pole pro zobrazení a editaci jednotlivých nastavení,
    jako je například zobrazení sekce a výběr významných článků.
    '''

    class Meta:
        '''
        Meta třída pro specifikaci modelu a polí, která budou zahrnuta ve formuláři.

        Tato meta třída definuje strukturu a vzhled formuláře pro editaci nastavení této sekce.
        Obsahuje informace o tom, který model je použit pro tento formulář,
        jaká pole jsou zahrnuta a jaké widgety jsou použity pro jejich zobrazení.
        '''

        # Nastavení modelu a prázdného seznamu pro pole sekce
        model = HomePageGallerySection
        fields = ['display_gallery_section', 'gallery_article_1', 'gallery_article_2', 'gallery_article_3', 'gallery_article_4']

        # Nastavení vzhledu widgetů pro pole formuláře
        widgets = {
            'display_gallery_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gallery_article_1': forms.Select(attrs={'class': 'form-control'}),
            'gallery_article_2': forms.Select(attrs={'class': 'form-control'}),
            'gallery_article_3': forms.Select(attrs={'class': 'form-control'}),
            'gallery_article_4': forms.Select(attrs={'class': 'form-control'}),
        }
