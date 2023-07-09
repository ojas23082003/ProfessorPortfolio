from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'home':True}) 

def publications(request):
    return render(request, 'publications.html',{'publications':True})

def students(request):
    return render(request, 'students.html',{'students':True})

def biography(request):
    return render(request, 'biography.html',{'biography':True})

def projects(request):
    return render(request, 'projects.html',{'projects':True})

def consultancy(request):
    return render(request, 'consultancy.html',{'consultancy':True})

def collaborations(request):
    return render(request, 'collaborations.html',{'collaborations':True})

def fvisits(request):
    return render(request, 'fvisits.html',{'fvisits':True})

def others(request):
    return render(request, 'others.html',{'others':True})