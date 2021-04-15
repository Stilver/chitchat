from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('signup', views.signup, name='signup'),
    path('check_signup', views.check_signup, name='check_signup')
]
