from . import views
from django.urls import path

app_name = "inventories"

urlpatterns = [
    path('list/', views.inventory_list, name='list'),
]