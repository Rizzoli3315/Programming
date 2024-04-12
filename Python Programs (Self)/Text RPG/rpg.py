# RPG GAME 'ESCAPE THE MONSTER HOUSE'
# BY ARYAN GUPTA
# 10 MARCH 2019

import time

def showInstructions():
    #main menu and commands
    print('''
RPG Game
========
Commands:
   go [direction]->(north,south,east,west,up,down)
   get [item]
========
Objective:
   Monsters have invaded your house!! Collect
   all your valuable items and escape.Dodge the
   monsters and escape from the house.Don't make
   it too late or you will be eaten alive!!!
   Collect all the items which will help you
   escape.In total there are ten items which
   are scattered in different rooms, along with
   hungry monsters which will kill you the moment
   they set their ugly eyes upon you.You are
   alone in the house and have to survive
   yourself.If you survive, we will meet again
   but till then GOOD LUCK.SAYONARA!!! ''')

def showStatus():
    #print players current status
    print('----------------------')
    print('You are in the ' + currentRoom)
    #inventory
    print('Inventory : ' + str(inventory))
    #print item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("----------------------")

#an inventory which is initially empty
inventory=[]

# a dictionary linking a room to other rooms
rooms={
           'Hall' : {
                  'south':'Kitchen',
                  'east' :'Dining Room',
                  'item' : 'key',
                  'west' : 'Master Bedroom'
                },

           'Kitchen' : {
                  'north':'Hall',
                  'Esst':'Living Room',
                  'item':'monster'
                },

           'Dining Room' : {
                  'west':'Hall',
                  'south':'Living Room'
                },

           'Living Room' : {
                  'north':'Dining Room',
                  'west':'Kitchen',
                  'item':'potion'
                },

           'Master Bedroom' : {
                  'east':'Hall',
                  'south':'Washroom',
                  'item': 'armour',
                  'west':'Stairs'
                },

           'Washroom' : {
                  'north':'Master Bedroom',
                  'item':'monster'
                },
             
           'Stairs' : {
                  'east':'Master Bedroom',
                  'up':'Hallway',
                  'down':'Study'
                },
              
           'Hallway': {
                  'down':'Stairs',
                  'east':'Library',
                  'north':'Small Bedroom',
                  'south':''
                },

           'Study':{
                  'up':'Stairs'
                }     


      }

#Start the player in the hall
currentRoom='Hall'

showInstructions()

#loop forever
while True:

    showStatus()

    #get the player's next move
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move=''
    while move == '':
        move = input('> ')

    move = move.lower().split()

    #if they type 'go' first
    if move[0]=='go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
            
    #if they type 'get' first
    if move[0] == 'get':
        #if the room contains an item, and the item is the one they want to get
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to the inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1]+' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get '+ move[1] + '!')

    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
         print('A monster has got you...')
         time.sleep(2)
         print('GAME OVER!')
         break
 
    if currentRoom == 'Dining Room' and 'key' in inventory and 'potion' in inventory and 'armour' in inventory:
        print(''' You escaped the house.''')
        time.sleep(2)
        print(''' YOU WIN!!!''')
        break
