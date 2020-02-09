from item.static import Item
from block_group.inode import Inode
from directory.file import File
from superblock.superblock import Superblock
from factory.filesystem import filesystem_factory
from factory.superblock import superblock_factory


class Directory:
    STATIC_FILE_FIELDS_LENGTH = 8

    def __init__(self, address):
        self.file_structure = [
            Item('inode', Item.TYPE_NUMERIC, 0, 4),
            Item('rec_len', Item.TYPE_NUMERIC, 4, 2),
            Item('name_len', Item.TYPE_NUMERIC, 6, 1),
            Item('file_type', Item.TYPE_NUMERIC, 7, 1),
        ]
        self.file = None
        self._filesystem = filesystem_factory.get()
        self.superblock = superblock_factory.get()
        self.address = address
        self.get_files()

    def get_file(self, record_offset=0):
        _file = File()
        block = self._filesystem.read(self.calculate_offset(
            record_offset), Directory.STATIC_FILE_FIELDS_LENGTH + 10)
        for element in self.file_structure:
            setattr(
                _file,
                element.name,
                element.get_value(block)
            )
        setattr(
            _file,
            'file_name',
            Item(
                'file_name',
                Item.TYPE_STRING,
                0,
                _file.name_len
            ).get_value(self._filesystem.read(
                self.calculate_offset(Directory.STATIC_FILE_FIELDS_LENGTH + record_offset), _file.name_len))
        )
        return _file

    def get_files(self):
        self.file = self.get_file(0)
        current = self.file
        offset = 0
        while not current.is_last_file():
            offset += current.rec_len
            current.next_file = self.get_file(offset)
            current = current.next_file

    def calculate_offset(self, offset):
        start = self.superblock.get_block_size() * self.address
        return start + offset

    def ls(self):
        files = 'name type created_at size\n'
        files += '--- --- --- ---'
        current = self.file
        while current is not None:
            files += "\n{} {} {} {}".format(
                current.file_name,
                current.file_type,
                current.get_inode().i_ctime,
                current.get_inode().i_size
            )
            current = current.next_file

        return self.padding(files)

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
            formatted_text += "{0:{spaces}} {1}   {2}    {3}\n".format(
                txt[0], txt[1], txt[2], txt[3], spaces=spacing)
        return formatted_text


def get_root_directory():
    inode = Inode(2)
    dir_addr = inode.get_direct_blocks()

    return Directory(dir_addr)
