print("### 09 main/users/managers.py")

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        # Check if a valid email is provided
        if not email:
            raise ValueError(_("The Email must be set"))

        # Normalize the email for consistency
        email = self.normalize_email(email)

        # Create a new user instance with the provided email and extra fields
        user = self.model(email=email, **extra_fields)

        # Set the user's password
        user.set_password(password)

        # Save the user to the database
        user.save()

        # Set default profile image if not provided
        if not user.profile_picture:
            default_image_path = os.path.join("images", "profile_pictures", "users", "default.jpg")
            user.profile_picture = default_image_path

        # Return the created user
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        # Set default values for is_staff, is_superuser, and is_active
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        # Ensure is_staff and is_superuser are True for a SuperUser
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        # Call the create_user method to create a superuser
        return self.create_user(email, password, **extra_fields)
