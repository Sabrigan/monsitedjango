from django.http import Http404


class Post():
    POSTS = [
        {'id': 1, 'title': 'first post', 'body': 'first body', },
        {'id': 2, 'title': 'second post', 'body': 'second body', },
        {'id': 3, 'title': 'third post', 'body': 'third body', },
    ]

    @classmethod
    def all(cls):
        return cls.POSTS

    @classmethod
    def find(cls, id):
        try:
            return cls.POSTS[int(id) - 1]
        except:
            raise Http404('Déso post #{} pas trouvé'.format(id))
