# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class CustomAuthConfig(AppConfig):
    name = 'custom_auth'

    def ready(self):
        import custom_auth.signals
