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

    def __init__(self):
        self.inode = 0
        self.rec_len = 0
        self.name_len = 0
        self.file_type = 0
        self.file_name = ''
        self.next_file = None

    def is_last_file(self):
        return self.file_type == File.EXT2_FT_UNKNOWN

    def __str__(self):
        return str(self.file_name)
    
    def get_inode(self):
        return self.inode

    def get_file_type(self):
        return self.file_type