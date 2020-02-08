class Filesystem:

    class __Filesystem:
        name = None

        def __init__(self, name):
            self.name

    instance = None

    def __init__(self, name = None):
        if not Filesystem.instance:
            Filesystem.instance = Filesystem.__Filesystem(name)
        if name is not None:
            Filesystem.instance.name = name

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        setattr(self.instance, name, value)

    def read(self, offset, length, relative = 0):
        with open(self.name, 'rb') as _file:
            _file.seek(offset, relative)
            result = _file.read(length)

        return result
