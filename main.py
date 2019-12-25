from datetime import datetime
import sys

from fs.superblock import Superblock
from block_group.descriptor import Descriptor
from block_group.inode import Inode
from directory.directory import Directory

filesystem = sys.argv[1] if len(sys.argv) > 1 else 'fs.img'

with open(filesystem, "rb") as file:
    file.seek(1024)
    superblock = file.read(1024)

sb = Superblock(superblock)
print(str(sb))

#for element in sb.get_all():
#    print(element)

#for element in bg.get_all():
#    print(element)
#
#
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