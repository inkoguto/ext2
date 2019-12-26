from datetime import datetime
import sys
import binascii
from superblock.superblock import Superblock
from superblock import get_superblock
from block_group.descriptor import Descriptor
from block_group.inode import Inode
from directory.directory import Directory

filesystem = sys.argv[1] if len(sys.argv) > 1 else 'fs.img'
sb = get_superblock(filesystem)
with open(filesystem, "rb") as file:
    file.seek(1024 + sb.s_log_block_size)
    block_group_descriptor = file.read(sb.s_log_block_size)

descriptor = Descriptor(block_group_descriptor)

with open(filesystem, "rb") as file:
    file.seek(sb.s_log_block_size * descriptor.bg_block_bitmap)
    block_bitmap = file.read(sb.s_log_block_size)
    inode_bitmap = file.read(sb.s_log_block_size)
print("superblock: \n{}\n1st block group: \n{}".format(sb, descriptor))
#with open(filesystem, "rb") as file:
#    file.seek(8*1024)
#    inodes = file.read(11*128)
#
#i2 = Inode(inodes[128:2*128])
#print('2nd inode')
#for i in i2.get_all():
#    print(i)
#
#print(i2.get_direct_blocks())
#with open(filesystem, "rb") as file:
#    file.seek(24 * 1024)
#    directory = file.read(15*4)
#d = Directory(directory)
#print(d)
#