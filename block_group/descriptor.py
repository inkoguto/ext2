from item.static import Item
from superblock.superblock import Superblock
from filesystem import Filesystem

class Descriptor:
    START = 2048
    BLOCK_GROUP_SIZE = 32


    def __init__(self, index = 0):
        self.structure = [
            Item('bg_block_bitmap', Item.TYPE_NUMERIC, 0, 4),
            Item('bg_inode_bitmap', Item.TYPE_NUMERIC, 4, 4),
            Item('bg_inode_table', Item.TYPE_NUMERIC, 8, 4),
            Item('bg_free_blocks_count', Item.TYPE_NUMERIC, 12, 2),
            Item('bg_free_inodes_count', Item.TYPE_NUMERIC, 14, 2),
            Item('bg_use_dirs_count', Item.TYPE_NUMERIC, 16, 2),
            Item('bg_pad', Item.TYPE_NUMERIC, 18, 2),
            Item('bg_reserved', Item.TYPE_NUMERIC, 20, 12)
        ]
        filesystem = Filesystem()
        self.block_group = filesystem.read(Descriptor.START + index * Descriptor.BLOCK_GROUP_SIZE, Descriptor.BLOCK_GROUP_SIZE)
        self.read()

    def read(self):
        for item in self.structure:
            setattr(self, item.name, item.get_value(self.block_group))

    def __str__(self):
        descriptor = ''

        for item in self.structure:
            descriptor += "{}: {}\n".format(item.name,
                                            getattr(self, item.name))

        return descriptor
