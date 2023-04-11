# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book, Circulation


class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book


class CirculationAdmin(admin.ModelAdmin):
    class Meta:
        model = Circulation
# Register your models here.


admin.site.register(Book, BookAdmin)
admin.site.register(Circulation, CirculationAdmin)