from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import venue, hkumember, CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('username','email','first_name','last_name','password1','password2')
        }),
    )
    list_display = ['username',]


admin.site.register(venue)
admin.site.register(hkumember)
admin.site.register(CustomUser, CustomUserAdmin)