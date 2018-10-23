# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class URL(models.Model):
    url = models.TextField(null=False)
    short = models.CharField(max_length=32)
    count = models.IntegerField(default=0)
