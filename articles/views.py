# from django.shortcuts import render
from django.http.response import JsonResponse
# from rest_framework import status

from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework.decorators import api_view
from scrapyd_api import ScrapydAPI
from django.db.models import Q
from django.http import Http404
scrapyd = ScrapydAPI('http://localhost:6800')


@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        txt = request.GET.get('article_txt', '')
        writer = request.GET.get('article_writer', '')
        print(list(request.GET.get('return', '').split(",\"
                                                       "")))
        articles = Article.objects.all()
        if txt:
            articles = articles.filter(Q(article_txt__icontains=txt))
        if writer:
            articles = articles.filter(Q(article_writer__icontains=writer))
        articles_serializer = ArticleSerializer(articles, many=True)
        #print([type(l['response']) for l in articles_serializer.data])
        return JsonResponse(articles_serializer.data, safe=False)


