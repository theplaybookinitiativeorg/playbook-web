from django.conf.urls import url
from web import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^plays/$', views.ListPlayView.as_view(), name='play-list'),
    url(r'^play/$', views.CreatePlayView.as_view(), name='play-new')
]