from django.shortcuts import render, redirect, render_to_response

def home(request):

    return render(request, 'Notes/note_section.html')

def home1(request):

    return render(request, 'Notes/practice.html')