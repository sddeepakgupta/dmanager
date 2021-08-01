from django.contrib import admin

# Register your models here.
from blogmanager.models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tutorial, TutorialAdmin)