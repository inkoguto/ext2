import datetime

class Ext2Decoder:
    def __init__(self):
        pass

    def detect(self, _type):
        if _type == Item.TYPE_NUMERIC:
            return lambda x : int.from_bytes(x, byteorder='little')
        elif _type == Item.TYPE_STRING:
            return lambda x : x
        elif _type == Item.TYPE_DATETIME:
            return lambda x :  datetime.datetime.fromtimestamp(int.from_bytes(x, byteorder='little')).isoformat() if int.from_bytes(x, byteorder='little') > 0  else 0
        elif _type == Item.TYPE_SIZE:
            return lambda x : 1024 << int.from_bytes(x, byteorder='little')

    def decode(self, item):
        decoder = self.detect(item.type)
        return decoder(item.raw_value)

class Item:
    TYPE_NUMERIC = 0
    TYPE_STRING = 1
    TYPE_DATETIME = 2
    TYPE_SIZE = 3

    def __init__(self, name, _type, begin, offset, decoder=Ext2Decoder()):
        self.name = name
        self.type = _type
        self.begin = begin
        self.offset = offset
        self.decoder = decoder
        self.value = None
        self.raw_value = None

    def get_value(self, superblock):
        if self.raw_value is None:
            self.raw_value = superblock[self.begin:self.begin + self.offset]
        
        self.value = self.decode()

        return self.value

    def decode(self):
        if self.decoder is not None:
            return self.decoder.decode(self)

        return None

superblock_structure = [
    Item('s_inodes_count', Item.TYPE_NUMERIC, 0, 4),
    Item('s_blocks_count', Item.TYPE_NUMERIC, 4, 4),
    Item('s_blocks_count', Item.TYPE_NUMERIC, 4, 4),
    Item('s_r_blocks_count', Item.TYPE_NUMERIC, 8, 4),
    Item('s_free_blocks_count', Item.TYPE_NUMERIC, 12, 4),
    Item('s_free_inodes_count', Item.TYPE_NUMERIC, 16, 4),
    Item('s_first_data_block', Item.TYPE_NUMERIC, 20, 4),
    Item('s_log_block_size', Item.TYPE_SIZE, 24, 4),
    Item('s_log_frag_size', Item.TYPE_SIZE, 28, 4),
    Item('s_blocks_per_group', Item.TYPE_NUMERIC, 32, 4),
    Item('s_frags_per_group', Item.TYPE_NUMERIC, 36, 4),
    Item('s_inodes_per_group', Item.TYPE_NUMERIC, 40, 4),
    Item('s_mtime', Item.TYPE_DATETIME, 44, 4),
    Item('s_wtime', Item.TYPE_DATETIME, 48, 4),
    Item('s_mnt_count', Item.TYPE_NUMERIC, 52, 2),
    Item('s_max_mnt_count', Item.TYPE_NUMERIC, 54, 2),
    Item('s_magic', Item.TYPE_NUMERIC, 56, 2),
    Item('s_state', Item.TYPE_NUMERIC, 58, 2),
    Item('s_errors', Item.TYPE_NUMERIC, 60, 2),
    Item('s_minor_rev_level', Item.TYPE_NUMERIC, 62, 2),
    Item('s_lastcheck', Item.TYPE_DATETIME, 64, 4),
    Item('s_checkinterval', Item.TYPE_NUMERIC, 68, 4),
    Item('s_creator_os', Item.TYPE_NUMERIC, 72, 4),
    Item('s_rev_level', Item.TYPE_NUMERIC, 76, 4),
    Item('s_def_resuid', Item.TYPE_NUMERIC, 80, 2),
    Item('s_def_resgid', Item.TYPE_NUMERIC, 82, 2),
    Item('s_first_ino', Item.TYPE_NUMERIC, 84, 4),
    Item('s_inode_size', Item.TYPE_NUMERIC, 88, 2),
    Item('s_block_group_nr', Item.TYPE_NUMERIC, 90, 42),
    Item('s_feature_compat', Item.TYPE_NUMERIC, 92, 4),
    Item('s_feature_incompat', Item.TYPE_NUMERIC, 96, 4),
    Item('s_featre_ro_compat', Item.TYPE_NUMERIC, 100, 4),
    Item('s_uuid', Item.TYPE_NUMERIC, 104, 16),
    Item('s_volume_name', Item.TYPE_STRING, 120, 16),
    Item('s_last_mounted', Item.TYPE_STRING, 136, 64),
    Item('s_algo_bitmap', Item.TYPE_NUMERIC, 200, 4),
    Item('s_prealloc_blocks', Item.TYPE_NUMERIC, 204, 1),
    Item('s_prealloc_dir_blocks', Item.TYPE_NUMERIC, 205, 1),
    Item('s_journal_uuid', Item.TYPE_NUMERIC, 208, 16),
    Item('s_journal_inum', Item.TYPE_NUMERIC, 224, 4),
    Item('s_journal_dev', Item.TYPE_NUMERIC, 228, 4),
    Item('s_last_orphan', Item.TYPE_NUMERIC, 232, 4),
    Item('s_hash_seed', Item.TYPE_NUMERIC, 236, 16),
    Item('s_def_hash_version',Item.TYPE_NUMERIC, 252, 1),
    Item('s_default_mount_options', Item.TYPE_NUMERIC, 256, 4),
    Item('s_first_meta_bg', Item.TYPE_NUMERIC, 260, 4),
]


class Superblock:
    EXT2_MAGIC_NUMBER = 0xef53

    class __Superblock:
        def __init__(self, superblock, superblock_structure):
            self.superblock = superblock
            self.superblock_structure = superblock_structure

    instance = None
    def __init__(self, superblock, superblock_structure):
        if not Superblock.instance:
            Superblock.instance = Superblock.__Superblock(superblock, superblock_structure)
        else:
            Superblock.instance.superblock = superblock
            Superblock.instance.superblock_structure = superblock_structure
        
        self.check_magic_number()
    
    def __getattr__(self, name):
        return getattr(self.instance, name)

    def check_magic_number(self):
        magic_number = self.get('s_magic')
        if magic_number != Superblock.EXT2_MAGIC_NUMBER:
            raise Exception('not ext2')

    def get(self, name):
        try:
            match, = [ chunk for chunk in self.superblock_structure if chunk.name == name]
        except ValueError:
            raise Exception('element does not exists')

        return match.get_value(self.superblock)

    def get_all(self):
        for element in self.superblock_structure:
            yield [element.name, element.get_value(self.superblock)]

        return None
