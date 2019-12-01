from datetime import datetime

with open("fs.img", "rb") as file:
    _ = file.read(1024)
    superblock = file.read(1024)

superblock_struct = [
    ['total_inodes', 0, 3, 4],
    ['total_blocks', 4, 7, 4],
    ['blocks_reserved_for_superuser', 8, 11, 4],
    ['unnalocated_blocks', 12, 15, 4],
    ['unnalocated_inodes', 16, 19, 4],
    ['block_containing_superblock', 20, 23, 4],
    ['block_size', 24, 27, 4]
]

def read_superblock(superblock, start, end):
    return superblock[start:end]

for v in superblock_struct:
    field = read_superblock(superblock, v[1], v[2]+1)
    print(v[0] + ' ' + str(int.from_bytes(field, byteorder='little')))
