from datetime import datetime
import sys

from fs.superblock import Superblock
from fs.superblock import superblock_structure
from block_group.descriptor import Descriptor
from block_group.descriptor import block_group_structure
from block_group.inode import Inode
from directory.directory import Directory

filesystem = sys.argv[1] if len(sys.argv) > 1 else 'fs.img'

with open(filesystem, "rb") as file:
    _ = file.read(1024)
    superblock = file.read(1024)
    block_group = file.read(1024)

sb = Superblock(superblock, superblock_structure)
bg = Descriptor(block_group, block_group_structure)
for element in sb.get_all():
    print(element)

print('1st block group')

for element in bg.get_all():
    print(element)


with open(filesystem, "rb") as file:
    file.seek(84*1024)
    inodes = file.read(15*128)

i2 = Inode(inodes[11*128:11*128+128])
print('2nd inode')
print(i2)
with open(filesystem, "rb") as file:
    file.seek(513 * 1024)
    directory = file.read(15*4)
d = Directory(directory)
print(d)
