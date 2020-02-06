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
                if entry.is_last_entry():
                    break
                self.entries.append(entry)

    def ls(self):
        entries = 'name type\n'
        entries += '--- ---'
        for entry in self.entries:
            entries += "\n{} {}".format(entry.name, entry.file_type)

        return self.padding(entries)

    def get_info(self, name):
        for entry in self.entries:
            if name == entry.name:
                return str(entry)

    def padding(self, text):
        formatted_text = ''
        arr = text.split('\n')
        length = 0
        for ell in arr:
            for txt in ell.split(' '):
                if len(txt) > length:
                    length = len(txt)
        
        spacing = length + 5
        for ell in arr:
            txt = ell.split(' ')
            formatted_text += "{0:{spaces}}{1}\n".format(txt[0], txt[1], spaces=spacing) 
        return formatted_text


def get_root_directory(filesystem, superblock, group_descriptor):
    block_size = superblock.s_log_block_size
    inode_size = superblock.s_inode_size
    inode_table_idx = group_descriptor.bg_inode_table
    with open(filesystem, 'rb') as file:
        idx = inode_table_idx * block_size + inode_size
        file.seek(idx)
        root_directory = file.read(inode_size)
        inode = Inode(root_directory)
        dir_addr = inode.get_direct_blocks()
    
    return Directory(filesystem, dir_addr)