from pathlib import Path
from typing import List


class Directory:

    def __init__(self, path: str, parent):
        self.path = path
        self.parent = parent
        self.children = []
        self.files_size = 0

    def add_info(self, children: List, files_size: int):
        for child in children:
            self.children.append(Directory(child, self))
        self.files_size = files_size

    def get_child(self, dir_name):
        for child in self.children:
            if child.path == dir_name:
                return child
        raise ValueError(f'Directory name {dir_name} does not exist in directory {self.path}')

    def get_size(self):
        size = self.files_size
        for child in self.children:
            size += child.get_size()
        return size

    def __repr__(self):
        return f'path: "{self.path}", files_size: {self.files_size}'

