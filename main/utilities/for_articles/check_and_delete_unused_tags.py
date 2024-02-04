from articles.models.article import Article

def check_and_delete_unused_tags(instance, list_of_new_tags_name):
    '''
    Metoda na zjištění zda smazané tagy k mají i jiný výskyt.
    Pokud ne, smaže tag z databáze

    :param old_tags: Staré tagy
    :param current_tags: Nové tagy
    :return: Upravená databáze tagů
    '''


    old_instance_tags = instance.tags.all()
    deleted_tags = []

    for tag in old_instance_tags:

        if tag.name not in list_of_new_tags_name:
            deleted_tags.append(tag)

    if deleted_tags:

        for tag in deleted_tags:
            if not Article.objects.filter(tags=tag).exclude(id=instance.id).exists():
                tag.delete()

