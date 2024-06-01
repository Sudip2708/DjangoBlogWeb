from django.urls import reverse_lazy

def get_success_url(self):
    '''
    Metoda pro vytvoření návratové adresy (po úspěšném uložení formuláře).

    Metoda nejprve zjistí, zda bylo kliknuto na tlačítko
    s definicí návratu na rozpracovaný článek a pokračování v úpravě ('continue_editing'),
    nebo na tlačítko pro zobrazení stránky s článkem.

    Metoda následně vrací požadovanou adresu.
    '''

    if self.request.POST.get('submit_change') == 'continue_editing':
        success_url = reverse_lazy('article-update',
                                   kwargs={'slug': self.object.slug, 'current_tab': self.current_tab}
                                   )
    else:
        success_url = reverse_lazy('article-detail',
                                   kwargs={'slug': self.object.slug}
                                   )
    return success_url
