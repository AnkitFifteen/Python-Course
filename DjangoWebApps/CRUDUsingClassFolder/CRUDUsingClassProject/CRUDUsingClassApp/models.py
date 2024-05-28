from django.db import models

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=100)

    class Meta:
        db_table = "Tasks"