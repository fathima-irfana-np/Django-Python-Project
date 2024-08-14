from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    
class Post(models.Model):
    title=models.CharField(max_length=255)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    job_title=models.CharField(max_length=200)
    description=models.TextField()
    description2=models.TextField()
    description3=models.TextField(default=0)
    image=models.ImageField(upload_to="media/post")
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title 

class Profile(models.Model):
    name=models.CharField(max_length=255,default="name")
    username=models.CharField(max_length=255)
    # password = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254,default="email@gmail.com")
    address = models.TextField(default="address")
    place = models.CharField(max_length=255 ,default="place")
    image =models.ImageField(upload_to="static/img" , default='media/def.jpg')
    phonenumber=models.BigIntegerField(default="0000000000")
    Created_at = models.DateTimeField(auto_now_add=True) 
 
    
class Productcategory(models.Model):
    title=models.CharField(max_length=305)
    def __str__(self):
        return self.title 
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productcategory = models.ForeignKey(Productcategory, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="static/assets/img")
    price=models.FloatField(max_length=254)
    description=models.TextField(max_length=255)
    Created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Multipleimage(models.Model):
    image = models.ImageField(upload_to='Multipleimage',null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True, default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, default=None)
    created_at = models.TimeField(auto_now_add=True)
    def str(self):
      return str(self.image)