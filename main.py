from datetime import datetime
from superblock.superblock import Superblock
from superblock.superblock import superblock_structure


with open("fs.img", "rb") as file:
    _ = file.read(1024)
    superblock = file.read(1024)

sb = Superblock(superblock, superblock_structure)


for element in sb.get_all():
    print(element)