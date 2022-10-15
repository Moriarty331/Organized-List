from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('deleteitem/<int:pk>', views.deleteItem, name="deleteitem"),
    path('deletelist<int:pk>', views.deleteList, name="deletelist"),
    path('update/<int:pk>', views.update, name="update"),
]