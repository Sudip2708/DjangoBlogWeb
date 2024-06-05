class AnonymousPropertyMixin:
    '''
    Mixin for the class AnonymousUserWithSettings adding properties.

    This mixin adds the following properties to the class:
    - is_authenticated: Property indicating that the user is not authenticated.
    - is_anonymous: Property indicating that the user is an anonymous user.
    - is_staff: Property indicating that the user is not in the staff group.
    - is_superuser: Property indicating that the user is not a superuser.
    - is_active: Property indicating that the user account is not active.
    '''
    @property
    def is_authenticated(self):
        return False

    @property
    def is_anonymous(self):
        return True

    @property
    def is_staff(self):
        return False

    @property
    def is_superuser(self):
        return False

    @property
    def is_active(self):
        return False
