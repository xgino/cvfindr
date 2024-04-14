from django.contrib import admin
from .models import Site

# Register your models here.
@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'mail')
    search_fields = ('name', 'address', 'phone', 'mail')

    # Disable the delete button
    def has_delete_permission(self, request, obj=None):
        return False

    # Disable "Save and add another" and "Save and continue editing" buttons
    def has_add_permission(self, request):
        return False
