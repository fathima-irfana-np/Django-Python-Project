from django.urls import path
from . import views

urlpatterns = [
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('',views.index_2,name='index_2'),
    path('index_2',views.index_2,name='index_2'),
    # path('registration',views.register,name='registration'),
    path('login',views.log,name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('profile',views.profile,name='profile'),
    path('postproduct',views.postproduct,name='postproduct'),
    path('upload_image/', views. upload_image, name='upload_image'),
    path('delete_image/', views. delete_image_view, name='delete_image_view'),
    path('myproducts/<int:user_id>',views.myproduct,name='myproducts'),
    path('delete_product/',views.delete_product_view,name='delete_product'),
    path('editproduct/<int:product_id>',views.editproduct,name='editproduct'),
    path('singleproduct/<int:product_id>',views.singleproducts,name='singleproduct'),
    path('product',views.product,name='product'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('changepassword/<int:user_id>',views.changepassword,name='changepassword'),
    path('search/ajax/', views.product_search_ajax, name='product_search_ajax'),
    path('change_password/',views.change_password,name='change_password'),
    path('editproduct/',views.edit_product,name='editproduct'),

   path('changepassword/changepassword/28/',views.change_password,name='change_password'),

    path('product/<int:product_id>/', views.singleproducts, name='single_product'),
    path('search_cateogry/ajax/', views.product_cateogry_search_ajax, name='product_cateogry_search_ajax'),
    path('singlecategory/<int:cateogry_id>/', views.cateogry, name='singlecategory'),
    path('search/ajax/', views.product_search_ajax, name='product_search_ajax'),
]
