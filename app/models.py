from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Entity(models.Model):
    """
        Entity model
    """
    modified_by = models.ForeignKey('User', on_delete=models.CASCADE)
    value = models.IntegerField()
    properties = models.ManyToManyField('Property')
    
    def __str__(self):
        return f'Entity {self.id}'

    class Meta:
        verbose_name_plural = 'Entities'

class Property(models.Model):
    """
        Property model
    """
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.key}-{self.value}'

    class Meta:
        verbose_name_plural = 'Properties'


class User(AbstractUser):
    pass