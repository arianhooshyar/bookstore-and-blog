from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Blog(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Blog_detail_View', args=[self.id])


class Comment(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('Blog_List_View', args=[self.id])
