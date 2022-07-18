from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('display/<int:id>', views.display, name='display'),
    path('add', views.add, name='add'),
]