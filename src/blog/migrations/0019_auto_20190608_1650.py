# Generated by Django 2.1.7 on 2019-06-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190608_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_projet',
            name='image1',
            field=models.ImageField(blank=True, upload_to='img/'),
        ),
    ]
