from django.urls import path
from . import views 

urlpatterns  = [
    path('reg/', views.reg, name = 'reg'),
    path('check/<str:id>', views.check, name = 'check'),
    path('available/', views.check_available, name = 'check_available'),
    path('available-2/', views.check_available2, name = 'check_available2'),
    path('exists/<str:id>', views.is_exists, name = 'is_exists')
]