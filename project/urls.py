from django.contrib import admin
from django.urls import path
from home.views import home, email

urlpatterns = [
path('submit/', email, name='email'),
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]
