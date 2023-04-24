# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Book, Circulation
from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    books = Book.objects.filter(available_copies__gt=0)
    context = {'available_books': books,
               'user': request.user,}

    return render(request, "home.html", context)


def catalogue(request):
    books = Book.objects.filter(available_copies__gt=0)
    context = {'books': books,
               'user': request.user,}
    return render(request, "catalogue.html", context)


def available_books(request):
    books = Book.objects.filter(available_copies__gt=0)
    context = {'available_books': books,
               'user': request.user,}
    return render(request, "available_books.html", context)


def profile(request):
    books = Book.objects.filter(circulation__student=request.user, circulation__status="Checked Out")
    circulation = Circulation.objects.filter(student=request.user, status="Checked Out")
    context = {'books': books,
               'circulations': circulation,
               'user': request.user,
              }
    print(books)
    return render(request, "profile.html", context)


def checkout_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.available_copies -= 1
    book.save()
    circulation = Circulation.objects.create(student=request.user, book=book, title=book.title, status="Checked Out")
    circulation.due_date = timezone.now() + timezone.timedelta(days=14)
    circulation.save()
    return redirect('profile')

def checkin_book(request, circulation_id):
    circulation = Circulation.objects.get(id=circulation_id, student=request.user, status="Checked Out")
    book = circulation.book
    book.available_copies += 1
    book.save()
    circulation.status = "Checked In"
    circulation.checked_in = timezone.now()
    circulation.save()
    return redirect('profile')
