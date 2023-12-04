from django.urls import include, path

from ecommerce_app import views

app_name = 'ecommerce_app'
urlpatterns = [
    path('', views.all_products_cat, name='all_products_cat'),
    path('<slug:c_slug>/', views.all_products_cat, name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/', views.product_details, name='product_details'),

]
