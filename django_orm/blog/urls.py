from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name = 'home'),
	# path('login/', views.login_user, name='login'),
	path('register/', views.register_user, name='register'),
	path('logout/', views.logout_user, name='logout'),
	path('record/<int:pk>', views.customer_record, name='record'),
	path('record/delete/<int:pk>', views.delete_record, name='delete_record'),
	path('record/add', views.add_record, name='add_record'),

]