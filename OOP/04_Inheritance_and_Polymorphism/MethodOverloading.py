import abc

class GetSetParent(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0any().

    def set_val(self, value):
        self.val = value
        return

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):
    def set_val(self, value):   #Specializing
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value)

    def showdoc(self):
        print('GetSetInt object ({0}) only accepts integer values'.format(id(self)))

x = GetSetInt(3)
x.set_val(5)

print(x.set_val(5))
x.showdoc()
