from datetime import datetime
import sys
import binascii
from superblock.superblock import Superblock
from superblock import get_superblock, get_backups
from block_group.descriptor import Descriptor
from block_group.inode import Inode
from block_group import get_block_descriptor
from directory.directory import get_root_directory, Directory

if __name__ == "__main__":
    filesystem = sys.argv[1] if len(sys.argv) > 1 else 'fs.img'
    sb = get_superblock(filesystem)
    print("superblock: \n{}\n".format(sb))

    for index in range(0, sb.get_block_groups_count()):
        descriptor = get_block_descriptor(filesystem, index)
        print("{} block group:\n{}".format(index, descriptor))

    directory = get_root_directory(filesystem, get_block_descriptor(filesystem, 0))
    print(directory.ls())
    print(directory.get_info('test'))