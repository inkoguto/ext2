def get_superblock():
    pass

def get_superblock_backups():
    pass

class Item:
    def __init__(self, type, start, offset):
        self.type = type,
        self.start = start,
        self.offset = offset
        self.value = ''

    def __repr__(self):
        pass

class Superblock:
    def __init__(self, superblock):
        self.superblock = superblock
    
    def __repr__(self):
        pass