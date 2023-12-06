from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from NewsApp.serializers import BusinessSerializer, GallarySerializer, PoliticsSerializer, EconomicsSerializer, EntertainmentSerializer, LifestyleSerializer, TechnoloySerializer
from NewsApp.models import Business, Gallary, Politics, Economics, Entertainment, Lifestyle, Technoloy

@api_view(['GET'])
def api_list(request):
    api_list_data = {
        'Business': "Get All news related to Business",
        'Gallary': "Get All news related to Gallary",
        'Politics': "Get All news related to Politics",
        'Economics': "Get All news related to Economics",
        'Entertainment': "Get All news related to Entertainment",
        'Lifestyle': "Get All news related to Lifestyle",
        'Technoloy': "Get All news related to Technoloy",
    }
    return Response(api_list_data)


@api_view(['GET'])
def business_list(request):
    queryset = Business.objects.all()
    data = BusinessSerializer(queryset, many=True).data
    return Response(data)

@api_view(['GET'])
def gallary_list(request):
    queryset = Gallary.objects.all()
    data = GallarySerializer(queryset, many=True).data
    return Response(data)

@api_view(['GET'])
def politics_list(request):
    queryset = Politics.objects.all()
    data = PoliticsSerializer(queryset, many=True).data
    return Response(data)

@api_view(['GET'])
def economics_list(request):
    queryset = Economics.objects.all()
    data = EconomicsSerializer(queryset, many=True).data
    return Response(data)

@api_view(['GET'])
def entertainment_list(request):
    queryset = Entertainment.objects.all()
    data = EntertainmentSerializer(queryset, many=True).data
    return Response(data)

@api_view(['GET'])
def lifestyle_list(request):
    queryset = Lifestyle.objects.all()
    data = LifestyleSerializer(queryset, many=True).data
    return Response(data)

@api_view(['GET'])
def technoloy_list(request):
    queryset = Technoloy.objects.all()
    data = TechnoloySerializer(queryset, many=True).data
    return Response(data)
