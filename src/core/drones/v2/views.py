from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones import views


class ApiRootVersion2(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, format=None):
        return Response({
            'vehicle-categories': reverse(
                views.DroneCategoryList.name, request=request, format=format),
            'vehicle': reverse(
                views.DroneList.name, request=request, format=format),
            'pilots': reverse(
                views.PilotList.name, request=request, format=format),
            'competitions': reverse(
                views.CompetitionList.name, request=request, format=format),
            })
