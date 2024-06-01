from asgiref.sync import sync_to_async

async def handle_picture_post_save(user):
    '''
    Asynchronní handler pro zachycení post_save signálu pro zpracování nově uloženého profilového obrázku.

    Handler pracuje s atributem, který formulář nastaví na hodnotu True,
    pokud je součástí formuláře i nový profilový obrázek uživatele.

    Nejprve handler volá metodu, která pro daný obrázek zpracuje a vytvoří jeho miniaturu.
    Poté tyto obrázky přiřadí k příslušným polím v modelu a uloží je.

    '''

    # Kontrola změny profilového obrázku
    if user.new_picture:

        # Spuštění procesu pro úpravu obrázku
        picture_paths = user.profile_picture_processing()
        user.new_picture = False

        # Aktualizace polí v modelu uživatele
        user.profile_picture = picture_paths['profile_picture']
        user.profile_picture_thumbnail = picture_paths['thumbnail']

        # Uložení změn v databázi
        await sync_to_async(user.save)()
