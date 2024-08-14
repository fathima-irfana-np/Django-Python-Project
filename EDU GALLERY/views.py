from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import MultipleImageUploadForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login,update_session_auth_hash,get_user_model
from django.views.decorators.http import require_POST

def about(request):
    team=Post.objects.filter(category_id=2)
    testimonial=Post.objects.filter(category_id=3)
    data={
        'team':team,
        'testimonial':testimonial,
    }
    
    return render(request,"about.html",data)

def contact(request):
    return render(request,"contact.html")

def index_2(request):
    home_title_carosal= Post.objects.filter(category_id=1)
    data={
        'home_title_carosal':home_title_carosal
    }
    return render(request,"index_2.html",data)

def singleproduct(request,product_id):
    return render(request,"single-product.html")
# def register(request):
#     if request.method == 'POST':
#             username = request.POST.get('username')
#             password =request.POST.get('password')
#             confirmpassword =request.POST.get('confirmpassword')
#             name = request.POST.get('name')
#             email =request.POST.get('email')
#             # image =request.FILES['image']
#             # address =request.POST.get('address')
#             # place =request.POST.get('place')
#             phonenumber =request.POST.get('phonenumber')
#             if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
#                 return JsonResponse({'error': 'Username or email is already in use.'}, status=400)
            
#             if password != confirmpassword:
#                 return JsonResponse({'error':'Passwords are not same'}, status=400)
#             user = User(username=username, email=email)
#             user.set_password(password)
#             user.save()
#             profile = Profile(user=user,name=name,username=username,phonenumber=phonenumber,email=email,password=password)
#             profile.save()
#             return JsonResponse({'message': 'User registered successfully'})
#     return render(request,"registration.html")

def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return JsonResponse({'error': 'Invalid credentials. username password is incorrect.'}, status=400)
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect(index_2)

@login_required
def profile(request):
     user_id= request.user.id 
     try:
        user_profile=Profile.objects.get(user_id=user_id)
        data={
                'user':request.user,
                'profile':user_profile,
                }
     except:
         data={
             'user':request.user,
             
         }
     return render(request, 'profile.html', data)

@login_required
def postproduct(request):
    multi_images=Multipleimage.objects.all()
    all_product=Productcategory.objects.all()
    data={
       'all_product':all_product,
    }
    if request.method == 'POST':
        multi_images = request.POST.getlist('newsfeedsmultipleimg[]')
        # product_catgeory=request.POST.get('product_catgeory')
        productcategory=request.POST['product_catgeory']
        name=request.POST['title']
        price=request.POST['price']
        description=request.POST['Description']
        image=request.FILES['productimage']
        product = Product(name=name,price=price,description=description,image=image,productcategory_id=productcategory,user_id=request.user.id)
        product.save()
        product_id = product.id

        for multimage in multi_images:
            product_muti_image = Multipleimage(image=multimage,product_id=product_id,user_id=request.user.id)
            product_muti_image.save()  
            Multipleimage.objects.filter(product_id__isnull=True).delete()
        return JsonResponse({'message':'product added sucessfully'})
    return render(request,'postproduct.html',data)

@login_required
def upload_image(request):
    if request.method=='POST':
        form=MultipleImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_image=form.save(commit=False)
            image_id=request.POST.get('images')
            uploaded_image.product_id_id=image_id
            uploaded_image.user_id_id=image_id
            uploaded_image.save()
            return JsonResponse({'success':True,'url':uploaded_image.image.url,'image_id':uploaded_image.id,'name': uploaded_image.image.name})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

@login_required
@require_POST
def delete_image_view(request):
    try:
        image_id = request.POST.get('image_id')
        image = Multipleimage.objects.get(id=image_id)
        image.delete()

        return JsonResponse({'success': True})

    except Exception as e:
        return JsonResponse({'success': False, 'error_message': str(e)})



@login_required
@require_POST
def delete_product_view(request):
    try:
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        product.delete()

        return JsonResponse({'success': True})

    except Exception as e:
        return JsonResponse({'success': False, 'error_message': str(e)})


def myproduct(request,user_id):
    products = Product.objects.filter(user_id=user_id)
    product=Productcategory.objects.all()
    data={
            'products':products,
            'product':product,
            
    }
    return render(request,"myproducts.html",data)

@login_required
def editproduct(request, product_id):  
    product = get_object_or_404(Product, id=product_id)
    all_product = Productcategory.objects.all()
    products = Product.objects.get(id=product_id)
    multi_img = Multipleimage.objects.filter(product=product_id)
   
    data = {
        'product': product,
        'all_product': all_product,
        'products': products,
        'multi_img': multi_img,
        
    }
    return render(request, 'editproduct.html', data)




@login_required
def edit_product(request):
    multi_images = Multipleimage.objects.all()
    if request.method == 'POST':
        product_catgeory_id=request.POST.get('product_category')
        product_catgeory=get_object_or_404(Productcategory,id=product_catgeory_id)
        title=request.POST.get('title')
        price=request.POST.get('price')
        Description2=request.POST.get('description')
        product_id=request.POST.get('product_id')

        product = Product.objects.get(id=product_id)
        product.product_catgeory = product_catgeory
        product.title = title
        product.price = price
        product.Description2 = Description2
        if 'Image' in request.FILES:
              product.Image = request.FILES['Image']
        product.save()
        
        return JsonResponse({'message': 'Updated successfully!'})


