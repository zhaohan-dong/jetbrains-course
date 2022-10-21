from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View

data = []


class BaseView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Coming soon')

class NewsView(View):
    def get(self, request, link, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, 'r') as json_file:
            link = int(kwargs['link'])
            news = [n for n in news_from_json if n['link'] == art_link][0]
            context['title'] = art["title"]
            context['text'] = art["text"]
            context['created'] = art['created']
            return context
# Create your views here.
