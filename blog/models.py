from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Blog(models.Model):
    title  = models.CharField(max_length=255)
    url    = models.SlugField('url', max_length=255, blank=True)
    author = models.IntegerField()
    body   = models.TextField()
    tags   = models.CharField(max_length=255, default=" ")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status     = models.IntegerField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_id = models.IntegerField()
    name    = models.CharField(max_length=255)
    email   = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio  = models.TextField(max_length=500,blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True,blank=True)

    @receiver(post_save,sender=User)
    def update_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()