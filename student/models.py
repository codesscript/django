from django.db import models

# Create your models here.
from django.db.models import CharField


class students(models.Model):
    username=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    mob_no = models.TextField(max_length=15)

    class Meta:
        db_table ="student"