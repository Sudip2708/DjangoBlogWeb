from asgiref.sync import sync_to_async


async def handle_picture_post_save(article):
    '''
    Asynchronous handler for capturing the post_save signal to process newly saved images.

    The handler works with an attribute provided by the form, which is set to True
    if the main image for the article is part of the form.

    The signal first calls a method that creates 4 different sizes for the image.
    Then, these images are assigned to the corresponding fields and saved.
    '''

    # Check if the main picture has been changed
    if article.new_picture:

        # Run the process to process the image
        picture_paths = article.main_picture_processing()
        article.new_picture = False

        # Update the individual fields in the article model
        article.main_picture_max_size = picture_paths['max-size']
        article.main_picture_for_article = picture_paths['for_article']
        article.main_picture_preview = picture_paths['preview']
        article.main_picture_thumbnail = picture_paths['thumbnail']

        # Save the changes to the database
        await sync_to_async(article.save)()
