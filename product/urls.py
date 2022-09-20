from django.urls import path
from product import views

urlpatterns = [
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home'),
    # users
    path('add_user/',views.add_users,name='add_user'),
    path('edit_user/<int:id>/',views.edit_user,name='edit_user'),
    # products
    path('product_add/',views.add_product,name='product_add'),
    path('products/',views.products,name='products'),
    path('edit_product/<int:id>/',views.edit_product,name='edit_product'),
    path('status_change/<int:id>/',views.status_change,name='status_change'),
    path('delete_product/<int:id>/',views.delete_product,name='delete_product'),
    
    ]