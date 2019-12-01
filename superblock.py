base_superblock_fields = [
    ['total_inodes', 0, 3, 4],
    ['total_blocks', 4, 7, 4],
    ['reserved_blocks', 8, 11, 4],
    ['unnalocated_blocks', 12, 15, 4],
    ['unnalocated_inodes', 16, 19, 4],
    ['block_containing_superblock', 20, 23, 4],
    ['block_size', 24, 27, 4],
    ['fragment_size', 28, 31, 4],
    ['blocks_in_group', 32, 35, 4],
    ['fragments_in_group', 36, 39, 4],
    ['inodes_in_group', 40, 43, 4],
    ['last_mounted', 44, 47, 4],
    ['last_written', 48, 51, 4],
    ['mounts_since_last_check', 52, 53, 2],
    ['mounts_to_next_check', 54, 55, 2],
    ['ext2_signature', 56, 57, 2],
    ['filesystem_state', 58, 59, 2],
    ['error_behavior', 60, 61, 2],
    ['minor_version', 62, 63, 2],
    ['last_check', 64, 67, 4],
    ['check_interval', 68, 71, 4],
    ['os_id', 72, 75, 4]
    ['major_version', 76, 79, 4],
    ['superuser_id', 80, 81, 2],
    ['superuser_group', 82, 83, 2]
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


