from django.db import models
# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"