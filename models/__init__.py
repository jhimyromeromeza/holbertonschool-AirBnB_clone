#!/usr/bin/python3
"""the init file for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
