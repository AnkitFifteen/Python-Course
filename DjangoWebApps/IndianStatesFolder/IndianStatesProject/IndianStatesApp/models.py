from django.db import models

# Create your models here.
class State(models.Model):
    Name = models.CharField(max_length=100)
    Population = models.BigIntegerField()
    Language = models.CharField(max_length=100)
    Capital = models.CharField(max_length=100)

    class Meta:
        db_table = "State"