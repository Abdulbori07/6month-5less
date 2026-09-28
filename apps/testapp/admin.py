from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'email',
        'username',
        'role',
        'is_verified',
        'is_staff',
        'is_active',
    )

    list_filter = (
        'role',
        'is_verified',
        'is_staff',
        'is_superuser',
        'is_active',
    )

    search_fields = (
        'email',
        'username',
    )

    ordering = (
        'email',
    )

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),

        ('Личная информация', {
            'fields': (
                'username',
                'first_name',
                'last_name',
                'bio',
                'birth_date',
            )
        }),

        ('Права доступа', {
            'fields': (
                'role',
                'is_verified',
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),

        ('Важные даты', {
            'fields': (
                'last_login',
                'date_joined',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'role',
                'is_verified',
                'is_staff',
                'is_active',
            ),
        }),
    )