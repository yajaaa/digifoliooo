from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)

class Portfolio(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.TextField(max_length=100)
    Major = models.CharField(max_length=20, default = "")
    Minor = models.CharField(max_length = 20, default = "")
    Year = models.IntegerField()
    Resume = models.FileField(upload_to='resumes/', default='default_resume.pdf')
    Email = models.CharField(max_length=100, default = "")
    LinkedIn = models.URLField(max_length=100, default = "")
    GitHub = models.URLField(max_length = 100, default = "")