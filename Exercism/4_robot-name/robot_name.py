# Logic to create a new random name
import random
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
def createName():
        name = ""
        for i in range(2):
            name += letters[random.randint(0,25)].upper()
        for i in range(3):
            name += numbers[random.randint(0,9)]
        return name    

class Robot:
    names = {}
    def __init__(self):
        self.name = None
        self.reset()
    def reset(self):
        # Repeat until you have a unused name
        while self.name == None or self.name in Robot.names:
            self.name = createName()
        # Add name to list of used names
        Robot.names[self.name] = 1
