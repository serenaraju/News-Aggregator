from django.urls import path
from django.conf.urls import url
from news.views import scrape, news_list, contacts, about

app_name = 'news'

urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', news_list, name="home"),
  path('contacts.html', contacts, name="contacts"),
  path('about.html', about, name="about"),
]