from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.predict_view, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('prediction/', views.predict_view, name='prediction'),
]
