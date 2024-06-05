from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Class for changing user and superuser identification settings.

    This class changes the user and superuser identification settings
    from username (which is default for user login) to user email.

    This step simplifies the user account creation process,
    where only an email and password are needed instead of defining a username.

    This step also affects the login process,
    where the user is required to use their email instead of a username.

    Model methods:
    - create_user: Method for creating a user instance.
    - create_superuser: Method for creating a superuser instance.
    """

    def create_user(self, email, password, **extra_fields):
        '''
        Method for creating a user instance.

        The method first checks if an email and password are provided.
        If not, it raises an exception with a request to provide them.

        Then it normalizes the email and assigns its value to the user instance,
        where it serves as the primary identifier.

        It then adds the provided password to the user instance and saves the instance.

        The method returns the newly created user instance with the defined email and password.
        '''

        if not email:
            raise ValueError("E-mail must be provided.")
        if not password:
            raise ValueError("Password must be provided.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Method for creating a superuser instance.

        The method first sets the values for the following keys:
        - is_staff: Allowing access to manage the application or its administrative functions.
        - is_superuser: Allowing to perform all operations and access all functions and data in the application.
        - is_active: Allowing the user to log in to the system.
        to True (creating a new key if it doesn't exist).

        Then the method checks the correct settings of these values,
        and if they are not set correctly, it raises an exception.

        The method returns a superuser instance
        by calling the user creation method
        with permissions set for a superuser.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
