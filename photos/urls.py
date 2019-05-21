from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPhoto.as_view()),
    path('<int:pk>/', views.DetailPhoto.as_view()),
]
