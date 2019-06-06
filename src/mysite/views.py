from django.shortcuts import render

from blog.models import Post_Bio

def home(request):
    posts_bio = Post_Bio.objects.all()
    #    return render(request, 'blog/bio.html', {'posts': posts_bio})
    return render(request, 'blog/pages/bio.html', {'posts': posts_bio})

def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def handler404(request, exception):
    return render(request, 'errors/Erreur404.html')


def handler500(request):
    return render(request, 'errors/Erreur500.html')
