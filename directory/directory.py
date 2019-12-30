from item.static import Item


class Directory:
    def __init__(self, block):
        self.structure = [
            Item('inode', Item.TYPE_NUMERIC, 0, 4),
            Item('rec_len', Item.TYPE_NUMERIC, 4, 2),
            Item('name_len', Item.TYPE_NUMERIC, 6, 1),
            Item('file_type', Item.TYPE_NUMERIC, 7, 1),
            Item('name', Item.TYPE_BYTE, 8, 32),
        ]

        self.block = block
        self.inode = ''
        self.rec_len = ''
        self.name_len = ''
        self.file_type = ''
        self.name = ''

        self.read()

    def read(self):
        for element in self.structure:
            setattr(self, element.name, element.get_value(self.block))

    def __str__(self):
        return ""
