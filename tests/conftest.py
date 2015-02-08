import os
import sys
import tempfile

from runtests import RUNTESTS_DIR


collect_ignore = []

def pytest_configure():
    sys.path.insert(0, RUNTESTS_DIR)

    from django.db import connection

    if connection.vendor != 'postgresql':
        collect_ignore.extend(['postgres_tests', 'postgres'])


def pytest_sessionstart():
    TEMP_DIR = tempfile.mkdtemp(prefix='django_')
    os.environ['DJANGO_TEST_TEMP_DIR'] = TEMP_DIR
