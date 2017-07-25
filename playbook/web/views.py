from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.http import HttpResponse
from web.models import Play
from django.urls import reverse

class HomePageView(TemplateView):
    template_name = 'index.html'

# class AboutPageView(TemplateView):
#     template_name = 'about.html'

# class ListPlayView(ListView):
#     model = Play
#     template_name = 'play_list.html'

# class CreatePlayView(CreateView):
#     model = Play
#     fields = ['name', 'director', 'actors', 'group', 'plot', 'rating', 'youtube_link']
#     template_name = 'edit_list.html'
    
#     def get_success_url(self):
#         return reverse('play-list')