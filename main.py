from datetime import datetime
import sys
import binascii
from superblock.superblock import Superblock
from superblock import get_superblock, get_backups
from block_group.descriptor import Descriptor
from block_group.inode import Inode
from directory.directory import Directory

filesystem = sys.argv[1] if len(sys.argv) > 1 else 'fs.img'
sb = get_superblock(filesystem)
with open(filesystem, "rb") as file:
    file.seek(1024 + sb.s_log_block_size)
    block_group_descriptor = file.read(sb.s_log_block_size)

descriptor = Descriptor(block_group_descriptor)

print("superblock: \n{}\n1st block group: \n{}".format(sb, descriptor))