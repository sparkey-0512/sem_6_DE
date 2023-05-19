from django.db import models

class Files(models.Model):
    imgs = models.FileField(upload_to='file')