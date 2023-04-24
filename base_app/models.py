# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from custom_auth.models import BaseUser
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    total_copies = models.IntegerField(default=0)
    available_copies = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default_book.png')

    def __str__(self):
        return self.title


class Circulation(models.Model):
    student = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    checked_out = models.DateTimeField(auto_now_add=True)
    checked_in = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.book.title

    def is_overdue(self):
        if self.due_date < timezone.now():
            return True
        return False
