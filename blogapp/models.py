from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

#Creating a post table in the database
class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)

    #if the published date is blank and null it stores it since it is true
    published_date = models.DateTimeField(blank=True,null=True)

   #The publish method is to know the time the post was published
    def publish(self):

        self.published_date = timezone.now()

        self.save()


    #The method to show the title of the post and returns all data
    def __str__(self):

        return self.title

#class Comment(models.Model):


