from rest_framework.decorators import action
from rest_framework import viewsets
from .serializers import NewsCreateSerializer, NewsListSerializer, NewsDetailSerializer, NewsDeleteSerializer
from django.shortcuts import render
from rest_framework.serializers import Serializer, CharField, IntegerField
from rest_framework.decorators import api_view
from .models import Category, News
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken


# class NewsListAPIView(ListAPIView):
#     serializer_class = NewsListSerializer
#     queryset = News.objects.all()
#
#
# # class NewListAPIView2(APIView):
# #     def get(self, request):
# #         news = [{'id': i.id, 'title': i.title} for i in News.objects.all()]
# #         return Response(news)
#
#
# @api_view(['POST'])
# def new_post(request):
#     serializer = NewsCreateSerializer(data=request.POST)
#     serializer.is_valid()
#     category = Category.objects.get(id=serializer.validated_data['category_id'])
#     news = News.objects.create(
#         title=serializer.validated_data['title'],
#         category=category
#     )
#     return Response(serializer.data)
#
#
# class NewsRetriveAPIView(RetrieveAPIView):
#     serializer_class = NewsDetailSerializer
#     queryset = News.objects.all()
#
#
# class NewDestroyAPIview(DestroyAPIView):
#     serializer_url_field = NewsDeleteSerializer
#     queryset = News.objects.all()


# class NewViewSet(viewsets.ModelViewSet):
#         queryset = News.objects.all()
#         serializer_class = NewsListSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = NewsListSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer

    @action(detail=True, methods=['GET'], url_path='product')
    def get_product(self, request, *args, **kwargs):
        instance = self.get_object()
        products = instance.products.all(category_id=kwargs.get('pk'))
        serializer = NewsListSerializer(products, many=True)
        return Response(serializer.data)

