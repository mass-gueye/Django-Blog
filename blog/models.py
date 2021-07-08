from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption

class Post(models.Model):
    image = models.ImageField(upload_to="static/images", max_length=200, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField(default="",null=False) # new
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
