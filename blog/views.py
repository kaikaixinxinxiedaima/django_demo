from django.shortcuts import render
from rest_framework.response import Response
from blog.models import Article
from .serializers import ArticleSerializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
import json


# Create your views here.

#基于类的视图
# class ArticleHandle(APIView):
#
#     def get(self, request, format=None):
#         article_list = Article.objects.all()
#         s = ArticleSerializers(article_list, many=True)
#         return Response(s.data)
#
#     def post(self, request, format=None):
#         s = ArticleSerializers(data=request.data)
#         if s.is_valid():
#             s.save();
#             return Response(s.data, status=status.HTTP_201_CREATED)
#
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)



# #混合类1
# class ArticleHandle(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


#混合类2
class ArticleListHandle(generics.ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

class ArticleDetailHandle(generics.RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

