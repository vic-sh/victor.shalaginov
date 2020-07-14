class MaxSizeList(object):

    def __init__(self, LengthOfList):
        self.MaxLengthOfList = LengthOfList
        #self.CurrentLengthOfList = 0
        self.ListOfElements = []

    def push(self, ElementOfList):
        if len(self.ListOfElements) >= self.MaxLengthOfList:
            self.ListOfElements.pop(0)
            self.ListOfElements.append(ElementOfList)
        else:
            self.ListOfElements.append(ElementOfList)
    
    def get_list(self):
        return self.ListOfElements
            
a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
