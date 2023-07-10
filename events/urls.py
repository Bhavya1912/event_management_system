from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet, basename='event')
router.register(r'registrations', views.RegistrationViewSet, basename='registration')
router.register(r'venues', views.VenueViewSet, basename='venue')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('registrations/<int:pk>/accept/', views.RegistrationViewSet.as_view({'post': 'accept_registration'}), name='accept-registration'),
    path('registrations/<int:pk>/reject/', views.RegistrationViewSet.as_view({'post': 'reject_registration'}), name='reject-registration'),
    path('events/<int:pk>/generate_attendee_list/', views.RegistrationViewSet.as_view({'post': 'generate_attendee_list'}), name='generate-attendee-list'),
    path('venues/<int:pk>/upcoming_events/', views.VenueViewSet.as_view({'get': 'list_upcoming_events'}), name='upcoming-events'),
    path('users/<int:pk>/registration_history/', views.UserViewSet.as_view({'get': 'retrieve_registration_history'}), name='registration-history'),
    path('users/<int:pk>/event_participation/', views.UserViewSet.as_view({'get': 'retrieve_event_participation'}), name='event-participation'),
]
