import os
import tempfile

def pytest_sessionstart():
    TEMP_DIR = tempfile.mkdtemp(prefix='django_')
    os.environ['DJANGO_TEST_TEMP_DIR'] = TEMP_DIR
