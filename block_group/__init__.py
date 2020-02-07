from block_group.descriptor import Descriptor
from superblock.superblock import Superblock

BLOCK_GROUP_SIZE = 32

def get_block_descriptor(filesystem, index):
    superblock = Superblock()
    block_size = superblock.s_log_block_size
    with open(filesystem, 'rb') as filehandler:
        filehandler.seek(2 * block_size + index * BLOCK_GROUP_SIZE)

        return Descriptor(filehandler.read(BLOCK_GROUP_SIZE))

    return None