from django.urls import path
from . import views

urlpatterns = [
    path("",views.login_user,name="login"),
    path("signup_user/",views.signup_user,name='signup')

]