from django.urls import path
from .views import login, logout_view

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),  # Add this line
]