@login_required
# @csrf_exempt
def upload_multi_image(request):

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        form = MultipleImageUploadForm(request.POST, request.FILES)

        if product_id is None:
            return JsonResponse({'success': False, 'errors': 'product_id is required'})

        if form.is_valid():
            uploaded_image = form.save(commit=False)
            uploaded_image.product_id = product_id
            uploaded_image.save()

            return JsonResponse({'success': True, 'url': uploaded_image.image.url, 'product': uploaded_image.product_id,'image_id':uploaded_image.id, 'name': uploaded_image.image.name})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

def singleproducts(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    profile=Profile.objects.get( user_id= product.user_id)
    product_categories = Productcategory.objects.filter(product=product)
    category_ids = [category.id for category in product_categories]
    productlist = Product.objects.filter(productcategory__in=category_ids).exclude(id=product_id)
    multi_image_product=Multipleimage.objects.filter(product=product_id)
    print(profile)
    data={
                'product':product,
                'productlist':productlist,
                'multi_image_product':multi_image_product,
                'profile':profile,
         }
    return render(request,"singleproduct.html",data)

    
def product(request):
        # shophead=Post.objects.filter(category_id=25) 
        products=Product.objects.all()
        productcategory=Productcategory.objects.all()
        # endlogo= Post.objects.filter(category_id=13)
        # nextpage=Post.objects.filter(category_id=27)
        data={
                
                'products':products,
                'productcategory':productcategory,
                
        }
        return render(request,'product.html',data)

    

def cateogry(request,cateogry_id):
        cateogry=Productcategory.objects.get(id=cateogry_id)
        # shophead=Post.objects.filter(category_id=25) 
        products=Product.objects.filter(productcategory_id=cateogry_id)
        productcategory=Productcategory.objects.all()
        endlogo= Post.objects.filter(category_id=13)
        # nextpage=Post.objects.filter(category_id=27)
        # aboutus=Post.objects.get(category_id=38)
        data={
                
                'products':products,
                'productcategory':productcategory,
                'endlogo':endlogo,
             
                'cateogry':cateogry,
        }
        return render(request,'category.html',data)


def product_cateogry_search_ajax(request):
    if request.method == 'GET':
        search_str = request.GET.get('productname', '')
        cateogry_id = request.GET.get('cateogry_id', '')

        products = Product.objects.all()

        # Filter products based on category if category ID is provided
        if cateogry_id:
            products = products.filter(product_catgeory_id=cateogry_id)

        # Apply search filter
        if search_str:
            products = products.filter(title__iregex=r"{}".format(search_str))

        results = [
            {
                'title': product.title,
                'price': product.price,
                'image': product.Image.url,
                'description': product.Description1,
                'id': product.id,
                'catgeory': product.product_catgeory_id,
            }
            for product in products
        ]

        return JsonResponse({'results': results})
    else:
        return JsonResponse({'error': 'Invalid request method'})
 
   
    


def product_search_ajax(request):
    if request.method == 'GET':    
        search_str = request.GET.get('productname', '')
    
        if search_str:
            products = Product.objects.filter(title__iregex=r"{}".format(search_str))
        else:
            products = Product.objects.all()
        
        results = [
            {
                'title': product.title,
                'price': product.price,
                'image': product.Image.url,
                'description': product.Description1,
                'id': product.id,
                'catgeory':product.product_catgeory_id,
            }
            for product in products
        ]
        
        return JsonResponse({'results': results})
    else:
            return JsonResponse({'error': 'Invalid request method'})

    
from django.http import JsonResponse
from .models import Product  # Make sure to import your Product model

def product_search_ajax(request):
    search_str = request.GET.get('productname', '')
    
    if search_str:
        # Use title_iregex instead of title_iregex=r"{}".format(search_str)
        products = Product.objects.filter(name__iregex=search_str)
    else:
        products = Product.objects.all()
    
    results = [
        {
            'name': product.name,
            'price': product.price,
            'image': product.image.url,
            'description': product.description,
            'product_catgeory': product.productcategory.title,  # Corrected typo
            'id': product.id,
        }
        for product in products
    ]
    
    return JsonResponse({'results': results})

@login_required
def editprofile(request):
    user_id = request.user.id
    user_profile = Profile.objects.get(user_id=user_id)
    data = {
        'log_det1': request.user,
        'log_det2': user_profile,
    }

    if request.method == 'POST':
        # username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        place = request.POST.get('place')
        phonenumber = request.POST.get('phonenumber')

        user = request.user
        # user.username = username
        user.email = email
        user.save()

        user_profile.name = name
        # user_profile.username = username
        user_profile.email = email
        user_profile.address = address
        user_profile.place = place
        user_profile.phonenumber = phonenumber

        if image:
            user_profile.image = image

        user_profile.save()
        return redirect('profile')

    # return render(request, "editprofile.html", data)
    return render(request,"editprofile.html",data)

@login_required
def changepassword(request,user_id):
    ids=user_id
    user = User.objects.get(id=ids)
    data = {
        'users': user,
    }
    return render(request, 'changepassword.html',data)

def change_password(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # Check old password
        if not user.check_password(old_password):
            return JsonResponse({'success': False, 'message': 'Incorrect old password'})
        
        if new_password == old_password :
            return JsonResponse({'success': False, 'message': 'New password and old password are same '})

        # Check if new password and confirm password match
        if new_password != confirm_password:
            return JsonResponse({'success': False, 'message': 'New password and confirm password do not match'})
        
        if not new_password:
            return JsonResponse({'success': False, 'message': 'New password cannot be empty'})

        # Change the password
        user.set_password(new_password)
        user.save()

        # Update session to reflect the new password
        update_session_auth_hash(request, user)

        return JsonResponse({'success': True, 'message': 'Password changed successfully'})

    return JsonResponse({'success': False, 'message': 'Invalid request'})