from . import views
from django.urls import path

app_name = "stores"

urlpatterns = [
    path('list/', views.store_list, name='list'),
]