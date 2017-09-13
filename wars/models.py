# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models


class Weapow(models.Model):
    name = models.CharField(max_length=150)
    damage = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class StarShip(models.Model):
    name = models.CharField(max_length=150)
    weapows = models.ManyToManyField(Weapow, blank=True)

    def __str__(self):
        return self.name
