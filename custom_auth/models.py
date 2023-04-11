# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser

from django.db import models

from .managers import CustomUserManager


# Create your models here.
class BaseUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Employee(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='employee')
    job_role = models.CharField(max_length=40)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_hired = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='student')

