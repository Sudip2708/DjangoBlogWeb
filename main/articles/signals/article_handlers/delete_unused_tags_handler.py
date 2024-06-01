from taggit.models import Tag, TaggedItem

def handle_delete_unused_tags_post_save(article):
    '''
    Handler pro zpracování post-save požadavku pro kontrolu a případné smazání tagů.

    Handler je připojen k modelu Articles a kontroluje jeho atribut self.tags_to_delete, což je seznam smazaných tagů,
    který je naplněn metodou save ve formuláři při kontrole změny stavu tagů.

    Pokud seznam obsahuje nějaký tag, provede se cyklus, který projde tento seznam a pro každý nalezený tag
    vytvoří proměnnou s jeho instancí. Poté se na základě této instance vyhledají všechny výskyty daného tagu
    ve vazební tabulce a spočítá se jejich počet.

    Pokud je výsledná hodnota 0, tag je odstraněn.

    Pokud je výsledná hodnota 1, porovná se ID aktuálního článku s ID článku, ke kterému je tag přiřazen.
    Pokud jsou ID shodná, tag je odstraněn.

    Nakonec se atribut 'tags_to_delete' instance nastaví na prázdný seznam.
    '''

    # Kontrola, zda došlo ke smazání nějakého tagu
    if article.tags_to_delete:

        # Cyklus pro procházení seznamem smazaných tagů
        for tag_name in article.tags_to_delete:

            # Získání instance tagu a počtu výskytů ve vazební tabulce
            tag = Tag.objects.get(name=tag_name)
            tagged_items = TaggedItem.objects.filter(tag_id=tag.id)
            tagged_items_count = tagged_items.count()

            # Pokud se tag ve vazební tabulce nevyskytuje, je odstraněn
            if tagged_items_count == 0:
                tag.delete()

            # Pokud se tag vyskytuje pouze v aktuálním článku (odkud byl smazán), je odstraněn
            elif tagged_items_count == 1:
                article_id = tagged_items.first().object_id
                if article_id == article.id:
                    tag.delete()

        # Vyprázdnění seznamu pro kontrolu smazaných tagů
        article.tags_to_delete = []
