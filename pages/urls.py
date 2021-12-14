from django.urls import path
from .views import HomePageView, AboutPageView, ImageGalleryView, SpaceView, NatureView, AbstractView

urlpatterns = [
    path('abstract.html', AbstractView.as_view(), name='abstract'),
    path('nature.html', NatureView.as_view(), name='nature'),
    path('space.html', SpaceView.as_view(), name='space'),
    path('imagegallery.html', ImageGalleryView.as_view(), name='imagegallery'),
    path('about.html', AboutPageView.as_view(), name='about'),
    path('home.html', HomePageView.as_view(), name='home'),
]
