"""
URL configuration for IndianStatesProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from IndianStatesApp.views import ViewStates, CreateState, UpdateState, DeleteState

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ViewStates.as_view(), name = "ViewStates"),
    path("show-states/", ViewStates.as_view(), name = "ViewStates"),
    path("create-state/", CreateState.as_view(), name = "CreateState"),
    path("update-state/<int:pk>/", UpdateState.as_view(), name = "UpdateState"),
    path("delete-state/<int:pk>/", DeleteState.as_view(), name = "DeleteState"),
]
