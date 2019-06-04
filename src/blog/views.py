from django.shortcuts import render, get_object_or_404

from .models import Post


# from .mocks import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def show(request, id):
    post = get_object_or_404(Post, pk=id)
    #    try:
    #        post = Post.objects.get(pk = id)
    #    except Post.DoesNotExist:
    #        raise Http404('Sorry the post #{} was not found'.format(id))
    return render(request, 'blog/show.html', {'post': post})


def bio(request):
    # def bio(request, id):
    # post-bio = get_object_or_404(PostBio, pk=id)
    # return render(request, 'blog/bio.html', {'post-bio': post-bio})
    return render(request, 'blog/pages/bio.html')

def projets(request):
    # def bio(request, id):
    # post-bio = get_object_or_404(PostBio, pk=id)
    # return render(request, 'blog/bio.html', {'post-bio': post-bio})
    return render(request, 'blog/pages/projets.html')


def competences(request):
    # def bio(request, id):
    # post-bio = get_object_or_404(PostBio, pk=id)
    # return render(request, 'blog/bio.html', {'post-bio': post-bio})
    return render(request, 'blog/pages/competences.html')



def experiences(request):
    # def bio(request, id):
    # post-bio = get_object_or_404(PostBio, pk=id)
    # return render(request, 'blog/bio.html', {'post-bio': post-bio})
    return render(request, 'blog/pages/experiences.html')



def informatique(request):
    # def bio(request, id):
    # post-bio = get_object_or_404(PostBio, pk=id)
    # return render(request, 'blog/bio.html', {'post-bio': post-bio})
    return render(request, 'blog/pages/informatique.html')



def autre(request):
    # def bio(request, id):
    # post-bio = get_object_or_404(PostBio, pk=id)
    # return render(request, 'blog/bio.html', {'post-bio': post-bio})
    return render(request, 'blog/pages/autre.html')
