from rest_framework import generics, filters
from  uni_data.models import *
from .serializers import * 

class CampusView(generics.ListCreateAPIView):
	queryset = Campus.objects.all()
	serializer_class = CampusSerializer


class CampusDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Campus.objects.all()
	serializer_class = CampusSerializer


#Contact views
class UniversidadView(generics.ListCreateAPIView):
	queryset = Universidad.objects.all()
	serializer_class = UniversidadSerializer


class UniversidadDetailView(generics.RetrieveUpdateAPIView):
	queryset = Universidad.objects.all()
	serializer_class = UniversidadSerializer

