from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'
