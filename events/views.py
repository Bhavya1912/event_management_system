from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Event, Registration, Venue
from .serializers import (
    EventSerializer, RegistrationSerializer, VenueSerializer, UserSerializer
)
from .permissions import IsEventCreator, IsAdminUser
import datetime

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsEventCreator]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        registration = self.get_object()
        registration.accepted = True
        registration.save()
        return Response({'message': 'Registration accepted'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        registration = self.get_object()
        registration.accepted = False
        registration.save()
        return Response({'message': 'Registration rejected'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def generate_attendee_list(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        attendees = event.registration_set.filter(accepted=True)
        # Add your code here to generate the attendee list
        # You can customize the response data or export it in a specific format
        return Response({'message': 'Attendee list generated'}, status=status.HTTP_200_OK)

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    @action(detail=True, methods=['get'])
    def upcoming_events(self, request, pk=None):
        venue = self.get_object()
        upcoming_events = Event.objects.filter(venue=venue, date__gte=datetime.date.today())
        serializer = EventSerializer(upcoming_events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    @action(detail=True, methods=['get'])
    def registration_history(self, request, pk=None):
        user = self.get_object()
        registrations = Registration.objects.filter(user=user)
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def event_participation(self, request, pk=None):
        user = self.get_object()
        events = Event.objects.filter(registration__user=user)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
