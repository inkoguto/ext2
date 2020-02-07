from item.static import Item
from block_group.inode import Inode
from directory.file import File
from superblock.superblock import Superblock

class Directory:
    def __init__(self, _filesystem, address):
        self.files = []
        self._filesystem = _filesystem
        self.address = address
        self._list()

    def _list(self):
        with open(self._filesystem, 'rb') as _filesystem:
            _filesystem.seek(self.address * 1024)
            while True:
                _file = File(_filesystem)
                if _file.is_last_file():
                    break
                self.files.append(_file)

    def ls(self):
        entries = 'name type\n'
        entries += '--- ---'
        for _file in self.files:
            entries += "\n{} {}".format(_file.name, _file.file_type)

        return self.padding(entries)

    def get_info(self, name):
        for _file in self.files:
            if name == _file.name:
                return str(_file)

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


def get_root_directory(filesystem, group_descriptor):
    superblock = Superblock()
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

def get_directory(filesystem, inode):
    pass