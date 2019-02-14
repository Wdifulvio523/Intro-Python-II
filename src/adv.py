from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["stick", "rock"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["candlestick"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["telescope", "sword"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["axe", "broken axe"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
arlier adventurers. The only exit is to the south.""", ["chest", "skeleton"]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player("Bill", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player_input = None
while (player_input is not 'q'):
    print(f'''You are holding {p.items}, and you are at the {p.currentRoom.name} which has the items {p.currentRoom.items}:
'{p.currentRoom.description}.'
 Please pick a direction to go in (n, e, s, w). Or, you can pick up an item using (p)''')
    player_input  = input("Enter your direction: ")
    previous_room = p.currentRoom
    if player_input != "p" and player_input != "d":
        p.move(player_input)
    else:
        p.itemInteraction(player_input)
    if p.currentRoom == None:
        print("You cannot do that punk!")
        p.currentRoom=previous_room
