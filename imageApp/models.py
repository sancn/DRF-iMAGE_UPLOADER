from django.db import models

# Create your models here.

class UploadedImage(models.Model):
    image_url = models.ImageField(upload_to='uploads/')
