from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def publications(request):
    return render(request, 'publications.html')

def students(request):
    return render(request, 'students.html')