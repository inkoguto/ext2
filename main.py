from datetime import datetime
import sys
import binascii
from superblock.superblock import Superblock
from superblock import get_superblock, get_backups
from block_group.descriptor import Descriptor
from block_group.inode import Inode
from block_group import get_block_descriptors
from directory.directory import get_root_directory

if __name__ == "__main__":
    filesystem = sys.argv[1] if len(sys.argv) > 1 else 'fs.img'
    sb = get_superblock(filesystem)
    print("superblock: \n{}\n".format(sb))
    descriptors = []
    for index, descriptor in get_block_descriptors(filesystem, sb):
        descriptors.append(descriptor)
        print("{} block group:\n{}".format(index, descriptor))

    d = get_root_directory(filesystem, sb, descriptors[0])
    print(d)