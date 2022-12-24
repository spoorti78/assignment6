class Dog:
    def __init__(self,name,age,coatcolor):
        self.name=name
        self.age=age
        self.coatcolor=coatcolor

    def description(self):
        print("The name of the DOG is : " +self.name)
        print("The age of the DOG is:  ", self.age)
    
    def get_info(self):
        print("The coatcolor is: "  +self.coatcolor)


class JackRussellTerrier(Dog):
    def myHuman(self):
        print("The name of my Human is spoorti")

    def favFood(self):
        print("Oscar's favourite food to eat is chicken")
       

class Bulldog(Dog):
    def myHuman(self):
        print("The name of my Human is Anuj")

    def favFood(self):
        print("Cupper's favourite food to eat is pedigree")
       
print("*****************The Details of Dog_1**********************")

jack =JackRussellTerrier("Oscar",3,"Blue")
jack.description()
jack.get_info()
jack.myHuman()
jack.favFood()

print("*****************The Details of Dog_2**********************")

bull = Bulldog("Cupper",4,"Beige")
bull.description()
bull.get_info()
bull.myHuman()
bull.favFood()