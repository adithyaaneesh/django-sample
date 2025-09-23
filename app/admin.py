from django.contrib import admin
from .models import App
# Register your models here.

class AppAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","phone","date")

admin.site.register(App,AppAdmin)