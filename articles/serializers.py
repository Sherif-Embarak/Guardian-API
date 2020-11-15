from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('category',
                  'response',
                  'subcat_name',
                  'page_name',
                  'article_writer',
                  'article_time',
                  'article_title',
                  'article_caption',
                  'article_txt')
