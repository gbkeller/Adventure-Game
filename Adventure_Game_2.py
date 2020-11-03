import time
import random


def set_monster():
    monsters = ["orc", "thief", "gremlin", "wizard"]
    return random.choice(monsters)


def set_weapon():
    weapons = ["sword", "lute"]
    return random.choice(weapons)


def print_pause(text):
    print(text, flush=True)
    time.sleep(1)


def intro(monster):
    print_pause("You find yourself standing in an open field,\n"
                "filled with grass and yellow flowers\n")
    print_pause(f"Rumor has it that a wicked {monster} is somewhere\n"
                "around here, and has been terrifying the nearby village\n")
    print_pause("To your right, is the opening to a cave.\n")
    print_pause("To your left, is a small house.\n")


def house(items, weapon, monster):
    print_pause("You knock on the door of the house\n")
    print_pause(f"Immediately, the door flies open, \n"
                f"and there stands the {monster}\n")
    if "sword" in items:
        print_pause(f"You attack with your sword, and the {monster} flees!\n")
        play_again()
    elif "lute" in items:
        print_pause("You play a lullaby of breathtaking beauty")
        print_pause(f"The {monster} falls into a deep slumber.")
        print_pause("You sneak carefully back to the field\n")
        get_choice(items, weapon, monster)
    else:
        print_pause("You realize you have only your rusty dagger.\n")
        print_pause(f"The {monster} attacks!\n")
        if random.randint(-50, 50) < 0:
            print_pause("You made a valient struggle, but it wasn't enough\n")
            play_again()
        else:
            print_pause(f"You manage to fend off the {monster}\n"
                        "and stagger back into the field\n")
            get_choice(items, weapon, monster)


def cave(items, weapon, monster):
    if len(items) == 2:
        print_pause("You have already found all the weapons here\n")
        get_choice(items, weapon, monster)
    elif len(items) == 0:
        weapon = set_weapon()
    else:
        if "sword" in items:
            weapon = "lute"
        if "lute" in items:
            weapon = "sword"
    print_pause("You peer into a cave")
    print_pause(f"In the dim light, you see a {weapon}")
    print_pause(f"You pick up the {weapon} and head back to the field.\n")
    items.append(weapon)
    get_choice(items, weapon, monster)


def play_again():
    again = input("Do you wish to play again?\n"
                  "Please say 'yes' or 'no.'\n").lower()
    if "no" in again:
        print_pause("OK, I hope you had fun!")
    elif "yes" in again:
        print_pause("Great!")
        play_game()
    else:
        print_pause("Please enter a valid choice")
        play_again()


def get_choice(items, weapon, monster):
    choice = input("Enter 1 to knock on the door of the house.\n"
                   "Enter 2 to peer into the cave.\n"
                   "What would you like to do?\n"
                   "(Please enter 1 or 2)")
    if choice == "1":
        house(items, weapon, monster)
    elif choice == "2":
        cave(items, weapon, monster)
    else:
        print("Please enter a valid choice\n")
        get_choice(items, weapon, monster)


def play_game():
    items = []
    weapon = ""
    monster = set_monster()
    intro(monster)
    get_choice(items, weapon, monster)


play_game()
