from django.views.generic import ListView, CreateView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy
from .models import Trip, CompanionRequest, Booking
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm


class Template(TemplateView):
    template_name='base_generic.html'
    



class TripListView(ListView):
    model = Trip
    template_name = 'trip_list.html'
    context_object_name = 'trips'

class TripCreateView(CreateView):
    model = Trip
    template_name = 'trip_form.html'
    fields = ['user', 'start_location', 'end_location', 'date', 'seats_available', 'description', 'status']
    success_url = reverse_lazy('trip_list')

class TripUpdateView(UpdateView):
    model = Trip
    fields = '__all__'
    template_name = 'trip_update.html'  
    success_url = reverse_lazy('trip_list')

class TripDeleteView(DeleteView):
    model = Trip
    template_name = 'trip_confirm_delete.html'
    success_url = reverse_lazy('trip_list')

class CompanionRequestListView(ListView):
    model = CompanionRequest
    template_name = 'companion_request_list.html'
    context_object_name = 'companion_requests'

class CompanionRequestCreateView(CreateView):
    model = CompanionRequest
    fields = ['user', 'trip', 'start_location', 'end_location', 'date', 'description', 'status']
    template_name = 'companion_request_form.html'
    success_url = reverse_lazy('companion_request_list')

class CompanionRequestUpdateView(UpdateView):
    model = CompanionRequest
    template_name = 'companion_request_form.html'
    fields = ['start_location', 'end_location', 'date', 'description', 'status']
    success_url=reverse_lazy('companion_request_list.html')


class CompanionRequestDeleteView(DeleteView):
    model = CompanionRequest
    template_name = 'companion_request_confirm_delete.html'
    success_url = reverse_lazy('companion_request_list')

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'

class BookingCreateView(CreateView):
    model = Booking
    fields = ['user', 'trip']  
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list') 

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['user', 'trip']
    template_name = 'booking_form.html' 
    success_url=reverse_lazy('booking_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')



class CompanionRequestCreateView(CreateView):
    model = CompanionRequest
    fields = ['user', 'trip', 'start_location', 'end_location', 'date', 'description', 'status']
    template_name = 'companion_request_form.html'
    success_url = reverse_lazy('companion_request_list')