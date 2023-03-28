from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    date = models.DateField()
    post_img = models.FileField(upload_to='photos/', max_length=400, null=True, default=None)
    author = models.TextField()

    def __str__(self): # replace object to post name in sqlite
        return self.title

class Customer(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    address = models.CharField(max_length=400)
    phone = models.IntegerField()

    def __str__(self):
        return self.email