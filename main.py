from datetime import datetime

with open("fs.img", "rb") as file:
    _ = file.read(1024)
    superblock = file.read(1024)

def read_superblock(superblock, start, end):
    return superblock[start:end]

for v in superblock_struct:
    field = read_superblock(superblock, v[1], v[2]+1)
    print(v[0] + ' ' + str(int.from_bytes(field, byteorder='little')))
