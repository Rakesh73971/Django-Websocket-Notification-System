from django.urls import path
from . import views

urlpatterns = [
    path('',views.notify,name='notify')
]