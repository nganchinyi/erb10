from django.contrib import admin
from .models import Chef

# Register your models here.
class ChefAdmin(admin.ModelAdmin):
    list_display = "name", "email", "hire_date", "is_mvp"
    list_display_links = "name", "email"
    list_editable = "is_mvp",
    search_fields = "name",
    list_per_page = 25
    
admin.site.register(Chef, ChefAdmin)
