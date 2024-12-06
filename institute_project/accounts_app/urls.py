from django.urls import path
from .import views

urlpatterns = [
     path('accounts/login/',views.login_view, name='login'),
     path('sign_up/',views.sign_up, name='sign_up'),
     path('reset/',views.resetpassword, name='reset')
]