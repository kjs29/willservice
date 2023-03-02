from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('thankyou_contact/', views.thankyou_contact, name='thankyou_contact'),
]
