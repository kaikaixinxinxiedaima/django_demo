from django.shortcuts import render
from rest_framework.response import Response
from blog.models import Article
from .serializers import ArticleSerializers
from rest_framework.decorators import api_view
from rest_framework import status
import json


# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    """
    所有博客
    """
    if request.method == 'GET':
        article_list = Article.objects.all()
        s = ArticleSerializers(article_list, many=True);
        return Response(s.data)

    """
    创建出版社
    """
    if request.method == 'POST':
        s = ArticleSerializers(data=request.data)
        if s.validated_data:
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = ArticleSerializers.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        s = ArticleSerializers(article)
        return Response(s.data)
