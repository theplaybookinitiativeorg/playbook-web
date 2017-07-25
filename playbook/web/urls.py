from django.conf.urls import url
from web import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
]