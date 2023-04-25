# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone

from custom_auth.models import Student, Employee
from .models import Book, Circulation
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def home(request):
    books = Book.objects.filter(available_copies__gt=0)[0:6]
    context = {
        'available_books': books,
        'user': request.user
    }
    return render(request, "home.html", context)


def catalogue(request):
    books = Book.objects.filter(available_copies__gt=0)
    p = Paginator(books, 30)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        'books': page_obj,
        'user': request.user,
        }
    return render(request, "catalogue.html", context)


def available_books(request):
    books = Book.objects.filter(available_copies__gt=0)
    context = {'available_books': books,
               'user': request.user,}
    return render(request, "available_books.html", context)


def profile(request):
    books = Book.objects.filter(circulation__student=request.user, circulation__status="Checked Out")
    circulation = Circulation.objects.filter(student=request.user, status="Checked Out")
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None
    try:
        employee = Employee.objects.get(user=request.user)
    except Employee.DoesNotExist:
        employee = None
    context = {'books': books,
               'circulations': circulation,
               'user': request.user,
               'employee': employee,
               'student': student,
              }
    print(books)
    return render(request, "profile.html", context)


def checkout_book(request, book_id):
    if request.user.is_anonymous:
        return redirect('login')
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


def contact(request):
    return render(request, "contact.html")
