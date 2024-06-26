from django.contrib import admin
from django.urls import path,re_path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("index",views.home),
    path("page1",views.page1),
    path("page2",views.page2),
    path("about",views.about),
]
