#!/usr/bin/python3
""" Package init module """
import sys
from models.engine.file_storage import FileStorage
from models import user

sys.modules['models.tmp_user'] = user

storage = FileStorage()
storage.reload()
