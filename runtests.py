#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

    # Django >=1.8
    import django
    if getattr(django, 'setup', False):
        django.setup()

    from django.conf import settings
    # WTF??? Otherwise it doesn't work with Django 1.4
    settings.DATABASES

    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))
