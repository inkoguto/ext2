from element.item import Item

class Inode:
    STRUCTURE = [
        Item('i_mode', Item.TYPE_BYTE, 0, 2),
        Item('i_uuid', Item.TYPE_NUMERIC, 2, 2),
        Item('i_size', Item.TYPE_NUMERIC, 4, 4),
        Item('i_atime', Item.TYPE_DATETIME, 8, 4),
        Item('i_ctime', Item.TYPE_DATETIME, 12, 4),
        Item('i_mtime', Item.TYPE_DATETIME, 16, 4),
        Item('i_dtime', Item.TYPE_DATETIME, 20, 4),
        Item('i_gid', Item.TYPE_NUMERIC,  24, 2),
        Item('i_links_count', Item.TYPE_NUMERIC, 26, 2),
        Item('i_blocks', Item.TYPE_NUMERIC, 28, 4),
        Item('i_flags', Item.TYPE_NUMERIC, 32, 4),
        Item('i_osd1', Item.TYPE_NUMERIC, 36, 4),
        Item('i_block', Item.TYPE_BYTE, 40, 15*4),
        Item('i_generation', Item.TYPE_NUMERIC, 100, 4),
        Item('i_file_acl', Item.TYPE_NUMERIC, 104, 4),
        Item('i_dir_acl', Item.TYPE_NUMERIC, 108, 4),
        Item('i_faddr', Item.TYPE_NUMERIC, 112, 4),
        Item('i_osd2', Item.TYPE_NUMERIC, 116, 12)
    ]

    def __init__(self, block):
        self.block = block
        self.i_mode = '' 
        self.i_uid = ''
        self.i_size = ''
        self.i_atime = ''
        self.i_ctime = ''
        self.i_mtime = ''
        self.i_dtime = ''
        self.i_gid = ''
        self.i_links_count = ''
        self.i_blocks = ''
        self.i_flags = ''
        self.i_osd1 = ''
        self.i_block = ''
        self.i_generation = ''
        self.i_file_acl = ''
        self.i_dir_acl = ''
        self.i_faddr = ''
        self.i_osd2 = ''

        self.read()

    def read(self):
        for element in Inode.STRUCTURE:
            setattr(self, element.name, element.get_value(self.block))

    def __str__(self):
        print(int.from_bytes(self.i_block[0:4], byteorder='little'))
        return str(self.i_mode)

