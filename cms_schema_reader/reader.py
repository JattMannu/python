import os
import json

class Reader():
    def __init__(self, full_file_path):
        self._full_file_path = full_file_path
        self._file_content = None #TODO Should i store the file ? Single Responsiablity Principle broken?

    @property
    def full_file_path(self):
        return self._full_file_path

    @full_file_path.setter
    def full_file_path(self, value):
        assert os.path.exists(value)
        assert os.path.isfile(value)
        self._full_file_path = value

    def read(self):
        with open(self._full_file_path) as f:
            return json.load(f)