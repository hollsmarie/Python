# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..loginReg.models import *


class CourseManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['courseName']) < 5:
            errors["Course Name"] = "Course name must be at least 5 characters long"
        if len(postData['courseDescription']) < 15:
            errors["Course Description"] = "Course description must be at least 15 characters long"
        return errors

        
class Course(models.Model):
    courseName = models.CharField(max_length=30)
    courseDescription = models.CharField(max_length=30)
    favorites = models.ManyToManyField(User, related_name="userFaves")
    userAdded = models.ForeignKey(User, related_name="userAdds")
    dateAdded = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()
    
