from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models.user_profile_model import UserProfile

# Unregister initial User
admin.site.unregister(User)

# Register UserProfile with UserAdmin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')


# Registret extend User model with UserProfileInline
admin.site.register(User, UserAdmin)