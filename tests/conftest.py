import os
import sys
import tempfile

from runtests import RUNTESTS_DIR, setup


collect_ignore = []

def pytest_configure():
    sys.path.insert(0, RUNTESTS_DIR)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'test_sqlite'

    setup(3, [])

    from django.db import connection
    if connection.vendor != 'postgresql':
        collect_ignore.extend(['postgres_tests', 'postgres'])

    if not connection.features.gis_enabled:
        collect_ignore.append('django/contrib/gis/tests')


def pytest_sessionstart():
    TEMP_DIR = tempfile.mkdtemp(prefix='django_')
    os.environ['DJANGO_TEST_TEMP_DIR'] = TEMP_DIR
