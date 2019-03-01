from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('', views.home, name='home'),
    path('practice/', views.home1, name='home1'),
    path('createnote/', views.createnote, name='createnote'),
    path('deleteenote/<int:pk>', views.deleteenote, name='deleteenote'),
    # urls for operations on note

    # path('updatenotes/<int:pk>', views.updatenotes, name='updatenotes'),

    # path('copynote/<int:pk>', views.copynote, name='copynote'),
    path('setcolor/', views.setcolor, name='setcolor'),
    path('isarchive/', views.isarchive, name='isarchive'),
    path('showarchive/', views.showarchive, name='showarchive'),
    path('showtrash/', views.showtrash, name='showtrash'),
    # path('readallnotes/', views.readallnotes, name='readallnotes'),
    # path('restore/<int:pk>', views.restore, name='restore'),
    path('ispinned/', views.ispinned, name='ispinned'),
]

urlpatterns = format_suffix_patterns(urlpatterns)