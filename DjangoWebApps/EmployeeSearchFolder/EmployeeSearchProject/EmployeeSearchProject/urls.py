"""
URL configuration for EmployeeSearchProject project.

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
from EmployeeSearchApp.views import ViewEmployees, RegisterEmployee, SearchNameStartsWith, SearchNameContains, SearchAgeLessThanEqualTo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ViewEmployees.as_view(), name = "ViewEmployees"),
    path("show-students/", ViewEmployees.as_view(), name = "ViewEmployees"),
    path("register-student/", RegisterEmployee.as_view(), name = "RegisterEmployee"),
    path("name-starts-with/", SearchNameStartsWith, name = "SearchNameStartsWith"),
    path("name-contains/", SearchNameContains, name = "SearchNameContains"),
    path("age-lte/", SearchAgeLessThanEqualTo, name = "SearchAgeLessThanEqualTo")
]
