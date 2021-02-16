#!/usr/bin/python3

from models.engine.file_storage import FileStorage

print("debug>> init")
storage = FileStorage()
storage.reload()
