from django.urls import path
from . import  views

urlpatterns =[

    path('',views.home,name="layout"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('login_api/', views.Log.as_view(), name="login_api"),

]