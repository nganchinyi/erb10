from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published', "chef",'list_date'
    list_display_links = 'id', 'title'
    list_filter = 'chef', 'list_date'
    list_editable = 'is_published',
    search_fields = 'title', 'description', 'district',
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)