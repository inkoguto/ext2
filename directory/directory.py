from item.static import Item
from block_group.inode import Inode

class Directory:
    def __init__(self, block):
        self.structure = [
            Item('inode', Item.TYPE_NUMERIC, 0, 4),
            Item('rec_len', Item.TYPE_NUMERIC, 4, 2),
            Item('name_len', Item.TYPE_NUMERIC, 6, 1),
            Item('file_type', Item.TYPE_NUMERIC, 7, 1),
            Item('name', Item.TYPE_BYTE, 8, 32),
        ]

        self.block = block
        self.inode = ''
        self.rec_len = ''
        self.name_len = ''
        self.file_type = ''
        self.name = ''

        self.read()

    def read(self):
        for element in self.structure:
            setattr(self, element.name, element.get_value(self.block))

    def __str__(self):
        directory = ''
        for item in self.structure:
            directory += "{}: {} \n".format(item.name, getattr(self, item.name))

        return directory

def get_root_directory(filesystem, superblock, group_descriptor):
    block_size = superblock.s_log_block_size
    inode_table_idx = group_descriptor.bg_inode_table
    with open(filesystem, 'rb') as file:
        file.seek(84*1024 + 128)
        bitmap = file.read(128)
        inode = Inode(bitmap)
        dir_addr = inode.get_direct_blocks()
    
    print(dir_addr)

    with open(filesystem, 'rb') as file:
        file.seek(dir_addr * block_size)
        directory = Directory(file.read(40))

    return directory
