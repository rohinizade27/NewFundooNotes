from django.shortcuts import render, redirect, render_to_response

def home(request):

    return render(request, 'notes/note_section.html')

def home1(request):

    return render(request, 'notes/practice.html')