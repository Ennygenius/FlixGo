# Generated by Django 4.2.1 on 2023-06-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0002_alter_newmoviemodel_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='newmoviemodel',
            name='pgRating',
            field=models.IntegerField(default=0),
        ),
    ]
