# Django imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
# Rest framework imports
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# App imports
from .serializers import GeoIpSerializer, GeoSerializer
from .models import Geolocation
from .utilities import get_geo

# View for creating new user, no authorization is required 
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('geo-create')
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form': form})

# View for accessing geolocation data, authorization is required 
@api_view(['GET'])
def geo_detail(request, pk):
	geo = Geolocation.objects.get(ip=pk)
	serializer = GeoSerializer(geo, many=False)
	return Response(serializer.data)

# View for creating geolocation data, authorization is required 
@api_view(['GET', 'POST'])
def geo_create(request):
    serializer = GeoIpSerializer(data=request.data)
    if serializer.is_valid():
        ip = serializer.data['ip']
        result = get_geo(ip)
        return Response(result)
    else:
        return Response({"Error" : "Please choose different IP address"})

# View for removing geolocation data, authorization is required 
@api_view(['GET', 'DELETE'])
def geo_delete(request, pk):
	geo = Geolocation.objects.get(ip=pk)
	geo.delete()
	return Response({"Succes" : "Geolocation succsesfully deleted!"})

# Views for custom error handlers
@api_view(['GET'])
@permission_classes([AllowAny])
def page_not_found(response, exception):
    data = {
        "404" : "Page not found"
    }
    return Response(data, status=404)

@api_view(['GET'])
@permission_classes([AllowAny])
def server_error(response):
    data = {
        "500" : "Internal server error"
    }
    return Response(data, status=500)



    





