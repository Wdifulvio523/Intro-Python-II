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

CRED = '\033[91m'
CBLUE = '\033[34m'
CGREEN = '\033[92m'
CEND = '\033[0m'
print(CRED + str(p) + CEND)

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
# Guaranteed that q exits the game
while (player_input is not 'q'):
    # print details for the player, color coded for readability
    # Check the backpack for items. If no items tell player that
    if len(p.items) == 0:
        print(CGREEN + f'''\nThere is nothing in your backpack \n ''' + CEND)
    # If items are in the backpack, prints out the items
    else:
        print(CGREEN + f'''\nBackpack:''' + CEND)
        for item in p.items:
            print(f'{item}')
    print(CBLUE + f'''\nYou are at the {p.currentRoom.name} {p.currentRoom.description}.''' + CEND)
    # Check for items on the ground. If no items, tels player
    if len(p.currentRoom.items) == 0: 
        print(CBLUE + f'Looking around, you do not see anything on the ground' + CEND)
        print(CGREEN + f'Please pick a direction to go in (north, east, south, west).' + CEND)

    # if items are in the room, prints out the items
    else:
        print(CBLUE + f'Looking around, you see:' + CEND)
        for item in p.currentRoom.items:
            print(f'a {item}')
        print(CGREEN + f'''Please pick a direction to go in (north, east, south, west). Or, you can pick up an item''' + CEND)
    
    
    # start of player input
    player_input  = input(CRED + "\nWhat will you do? >>> " + CEND)
    #created variable that references currentRoom of player
    previous_room = p.currentRoom
    # two possibilities for a player to move 
    # either one word (n or north) or two words, starting with go (go north, go n) 
    if player_input != "p" and player_input != "d":
        p.move(player_input)
    if player_input.startswith("go "):
        direction = player_input.split(' ')
        p.move(direction[1])  
    # two possibilities for a player to pick up an item
    # two words, Starting with "get" will pick up the item referenced (get rock)
    if player_input.startswith("get "):
        items = player_input.split(' ')
        p.pickup(items[1])
    # if just "p", will prompt another input to ask what player wants to pick up
    if player_input == 'p':
        player_input = input("What do you want to pick up? ")
        p.pickup(player_input)
    # Same logic with drop
    if player_input.startswith("drop "):
        items = player_input.split(' ')
        p.drop(items[1])
    if player_input == "d":
        player_input = input("What do you want to drop? ")
        p.drop(player_input)
    # Error handling if there is no room in the players stated direction
    if p.currentRoom == None:
        print("You cannot do that punk!")
        p.currentRoom=previous_room
   
