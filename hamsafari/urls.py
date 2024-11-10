from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('',Template.as_view(),name='base_generic'),
    path('trips/',TripListView.as_view(), name='trip_list'),
    path('trip/new/',TripCreateView.as_view(), name='trip_create'),
    path('trip/update/<int:pk>/',TripUpdateView.as_view(), name='trip_update'),
    path('trip/<int:pk>/delete/',TripDeleteView.as_view(), name='trip_delete'),

    path('companion_requests/',CompanionRequestListView.as_view(), name='companion_request_list'),
    path('companion_request/new/',CompanionRequestCreateView.as_view(), name='companion_request_create'),
    path('companion_request/<int:pk>/edit/',CompanionRequestUpdateView.as_view(), name='companion_request_update'),
    path('companion_request/<int:pk>/delete/',CompanionRequestDeleteView.as_view(), name='companion_request_delete'),
   
    path('bookings/',BookingListView.as_view(), name='booking_list'),
    path('booking/new/',BookingCreateView.as_view(), name='booking_create'),
    path('booking/<int:pk>/update/',BookingUpdateView.as_view(), name='booking_update'),
    path('booking/<int:pk>/delete/',BookingDeleteView.as_view(), name='booking_delete'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
