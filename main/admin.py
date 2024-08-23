from django.contrib import admin
from . import models


class ImageInline(admin.TabularInline):
    model = models.CarImage
    extra = 3


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('Make', 'Model')
    inlines = [ImageInline]


@admin.register(models.VehicleDetails)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('Car',)


@admin.register(models.Plates)
class PlatesAdmin(admin.ModelAdmin):
    list_display = ('Number', 'Price', )