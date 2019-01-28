from assignment_7 import Food


class Meat(Food):
    def cook(self):
        print("\nI like to cook!")


meat1 = Meat("pork", "apple")
meat1.cook()
meat1.eat1()



