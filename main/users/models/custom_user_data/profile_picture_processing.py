import os
from common_data.image_processing import image_processing

def profile_picture_processing(self):
    '''
    Metoda pro vytvoření velikostních variant profilového obrázku uživatele.

    Metoda je použita v post_save signálu 'handle_picture_post_save' pro úpravu profilového obrázku.

    Metoda nejprve vytváří seznam se slovníky s parametry pro změnu obrázku 'pictures_parameters'.
    Poté funkce vytvoří proměnné potřebné pro následující cyklus,
    kde projde jednotlivé položky (slovníky) seznamu 'pictures_parameters'.
    Zde je nejprve volaná funkce pro zpracování a uložení nového obrázku dle zadaných parametrů,
    která vrací relativní cestu k obrázku, která se ukládá do slovníku 'picture_paths'.

    Po provedení cyklu metoda zkontroluje, zda nahraný obrázek
    je stále na svém umístění, a smaže ho.

    Metoda vrací slovník s relativními cestami k novým obrázkům,
    který je použit pro uložení cest do databáze,
    a to v post_save signálu pro úpravu profilového obrázku.
    '''

    # Seznam s údaji o obrázcích
    pictures_parameters = [
        {'name': 'profile_picture', 'width': 440, 'aspect_ratio': 1},
        {'name': 'thumbnail', 'width': 150, 'aspect_ratio': 1},
    ]

    # Načtení cesty k původnímu souboru
    image_path = self.profile_picture.path
    instance = self
    name = 'user'

    # Cyklus procházející seznam s údaji o obrázcích
    picture_paths = {}
    for image_parameters in pictures_parameters:
        relative_picture_path = image_processing(image_path, image_parameters, instance, name)
        picture_paths[image_parameters['name']] = relative_picture_path

    # Odstranění nahraného obrázku
    if os.path.exists(image_path):
        os.remove(image_path)

    return picture_paths
