from django.db import models

class MyImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')


class YogaCard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cards/')  # goes to media/cards/

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name