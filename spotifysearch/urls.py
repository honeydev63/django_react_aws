from django.urls import path
from . import views

app_name = 'backend'
urlpatterns = [
        path('search/', views.search, name='search'),
]