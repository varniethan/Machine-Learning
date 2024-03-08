class Animal():
    def __init__(self, name):
        self.name = name
        #create a private variable
        self.__private = 'private'
        #create a protected variable
        self._protected = 'protected'

    def speak(self):
        print(f'{self.name} says "Hello!"')

class Dog(Animal):
    def speak(self):
        print(f'{self.name} says "Woof!"')

class Cat(Animal):
    def speak(self):
        print(f'{self.name} says "Meow!"')

dog = Dog('Fido')
dog.speak()


"""
A very simple problem with many different solutions, but the main aim is to solve it in the most efficient way.
A man was given directions to go from point A to point B. 
The directions were: “SOUTH”, “NORTH”, “WEST”, “EAST”. Clearly “NORTH” and “SOUTH” are opposite, “WEST” and “EAST” too. 
Going to one direction and coming back in the opposite direction is a waste of time and energy. 
So, we need to help the man by writing a program that will eliminate the useless steps and will contain only the necessary directions. 
For example: The directions [“NORTH”, “SOUTH”, “SOUTH”, “EAST”, “WEST”, “NORTH”, “WEST”] should be reduced to [“WEST”]. 
This is because going “NORTH” and then immediately “SOUTH” means coming back to the same place. 
So we cancel them and we have [“SOUTH”, “EAST”, “WEST”, “NORTH”, “WEST”]. 
Next, we go “SOUTH”, take “EAST” and then immediately take “WEST”, which again means coming back to the same point. 
Hence we cancel “EAST” and “WEST” to giving us [“SOUTH”, “NORTH”, “WEST”]. 
It’s clear that “SOUTH” and “NORTH” are opposites hence canceled and finally we are left with [“WEST”].
"""
opposite = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
def answer(directions):
    # Loop through the list and print the current and next actions
    answer = directions
    i = 0
    while i < len(directions)-1:
        print(i, directions)
        if directions[i+1] == opposite[directions[i]]:
                directions.pop(i)
                directions.pop(i)
                i = 0
        else:
            i += 1
            
    return directions

print(answer(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))