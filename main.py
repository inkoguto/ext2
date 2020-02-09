from block_group import get_block_descriptor
from directory.directory import get_root_directory, change_directory
from factory.superblock import superblock_factory

if __name__ == "__main__":
    sb = superblock_factory.get()
    print("superblock:"
          "\n{}\n".format(sb))
    for index in range(0, sb.get_block_groups_count()):
        descriptor = get_block_descriptor(index)
        print("{} block group:\n{}".format(index, descriptor))

    directory = get_root_directory()
    print(directory)

    new_dir = change_directory(directory, 'testowy')
    print(new_dir)

    new_dir_2 = change_directory(new_dir, 'subtestdirectory')
    print(new_dir_2)

    new_dir_3 = change_directory(directory, 'test')
    print(new_dir_3)
