from random import randrange
game_paths = {
    "Haunted Forest": {
        "description": "You enter the Haunted Forest. Shadows loom, and the air is thick with an eerie mist. A distant growl echoes, sending chills down your spine.",
        "choices": {
            "Run": {
                "description": "You run through the forest, stumbling upon a mystical Holy Grail.",
                "next_choice": {
                    "Fight with Weapon": {
                        "dialogue": "Gripping the Holy Grail, you fend off the creature and survive.",
                        "outcome": " You win"
                    },
                    "Not Fight": {
                        "dialogue": "Hesitating, you’re left defenseless, and the creature strikes.",
                        "outcome": "You lose"
                    }
                }
            },
            "Stand Ground": {
                "description": "You look for shelter, but encounter a snake.",
                "next_choice": {
                    "Use Herb": {
                        "dialogue": "You chew herbs, surviving the snakebite.",
                        "outcome": "You win"
                    },
                    "No Herb": {
                        "dialogue": "Without herbs, the poison takes hold.",
                        "outcome": "You lose"
                    }
                }
            }
        }
    },
    "Ancient Cave": {
        "description": "The cave walls glisten as you walk deeper.",
        "choices": {
            "Explore Deeper": {
                "description": "You find a pulsing artifact.",
                "next_choice": {
                    "Take Artifact": {
                        "dialogue": "You reach for the artifact as a shadowy figure appears.",
                        "next_choice": {
                            "Negotiate with Figure": {
                                "dialogue": "The figure vanishes, leaving the artifact in your care.",
                                "outcome": "win"
                            },
                            "Attempt to Flee": {
                                "dialogue": "The artifact’s curse claims you.",
                                "outcome": "lose"
                            }
                        }
                    },
                    "Leave Artifact": {
                        "dialogue": "You back away, but the ground collapses beneath you.",
                        "outcome": "lose"
                    }
                }
            },
            "Stay Near Entrance": {
                "description": "You encounter mysterious creatures.",
                "next_choice": {
                    "Attempt to Tame Creature": {
                        "dialogue": "The creature becomes your loyal companion.",
                        "outcome": "win"
                    },
                    "Retreat Carefully": {
                        "dialogue": "You escape safely, feeling an unsettling presence.",
                        "outcome": "win"
                    }
                }
            }
        }
    },
    "Abandoned Castle": {
        "description": "The castle is silent. You hear a faint whisper from the throne room.",
        "choices": {
            "Investigate Throne Room": {
                "description": "A spectral guardian looms, clutching a sword.",
                "next_choice": {
                    "Fight with Enchanted Weapon": {
                        "dialogue": "With a final strike, the guardian fades.",
                        "outcome": "win"
                    },
                    "Attempt to Befriend Guardian": {
                        "dialogue": "The guardian grants you safe passage and a small treasure.",
                        "outcome": "win"
                    }
                }
            },
            "Search Dungeon": {
                "description": "You find treasures, but a dark presence lurks.",
                "next_choice": {
                    "Ignore Treasure and Seek Map": {
                        "dialogue": "Your courage earns you safe passage and a map.",
                        "outcome": "win"
                    },
                    "Take Treasure": {
                        "dialogue": "The curse claims you as part of its hoard.",
                        "outcome": "lose"
                    }
                }
            }
        }
    }
}

def main():
    print("Welcome, adventurer! \n"
          "You find yourself standing on the edge of a mysterious land, "
          "faced with three different paths, each with its own perils and promises.")
    menu()
def menu():
    while True:
            scene_choice = validate_input("Choose Your Starting Point (enter the number to choose):\n1. The Haunted "
                                          "Forest\n2. The Ancient Cave\n3. The Abandoned Castle\nOr 0 to exit "
                                          "game.\n", (1, 2, 3, 0))
            if scene_choice == 0:
                print("Game has ended.")
                break
            elif scene_choice == 1:
                haunted_forest()
            elif scene_choice == 2:
                ancient_cave()
            elif scene_choice == 3:
                abandoned_castle()

def haunted_forest():
    print(f"Haunted Forest\n{game_paths["Haunted Forest"]["description"]} Do You:")
    for index, choice in enumerate(game_paths["Haunted Forest"]["choices"].keys(), start=1):
        print(f"{index}. {choice}")
    choice_1 = validate_input("", (1,2))
    if choice_1 == 1:
        print(f"{game_paths["Haunted Forest"]["choices"]["Run"]["description"]} Do You:")
        for index, choice in enumerate(game_paths["Haunted Forest"]["choices"]["Run"]["next_choice"].keys(), start=1):
            print(f"{index}. {choice}")
        choice_2 = validate_input("", (1,2))
        if choice_2 == 1:
            print(f"{game_paths["Haunted Forest"]["choices"]["Run"]["next_choice"]["Fight with Weapon"]["dialogue"]} {game_paths["Haunted Forest"]["choices"]["Run"]["next_choice"]["Fight with Weapon"]["outcome"]} !")


def validate_input(prompt_text, valid_options = ()) -> int:
    valid = False
    while not valid:
        user_input = input(prompt_text)
        try:
            user_input = int(user_input)
            if user_input not in valid_options:
                print(f"Invalid input, enter one of these: {valid_options}.")
            else:
                valid = True
                return user_input
        except ValueError:
            print("Invalid input, must be a integer.\n")



def ancient_cave():
    pass


def abandoned_castle():
    pass


if __name__ == "__main__":
    main()
