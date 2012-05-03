from django.db import models

class Cache(models.Model):
    hash = models.CharField(max_length=255, unique=True)
    data = models.TextField()

    def __unicode__(self):
        return self.hash
