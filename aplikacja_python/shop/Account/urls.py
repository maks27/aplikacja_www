from django.urls import path
from shop.Account.views import register_view

urlpatterns = [
    path('register', register_view),
]
