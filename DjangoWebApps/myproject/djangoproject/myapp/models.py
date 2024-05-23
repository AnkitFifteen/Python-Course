from django.db import models

# Create your models here.
class stu(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phoneno = models.BigIntegerField()
    currenttime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Student'