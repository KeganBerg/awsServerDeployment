from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about.html', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
