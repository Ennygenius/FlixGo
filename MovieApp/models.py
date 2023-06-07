from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class NewMovieModel(models.Model):
    title = models.CharField(max_length=250)
    image = models.CharField(max_length=700)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True )
    rating = models.FloatField()
    streaming = models.CharField(max_length=250)
    pgRating = models.IntegerField(default=0)


    def __str__(self):
        return self.title