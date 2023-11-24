from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class State(models.Model):
    state=models.CharField(max_length=50) 
     
    
    def __str__(self):
        return self.state 
class District(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    district=models.CharField(max_length=50)
      
    
        
    def __str__(self):
        return self.district
    
    
    
class Employee(models.Model):
    FullName=models.CharField(max_length=50)
    ID_Number=models.IntegerField()
    MY_GENDER = (("male","Male"), ("female","Female"), ("others","Others"))
    Gender=models.CharField(max_length=300,choices=MY_GENDER,verbose_name="Gender")
    phoneNumber=models.CharField(max_length=50)
    state=models.ForeignKey(State,on_delete=models.CASCADE)  
    district=ChainedForeignKey(District,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        sort=True)  
    def __str__(self):
        return self.FullName
    
    
    
# class Customer(models.Model):
#     FullName=models.CharField(max_length=50)    
#     phoneNumber=models.CharField(max_length=50)
#     MY_GENDER = (("male","Male"), ("female","Female"), ("others","Others"))
#     Gender=models.CharField(max_length=300,choices=MY_GENDER,verbose_name="Gender")
#     location=models.CharField(max_length=50)
#     def __str__(self):
#         return self.FullName


class OrderDetails(models.Model):
    Customer_Name=models.CharField(max_length=50)
    OrderId=models.CharField(max_length=50)
    # Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)  
    location=models.CharField(max_length=50)
    orderDate=models.DateField() 
    DeliveryTime=models.TimeField()
    staff=models.ForeignKey(Employee,on_delete=models.CASCADE) 
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.OrderId
    
    
class Food(models.Model):
    items=models.CharField(max_length=50)
    price = models.IntegerField()
    def __str__(self):
        return self.items
    
    
class OrderItems(models.Model):
    
    OrderId=models.ForeignKey(OrderDetails,on_delete=models.CASCADE)
    Items=models.ForeignKey(Food,on_delete=models.CASCADE)
    Quantity=models.CharField(max_length=50)
    def save(self, *args, **kwargs):
        total_price = float(self.Items.price) * int(self.Quantity)
        order_details = self.OrderId
        order_details.price += total_price
        order_details.save()

        super().save(*args, **kwargs)

    def _str_(self):
        return str(self.Items)
   