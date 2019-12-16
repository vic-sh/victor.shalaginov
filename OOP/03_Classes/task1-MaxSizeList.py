class MaxSizeList(object):
    def __init__(self, SizeOfClass):
        self.SizeOfClass = SizeOfClass
        self.ListOfElements = []
    def push(self, ElementToAdd):
        self.ElementToAdd = ElementToAdd
        if len(self.ListOfElements) < self.SizeOfClass:
            self.ListOfElements.append(self.ElementToAdd)
        else:
            self.ListOfElements.pop(0)
            self.ListOfElements.append(self.ElementToAdd)
    def get_list(self):
        return self.ListOfElements