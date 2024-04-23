from django.urls import path
from .views import *
urlpatterns = [
    path('name/<str:nickname>',name),
    path('',showAll),
    path('<int:id>',showOne),
    path('delete/<int:id>',deleteOne,name='delete'),
]