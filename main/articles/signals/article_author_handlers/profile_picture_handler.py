from asgiref.sync import sync_to_async


async def handle_picture_post_save(author):
    '''
    Asynchronní handler pro zachycení post_save signál pro zpracování nově uloženého profilového obrázku.

    Handler pracuje s atributem, kterému formulář dodá hodnotu True,
    pokud je ssoučástí formuláře i nový profilový obrázek autora.

    Signál nejprve volá metodu, která pro daný obrázek zpracuje a vytvoří jeho miniaturu.
    A po té tyto obrázky přiřadí k příslušným polím v modelu a uloží.
    '''

    # Kontrola zda byl změněn profilový obrázek
    if author.new_picture:

        # Zpuštění procesu pro úpravu obrázku
        picture_paths = author.profile_picture_processing()
        author.new_picture = False

        # Aktualizace jednotlivých polí v modelu článku
        author.profile_picture = picture_paths['profile_picture']
        author.profile_picture_thumbnail = picture_paths['thumbnail']

        # Uložení změn v databázi
        await sync_to_async(author.save)()



