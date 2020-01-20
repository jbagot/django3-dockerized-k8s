from django.contrib import admin
from api.models import Animal, AnimalType


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
