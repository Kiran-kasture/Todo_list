from django.urls import path
from .views import home, delete, update

urlpatterns=[
    path('',home,name='home'),
    path('delete/<int:id>/',delete,name='delete'),
    path('update/<int:pk>/',update,name='update')


]