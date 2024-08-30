from django.contrib import admin
from . import models


class ImageInline(admin.TabularInline):
    model = models.CarImage
    extra = 3

class CarSubPhotoInline(admin.TabularInline):
    model = models.CarSubmissionPhoto
    extra = 3


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('Make', 'Model')
    inlines = [ImageInline]


@admin.register(models.CarSubmission)
class DetailAdmin(admin.ModelAdmin):
    inlines = [CarSubPhotoInline]
    list_display = ('Make', 'Model', )


@admin.register(models.Plates)
class PlatesAdmin(admin.ModelAdmin):
    list_display = ('Number', 'Price', )

@admin.register(models.FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(models.TransmissionType)
class TransmissionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(models.TyreCondition)
class TyreConditionAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.TyreBrand)
class TyreBrandAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Body)
class BodyAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', )

@admin.register(models.Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'PhoneNumber', )