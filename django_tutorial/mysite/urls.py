from django.contrib import admin
from django.urls import path, include
from poll    import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('poll/', include('poll.urls')),  # Poll app URLs
    path('', views.home, name='home'),  # Serve index page at root URL
]








