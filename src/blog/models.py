from django.db import models

class TimstampModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Post_Bio(TimstampModel):
    title=models.CharField(max_length=50)
    body=models.TextField()

    def __str__(self):
        return self.title

