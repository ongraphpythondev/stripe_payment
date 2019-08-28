from django.urls import path
from .views import index, charge, payment

app_name = 'payment'

urlpatterns = [
    path('', index, name='home'),
    path('charge/', charge, name='charge'),
    path('payment/', payment, name='payment')
]
