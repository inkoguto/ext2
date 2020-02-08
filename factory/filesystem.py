import sys

from filesystem import Filesystem

class FilesystemFactory:
    name = None
    filesystem = None

    def __init__(self):
        self.name = sys.argv[1] if len(sys.argv) > 1 else 'fs.img'

    def get(self):
        if self.filesystem is not None:
            return self.filesystem

        return Filesystem(self.name)

filesystem_factory = FilesystemFactory()
