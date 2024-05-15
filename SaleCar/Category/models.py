from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class PrivateSetup(models.Model):
    HideCost= models.DecimalField(max_digits=10, decimal_places=2)
class Holder(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id
    def get_absolute_url(self):
        return reverse("holder_detail", kwargs={"pk": self.pk})
class Car(models.Model):
    # ID = models.AutoField(primary_key=True)
    BienSo = models.CharField(max_length=100)
    HangXe = models.CharField(max_length=50)
    LoaiXe = models.CharField(max_length=50)
    NamSX  = models.IntegerField()
    Color  = models.CharField(max_length=10)
    NgayNhap = models.DateField()

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})

class CarDetail(models.Model):
    # ID = models.AutoField(primary_key=True)
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    Holder = models.ForeignKey(Holder, on_delete=models.CASCADE)
    Cost= models.IntegerField() # models.ForeignKey(Cost, on_delete=models.CASCADE)
    Gia = models.DecimalField(max_digits=19, decimal_places=4)
    Note = models.CharField(max_length=100)

    def __str__(self):
        return f'Detail for {self.Car.id}'
class Order(models.Model):
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    CustomerName = models.CharField(max_length=100)
    SDT = models.IntegerField()
    Status = models.IntegerField()
    GhiChu= models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class OrderDetail(models.Model):
    # ID = models.AutoField(primary_key=True)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Tien = models.DecimalField(max_digits=10, decimal_places=2)
    GhiChu = models.CharField(max_length=100)






