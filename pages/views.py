from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ImageGalleryView(TemplateView):
    template_name = 'imagegallery.html'


class SpaceView(TemplateView):
    template_name = 'space.html'


class NatureView(TemplateView):
    template_name = 'nature.html'


class AbstractView(TemplateView):
    template_name = 'abstract.html'
