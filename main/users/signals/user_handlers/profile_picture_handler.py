from asgiref.sync import sync_to_async

async def handle_picture_post_save(user):
    '''
    Asynchronous handler to capture the post_save signal for processing a newly saved profile picture.

    The handler works with an attribute that the form sets to True
    if a new profile picture of the user is part of the form.

    First, the handler calls a method to process and create a thumbnail for the given image.
    Then it assigns these images to the respective fields in the model and saves them.

    '''

    # Checking for a change in the profile picture
    if user.new_picture:

        # Running the image processing process
        picture_paths = user.profile_picture_processing()
        user.new_picture = False

        # Updating fields in the user model
        user.profile_picture = picture_paths['profile_picture']
        user.profile_picture_thumbnail = picture_paths['thumbnail']

        # Saving the changes to the database
        await sync_to_async(user.save)()
