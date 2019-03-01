from django.shortcuts import render, redirect, render_to_response


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework_jwt.settings import api_settings
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Notes


def home(request):
    allnotes = Notes.objects.all().order_by('-created_time')
    # all_labels = Labels.objects.all().order_by('-created_time')
    # map_labels = MapLabel.objects.all().order_by('-created_time')
    print(allnotes)
    context = {  # 'title':title,
        # 'description':description
        'allnotes': allnotes}
    # for i in range(len(map_labels)):
    #     print('notename:-->', map_labels[i])
    return render(request, 'notes/note_section.html', context)

     # return render(request, 'notes/note_section.html')


def home1(request):
    response_data = {}
    allnotes = Notes.objects.all().order_by('-created_time')
    response_data['message'] = serializers.serialize('json', allnotes)
    return JsonResponse(response_data)

    # return render(request, 'notes/note_section.html')



from django.http import JsonResponse
from django.core import serializers


def createnote(request):
    if request.method == 'POST':

        # get username and password from submitted form
        title = request.POST.get('title')
        print("title:",title)


        description = request.POST.get('description')
        print("description:", description)

        color = request.POST.get('color')
        print("color:", color)

        is_archived = request.POST.get('is_archive')
        print("is_archived:", is_archived)

        image = request.POST.get('image')
        print("image:", image)


        is_pinned  = request.POST.get('is_pinned')
        print("is_pinned:", is_pinned)


        notes = Notes(title=title,description=description,color=color,is_archived=is_archived,image=image,is_pinned=is_pinned)


        # title and description should not be null
        if title !="" and description!="":
            # save it to database
            is_exists=Notes.objects.filter(title=title).exists()

            if is_exists is not True:

                notes.save()
            return redirect('home')
        # order notes according to it's creation time
        allnotes = Notes.objects.all().order_by('-created_time')

        # response_data = {}
        #
        # response_data['message'] = serializers.serialize('json', allnotes )
        # all_labels = Labels.objects.all().order_by('-created_time')
        # map_labels = MapLabel.objects.all().order_by('-created_time')

        # print(allnotes)

        # return JsonResponse(response_data)
        context = {  # 'title':title,
        # 'description':description
        'allnotes': allnotes }
        return render(request, 'notes/note_section.html',context)



def deleteenote(request, pk):
    if request.method == 'GET':
        # get the note with requested id
        note = Notes.objects.get(pk=pk)
        print(note.trash)
        if note.trash == False:
           note.trash = True
           note.save()
           return redirect('home')
        else:
            note.is_deleted=True
            # delete note
            note.delete()
            return redirect('showtrash')

    allnotes = Notes.objects.all().order_by('-created_time')
    # all_labels = Labels.objects.all().order_by('-created_time')
    # map_labels = MapLabel.objects.all().order_by('-created_time')
    context = {  # 'title':title,# 'description':description
    'allnotes': allnotes }

    return render(request, 'notes/show-trash.html', context)

def setcolor(request):
    if request.method == 'POST':
        color = request.POST.get('color')
        id = request.POST.get('id')
        note = Notes.objects.get(id=id)
        note.color = request.POST.get('color')
        print(color)
        print(id)
        note.save()


    allnotes = Notes.objects.all().order_by('-created_time')
    # all_labels = Labels.objects.all().order_by('-created_time')
    # map_labels = MapLabel.objects.all().order_by('-created_time')
    print(allnotes)
    response_data = {}
    response_data['message'] = serializers.serialize('json', allnotes)
    return JsonResponse(response_data)


def ispinned(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        note = Notes.objects.get(id=id)
        if note.is_pinned  == False:
            note.is_pinned = True
            note.save()
        else:
            note.is_pinned = False
            note.save()


        response_data = {}
        allnotes = Notes.objects.all().order_by('-created_time')
        response_data['message'] = serializers.serialize('json',allnotes)
        return JsonResponse(response_data)


def isarchive(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        note = Notes.objects.get(id=id)

        if note.is_archived == False:
           note.is_archived = True
           note.save()
        else:
            note.is_archived = False
            note.save()

        response_data = {}
        allnotes = Notes.objects.all().order_by('-created_time')
        response_data['message'] = serializers.serialize('json', allnotes)
        return JsonResponse(response_data)

def showarchive(request):
    allnotes = Notes.objects.all().order_by('-created_time')
    # all_labels = Labels.objects.all().order_by('-created_time')
    # map_labels = MapLabel.objects.all().order_by('-created_time')
    print(allnotes)
    context = {  # 'title':title,
        # 'description':description
        'allnotes': allnotes}
    return render(request, 'notes/show-archive.html', context)


def showtrash(request):
    allnotes = Notes.objects.all().order_by('-created_time')
    # all_labels = Labels.objects.all().order_by('-created_time')
    # map_labels = MapLabel.objects.all().order_by('-created_time')
    print(allnotes)
    context = {  # 'title':title,
        # 'description':description
        'allnotes': allnotes}
    return render(request, 'notes/show-trash.html', context)
