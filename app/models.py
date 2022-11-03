from enum import unique
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)

    def __str__(self):
            return f'City: {self.city} - Street: {self.street} - Zip Code: {self.zip}'

class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time '),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=40, unique=True)
    # location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skill = models.ManyToManyField(Skill)
    type = models.CharField(max_length=200, null=False, choices=JOB_TYPE_CHOICES)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            return super(JobPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title