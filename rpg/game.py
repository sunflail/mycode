#!/usr/bin/env python3
"""
RPG project, forked from RZFeezer
Expansion author: Sunflail
Practice with slicing and dictionary modeling
"""

def showInstructions():
    """
    Shows instructions upon game start.
    :return:
    """
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use [item]
  help - brings up this menu again at any time
  q - quit at any time
''')

def setupGame():
    # an inventory, which is initially empty
    inventory = []
    # status effects, initially empty
    status_effects = []
    # A dictionary linking a room to other rooms
    rooms = {
        'Hall': {
            'south': 'Kitchen',
            'east': 'Dining Room',
            'item': 'key',
            'creature': 'cat'
        },
        'Kitchen': {
            'north': 'Hall',
            'creature': 'monster',
        },
        'Dining Room': {
            'west': 'Hall',
            'south': 'Garden',
            'item': 'potion',
            'north': 'Pantry',
        },
        'Garden': {
            'north': 'Dining Room'
        },
        'Pantry': {
            'south': 'Dining Room',
            'item': 'cookie',
        }
    }
    # start the player in the Hall
    currentRoom = 'Hall'
    return currentRoom, inventory, rooms, status_effects

def gameLoop():
    currentRoom, inventory, rooms, status_effects = setupGame()

    def showStatus():
        """
        Shows current status on entering each room or when called.
        :return:
        """
        # print the player's current status
        print('---------------------------')
        print('You are in the ' + currentRoom)
        # print the current inventory
        print('Inventory : ' + str(inventory))
        # print current status effects if any are present
        if len(status_effects) > 0:
            print(f'Current status effects: {status_effects}')
        # print an item if there is one
        if "item" in rooms[currentRoom]:
            print('You see a ' + rooms[currentRoom]['item'])
        # print if there is a cat in the room
        if "creature" in rooms[currentRoom] and "cat" in rooms[currentRoom]['creature']:
            print('You see a mangy cat on the ground, eating scraps off the floor.')
        print("---------------------------")

    while True:

        showStatus()

        # get the player's next 'move'
        # .split() breaks it up into an list array
        # eg typing 'go east' would give the list:
        # ['go','east']
        move = ''
        while move == '':
            move = input('>')

        # split allows an items to have a space on them
        # get golden key is returned ["get", "golden key"]
        move = move.lower().split(" ", 1)

        # global quit option
        if move[0] == 'q':
            print('\nTake a break, try again another day hero!')
            exit(0)

        # display instructions again on command
        if move[0] == 'help':
            showInstructions()

        # if they type 'go' first
        if move[0] == 'go':
            # check that they are allowed wherever they want to go
            if move[1] in rooms[currentRoom]:
                # set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
            # there is no door (link) to the new room
            else:
                print('You can\'t go that way!')

        # if they type 'get' first
        if move[0] == 'get':
            # if the room contains an item, and the item is the one they want to get
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                # add the item to their inventory
                inventory += [move[1]]
                # display a helpful message
                print(move[1] + ' got!')
                # delete the item from the room
                del rooms[currentRoom]['item']
            # otherwise, if the item isn't there to get
            else:
                # tell them they can't get it
                print('Can\'t get ' + move[1] + '!')

        # if they type 'use' first
        if move[0] == 'use':
            # check inventory for item
            if move[1] in inventory and move[1] == 'potion':
                print("You use the potion and become enraged. The potion crumbles to dust.")
                status_effects.append('Enraged')
                inventory.remove(move[1])
            elif move[1] in inventory:
                print(f'You use the {move[1]} and it crumbles to dust.')
                inventory.remove(move[1])
            else:
                print("You don't have anything that sounds like that to use.")

        ## Define non violent way a player can win
        if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
            print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
            break

        ## If a player enters a room with a monster BUT HAS A COOKIE
        if 'creature' in rooms[currentRoom]:
            if 'monster' in rooms[currentRoom]['creature']:
                if 'cookie' in inventory:
                    print('The monster takes your cookie and runs away! Whew!')
                    del rooms[currentRoom]['creature']
                    inventory.remove('cookie')
                elif 'cat-with-cookie' in inventory:
                    print(
                        'The monster tries to take the cookie from the cat and the cat kills the monster, then sits down to finish the cookie.')
                    del rooms[currentRoom]['creature']
                    inventory.remove('cat-with-cookie')
                # Violent win condition
                elif 'Enraged' in status_effects:
                    print(
                        'Being enraged, you notice the monster and react before it can, ripping it in two. Praise Odin. Feeling empowered from the kill, you break through the south wall and stomp off to your freedom.')
                    break
                elif 'monster' in rooms[currentRoom]['creature']:
                    print('A monster has got you... GAME OVER!')
                    break
            elif 'cat' in rooms[currentRoom]['creature']:
                if 'cookie' in inventory:
                    print('The cat takes your cookie and runs away! After it!')
                    # cat takes cookie and retreats to the pantry
                    rooms['Pantry']['item'] = 'cat-with-cookie'
                    inventory.remove('cookie')
                    del rooms[currentRoom]['creature']
                # Enraged use on cat condition
                elif 'Enraged' in status_effects:
                    print(
                        "You're bloodsoaked vision sees the mangy cat. It looks delicious. You eat it, and it sates your blood thirst. You are no longer enraged.")
                    del rooms[currentRoom]['creature']
                    status_effects.remove('Enraged')

def main():
    """
    Where the action happens.
    :return:
    """
    showInstructions()
    gameLoop()

main()

if __name__ == "__main__":
    main()
