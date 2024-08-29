# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, RequestedService

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'date_of_birth', 'field_of_work', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'field_of_work')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'field_of_work')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(RequestedService)
class RequestedServiceAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'address', 'service_time', 'date_requested']
    list_filter = ['date_requested', 'service__field']
    search_fields = ['user__username', 'service__name', 'address']