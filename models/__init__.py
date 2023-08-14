#!/usr/bin/python3
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()

# Call reload() method on the storage variable to load data from the JSON file
storage.reload()

