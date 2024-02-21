from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.models import CustomUser


# Odstranění registrace Group z administrátorského rozhraní
admin.site.unregister(Group)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    '''
    Registrace CustomUser do administrátorského rozhraní
    '''
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'is_superuser', 'linked_author_id']