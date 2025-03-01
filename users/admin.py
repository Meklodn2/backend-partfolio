from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_image','bio')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('profile_image','bio')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)