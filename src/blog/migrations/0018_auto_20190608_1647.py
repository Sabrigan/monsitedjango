# Generated by Django 2.1.7 on 2019-06-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190608_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_projet',
            name='image1',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
