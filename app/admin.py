from django.contrib import admin

# Register your models here.
from .models import Site, Group, Client
from .forms import SiteAdminForm

class SiteAdmin(admin.ModelAdmin):
    form = SiteAdminForm
    filter_horizontal = ('groups',)
    raw_id_fields = ('client',)
    
class GroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('subgroups',)
    raw_id_fields = ('client',)

admin.site.register(Site, SiteAdmin) #links the model and the form
admin.site.register(Group, GroupAdmin)
admin.site.register(Client)
