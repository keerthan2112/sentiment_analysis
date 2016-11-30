from django.db import models



class Topics(models.Model):
    topic = models.CharField(max_length=15)

    def __str__(self):
        return self.topic