from item.static import Item
from block_group.inode import Inode
from directory.entry import Entry

class Directory:
    def __init__(self, _file, address):
        self.entries = []
        self._file = _file
        self.address = address
        self._list()

    def _list(self):
        with open(self._file, 'rb') as _file:
            _file.seek(self.address * 1024)
            while True:
                entry = Entry(_file)
                self.entries.append(entry)
                if entry.is_last_entry():
                    break

    def __str__(self):
        entries = ''
        for entry in self.entries:
            entries += "{} \n".format(entry.name)

        return entries

def get_root_directory(filesystem, superblock, group_descriptor):
    block_size = superblock.s_log_block_size
    inode_size = superblock.s_inode_size
    inode_table_idx = group_descriptor.bg_inode_table
    with open(filesystem, 'rb') as file:
        file.seek(inode_table_idx * block_size + inode_size)
        root_directory = file.read(inode_size)
        inode = Inode(root_directory)
        dir_addr = inode.get_direct_blocks()
    
    return dir_addr