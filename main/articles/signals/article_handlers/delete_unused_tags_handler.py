from taggit.models import (
    Tag,
    TaggedItem,
)


def handle_delete_unused_tags_post_save(article):
    '''
    Handler for processing post-save requests to check and potentially delete tags.

    The handler is attached to the Articles model and checks its attribute self.tags_to_delete,
    which is a list of deleted tags populated by the save method in the form when checking tag state changes.

    If the list contains any tags, a loop is executed to iterate through this list,
    and for each found tag, a variable with its instance is created. Then, based on this instance,
    all occurrences of the tag in the intermediate table are searched, and their count is calculated.

    If the resulting count is 0, the tag is deleted.

    If the resulting count is 1, the ID of the current article is compared to the ID of the article to which the tag is assigned.
    If the IDs match, the tag is deleted.

    Finally, the 'tags_to_delete' attribute of the instance is set to an empty list.
    '''

    # Check if any tags have been deleted
    if article.tags_to_delete:

        # Loop to iterate through the list of deleted tags
        for tag_name in article.tags_to_delete:

            # Get the tag instance and the count of occurrences in the intermediate table
            tag = Tag.objects.get(name=tag_name)
            tagged_items = TaggedItem.objects.filter(tag_id=tag.id)
            tagged_items_count = tagged_items.count()

            # If the tag does not occur in the intermediate table, it is deleted
            if tagged_items_count == 0:
                tag.delete()

            # If the tag occurs only in the current article (from which it was deleted), it is deleted
            elif tagged_items_count == 1:
                article_id = tagged_items.first().object_id
                if article_id == article.id:
                    tag.delete()

        # Empty the list for checking deleted tags
        article.tags_to_delete = []
