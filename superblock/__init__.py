from math import ceil

from superblock.superblock import Superblock
from filesystem import Filesystem
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

def get_superblock():
    filesystem = Filesystem()
    return Superblock(filesystem.read(1024, SUPERBLOCK_SIZE))

def get_backups(filesystem, superblock):
    if superblock.get_block_groups_count() > 1:
        with open(filesystem, "rb") as file:
            file.seek(superblock.get_block_group_size()+1024)
            backup = file.read(SUPERBLOCK_SIZE)
        
        return backup

    return []
