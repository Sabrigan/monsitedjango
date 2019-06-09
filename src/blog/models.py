from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django_mysql.models import ListCharField




class TimstampModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Post_Bio(TimstampModel):
    title=models.CharField(max_length=50)
    body=models.TextField()
    start_date=models.DateField()

    def __str__(self):
        return self.title


class Post_Projet(TimstampModel):
    title=models.CharField(max_length=150)
    intro=models.TextField()
    domain=ListCharField(
        base_field=models.CharField(max_length=25),
        size=6,
        max_length=(6 * 26)  # 6 * 10 character nominals, plus commas
    )
    body=models.TextField()
    image1=models.ImageField(blank=True,upload_to='img/')
    legende1=models.CharField(max_length=100,blank=True)
    avatar1 = ImageSpecField(source='image1',processors=[ResizeToFill(300, 150)], options={'quality': 60})
    image2 = models.ImageField(blank=True, upload_to='img/')
    legende2 = models.CharField(max_length=100, blank=True)
    avatar2 = ImageSpecField(source='image2',processors=[ResizeToFill(300, 150)], options={'quality': 60})
    image3 = models.ImageField(blank=True, upload_to='img/')
    legende3 = models.CharField(max_length=100, blank=True)
    avatar3 = ImageSpecField(source='image3',processors=[ResizeToFill(300, 150)], options={'quality': 60})
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return self.title

