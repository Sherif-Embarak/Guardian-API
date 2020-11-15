from django.conf.urls import url
from articles import views

urlpatterns = [
    url(r'^api/articles$', views.article_list)
]
