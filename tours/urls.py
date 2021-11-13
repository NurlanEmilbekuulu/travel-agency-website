from django.urls import path

from tours import views

app_name = 'tours'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index')
]
