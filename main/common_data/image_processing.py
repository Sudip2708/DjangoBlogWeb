import os
from PIL import Image

from .image_resize_and_crop import image_resize_and_crop


def image_processing(image_path, image_parameters, instance, name):
    '''
    Function for processing a new image and replacing the original.

    This function is used in the following files:
    - articles/models/article_data/main_picture_processing.py
    - articles/models/article_author_data/profile_picture_processing.py
    - users/models/custom_user_data/profile_picture_processing.py

    The function expects the following parameters:
    - image_path: Path to the processed image.
    - image_parameters: Parameters for image processing.
    - id: ID instance for
    - name: Name of the model the image relates to.

    The function first opens the image in PIL and then extracts values from the parameters
    for the image aspect ratio and the desired maximum width.
    It then calls the 'image_resize_and_crop' function to resize the image.

    The function then creates variables for the image directory path 'image_directory'
    and generates the file name from the 'name' value, 'instance_id', and the image width value.
    Together, it creates the absolute path for saving the image 'new_image_path'.

    The function then checks if there is already a file at this path.
    If so, it deletes it because it's the previous image.

    Then it saves the new image to the specified location.

    Finally, the function creates and returns the relative path to the image.
    '''

    # Resize the image
    image = Image.open(image_path)
    new_aspect_ratio = image_parameters['aspect_ratio']
    new_width = image_parameters['width']
    processed_image = image_resize_and_crop(image, new_width, new_aspect_ratio)

    # Get the path for saving the image
    image_directory = os.path.dirname(image_path)
    new_image_name = f'{name}-{instance.id:08d}-{image_parameters["width"]:04d}.jpg'
    new_image_path = os.path.join(image_directory, new_image_name)

    # Remove the original image
    if os.path.exists(new_image_path):
        os.remove(new_image_path)

    # Save the new image to the media folder
    processed_image.save(new_image_path)

    # Create and return the relative path to the image
    relative_picture_path = os.path.join(instance.upload_path, new_image_name)
    return relative_picture_path
