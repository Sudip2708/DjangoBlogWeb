from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group

# Odstranění registrace Group z administrátorského rozhraní
admin.site.unregister(Group)

# Registrace CustomUser do administrátorského rozhraní
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'is_superuser']