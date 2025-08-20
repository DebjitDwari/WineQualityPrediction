
from django.contrib import admin
from django.urls import path
from .views import home,index,about,contact 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ,name="index"),
    path('index/', home, name="home"),
    path('about', about, name="about"),
    path('contact', contact, name="contact")
]
