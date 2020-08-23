# import re
import sys

lever = bool()
redstone_dust = bool()
# redstone_signal = bool()

def lever_switch():
    print("Will the lever be on or off?")
    print("Type yes or no")
    conv1 = input("")

    if conv1 == "yes":
        lever == True
        while True:
            intro()
        else:
            print("Redstone execution stopped")
    elif conv1 == "no":
        print("Define some other redstone power source as it wont work without lever")


redstone_repeater = (redstone_dust**2)

# redstone_torch = bool()

commands = '''
/summon lightning_bolt ~ ~ ~ : summon a lightning bolt at the current position
/time set day : set the time to day
/time set noon : set the time to noon
/time set night : set the time to night 
/weather storm : set the weather to rain and storm
/weather clear : set the weather to clear
/give @s diamond 64 : give 1 stack of diamonds to player
/give @s iron_ingot 64 : give 1 stack of iron to player
/whoami : show player information
/select : select a block (syntax : /select <blockname>)
/place : place the selected block (syntax : /place <blockname>)
/credits : Display the author and co-authors of this program
/help : Display this message
'''
def console():
    print("Hello! I am a command block! :D")
    print("Minecraft Shell v1.16.2 , Java version(JDK):8")
    print("Type the commands here:")
    print("Type /help to get a list of commands")
    com = input(">")
    if com == "/summon lightning_bolt ~ ~ ~":
        print("[@: Summoned new lightning_bolt]")
        print("Player was struck by lightning and took 5 fire damage")
        while True: 
            intro()
    elif com == "/time set day":
        print("Set the time to 1000ticks or 7am in the world")
        while True:
            intro()
    elif com == "/time set noon":
        print("Set the time to 5000ticks or 12pm in the world")
        while True:
            intro()
    elif com == "/time set night":
        print("Set the time to 13000ticks or 8pm in the world")
        while True:
            intro()
    elif com == "/weather clear":
        print("Set the weather to clear")
        while True:
            intro()
    elif com == "/weather storm":
        print("Set the weather to storm")
        while True:
            intro()
    elif com == "/give @s diamond 64":
        print("Gave diamond(x64) to " ,name)
        while True:
            intro()
    elif com == "/give @s iron_ingot 64":
        print("Gave iron ingot(x64) to" ,name)
        while True:
            intro()
    elif com == "/whoami":
        print(name)
        while True:
            intro()
    elif com == "/exit":
        print(name, "left the game")
        sys.exit()
    elif com == "/help":
        print(commands)
        while True:
            intro()
    elif com == "/credits":
        print("Original Creator: shasankp000 (www.github.com/shasankp000/)")
        print("dm @steve._2004 on instagram for partnership and co-authoring")
        while True:
            intro()


def command_block():
    print("Set the activation status of command block:")
    print ("1. Does it require redstone?")
    print ("Answer in yes or no")
    conv2 = input("")
    if conv2 == "yes":
        print("Make sure the lever is on and the redstone signal is active")
        if lever == True:
            print("Redstone signal detected, starting..... ")  # Doesnt work , needs to be fixed :(
            console()
        else:
            print("no redstone power source detected")  # always skips to this line? Why?
    elif conv2 == "no":
        print("Selecting default power source, placed button at ~ ~ ~.")
        console()
def intro():
    print("What do you want to do?")    
    print("1. Mess around with command blocks")
    print("2. Place blocks and do something creative")
    print("3. Leave the game")
    print("Answer in 1, 2 or 3")
    print("NOTE: Everytime you do something, after that task is completed the game will again route you to this message in order to ask you what you want to do next.")

    conv4 = input("")

    if conv4 == "1":
        command_block()
    elif conv4 == "2":
        place_block()
    elif conv4 == "3":
        print("Opening command block")
        print("In command block console type /exit to leave the game")
        print("Be sure to visit again! :D ")
        command_block()


def place_block():
    print("Available blocks in inventory : redstone dust, redstone repeater , lever , command block")
    print("Select any block you want to from your inventory")
    print("/select <blockname> to select a block")
    print("/place <blockname> to place the block")
    conv3 = input("")
    if conv3 == "/select redstone dust":
        print("Selected redstone dust")
        while True:
            intro()
    elif conv3 == "/select redstone repeater":
        print("Selected redstone repeater")
        while True:
            intro()
    elif conv3 == "/select lever":
        print("Selected lever")
        while True:
            intro()
    elif conv3 == "/select command block":
        print("Selected command block")
        while True:
            intro()
    elif conv3 == "/place redstone dust":
        print("Placed redstone dust")
        while True:
            intro()
    elif conv3 == "/place redstone repeater":
        print("Placed redstone repeater")
        while True:
            intro()
    elif conv3 == "/place lever":
        print("Placed Lever")
        lever_switch()
        while True:
            intro()
    elif conv3 == "/place command block":
        print("Placed command block")
        print("Do you want to interact with the command block? (y/n)")
        conv5 = input("")
        if conv5 == "y":
            command_block()
        elif conv5 == "n":
            print("Destroyed command block")
            while True:
                intro()

print("Fun with Mctext V1.1 (Alpha)")
name = input("What is your name?(Mc username):")
print(name, "joined the game")
print("Welcome!" ,name) 
print(name, "was granted permission by server to place blocks and interact with items")
print("Default gamemmode : Creative")
intro()