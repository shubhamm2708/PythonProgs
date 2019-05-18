class Tree:
    def __init__(self,name,age,num): #defining a constructor in python using def keyword
        self.name=name
        self.age=age
        self.numberOfLeaves=num

    def Oxygen(self):
        print('I produce and give oxygen out for free')

    def Afforestation(self):
        print('Plant me more if you wanna survive')

class Mangotree(Tree):
    numberOfMangoes = 100
    height=9

    def warning(self):
        print('Do not pluck mangoes')

mango = Mangotree('MANGO' , 129, 100000)
print(mango.name)
