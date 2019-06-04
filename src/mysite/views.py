from django.shortcuts import render


def home(request):
    return render(request, 'blog/pages/bio.html')

def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def handler404(request, exception):
    return render(request, 'errors/Erreur404.html')


def handler500(request):
    return render(request, 'errors/Erreur500.html')
