from django.urls import include, path

from cart_app import views

app_name = 'cart_app'
urlpatterns = [
    path('', views.cart_details, name='cart_details'),

    path('add/<int:prod_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:prod_id>/',views.remove_cart_item,name='remove_cart_item'),
    path('delete_product/<int:prod_id>/',views.delete_cart_item, name='delete_cart_item'),

]
