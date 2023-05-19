from django.db import models

class Files(models.Model):
    txtFile = models.FileField(upload_to='txtFiles')