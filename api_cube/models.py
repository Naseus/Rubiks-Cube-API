from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model


class SolveTime(models.Model):
    time = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Algorithm(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    classification = models.CharField(max_length=25)
    alg_name = models.CharField(max_length=50)
    moves = models.CharField(max_length=100)


class Alternative(models.Model):
    alternative = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    base_alg = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
