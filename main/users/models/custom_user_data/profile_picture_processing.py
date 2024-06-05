import os
from common_data.image_processing import image_processing

def profile_picture_processing(self):
    '''
    Method for creating size variants of the user's profile picture.

    The method is used in the post_save signal 'handle_picture_post_save' to modify the profile picture.

    The method first creates a list of dictionaries with parameters for image transformation 'pictures_parameters'.
    Then, it creates variables needed for the following loop,
    where it iterates through the individual items (dictionaries) of the 'pictures_parameters' list.
    Here, the function for processing and saving a new image according to the specified parameters is called,
    which returns the relative path to the image, saved in the 'picture_paths' dictionary.

    After the loop, the method checks if the uploaded image
    is still in its location, and deletes it.

    The method returns a dictionary with relative paths to the new images,
    which is used to save the paths to the database,
    in the post_save signal for modifying the profile picture.
    '''

    # List with image data
    pictures_parameters = [
        {'name': 'profile_picture', 'width': 440, 'aspect_ratio': 1},
        {'name': 'thumbnail', 'width': 150, 'aspect_ratio': 1},
    ]

    # Get the path to the original file
    image_path = self.profile_picture.path
    instance = self
    name = 'user'

    # Loop through the list with image data
    picture_paths = {}
    for image_parameters in pictures_parameters:
        relative_picture_path = image_processing(image_path, image_parameters, instance, name)
        picture_paths[image_parameters['name']] = relative_picture_path

    # Remove the uploaded image
    if os.path.exists(image_path):
        os.remove(image_path)

    return picture_paths
