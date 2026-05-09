from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Bill(models.Model):
    customer_name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()

    def __str__(self):
        return self.customer_name


class BillItem(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subtotal = models.FloatField()

# Create your models here.
