from django.db import models

# Create your models here.
class items(models.Model):
    name = models.CharField(max_length=255) 
    class Meta:
        verbose_name_plural ="Items"

    def __str__(self):
        return self.name
           
