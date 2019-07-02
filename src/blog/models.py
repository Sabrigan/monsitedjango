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
        size=10,
        max_length=(10 * 26)  # 100 * 25 character nominals, plus commas
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



class Post_Experience(TimstampModel):
    title = models.CharField(max_length=150)
    description_sub_neg = models.TextField(blank=True)
    description_objective = models.TextField(blank=True)
    description_sub_pos = models.TextField(blank=True)
    entreprises = ListCharField(base_field=models.CharField(max_length=25,blank=True), size=5, max_length=(5 * 26))
    competences = ListCharField(base_field=models.CharField(max_length=25, blank=True), size=5, max_length=(5 * 26))
    duree = models.DurationField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    langages =  ListCharField(base_field=models.CharField(max_length=25,blank=True, default=" "),size=5, max_length=(5 * 26))
    utilisations = ListCharField(base_field=models.IntegerField(blank=True, default=0),size=5, max_length=(5 * 26))

    def __str__(self):
        return self.title