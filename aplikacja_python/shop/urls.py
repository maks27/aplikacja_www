from django.urls import path
from shop import views

urlpatterns = [
    path('shop/', views.snippet_list),
    path('shop/<int:pk>/', views.snippet_detail),
]