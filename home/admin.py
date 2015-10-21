from django.contrib import admin

from mezzanine.core.admin import SingletonAdmin
from home.models import FeaturedBox, LeftPanel, CenterPanel

# Register your models here.
class FeaturedBoxAdmin(SingletonAdmin):
        pass

admin.site.register(FeaturedBox, FeaturedBoxAdmin)

class LeftPanelAdmin(SingletonAdmin):
        pass

admin.site.register(LeftPanel, LeftPanelAdmin)

class CenterPanelAdmin(SingletonAdmin):
        pass

admin.site.register(CenterPanel, CenterPanelAdmin)
