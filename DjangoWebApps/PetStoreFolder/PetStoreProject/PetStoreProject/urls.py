"""
URL configuration for PetStoreProject project.

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
from django.conf import settings
from django.conf.urls.static import static
from PetStoreApp.views import ViewPets, SearchPets, RegisterUser, LoginUser, PetDetails, AddToCart, ViewCart, ChangeQuantity, OrderCheckout, PlaceOrder, Payment, LogoutUser, PetViewCustomManagerFunction, PlacePayUOrder

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginUser, name = 'LoginUser'),
    path("view-pets/", ViewPets.as_view(), name = "ViewPets"),
    path('pet-by-category/', PetViewCustomManagerFunction, name='PetByCategory'),
    path("search-pets/", SearchPets, name = 'SearchPets'),
    path("register-user/", RegisterUser, name = 'RegisterUser'),
    path("login-user/", LoginUser, name = 'LoginUser'),
    path("pet-details/<slug:slug>/", PetDetails.as_view(), name = 'PetDetails'),
    path("add-to-cart/", AddToCart, name = 'AddToCart'),
    path("view-cart/", ViewCart, name = 'ViewCart'),
    path('change-quantity/', ChangeQuantity, name='ChangeQuantity'),
    path('order-checkout/', OrderCheckout, name='OrderCheckout'),
    path('place-order/', PlaceOrder, name='PlaceOrder'),
    path('place-payu-order/', PlacePayUOrder, name='PlacePayUOrder'),
    path("payment-success/orderID/transactionID/", Payment, name="Payment"),
    path("logout-user/", LogoutUser, name="LogoutUser"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
