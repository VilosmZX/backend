from django.urls import path
from . import views 

urlpatterns  = [
    path('reg/', views.reg, name = 'reg'),
    path('check/<str:id>', views.check, name = 'check')
]