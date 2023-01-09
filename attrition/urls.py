from django.urls import path
from . import views

#URL config
urlpatterns = [
    path('',views.root, name='root')
]