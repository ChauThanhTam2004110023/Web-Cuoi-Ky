from django.urls import path
from . import views

app_name = 'home'



urlpatterns = [
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('login/', views.A_Login.as_view(), name='login'),
    path('logout/', views.A_Logout.as_view(), name='logout'),

    path('u-register/', views.U_RegisterPage.as_view(), name='u-register'),
    path('u-login/', views.U_Login.as_view(), name='u-login'),
    path('u-logout/', views.U_Logout.as_view(), name='u-logout'),



    path('', views.U_Index.as_view(),name='index'),
    path('category/<int:id>', views.U_Category.as_view(),name='category'),
    path('product/<int:id>/', views.U_Product.as_view(),name='product'),
    path('cart/<int:id>/', views.U_Cart.as_view(),name='cart'),
    path('search/', views.U_Search.as_view(), name='search'),
    
    path('us-index/', views.A_Index.as_view(), name='us-index'),
    path('us-customer/', views.A_Customer.as_view(), name='us-customer'),
    path('us-products/', views.A_Product.as_view(), name='us-products'),
    path('us-order/', views.A_Order.as_view(), name='us-order'),
    path('us-inventory/', views.A_Inventory.as_view(), name='us-inventory'),
    path('us-account/', views.A_Account.as_view(), name='us-account'),
    path('us-tasks/', views.A_Tasks.as_view(), name='us-tasks'),

    

    path('a-new/', views.A_New.as_view(), name='a-new'),
    path('a-update/<int:id>/', views.A_Updated_Products.as_view(), name='a-update'),
    path('a-delete/<int:id>/', views.A_Delete_Products.as_view(), name='a-delete'),

    
    path('a-inventory/', views.A_Created_Inventory.as_view(), name='a-inventory'),
    path('a-update-inventory/<int:id>/', views.A_Updated_Inventory.as_view(), name='a-update-inventory'),
    path('a-delete-inventory/<int:id>/', views.A_Delete_Inventory.as_view(), name='a-delete-inventory'),
    path('a-searchs/', views.A_Search_Products.as_view(), name='a-searchs'),


    path('cart', views.V_Cart.as_view(),name='cart'),

    # path('a-login/', views.A_Login.as_view(), name='a-login')

]