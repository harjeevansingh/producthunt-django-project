from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # signup
    path('login/', views.login, name='login'),      # login
    path('logout/', views.logout, name='logout'),   # logout

]
