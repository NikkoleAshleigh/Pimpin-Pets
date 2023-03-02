from django.contrib import admin
from pimpin_app.models import Pets

class PetsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pets)