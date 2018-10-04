from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from . import models

class Home(ListView):
	model = models.News
	template_name = 'blog/index.html'

	def get_context_data(self, **kwargs):
		kwargs['noticias'] = models.News.objects.all().order_by('-create')[:10]
		kwargs['campeoes'] = models.Champion.objects.all()[:5]
		return super(Home, self).get_context_data(**kwargs)

class ChampionView(DetailView):
	model = models.Champion
	template_name = 'blog/champion.html'

class ChampionsView(ListView):
	model = models.Champion
	template_name = 'blog/champions.html'

class NewsView(ListView):
	model = models.News
	template_name = 'blog/noticias.html'

class ResultsView(ListView):
	model = models.News
	template_name = 'blog/results.html'

	def get_queryset(self, **kwargs):
		if 'q' in self.request.GET:
			object_list = self.model.objects.filter(name__icontains = self.request.GET['q'])
		else:
			object_list = self.model.objects.all()
		return object_list

class NewsDetail(DetailView):
	model = models.News
	template_name = 'blog/post.html'

class About(TemplateView):
	template_name = 'blog/about.html'

    