from math import ceil
from item.static import Item

class Superblock:
    EXT2_MAGIC_NUMBER = 0xef53

    STRUCTURE = [
        Item('s_inodes_count', Item.TYPE_NUMERIC, 0, 4),
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
        Item('s_block_group_nr', Item.TYPE_BYTE, 90, 42),
        Item('s_feature_compat', Item.TYPE_NUMERIC, 92, 4),
        Item('s_feature_incompat', Item.TYPE_NUMERIC, 96, 4),
        Item('s_feature_ro_compat', Item.TYPE_NUMERIC, 100, 4),
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
        Item('s_hash_seed', Item.TYPE_BYTE, 236, 16),
        Item('s_def_hash_version', Item.TYPE_NUMERIC, 252, 1),
        Item('s_default_mount_options', Item.TYPE_NUMERIC, 256, 4),
        Item('s_first_meta_bg', Item.TYPE_NUMERIC, 260, 4),
    ]

    class __Superblock:
        def __init__(self, superblock):
            self.superblock = superblock

    instance = None

    def __init__(self, superblock = None):
        if not Superblock.instance:
            Superblock.instance = Superblock.__Superblock(
                superblock)
        else:
            if superblock is not None:
                Superblock.instance.superblock = superblock

        self.read()
        self.check_magic_number()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def read(self):
        for item in Superblock.STRUCTURE:
            setattr(self, item.name, item.get_value(self.superblock))

    def check_magic_number(self):
        magic_number = self.s_magic
        if magic_number != Superblock.EXT2_MAGIC_NUMBER:
            raise Exception('not ext2')

    def get_block_groups_count(self):
        return ceil(self.s_blocks_count / self.s_blocks_per_group)

    def get_block_group_size(self):
        return self.s_blocks_per_group * self.s_log_block_size

    def get_inode_size(self):
        return self.s_inode_size

    def get_inodes_per_group(self):
        return self.s_inodes_per_group

    def __str__(self):
        superblock = ''
        for item in Superblock.STRUCTURE:
            superblock += "{}: {}\n".format(item.name, getattr(self, item.name))

        return superblock