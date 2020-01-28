from item.static import Item

class Entry:
    EXT2_FT_UNKNOWN = 0
    EXT2_FT_REG_FILE = 1
    EXT2_FT_DIR = 2
    EXT2_FT_CHRDEV = 3
    EXT2_FT_BLKDEV = 4
    EXT2_FT_FIFO = 5
    EXT2_FT_SOCK = 6
    EXT2_FT_SYMLINK = 7

    def __init__(self, _file):
        self.structure = [
            Item('inode', Item.TYPE_NUMERIC, 0, 4),
            Item('rec_len', Item.TYPE_NUMERIC, 0, 2),
            Item('name_len', Item.TYPE_NUMERIC, 0, 1),
            Item('file_type', Item.TYPE_NUMERIC, 0, 1),
        ]
        self._file = _file
        self.inode = 0
        self.rec_len = 0
        self.name_len = 0
        self.file_type = 0

        for element in self.structure:
            bitmap = self.read_filesystem(element.offset)
            print(self._file.tell())
            setattr(self, element.name, element.get_value(bitmap))
#            print("{}: {}\n".format(element.name, getattr(self, element.name)))
        self.name = Item('name', Item.TYPE_STRING, 0, self.rec_len).get_value(self.read_filesystem(self.name_len))
        padding = self.rec_len - (4 + 2 + 1 + 1 + self.name_len)
        self._file.read(padding)

    def read_filesystem(self, length):
        return self._file.read(length)

    def is_last_entry(self):
        return self.file_type == Entry.EXT2_FT_UNKNOWN

    def __str__(self):
        return "{}\n".format(self.name)