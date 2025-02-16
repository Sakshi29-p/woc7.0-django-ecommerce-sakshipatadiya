"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login_user,name="login_user"),
    path('logout/',views.logout_user,name="logout_user"),
    path('register/',views.register_user,name="register_user"),
    path('update_user/',views.update_user,name="update_user"),
    path('about/',views.about,name='about'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:foo>',views.category,name='category'),
    path('allCategory/',views.allCategory,name='allCategory'),
    path('search/',views.search,name="search"),
]
