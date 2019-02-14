# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, currentRoom, items=[]):
        self.currentRoom = currentRoom
        self.name = name
        self.items = items
    def __str__(self):
        return f"\nHello {self.name}! \n"
    #move function takes in a direction string
    def move(self, direction):
    # checks string for both long and short form
        if direction == "north" or direction == "n":
            self.currentRoom = self.currentRoom.n_to
        if direction == "south" or direction == "s":
            self.currentRoom = self.currentRoom.s_to
        if direction == "east" or direction == "e":
            self.currentRoom = self.currentRoom.e_to
        if direction == "west" or direction == "w":
            self.currentRoom = self.currentRoom.w_to
    #pickup function takes in an action string
    def pickup(self, action):
        #checks whether the action is inside of the currentroom.items list
        if action in self.currentRoom.items:
            #if so, adds to player item list and removes from currentroom items list
            self.items.append(action)
            self.currentRoom.items.remove(action)

    #reverse logic on drop
    def drop(self, action):
        if action in self.items:
            self.items.remove(action)
            self.currentRoom.items.append(action)
