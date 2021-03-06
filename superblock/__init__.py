from math import ceil

from superblock.superblock import Superblock

SUPERBLOCK_SIZE = 1024
BOOT_RECORD = 512
ADDITIONAL_BOOT_RECORED = 512
SUPERBLOCKS = [
    1,
    2
]

SUPERBLOCKS_FACTOR = [
    3,
    5,
    7
]

def get_superblock(filesystem):
    with open(filesystem, "rb") as file:
        file.seek(1024)
        superblock = file.read(SUPERBLOCK_SIZE)

    return Superblock(superblock)

def get_backups(filesystem, superblock):
    if superblock.get_block_groups_count() > 1:
        with open(filesystem, "rb") as file:
            file.seek(superblock.get_block_group_size()+1024)
            backup = file.read(SUPERBLOCK_SIZE)
        
        return backup

    return []
