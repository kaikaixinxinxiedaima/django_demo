from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Article
from django.core.paginator import Paginator
from .serializers import ArticleSerializers
from django.http import HttpResponse
import json
from django.core import serializers
from rest_framework.decorators import api_view

# Create your views here.
class Aiticle(APIView):
    def hello_word(self, request, format=None):
        return Response("hello word")


    def get_all_article(request):
        article_list = Article.objects.all()


        # data = []
        # for item in article_list:
        #     article = {
        #         'title': item.title,
        #         'brief_content': item.brief_content,
        #     }
        #     data.append(article)
        #
        # return HttpResponse(json.dumps(data),content_type="application/json")



        # data = serializers.serialize('json', article_list)
        # return HttpResponse(data,content_type="application/json")


        serializers = ArticleSerializers(article_list, many=True)

        return HttpResponse(json.dumps(serializers.data), content_type="application/json")



    def get_index_page(request):
        page = request.GET.get('page')
        if page:
            page = int(page)
        else:
            page = 1

        article_list = Article.objects.all()
        top5_article_list = Article.objects.order_by('-publish_date')[:5]

        #每页多少条
        paginator = Paginator(article_list, 1)
        page_article_list = paginator.page(page)
        #页数
        page_num = paginator.num_pages
        #上一页
        if page_article_list.has_previous():
            pre_page = page - 1
        else:
            pre_page = page
        #下一页
        if page_article_list.has_next():
            next_page = page + 1
        else:
            next_page = page
        return render(request, 'blog/index.html',
                                       {
                                           'article_list': page_article_list,
                                           'page_num': range(1, page_num +1),
                                           'curr_page': page,
                                           'pre_page': pre_page,
                                           'next_page': next_page,
                                           'top5_article_list': top5_article_list
                                       })

    def get_detail_page(request, article_id):
        article_list = Article.objects.all()
        curr_article = None
        pre_article = None
        next_article = None
        pre_index = 0
        next_index = 0

        for index, article in enumerate(article_list):
            #处理前后一篇文章
            if index == 0:
                pre_index = 0
                if len(article_list) == 1:
                    next_index = 0
                else:
                    next_index = index + 1
            elif index == len(article_list) - 1:
                pre_index = index - 1
                next_index = index
            else:
                pre_index = index - 1
                next_index = index +1

            if article.article_id == article_id:
                curr_article = article
                pre_article = article_list[pre_index]
                next_article = article_list[next_index]
                break


        return render(request, 'blog/detail.html',
                      {
                          'article': curr_article,
                          'pre_article': pre_article,
                          'next_article': next_article
                      })
