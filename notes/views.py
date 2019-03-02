from django.shortcuts import render, redirect
from .models import Notes,Labels,MapLabel


def home(request):
    allnotes = Notes.objects.all().order_by('-created_time')
    all_labels = Labels.objects.all().order_by('-created_time')
    # map_labels = MapLabel.objects.all().order_by('-created_time')
    print(allnotes)
    context = {  # 'title':title,
        # 'description':description
        'allnotes': allnotes,'all_labels':all_labels}
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


def copynote(request, pk):
    if request.method == 'GET':
        # get note with given id
        note = Notes.objects.get(pk=pk)
        # set title of requested id to new note
        title = note.title
        color = note.color
        trash = note.trash
        is_archived = note.is_archived
        image = note.image
        is_pinned = note.is_pinned
        # set description of requested id to new note
        description = note.description
        # create ojbect of new copy
        newcopy = Notes(title=title, description=description,color=color,trash=trash, is_archived= is_archived,
                        image= image, is_pinned =is_pinned )
        # save newcopy to database
        newcopy.save()
        allnotes = Notes.objects.all().order_by('-created_time')
        all_labels = Labels.objects.all().order_by('-created_time')
        map_labels = MapLabel.objects.all().order_by('-created_time')
        print(allnotes)
        context = {  # 'title':title,
            # 'description':description
            'allnotes': allnotes, 'all_labels': all_labels,'map_labels':map_labels}
    return render(request, 'notes/note_section.html', context)


def restore(request,pk):
    if request.method == 'GET':
        # get the note with requested id
        note = Notes.objects.get(pk=pk)
        if note.trash == True:
            note.trash = False
            note.save()

        return redirect('home')

    allnotes = Notes.objects.all().order_by('-created_time')
    all_labels = Labels.objects.all().order_by('-created_time')
    map_labels = MapLabel.objects.all().order_by('-created_time')
    print(allnotes)
    context = {  # 'title':title,
        # 'description':description
        'allnotes': allnotes, 'all_labels': all_labels,'map_labels':map_labels}
    return render(request, 'notes/note_section.html', context)


def create_label(request):

    if request.method == 'POST':
        # label = Labels.objects.get(pk=pk)
        # get note id and label name from submitted form
        label_name = request.POST.get('label')
        print(label_name)
        label = Labels(label_name=label_name)
        # title and description should not be null
        if label_name!= "":
            # save it to database
            label.save()
            return redirect('home')
        # order notes according to it's creation time
        all_labels = Labels.objects.all().order_by('-created_time')

    context = {  # 'title':title,
            # 'description':description
            'all_labels': all_labels}
    return render(request, 'notes/note_section.html', context)


# method to delete label
def delete_label(request,pk):
    if request.method == 'GET':
        # get label id
        label = Labels.objects.get(pk=pk)
        # delete label
        label.delete()
        return redirect('home')
        # order notes according to it's creation time
        allnotes = Notes.objects.all().order_by('-created_time')
        print(allnotes)
        context = {  # 'title':title,
            # 'description':description
            'allnotes': allnotes}
    return render(request, 'notes/note_section.html', context)

# method to update label
def update_label(request, pk):
    if request.method == 'POST':
        # get note with requested id
        label = Labels.objects.get(pk=pk)
        # set new tile to requested id
        label.label_name = request.POST.get('label_name')
        print(label.label_name)
        # set new description to requested id

        if label.label_name !="":
            # save note
            label.save()
            return redirect('home')
        allnotes = Notes.objects.all().order_by('-created_time')
        context = {  # 'title':title,
        # 'description':description
        'allnotes': allnotes}
    return render(request, 'notes/note_section.html', context)


def addLabelOnNote(request):
    if request.method == 'POST':

        label_id = request.POST.get('label_id')
        note_id = request.POST.get('note_id')
        print(label_id)
        print(note_id)

        note = Notes.objects.get(id=note_id)
        print(note)
        label = Labels.objects.get(id=label_id)
        # print(label)
        #
        # note_label=label.label_name
        # print(label.label_name)

        # note.labels.append(note_label)
        # # note.labels = note_label
        # note.save()

        # print(label.label_name)
        # print(note.title)


        maplabel=MapLabel.objects.filter(note_id=note,label_id=label)
        print(maplabel)
        if len(maplabel) == 0:
            obj = MapLabel(note_id=note, label_id=label)
            obj.save()

        return redirect('readallnotes')
    return render(request,'notes/create-note.html')


def get_label_notes(request, pk):
        label = Labels.objects.get(pk=pk)
        if label:
            # print("value", label)
            # n_id = label.note_id
            try:
                L = MapLabel.objects.filter(label_id=label)
                # print('test', L)
            except:
                return render(request, 'notes/show_label.html',[])

            note_list = []
            note_obj = []
            for i in range(len(L)):
                obj = L[i]
                note_obj = Notes.objects.filter(title=obj)
                print(note_obj, '-->note_obj')

                note_list.append(note_obj)

            print(note_list)
            list=[]
            for j in range(len(note_list)):
                for k in range(len(note_list[j])):
                    print((note_list[j][k]))
                    list.append((note_list[j][k]))

            all_labels = Labels.objects.all().order_by('-created_time')
            map_labels = MapLabel.objects.all().order_by('-created_time')

            context = {'list': list, 'all_labels': all_labels,'map_labels':map_labels}
            print(type(all_labels))
            print(list)
        return render(request, 'notes/show_label.html', context=context)