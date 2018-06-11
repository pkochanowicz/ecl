from django.db import models


# Create your models here.
class Lecturer(models.Model):
    name = models.CharField(max_length=32)
    biography = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='images/lecturers/%Y/%m/%d', default='images/lecturers/default-lecturer.png', blank=True, null=True)
