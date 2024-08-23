from django.db import models
from . import choices


class Car(models.Model):
    '''Model for car information'''
    Make = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Category = models.CharField(max_length=50, choices=choices.CAR_TYPES)
    Name = models.CharField(max_length=100)
    Transmission = models.CharField(max_length=50, choices=choices.TRANSMISSION_TYPES, default=choices.EXTERIOR_TYPES[0][0])
    Color = models.CharField(max_length=50)
    Mileage = models.CharField(max_length=50)
    Fuel = models.CharField(choices=choices.FUEL_TYPES, max_length=50)
    BHP = models.IntegerField()
    Torque = models.IntegerField()
    CC = models.IntegerField()
    CO2 = models.IntegerField()
    Year = models.IntegerField()
    Insurance = models.CharField(max_length=100)
    About = models.CharField(max_length=500)


class VehicleDetails(models.Model):
    '''Vehicle Details for car registration'''
    Car = models.ForeignKey(Car,  related_name='CarInfo', on_delete=models.CASCADE)
    Registration = models.CharField(max_length=50)
    Year = models.IntegerField()
    Mileage = models.IntegerField()
    Color = models.CharField(max_length=50)
    FuelType = models.CharField(max_length=50, choices=choices.FUEL_TYPES)
    Transmission = models.CharField(max_length=50, choices=choices.EXTERIOR_TYPES, default=choices.EXTERIOR_TYPES[0][0])
    ServiceHistory = models.CharField(max_length=255)
    ServiceBookPresent = models.CharField(max_length=255)
    LastServiceDate = models.DateField()
    LastServiceMileage = models.IntegerField()
    NumberOfKeys = models.IntegerField()
    IsTheCarModified = models.BooleanField()
    TyreBrand = models.CharField(max_length=100)
    TyreCondition = models.CharField(max_length=100)
    ConditionDamageReport = models.CharField(max_length=255)
    OutstandingFinance = models.CharField(max_length=100)
    DesiredValue = models.IntegerField()


class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')


class Plates(models.Model):
    Number = models.CharField(max_length=50)
    Document = models.CharField(max_length=50)
    Transfer = models.CharField(max_length=50)
    Price = models.IntegerField()
