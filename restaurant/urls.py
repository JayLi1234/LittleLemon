from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu/<int:pk>', views.display_menu_items, name="menu_item"),
    path('api/menu-items', views.MenuItemsView.as_view()),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/bookings/<int:pk>', views.SingleBookingView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]