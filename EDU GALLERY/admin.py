from django.contrib import admin
from.models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','created_at')  
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'productcategory', 'name', 'image', 'price','description')
    fields = ('title', 'category', 'job_title', 'description', 'description2','description3','image', )
admin.site.register(Product, ProductAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'job_title', 'description', 'description2','description','image',)
    fields = ('title', 'category', 'job_title', 'description', 'description2','description3','image', )
admin.site.register(Post, PostAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username','name','user', 'email', 'image', 'address','phonenumber','place',)
    fields = ('username','name' ,'user', 'email', 'image', 'address','phonenumber','place',)
admin.site.register(Profile, ProfileAdmin)

class ProductcategoryAdmin(admin.ModelAdmin):
    list=('title')
    fields =('title',)
admin.site.register(Productcategory,ProductcategoryAdmin)

class Product_multi_images(admin.ModelAdmin):
    list_display = ('user', 'image','product',)
    fields = ('user', 'image','product',)
admin.site.register(Multipleimage, Product_multi_images)
