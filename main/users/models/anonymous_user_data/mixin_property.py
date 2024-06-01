class AnonynousPropertyMixin:
    '''
    Mixin pro třídu AnonymousUserWithSettings přidávající třídě property.

    Tento mixin přidává třídě následující vlastnosti:
    - is_authenticated: Vlastnost oznamující, že uživatel není přihlášen.
    - is_anonymous: Vlastnost oznamující, že uživatel je anonymním uživatelem.
    - is_staff: Vlastnost oznamující, že uživatel není ve skupině staff.
    - is_superuser: Vlastnost oznamující, že uživatel není superuživatel.
    - is_active: Vlastnost oznamující, že účet uživatele není aktivní.
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
