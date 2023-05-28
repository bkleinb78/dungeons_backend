from django.db import models


# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=15)
    hit_dice = models.IntegerField(default=0)
    # saving_throws  This needs 2 types
    # optional_skills This needs multiple lines of data
    # starting_equipment  This needs multiple lines of data
