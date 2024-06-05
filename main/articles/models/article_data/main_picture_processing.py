import os

from common_data.image_processing import image_processing


def main_picture_processing(self):
    '''
    Method for creating resized variants of the main article picture.

    This method is used in the post_save signal 'handle_picture_post_save' for modifying the main picture.

    The method first creates a list with dictionaries containing parameters for image transformation 'pictures_parameters'.
    Then, the function creates variables needed for the following loop,
    where it iterates over each item (dictionary) in the 'pictures_parameters' list.
    Here, the function for processing and saving the new image according to the given parameters is called first,
    which returns the relative path to the image, and it's saved in the 'picture_paths' dictionary.

    After the loop, the method checks if the uploaded image
    is still at its location and deletes it.

    The method returns a dictionary with relative paths to the new images,
    which is used for saving the paths to the database,
    in the post_save signal for modifying the main article picture.
    '''

    # List with image data
    pictures_parameters = [
        {'name': 'max-size', 'width': 1920, 'aspect_ratio': 'as_original'},
        {'name': 'for_article', 'width': 800, 'aspect_ratio': 'as_original'},
        {'name': 'preview', 'width': 440, 'aspect_ratio': 4/3},
        {'name': 'thumbnail', 'width': 150, 'aspect_ratio': 1},
    ]

    # Get the path to the original file and create a variable with the image opened in PIL
    image_path = self.main_picture_max_size.path
    instance = self
    name = 'article'

    # Loop through the list with image data
    picture_paths = {}
    for image_parameters in pictures_parameters:
        relative_picture_path = image_processing(image_path, image_parameters, instance, name)
        picture_paths[image_parameters['name']] = relative_picture_path

    # Remove the uploaded image
    if os.path.exists(image_path):
        os.remove(image_path)

    return picture_paths
