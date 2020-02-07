from item.static import Item

class File:
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
            setattr(self, element.name, element.get_value(bitmap))
        self.name = Item('name', Item.TYPE_STRING, 0, self.rec_len).get_value(self.read_filesystem(self.name_len))
        padding = self.rec_len - (4 + 2 + 1 + 1 + self.name_len)
        self._file.read(padding)

    def read_filesystem(self, length):
        return self._file.read(length)

    def is_last_file(self):
        return self.file_type == File.EXT2_FT_UNKNOWN

    def __str__(self):
        str_repr = ''
        for item in self.structure:
            str_repr += "{}: {}\n".format(item.name, getattr(self, item.name))

        return str_repr
    
    def get_inode(self):
        return self.inode

    def get_file_type(self):
        return self.file_type