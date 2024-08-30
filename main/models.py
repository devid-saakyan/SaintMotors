from django.db import models
from . import choices


class TransmissionType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class FuelType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Make(models.Model):
    name = models.CharField(max_length=50, unique=True)
    logo = models.ImageField(upload_to='car_logos/')

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50, unique=True)
    make = models.ForeignKey(Make, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hex = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Body(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class TyreCondition(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class TyreBrand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    '''Model for car information'''
    Make = models.ForeignKey(Make, on_delete=models.SET_NULL, null=True, blank=True)
    Model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, blank=True)
    BodyType = models.ForeignKey(Body, on_delete=models.SET_NULL, null=True, blank=True)
    Name = models.CharField(max_length=100)
    Transmission = models.ForeignKey(TransmissionType, on_delete=models.SET_NULL, null=True, blank=True)
    Color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    Mileage = models.CharField(max_length=50)
    Fuel = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, blank=True)
    BHP = models.IntegerField()
    Torque = models.IntegerField()
    CC = models.IntegerField()
    CO2 = models.IntegerField()
    Year = models.IntegerField()
    Price = models.IntegerField()
    Insurance = models.CharField(max_length=100)
    About = models.CharField(max_length=500)

    @property
    def logo(self):
        return self.Make.logo.url if self.Make and self.Make.logo else None



class CarSubmission(models.Model):
    '''Vehicle Details for car registration'''
    Make = models.ForeignKey(Make, on_delete=models.SET_NULL, null=True, blank=True)
    MakeName = models.CharField(max_length=50)
    Model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, blank=True)
    ModelName = models.CharField(max_length=50)
    Registration = models.CharField(max_length=50)
    Year = models.IntegerField()
    Mileage = models.IntegerField()
    Color = models.CharField(max_length=50)
    FuelType = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, blank=True)
    Transmission = models.ForeignKey(TransmissionType, on_delete=models.SET_NULL, null=True, blank=True)
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


class CallBack(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    Message = models.CharField(max_length=1000)


class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')


class CarSubmissionPhoto(models.Model):
    car_sub = models.ForeignKey(CarSubmission, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='car_sub_images/')


class Plates(models.Model):
    Number = models.CharField(max_length=50)
    Document = models.CharField(max_length=50)
    Transfer = models.CharField(max_length=50)
    Price = models.IntegerField()

    def __str__(self):
        return self.Number