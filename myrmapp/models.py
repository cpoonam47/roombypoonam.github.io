from django.db import models

class Ownerreg(models.Model):
    username = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    mobile=models.CharField(max_length=100) 
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    reg_date=models.DateTimeField('reg date')
    def __str__(self):
        return self.email
    
class Customer(models.Model):
    username = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    reg_date = models.DateTimeField('reg date')
    def __str__(self):
        return self.email    
class Roomdetails(models.Model):
    ownemail=models.CharField(max_length=100)
    roomtitle = models.CharField(max_length=100)
    roomdetails=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    subcategory=models.CharField(max_length=100)
    roomimg=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    adddate = models.DateTimeField('adddate')
    price=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    def __str__(self):
        return self.ownemail
class Country(models.Model):
    country_name=models.CharField(max_length=200)
    def __str__(self):
        return self.country_name
class State(models.Model):
    c=models.ForeignKey(Country, on_delete=models.CASCADE)
    St_name=models.CharField(max_length=200)
    def __str__(self):
        return self.St_name    
class City(models.Model):
    s=models.ForeignKey(State, on_delete=models.CASCADE)
    city_name=models.CharField(max_length=200)
    def __str__(self):
        return self.city_name   
class Roombook(models.Model):
    roomid=models.CharField(max_length=100)
    customerid = models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    bookdate = models.CharField(max_length=100)
    def __str__(self):
        return self.customerid

class Category(models.Model):
    category_name=models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class Sub_category(models.Model):
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=200)
    def __str__(self):
        return self.categoryid

class Feedbackown(models.Model):
    uid = models.ForeignKey(Ownerreg, on_delete=models.CASCADE)
    feeddetail = models.CharField(max_length=200)
    feedto = models.CharField(max_length=200)
    feed_date = models.DateTimeField('feed date')
    def __str__(self):
        return self.uid

class Feedbackcust(models.Model):
    uid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    feeddetail = models.CharField(max_length=200)
    feedto = models.CharField(max_length=200)
    feed_date = models.DateTimeField('feed date')
    def __str__(self):
        return self.uid
class Massege(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    description =models.TextField() 
    reply=models.CharField(max_length=200)  
    def __str__(self):
        return self.email
class Mail(models.Model):
    email=models.CharField(max_length=200)
    reply=models.CharField(max_length=200)
    def __str__(self):
        return self.email