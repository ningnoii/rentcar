"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
 	path('admin/', admin.site.urls, name="admin"),
    #path('login/', auth_views.LoginView.as_view()),
    #path('home/', views.home, name='home')
    path('cars_list/',views.CarListView.as_view(),name='cars_list'),
    path('person/', views.CreatePersonView.as_view(), name='person'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('rent_list',views.RentListView.as_view(),name='rent_list'),
    path('rent_car/',views.RentCar.as_view(),name='rent_car'),
    #path('return_car/',views.Return.as_view(),name = 'return_car'),
     #path('person_list/', views.ListPersonView.as_view(), name='person_list'),

   
    #path('admin/', admin.site.urls),
    #path('login/', auth_views.login, name='login'),
    #1path('logout/', auth_views.logout, name='logout'),
   # path('cars/',views.CarListView.as_view(), name='cars'),
]
