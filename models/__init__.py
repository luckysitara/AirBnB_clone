#!/usr/bin/python3
""" Package init module """
import sys
from models.engine.file_storage import FileStorage
from models import user
import models._checker_diag

sys.modules['models.tmp_user'] = user

storage = FileStorage()
storage.reload()
