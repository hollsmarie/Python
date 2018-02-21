# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models 
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['first']) < 2:
            errors["first"] = "First name cannot be blank!"
        if len(postData['last']) < 2:
            errors["last"] = "Last name cannot be blank!"
        if len(postData['email']) < 2:
            errors["email"] = "Email cannot be blank!"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid Email Address!"
        return errors

class User(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()