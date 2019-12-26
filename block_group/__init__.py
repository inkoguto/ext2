from block_group.descriptor import Descriptor

BLOCK_GROUP_SIZE = 32

def get_block_descriptors(filesystem, superblock):
    count = superblock.get_block_groups_count()
    block_size = superblock.s_log_block_size
    group_descriptors = {}
    with open(filesystem, 'rb') as filehandler:
        filehandler.seek(2 * block_size)
        for i in range(count):
            yield i, Descriptor(filehandler.read(BLOCK_GROUP_SIZE))

    return None