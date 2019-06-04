from django.db import models



class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name_plural = "PostS"



class Post(Timestamp):
    title = models.CharField(max_length=255)
    body = models.TextField()
    test = models.BooleanField(default=False)
    date_de_debut = models.DateTimeField(auto_now=False)
    date_de_fin = models.DateTimeField(auto_now_add=False)
    url_test = models.URLField(default="www.pierre-dauphin.hopto.org")
    image = models.ImageField(default="{%static img/fond1.jpg %}")


    def __str__(self):
        return self.title
