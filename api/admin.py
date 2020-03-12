from django.contrib import admin
from django.utils.safestring import mark_safe
from api.models import *

@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    list_display = ['anunciante', 'status', 'descricao']


    def status(self, obj):
        yes_icon = '<img src="/api/static/img/baseline-check_circle_outline.svg" alt="True">'
        no_icon = '<img src="/api/static/img/baseline-highlight_off.svg" alt="False">'
        
        if obj.status:
            return mark_safe('<a target="_blank" href="%s/change/">%s</a>' % (obj.pk, yes_icon))
        else:
            return mark_safe('<a target="_blank" href="%s/change/">%s</a>' % (obj.pk, no_icon))

    status.allow_tags = True
    status.short_description = 'Status'