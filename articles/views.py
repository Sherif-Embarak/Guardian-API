# from django.shortcuts import render
from django.http.response import JsonResponse
# from rest_framework import status

from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework.decorators import api_view
from scrapyd_api import ScrapydAPI
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse, HttpResponseServerError
from itertools import compress

scrapyd = ScrapydAPI('http://localhost:6800')


def check_return_list(return_list):
    return list(compress(return_list, [not hasattr(Article, i) for i in return_list]))


@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        txt = request.GET.get('article_txt', '')
        writer = request.GET.get('article_writer', '')
        return_list = request.GET.get('return', '')
        articles = Article.objects.all()
        if txt:
            articles = articles.filter(Q(article_txt__icontains=txt))
        if writer:
            articles = articles.filter(Q(article_writer__icontains=writer))

        articles_serializer = ArticleSerializer(articles, many=True)
        if return_list:
            return_list = list(return_list.split(","))
            try:
                data = articles_serializer.data
                subset = lambda d, keys: dict([(key, d[key]) for key in keys])
                data = [subset(article, return_list) for article in data]
                return JsonResponse(data, safe=False)
            except:
                return HttpResponseServerError(str("does not exist "+' , '.join(check_return_list(return_list))))
        else:
            return JsonResponse(articles_serializer.data, safe=False)
