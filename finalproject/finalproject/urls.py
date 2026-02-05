"""
URL configuration for finalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from bookreservation import views
# Import the LoginView and Logout View
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Creates path for home
    path("home/", views.dashboard, name="home"),
    # Creates the url path for the student and book information
    path("students/", views.student_info, name="studentinfo"),
    path("books/", views.book_info, name="bookinfo"),
    # Creates the url paths for the login and logout window
    path("login/", LoginView.as_view(template_name="bookreservation/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # Creates path for reservation window
    path("reserve/", views.book_reservation, name="reservation"),
    path("savereservation/", views.save_reservation, name="savereservation")
]
