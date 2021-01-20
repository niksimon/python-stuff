class Chef:
    def make_chicken(self):
        print("Chicken")
    def make_salad(self):
        print("Salad")
    def make_special_dish(self):
        print("Special dish")

class ChineseChef(Chef):
    def make_rice(self):
        print("Rice")

c = Chef()
c2 = ChineseChef()

c.make_chicken()
c.make_salad()
c2.make_chicken()
c2.make_rice()