from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.home, name='home'),
    path('practice/', views.home1, name='home1'),
]

urlpatterns = format_suffix_patterns(urlpatterns)