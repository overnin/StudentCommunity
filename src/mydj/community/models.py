from django.db import models

class GoogleGroup (models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name


class Post (models.Model):
    googlegroup = models.ForeignKey(GoogleGroup)
    post_date = models.DateTimeField()
    post_number = models.IntegerField()
