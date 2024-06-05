from asgiref.sync import sync_to_async


async def handle_picture_post_save(author):
    '''
    Asynchronous handler to capture the post_save signal for processing the newly saved profile picture.

    The handler works with an attribute to which the form provides a value of True
    if a new profile picture of the author is part of the form.

    First, the signal calls a method to process and create a thumbnail for the given image.
    Then it assigns these images to the respective fields in the model and saves them.
    '''

    # Checking if the profile picture has been changed
    if author.new_picture:

        # Initiating the process to process the image
        picture_paths = author.profile_picture_processing()
        author.new_picture = False

        # Updating the individual fields in the model
        author.profile_picture = picture_paths['profile_picture']
        author.profile_picture_thumbnail = picture_paths['thumbnail']

        # Saving the changes to the database
        await sync_to_async(author.save)()
