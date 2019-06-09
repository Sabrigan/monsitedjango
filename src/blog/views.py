from django.shortcuts import render, get_object_or_404, Http404

from .models import Post_Bio,Post_Projet

#def index(request):
#    posts = Post_Bio.objects.all()
#    pass
#    return render(request, 'blog/bio.html', {'posts': posts})


# def show(request, id):
#     try:
#         post = Post_Bio.objects.get(pk = id)
#     except Post_Bio.DoesNotExist:
#         raise Http404('Sorry the post #{} was not found'.format(id))
#     return render(request, 'blog/show.html', {'post': post})
def index(request):
    posts_bio = Post_Bio.objects.all()
#    return render(request, 'blog/bio.html', {'posts': posts_bio})
    return render(request, 'blog/pages/bio.html',{'posts': posts_bio})


def bio(request):
    posts_bio = Post_Bio.objects.all()
#    return render(request, 'blog/bio.html', {'posts': posts_bio})
    return render(request, 'blog/pages/bio.html',{'posts': posts_bio})

def projets(request):
    posts_projets = Post_Projet.objects.all()
    return render(request, 'blog/pages/projets.html', {'posts': posts_projets})
    #return render(request, 'blog/pages/projets.html')


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
