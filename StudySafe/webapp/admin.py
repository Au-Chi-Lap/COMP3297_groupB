from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import venue, hkumember, CustomUser, entryrecord
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name','is_device','is_taskforce'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Additional info', {
            'fields': ('is_device', 'is_taskforce')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Additional info', {
            'fields': ('is_device', 'is_taskforce')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )



admin.site.register(venue)
admin.site.register(hkumember)
admin.site.register(entryrecord)
admin.site.register(CustomUser, CustomUserAdmin)