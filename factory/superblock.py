from superblock.superblock import Superblock

class SuperblockFactory:
    superblock = None
    
    def get(self):
        if self.superblock is not None:
            return self.superblock

        return Superblock() 

superblock_factory = SuperblockFactory()
