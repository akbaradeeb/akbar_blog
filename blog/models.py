from django.db import models

class Blog(models.Model):
    title  = models.CharField(max_length=255)
    url    = models.CharField(max_length=255)
    author = models.IntegerField()
    body   = models.TextField()
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