from django.contrib import admin

from mezzanine.core.admin import SingletonAdmin
from home.models import HomePage

# Register your models here.
class HomePageAdmin(SingletonAdmin):
        pass

admin.site.register(HomePage, HomePageAdmin)
