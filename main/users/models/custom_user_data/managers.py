from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Třída slouží pro změnu nastavení identifikace uživatele a superuživatele.

    Tato třída mění nastavení identifikace uživatele a superuživatele
    z uživatelského jména (jen je defaultně nastaveno jako identifikátor
    pro přihlášení uživatele), na email uživatele.

    Tento krok zjednodušuje založení účtu uživatele,
    kdy při založení účtu není třeba definovat uživatelské jméno,
    ale postačuje pouze email a heslo.

    Tento krok také ovlivňuje i přihlášení do aplikace,
    kdy namísto uživatelského jména je vyžadován jeho email.

    Metody modelu:
    - create_user: Metoda pro vytvoření instance uživatele.
    - create_superuser: Metoda pro vytvoření instance superuživatele.
    """

    def create_user(self, email, password, **extra_fields):
        '''
        Metoda pro vytvoření instance uživatele.

        Metoda nejprve zkontroluje, zda byl zadaný email a heslo.
        Pokud ne, vyvolá výjimku s požadavkem na zadání.

        Následně provede normalizaci emailu,
        a přiřadí jeho hodnotu do instance user,
        kde bude sloužit jako hlavní identifikátor.

        Poté přidá k instanci uživatele i zadané heslo,
        a instanci uloží.

        Metoda navrací nově založenou instanci uživatele
        s definovaným emailem a heslem.
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
        Metoda pro vytvoření instance superuživatele.

        Metoda nejprve změní hodnotu pro klíče:
        - is_staff: Povolení ke správě aplikace nebo jejím administrativním funkcím.
        - is_superuser: Povolení provádět všechny operace a mít přístup ke všem funkcím a datům v aplikaci.
        - is_active: Povolení uživatelovi přihlašovat se do systému.
        Na hodnotu True (pokud klíč neexistuje, vytvoří nový).

        Metoda následně provede kontrolu správného nastavení těchto hodnot,
        a pokud nejsou správně nastavené, vyvolá výjimku.

        Metoda navrací instanci superuživatele
        voláním metody pro založení uživatele
        s nastavenými právy pro superuživatele.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
