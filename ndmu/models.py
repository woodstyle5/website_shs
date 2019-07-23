from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    #title = RichTextUploadingField(max_length=100, blank=True, config_name='title_editor')
    title = models.CharField(max_length=100, blank=True)
    content = RichTextUploadingField(default="")   
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    imgs = models.ImageField(upload_to='imgs/%Y/%m/%d/', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse('post-detail', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('ndmu.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = RichTextUploadingField(default="") 
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_date',)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Gallery(models.Model):
    title = models.CharField(max_length=20)
    info = models.CharField(max_length=150)
    image = models.ImageField(upload_to='imgs/%Y/%m/%d/', max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return self.title

