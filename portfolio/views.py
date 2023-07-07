from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'home':True}) 

def publications(request):
    return render(request, 'publications.html',{'publications':True})

def students(request):
    return render(request, 'students.html')