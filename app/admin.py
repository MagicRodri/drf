from django.contrib import admin

from .forms import EntityForm
from .models import Entity, Property


class PropertyInline(admin.TabularInline):
    model = Entity.properties.through
    extra = 1


class EntityAdmin(admin.ModelAdmin):

    form = EntityForm
    inlines = [PropertyInline]

admin.site.register(Entity, EntityAdmin)
admin.site.register(Property)