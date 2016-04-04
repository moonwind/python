class Thing() :pass

class Thing2():
    def __init__(self,letter):
        self.__letter = letter

    def __str__(self):
        return "class print "

    @property
    def letter(self):
        print('inside the get letter')
        return self.__letter
    @letter.setter
    def letter(self,letter):
        self.__letter = letter
        


class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol 
        self.number =number

class newElement(Element):
    def dump(self):
        print("name :",self.name,"  symbol : ",self.symbol," number :",self.number)

print(Thing);
example = Thing()
print(example)


oneThing = Thing2("abc")
print(oneThing)
print(oneThing.letter)
oneThing.letter = "qwer"
print(oneThing.letter)

dic = {'name':'Hydrogen','symbol':'H','number':99}



ele = Element(**dic)


print(ele.name,ele.number,ele.symbol)


print("")
print("test dump ")
newele = newElement(**dic);
newele.dump()
print(newele)






