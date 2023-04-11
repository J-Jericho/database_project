# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Book, Circulation
from django.shortcuts import render

# Create your views here.

def available_books(request):
    books = Book.objects.filter(available_copies__gt=0)
    context = {'available_books': books}
    return render(request, "available_books.html", context)


def my_books(request):
    books = Book.objects.filter(circulation__student=request.user, circulation__status="Checkout Out")
    context = {'my_books': books}
    return render(request, "my_books.html", context)
