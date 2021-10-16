from block_group.descriptor import Descriptor
from superblock.superblock import Superblock
from filesystem import Filesystem


descriptor_cache = {}

def get_block_descriptor(index):
    if index in descriptor_cache:
        return descriptor_cache[index]
    descriptor_cache[index] = Descriptor(index)

    return descriptor_cache[index]
