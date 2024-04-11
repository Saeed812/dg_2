from django.db import models
import datetime

class category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    
class customer(models.Model):
 first_name = models.CharField(max_length=50)
 last_name = models.CharField(max_length=50)   
 phone = models.CharField(max_length=50)
 g_mail = models.EmailField(max_length=50)
 password = models.CharField(max_length=100)
        
 def __str__(self):
   return f"{self.first_name}{self.last_name}"


class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=20, decimal_places=0000)
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    descriptions = models.CharField(max_length=500, default=True, blank=True, null=True)
    image = models.ImageField(upload_to="upload/product/")
    
    def __str__(self):
        return self.name
    

class order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    qounity = models.IntegerField(default=1)
    addres = models.CharField(max_length=120)
    phone = models.CharField(max_length=40)
    date = models.DateField(default=datetime.datetime.today)
    statues = models.BooleanField(default=False) 
    
    def __init__(self):
        return self.product
    

    
        
        

    