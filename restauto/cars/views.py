from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from  rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import NewSerializer
from .models import New
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import ListAPIView
from django.core.paginator import Paginator


class MyPagination(LimitOffsetPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50





@api_view(['GET'])
def cars(request):
    cars = New.objects.all()
    p = Paginator(cars, 20)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    serializer = NewSerializer(page_obj, many=True)
    return Response(serializer.data)


@api_view(['GET',])
def NewView(request):
    paginator = LimitOffsetPagination()
    p = PageNumberPagination()
    paginator.page_size = 3
    person_objects = New.objects.all()
    result_page = paginator.paginate_queryset(person_objects, request)
    serializer = NewSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET',])
def detail(request, id):
    new = New.objects.get(id=id)
    serializer = NewSerializer(new, many=False)
    return Response(serializer.data)



