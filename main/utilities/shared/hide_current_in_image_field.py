from django import forms


def hide_current_in_image_field():
    '''
    Metoda pro odebrání zobrazení pole Current z ImageField.

    :return: Upravené pole ImageField
    '''

    return forms.ImageField(
        required=False,
        error_messages = {'invalid':"Image files only"},
        widget=forms.FileInput
    )



