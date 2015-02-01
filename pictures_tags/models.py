from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.tag


class Picture(models.Model):
    subPath = models.CharField(max_length=4096, null=True)
    filename = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.filename
