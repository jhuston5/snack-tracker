from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


from django.views.generic import ListView
from .models import Snack

class SnackListView(ListView):
  template_name="snack_list.html"
  model = Snack()

class HomePageView(TemplateView):
  template_name ='home.html'

class AboutPageView(TemplateView):
  template_name='about.html'


class InfoPageView(TemplateView):
  template_name='info.html'
# Create your views here.
