from django.urls import path
from . import views

app_name = 'poll'  # Make sure app_name is defined to avoid 'detail' errors in templates
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('vote/<int:poll_id>/', views.vote, name='vote'),
    path('results/<int:poll_id>/', views.results, name='results'),
]
