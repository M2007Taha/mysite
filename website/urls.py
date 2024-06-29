from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name='home'),
    path("home",views.home,name='home'),
    path("index",views.home,name='indexs'),
    path("about",views.about,name='about'),
    path("login",views.login,name='login'),
    path("page1",views.page1),
    path("page2",views.page2),
]
