from django.db import models

# Create your models here.
class pop(models.Model):
    name = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)
    price = models.IntegerField(default=100)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name