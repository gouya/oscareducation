# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Scenario(models.Model):

    creator = models.CharField("Createur", max_length = 755)
    title = models.CharField("Titre", max_length = 255)
    skill = models.CharField("Compétences", max_length = 755)
    topic = models.CharField("Sujet", max_length = 755)
    grade_level = models.CharField("Niveau", max_length = 755)
    instructions = models.CharField("Instructions", max_length = 755)
    public = models.BooleanField("Visibilité")

    def __str__(self):
        return("titre:"+ self.title+" and instructions :" + self.instructions + "and public : " + str(self.public))

class TextElem(models.Model):

    id_scenario = models.IntegerField()
    order = models.IntegerField()
    title = models.CharField("Titre", max_length = 500)
    content = models.CharField("Contenu", max_length = 500)

    def __str__(self):
        return("titre:"+ self.title+" and content :" + self.content)

class ImgElem(models.Model):

    id_scenario = models.IntegerField()
    order = models.IntegerField()
    title = models.CharField("Titre", max_length = 500)
    url = models.CharField("url", max_length = 500)
    description = models.CharField("description", max_length = 500)

class VidElem(models.Model):

    id_scenario = models.IntegerField()
    order = models.IntegerField()
    title = models.CharField("Titre", max_length = 500)
    url = models.CharField("url", max_length = 500)
    description = models.CharField("description", max_length = 500)
