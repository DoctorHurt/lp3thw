from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if choice.isdigit():
        how_much = int(choice)
    else:
        print("Man, learn to type a number.")
        gold_room()

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard! A curse of death overcomes you!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    door_opened = False

    while True:
        choice = input("> ")

        if "take honey" in choice:
            dead("the bear looks at you then slaps your face off.")
        elif "taunt" in choice and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif "taunt" in choice and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif "open door" in choice and bear_moved:
            gold_room()
        elif bear_moved and door_opened == False:
            print("Better get that door opened first!")
        else:
            print("I got no idea what that means dude!")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job, you succeeded at FAIL!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
