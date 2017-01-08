from django.contrib import admin
from web.models import HomePage

class HomePageAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(HomePage, HomePageAdmin)