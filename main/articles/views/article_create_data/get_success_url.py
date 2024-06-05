from django.urls import reverse_lazy


def get_success_url(self):
    '''
    Method to create a success URL (after successfully saving the form).

    The method first checks whether the button clicked was
    to return to the draft article and continue editing ('continue_editing'),
    or to view the article page.

    The method then returns the desired URL.
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
