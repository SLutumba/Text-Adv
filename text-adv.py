from random import randrange


def main():

    print("Welcome, adventurer! \n"
          "You find yourself standing on the edge of a mysterious land, "
          "faced with three different paths, each with its own perils and promises.\n")

    while True:
        try:
            scene_choice = int(input("Choose Your Starting Point (enter the number to choose):\n"
              "1. The Haunted Forest\n"
              "2. The Ancient Cave\n"
              "3. The Abandoned Castle\n"
              "Or 0 to exit game.\n"))
            if scene_choice == 0:
                print("Game has ended.")
                break
            elif scene_choice == 1:
                haunted_forest()
            elif scene_choice == 2:
                ancient_cave()
            elif scene_choice == 3:
                abandoned_castle()
            else:
                print("Invalid input, please enter 1, 2, or 3 when choosing a scene.\n")

        except ValueError:
            print("Invalid input, must be a number.\n")

def haunted_forest():
    exception_flag = False

    print("The Haunted Forest.\n"
          "The trees tower over you, their gnarled branches stretching out like claws. "
          "An eerie mist weaves between the trunks, and shadows dance in the moonlight. "
          "You hear a low growl echoing in the distance...\n"
          "Options:")

    while not exception_flag:
        try:
            first_choice = int(input("1. Run\n"
                                     "OR\n"
                                     "2. Fight.\n"))
            if first_choice == 1:
                print("You turn and sprint back the way you came, hoping to outrun whatever lurks within.\n"
                      "You come to a crossroads where two paths emerge. Do you...")
                while not exception_flag:
                    try:
                        second_choice = int(input("1. Hide behind a tree\n"
                                                  "OR\n"
                                                  "2. Climb a tree:\n"))
                        exception_flag = True
                        while second_choice != 1 and second_choice != 2:
                            print("Invalid input. Please enter 1 or 2.")
                            second_choice = int(input("1. Hide behind a tree\n"
                                                      "OR\n"
                                                      "2. Climb a tree:\n"))
                        if second_choice == 1:
                            print("You duck behind a massive oak tree to catch your breath, hoping the creature didn’t follow.")
                            hide_outcome = [
                                "Bad Choice: The creature, a massive shadow wolf, finds your hiding spot. Its "
                                "jaws snap shut around you in an instant, and your adventure ends there in the "
                                "cold, unforgiving forest.",
                                "Good Choice: The creature loses interest, but you’re left shaken and "
                                "exhausted. As you leave, you find a strange amulet that tingles to the touch, "
                                "but you can’t shake the feeling that it’s cursed."]
                            print(f"{hide_outcome[randrange(0, 2)]}\n"
                                  f"Game Over.\n")

                        elif second_choice == 2:
                            print("You decide to climb up to get a better view and assess the threat.")
                            climb_outcome = [
                                "Bad Choice: The tree’s branches are covered in sticky, web-like strands. As "
                                "you climb, a massive, venomous spider descends, sinking its fangs into your "
                                "arm. The poison works quickly, and you fall unconscious, never to awaken.",
                                "Good Choice: You escape the creature below by leaping from branch to "
                                "branch until you reach the forest’s edge. You survive, but shadows haunt you, "
                                "following your every step."]
                            print(f"{climb_outcome[randrange(0, 2)]}\n"
                                  f"Game Over.\n")
                    except ValueError:
                        print("Invalid input, must be a integer.\n")
                        exception_flag = False
            elif first_choice == 2:
                print("You stand your ground, grabbing a stick as a weapon.\n"
                      "You notice something glowing in the underbrush nearby. Do you...")
                while not exception_flag:
                    try:
                        second_choice = int(input("1. Investigate the glow\n"
                                                  "OR\n"
                                                  "2. Shout a warning:\n"))
                        exception_flag = True
                        while second_choice != 1 and second_choice != 2:
                            print("Invalid input. Please enter 1 or 2.")
                            second_choice = int(input("1. Hide behind a tree\n"
                                                      "OR\n"
                                                      "2. Climb a tree:\n"))
                        if second_choice == 1:
                            print(
                                "Curious, you bend down and pick up the glowing object, finding a crystal dagger.")
                            investigate = [
                                "Bad Choice: As you prepare to fight, the creature lunges, its claws tearing through "
                                "you with ease. The dagger shatters in your hand, and darkness overtakes you as the "
                                "forest reclaims your soul.",
                                "Good Choice: You fend off the creature with the dagger, surprising it. The creature "
                                "retreats, but the blade leaves a dark mark on your skin, and strange dreams plague "
                                "you from that night onward."]

                            print(f"{investigate[randrange(0, 2)]}\n"
                                  f"Game Over.\n")

                        elif second_choice == 2:
                            print("You raise your voice, hoping to scare the creature off with your bravery.")
                            shout = [
                                "Bad Choice: The creature lunges, undeterred by your cries. In a moment of fierce "
                                "power, it overpowers you, and the last thing you hear is its haunting growl echoing "
                                "through the trees.",
                                "Good Choice: The creature, impressed by your courage, allows you to go free but "
                                "warns you never to return. You leave the forest alive, though forever marked by the "
                                "encounter."]
                            print(f"{shout[randrange(0, 2)]}\n"
                                  f"Game Over.\n")
                    except ValueError:
                        print("Invalid input, must be a integer.\n")
                        exception_flag = False
            else:
                print("Invalid input, enter 1 or 2.")

        except ValueError:
            print("Invalid input, must be a integer.\n")
            exception_flag = False

def ancient_cave():
    pass
def abandoned_castle():
    pass
if __name__ == "__main__":
    main()