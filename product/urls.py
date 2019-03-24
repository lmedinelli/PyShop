from . import views
from django.urls import path

# /product = path =''
# products/1/new
# etc

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]