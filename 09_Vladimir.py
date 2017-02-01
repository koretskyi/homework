import random

class Dishes():

    def __init__(self, dishes):
        self.name = dishes.split(',')
        self.cap_name = [el.strip().capitalize() for el in self.name]
        self.setList = list(set(self.cap_name))

    def calc_time(self):
        return random.randint(1, 60)

entered_dishes = input('What would you like?\n')
w = Dishes(entered_dishes)
for i in range(len(w.setList)):
        print(w.setList[i], (40 - len(w.setList[i])) * '.', w.calc_time())

