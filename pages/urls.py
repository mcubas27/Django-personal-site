from django.urls import path, include
from . import views
'''contact_patterns = [

    path('', views.successView, name='success'),
]'''

urlpatterns = [
    path('', views.emailView, name='emailView'),
    path('contact/', views.contact, name='contact'),
    #path('contact/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
]
