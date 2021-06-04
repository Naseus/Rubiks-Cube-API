from django.contrib.auth.models import User
from django.core.validators import validate_slug, RegexValidator
import re
from django.db import models

# Create your models here.
from django.db.models import Model

algorithm_validator = RegexValidator(
                                    regex=r'^([FRULBDMESXYZfrulbd](\'|2)? )*([FRULBDMESXYZfrulbd](\'|2)?)$'
                                     )


class SolveTime(models.Model):
    time = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.time = round(self.time, 2)
        super(SolveTime, self).save(*args, **kwargs)

    class Meta:
        get_latest_by = 'created'


class Algorithm(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True, validators=[validate_slug])
    classification = models.CharField(max_length=25)
    alg_name = models.CharField(max_length=50)
    moves = models.CharField(max_length=100, validators=[algorithm_validator])


class Alternative(models.Model):
    alternative = models.CharField(max_length=100, validators=[algorithm_validator])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    base_alg = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
