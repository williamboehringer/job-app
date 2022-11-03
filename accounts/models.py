from django.db import models

# Create your models here.
class Subscribe(models.Model):
    NEWSLETTER_OPTION = [
    ('Weekly','Weekly'),
    ('Monthly','Monthly')
]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    option = models.CharField(max_length=10, choices=NEWSLETTER_OPTION)
