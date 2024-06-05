def image_resize_and_crop(image, new_width='as_original', new_aspect_ratio='as_original'):
    '''
    Function for resizing and cropping an image.

    This function is part of the file common_data/image_processing.py,
    which is used in the following files:
    - articles/models/article_data/main_picture_processing.py
    - articles/models/article_author_data/profile_picture_processing.py
    - users/models/custom_user_data/profile_picture_processing.py

    The function expects the following parameters:
    - image: Image opened in PIL.
    - new_width: Desired width of the image in px (optional parameter).
    - new_aspect_ratio: Desired aspect ratio of the new image (width/height) (optional parameter).

    The function first creates a copy of the image and defines basic variables:
    - width: Image width value (in px).
    - height: Image height value (in px).
    - image_aspect_ratio: Aspect ratio value.

    Then the function checks if it was specified not to change the aspect ratio
    (new_aspect_ratio='as_original'). If so, it calculates the new_aspect_ratio value
    from the image height and width (this is needed in case the image will be resized, and its height needs to be calculated).

    If a value for the aspect ratio (new_aspect_ratio) is set,
    the function first determines if the new ratio is greater than the image aspect ratio.
    If so, it calculates the new height according to the new ratio and sets the crop values.
    If not, it calculates the new width according to the new ratio and sets the crop values.
    Then the function crops the image according to the calculated values.

    Then the function checks if a desired width for the image was specified
    and if the image width is greater than the desired width.
    If so, it calculates the desired height according to the ratio and resizes the image.

    The function returns the modified image opened in PIL.
    '''

    # Create a copy of the image and define basic variables
    new_image = image.copy()
    width, height = image.size
    image_aspect_ratio = width / height

    # When not changing the aspect ratio
    if new_aspect_ratio == 'as_original':

        # Set the image aspect ratio as the desired aspect ratio
        new_aspect_ratio = image_aspect_ratio

    else:

        # When the new dimension is 'wider' than the original image (height will be cropped)
        if new_aspect_ratio > image_aspect_ratio:
            img_height = int(width / new_aspect_ratio)
            top = (height - img_height) / 2
            bottom = height - top
            left, right = 0, width

        # When the new dimension is 'narrower' than the original image (width will be cropped)
        else:
            img_width = int(height * new_aspect_ratio)
            left = (width - img_width) / 2
            right = width - left
            top, bottom = 0, height

        # Crop the image
        new_image = new_image.crop((left, top, right, bottom))

    # When a desired width is specified and the image width is greater than the desired width
    if new_width != 'as_original' and width > new_width:

        # Calculate the desired height and resize the image
        new_height = int(new_width / new_aspect_ratio)
        new_image = new_image.resize((new_width, new_height))

    return new_image
