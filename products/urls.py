
from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>', views.detail, name='detail'),
    path('sell/', views.sell, name='sell'),
]
