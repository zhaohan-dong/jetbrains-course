from django.urls import path
from django.views import View


class CatView(View):
    pass


class DogView(View):
    pass


urlpatterns = [
    path('cat/', CatView),
    path('dog/', DogView),

]