base_superblock_fields = [
    ['s_inodes_count', 0, 4],
    ['s_blocks_count', 4, 4],
    ['s_r_blocks_count', 8, 4],
    ['s_free_blocks_count', 12 4],
    ['s_free_inodes_count', 16, 4],
    ['s_first_data_block', 20, 4],
    ['s_log_block_size', 24, 4],
    ['s_log_frag_size', 28, 4],
    ['s_blocks_per_group', 32, 4],
    ['s_frags_per_group', 36, 4],
    ['s_inodes_per_group', 40, 4],
    ['s_mtime', 44, 4],
    ['s_wtime', 48, 4],
    ['s_mnt_count', 52, 2],
    ['s_max_mnt_count', 54, 2],
    ['s_magic', 56, 2],
    ['s_state', 58, 2],
    ['s_errors', 60, 2],
    ['s_minor_rev_level', 62, 2],
    ['s_lastcheck', 64, 4],
    ['s_checkinterval', 68, 4],
    ['s_creator_os', 72, 4]
    ['s_rev_level', 76, 4],
    ['s_def_resuid', 80, 2],
    ['s_def_resgid', 82, 2],
    ['s_first_ino', 84, 4],
    ['s_inode_size', 88, 2],
    ['s_block_group_nr', 90, 42,
    ['s_feature_compat', 92, 4],
    ['s_feature_incompat', 96, 4],
    ['s_featre_ro_compat', 100, 4],
    ['s_uuid', 104, 16],
    ['s_volume_name', 120, 16],
    ['s_last_mounted', 136, 64],
    ['s_algo_bitmap', 200, 4],
    ['s_prealloc_blocks', 204, 1],
    ['s_prealloc_dir_blocks', 205, 1],
    ['s_journal_uuid', 208, 16],
    ['s_journal_inum', 224, 4],
    ['s_journal_dev', 228, 4],
    ['s_last_orphan', 232, 4],
    ['s_hash_seed', 236, 16],
    ['s_def_hash_version', 252, 1],
    ['s_default_mount_options', 256, 4],
    ['s_first_meta_bg', 260, 4]
]


filesystem_states = {
    1: 'clean',
    2: 'errors'
}

error_handling_method = {
    1: 'ignore',
    2: 'remount',
    3: 'kernel_panic'
}

creator_os_ids = {
    0: 'Linux',
    1: 'GNU HURD',
    2: 'MASIX',
    3: 'FreeBSD',
    4: 'Other'
}


