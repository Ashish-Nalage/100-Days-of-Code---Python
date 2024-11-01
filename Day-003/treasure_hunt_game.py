# Treasure Hunt Game: Choose paths and make decisions to find the treasure

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____ 
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/_____ / 
*******************************************************************************
''')

# Start the adventure
print('''
You\'re an adventurer on the trail of the Lost Treasure of El chapo, the famous pirate. 
With a map in hand and courage in your heart, you step into the unknown. 
Let\'s see if you can find the treasure… or if you end up in trouble!
''')

# Choose the first path
path1 = input('''
You land on the island and see two paths: one path is through a dark, creepy forest, and the other heads toward a bright, sunny beach. 
Type 'forest' to take the Forest Path or 'beach' to head for the Beach Path.
''').lower()

if path1 == "forest":
    print("\nYou bravely step into the dark forest.")
    
    # Choose how to cross the river
    path2 = input('''
After making it through the forest, you find a sparkling river. 
There\'s an old bridge over the river, and nearby, a small boat tied to a tree. 
Type 'bridge' to cross the Bridge or 'boat' to take the Boat.
''').lower()
    
    if path2 == "bridge":
        print("\nYou tiptoe across and make it to the other side.")
        
        # Choose which chest to open
        chest = input('''
Finally, you reach a cave with three chests inside: one shiny gold, one small wooden, and one rusty iron. 
Which one holds the treasure? 
Type 'gold' to open the Gold Chest, 'wooden' to open the Wooden Chest, or 'iron' to open the Iron Chest.
''').lower()
        
        if chest == "gold":
            print("You open it, and—pow! A trap sprays dust in your face. (Game Over)")
        elif chest == "wooden":
            print("Inside, you find the Lost Treasure of El chapo! You win!")
        elif chest == "iron":
            print("A snake jumps out! You run out of the cave in a hurry. (Game Over)")
        else:
            print("Invalid input")
    else:
        print("The boat springs a leak! It sinks, and you have to swim back. (Game Over)")

else:
    print('''
    You head for the beach, but a huge wave crashes down and sweeps you back to your ship.
    (Game Over)
    ''')
