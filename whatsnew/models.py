from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField

class Whatsnew(models.Model):
    #whatsnew_title = RichTextUploadingField(max_length=100, blank=True, config_name='title_editor')
    whatsnew_title = models.CharField(max_length=100, blank=True)
    whatsnew = RichTextUploadingField(default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    new_imgs = models.ImageField(upload_to='imgs/%Y/%m/%d/', max_length=255, null=True, blank=True)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.whatsnew_title

    def get_absolute_url(self):
    	return reverse('new-view', kwargs={'pk': self.pk})