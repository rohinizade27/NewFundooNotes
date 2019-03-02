from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('', views.home, name='home'),
    path('practice/', views.home1, name='home1'),

    # urls for operations on note
    path('createnote/', views.createnote, name='createnote'),
    path('deleteenote/<int:pk>', views.deleteenote, name='deleteenote'),

    # path('updatenotes/<int:pk>', views.updatenotes, name='updatenotes'),
    path('copynote/<int:pk>', views.copynote, name='copynote'),
    path('setcolor/', views.setcolor, name='setcolor'),
    path('isarchive/', views.isarchive, name='isarchive'),
    path('showarchive/', views.showarchive, name='showarchive'),
    path('showtrash/', views.showtrash, name='showtrash'),
    path('restore/<int:pk>', views.restore, name='restore'),
    path('ispinned/', views.ispinned, name='ispinned'),

    # urls for operation on Label
    path('create_label/', views.create_label, name='create_label'),
    path('addLabelOnNote/', views.addLabelOnNote, name='addLabelOnNote'),
    path('get_label_notes/<int:pk>', views.get_label_notes, name='get_label_notes'),
]

urlpatterns = format_suffix_patterns(urlpatterns)