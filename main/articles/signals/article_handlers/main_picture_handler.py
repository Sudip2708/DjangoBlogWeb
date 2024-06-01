from asgiref.sync import sync_to_async


async def handle_picture_post_save(article):
    '''
    Asynchronní handler pro zachycení post_save signál pro zpracování nově uloženého obrázku.

    Handler pracuje s atributem, kterému formulář dodá hodnotu True,
    pokud je ssoučástí formuláře i hlavní obrázek k článku.

    Signál nejprve volá metodu, která pro daný obrázek vytvoří 4 různé velikosti.
    A po té tyto obrázky přiřadí k příslušným polím a uloží.
    '''

    # Kontrola zda byl změněn profilový obrázek
    if article.new_picture:

        # Zpuštění procesu pro úpravu obrázku
        picture_paths = article.main_picture_processing()
        article.new_picture = False

        # Aktualizace jednotlivých polí v modelu článku
        article.main_picture_max_size = picture_paths['max-size']
        article.main_picture_for_article = picture_paths['for_article']
        article.main_picture_preview = picture_paths['preview']
        article.main_picture_thumbnail = picture_paths['thumbnail']

        # Uložení změn v databázi
        await sync_to_async(article.save)()



