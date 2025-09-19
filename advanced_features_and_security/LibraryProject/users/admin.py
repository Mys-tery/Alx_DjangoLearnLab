from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Show these fields in the admin list view
    list_display = ("username", "email", "date_of_birth", "is_staff")

    # Allow search by these fields
    search_fields = ("username", "email")

    # Add custom fields to the user form
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Add custom fields when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
