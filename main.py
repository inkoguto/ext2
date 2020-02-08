from block_group.descriptor import Descriptor
from block_group.inode import Inode
from block_group import get_block_descriptor
from directory.directory import get_root_directory, Directory
from filesystem import Filesystem
from factory.superblock import superblock_factory

if __name__ == "__main__":
    sb = superblock_factory.get()
    print("superblock: \n{}\n".format(sb))
    for index in range(0, sb.get_block_groups_count()):
        descriptor = get_block_descriptor(index)
        print("{} block group:\n{}".format(index, descriptor))

    directory = get_root_directory(get_block_descriptor(0))
    print(directory.ls())