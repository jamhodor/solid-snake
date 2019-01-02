from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'homepage/home.html')


def presentations(request):
    context = {
        "active":"presentations"
    }
    return render(request, 'homepage/presentations.html', context)

def editing(request):
    context = {
        "active":"editing"
    }
    return render(request, 'homepage/editing.html', context)

def homepages(request):
    context = {
        "active":"homepages"
    }
    return render(request, 'homepage/homepages.html', context)

def contact(request):
    return render(request, 'homepage/contact.html')

def disclaimer(request):
    return render(request, 'homepage/disclaimer.html')