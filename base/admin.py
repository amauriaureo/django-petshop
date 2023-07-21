from django.contrib import admin

from base.models import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    pass
