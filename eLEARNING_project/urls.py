"""
URL configuration for eLEARNING_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from eLEARNING_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home_Page_View,name='index'),
    path('index.html',views.Home_Page_View,name='index'),
    path('about.html',views.About_Page_View,name='about'),
    path('contact.html',views.Contact_Page_View,name='contact'),
    path('courses.html',views.Courses_Page_View,name='courses'),
    path('Order.html',views.Order_Page_View,name='Order'),
    path('our_team.html',views.Our_Team_Page_View,name='our_team'),
    path('page.html',views.Page_View,name='page'),
    path('show-order.html',views.show_order_Page_View,name='show-order'),
    path('testimonial.html',views.Testimonial_Page_View,name='testimonial'),
]
