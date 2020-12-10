from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('p/', views.NewView),
path('p/detail/<int:id>/', views.detail),
]


