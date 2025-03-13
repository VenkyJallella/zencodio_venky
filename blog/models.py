from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse
# Create your models here.

class blogpost(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    

