from django.urls import path
from .views import HomePageView, AboutPageView, InfoPageView, SnackListView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('about', AboutPageView.as_view(), name='about'),
  path('info', InfoPageView.as_view(), name='info'),
  path('', SnackListView.as_view(), name='snack')
]