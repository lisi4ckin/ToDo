from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Account
from .forms import UserCreationForm, UserChangeForm


# Register your models here.
class AccountAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'username', 'date_of_birth', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser', )

    fieldsets = (
        (None, {'fields': ('email', 'username', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('name', 'date_of_birth',)}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'username', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'date_of_birth')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name', 'username')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)

