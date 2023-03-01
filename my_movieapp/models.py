from django.db import models

# Create your models here.
class my_movie(models.Model):
    task_name = models.CharField(max_length=250)
    about = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.task_name