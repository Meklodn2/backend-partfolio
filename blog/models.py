from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tags')

    class Meta:
        ordering = [ '-date_posted']
        verbose_name ='Post'
        verbose_name_plural = 'Posts'


class Tags(models.Model):
    name = models.CharField((""), max_length=50)

    class Meta:
         verbose_name ='Tag'
         verbose_name_plural = 'Tags'

