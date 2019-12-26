import datetime

class Ext2Decoder:
    def __init__(self):
        pass

    def detect(self, _type):
        if _type == Item.TYPE_NUMERIC:
            return lambda x : int.from_bytes(x, byteorder='little')
        elif _type == Item.TYPE_STRING:
            return lambda x : x.decode('ascii')
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
    TYPE_BYTE = 4

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

        if self.type is Item.TYPE_BYTE:
            self.value = self.raw_value
        else:
            self.value = self.decode()

        return self.value

    def decode(self):
        if self.decoder is not None:
            return self.decoder.decode(self)

        return None

