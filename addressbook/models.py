from __future__ import unicode_literals

from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class ContactInfo(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    email = models.CharField(max_length=50)