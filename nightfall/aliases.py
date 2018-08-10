import itertools
from scroll_print import *


def move_alias_check(current_room_name, user_input):
    """Movement alias check.

    Sources used: # https://stackoverflow.com/questions/14264163/search-for-any
    -word-or-combination-of-words-from-one-string-in-a-list-python
    # https://docs.python.org/2/library/itertools.html

    Args:
        current_room_name (str): Name of the room the player is currently in.
        user_input (str): raw user input.

    Returns:
        str: If movement command is valid it will return the name of the room
            that the player wants to travel to. Otherwise it will return the
            user_input just as it was received.

    """
    # Tracks possible destinations so that correct room name can be returned if
    # input is valid.
    possible_destinations = {}

    # Alias check for staircases.
    stairs_alias = {}
    stairs_alias["staircase"] = ["stairs", "stairwell"]
    stairs_alias["blocked"] = ["covered"]

    for key in stairs_alias:
        for word in stairs_alias[key]:
            user_input = user_input.replace(word, key)

    # Find out what room the player is in currently so that the correct word
    # list can be generated for the rooms connected to that room.

    # Room 1
    if current_room_name == 'fortress entrance':
        # Contains both the words in the descriptions of doors and contains
        # variations of the names of rooms.
        dest_list = ([
                      ["large", "oak", "double", "door", "doors"],
                      ["entrance hall", "entrance", "door", "doors"],
                      ])

        # Match the room name to the description words matching that room.
        possible_destinations['entrance hall'] = dest_list

    # Room 2
    elif current_room_name == 'entrance hall':
        # Two destination lists are created because two rooms are connected to
        # this room.
        dest_list_1 = ([
              ["large", "oak", "double", "door", "doors"],
              ["fortress entrance", "entrance", "door", "doors"],
              ])

        possible_destinations['fortress entrance'] = dest_list_1

        dest_list_2 = ([
              ["painted", "door", "doors"],
              ["mess hall", "door", "doors"],
              ])

        possible_destinations['mess hall'] = dest_list_2

    # Room 3
    elif current_room_name == 'mess hall':
        dest_list_1 = ([
            ["painted", "door", "doors"],
            ["entrance hall", "door", "doors"],
            ])

        possible_destinations['entrance hall'] = dest_list_1

        dest_list_2 = ([
            ["large", "oak", "door", "doors"],
            ["store room", "door", "doors"],
            ])

        possible_destinations['store room'] = dest_list_2

        dest_list_3 = ([
            ["engraved", "old", "steel", "door"],
            ["kitchen", "door", "doors"],
            ])

        possible_destinations['kitchen'] = dest_list_3

    # Room 4
    elif current_room_name == 'store room':

        dest_list_1 = ([
            ["large", "oak", "door", "doors"],
            ["mess hall", "door", "doors"],
            ])

        possible_destinations['mess hall'] = dest_list_1

        dest_list_2 = ([
            ["vine", "blocked", "staircase"],
            ["washroom", "staircase"],
            ])

        possible_destinations['washroom'] = dest_list_2

    # Room 5
    elif current_room_name == 'kitchen':
        dest_list_1 = ([
            ["steel", "door", "doors"],
            ["mess hall", "door", "doors"],
            ])

        possible_destinations['mess hall'] = dest_list_1

    # Room 6
    elif current_room_name == 'washroom':
        dest_list_1 = ([
            ["staircase"],
            ["store room", "staircase"],
            ])

        possible_destinations['store room'] = dest_list_1

        dest_list_2 = ([
            ["ornate", "door", "doors"],
            ["sleeping chambers", "door", "doors"],
            ])

        possible_destinations['sleeping chambers'] = dest_list_2

        dest_list_3 = ([
            ["maple", "door", "doors"],
            ["smoking room", "door", "doors"],
            ])

        possible_destinations['smoking room'] = dest_list_3

    # Room 7
    elif current_room_name == 'smoking room':
        dest_list_1 = ([
            ["maple", "door", "doors"],
            ["washroom", "door", "doors"],
            ])

        possible_destinations['washroom'] = dest_list_1

        dest_list_2 = ([
            ["mahogany", "door", "doors"],
            ["supplies closet", "door", "doors"],
            ])

        possible_destinations['supplies closet'] = dest_list_2

    # Room 8
    elif current_room_name == 'sleeping chambers':
        dest_list_1 = ([
            ["ornate", "door", "doors"],
            ["washroom", "door", "doors"],
            ])

        possible_destinations['washroom'] = dest_list_1

        dest_list_2 = ([
            ["walnut", "door", "doors"],
            ["supplies closet", "door", "doors"],
            ])

        possible_destinations['supplies closet'] = dest_list_2

    # Room 9
    elif current_room_name == 'supplies closet':
        dest_list_1 = ([
            ["mahogany", "door", "doors"],
            ["smoking room", "door", "doors"],
            ])

        possible_destinations['smoking room'] = dest_list_1

        dest_list_2 = ([
            ["walnut", "door", "doors"],
            ["sleeping chambers", "door", "doors"],
            ])

        possible_destinations['sleeping chambers'] = dest_list_2

        dest_list_3 = ([
            ["birch", "door", "doors"],
            ["sauna room", "door", "doors"],
            ])

        possible_destinations['sauna room'] = dest_list_3

    # Room 10
    elif current_room_name == 'sauna room':
        dest_list_1 = ([
            ["birch", "door", "doors"],
            ["supplies closet", "door", "doors"],
            ])

        possible_destinations['supplies closet'] = dest_list_1

        dest_list_2 = ([
            ["marble", "staircase"],
            ["tower hall", "stairs", "staircase"],
            ])

        possible_destinations['tower hall'] = dest_list_2

    # Room 11
    elif current_room_name == 'tower hall':
        dest_list_1 = ([
            ["marble", "staircase"],
            ["sauna room", "stairs", "staircase"],
            ])

        possible_destinations['sauna room'] = dest_list_1

        dest_list_2 = ([
            ["large", "walnut", "double", "door", "doors"],
            ["archives", "door", "doors"],
            ])

        possible_destinations['archives'] = dest_list_2

    # Room 12
    elif current_room_name == 'archives':
        dest_list_1 = ([
            ["large", "walnut", "door", "doors"],
            ["tower hall", "door", "doors"],
            ])

        possible_destinations['tower hall'] = dest_list_1

        dest_list_2 = ([
            ["ash", "door", "doors"],
            ["reading room", "door", "doors"],
            ])

        possible_destinations['reading room'] = dest_list_2

        dest_list_3 = ([
            ["pine", "door", "doors"],
            ["room of last rites", "door", "doors"],
            ])

        possible_destinations['room of last rites'] = dest_list_3

    # Room 13
    elif current_room_name == 'reading room':
        dest_list_1 = ([
            ["ash", "door", "doors"],
            ["archives", "door", "doors"],
            ])

        possible_destinations['archives'] = dest_list_1

    # Room 14
    elif current_room_name == 'room of last rites':
        dest_list_1 = ([
            ["tungsten", "door", "doors"],
            ["final lair", "door", "doors"],
            ])

        possible_destinations['final lair'] = dest_list_1

        dest_list_2 = ([
            ["pine", "door", "doors"],
            ["archives", "door", "doors"],
            ])

        possible_destinations['archives'] = dest_list_2

    # Room 15
    elif current_room_name == 'final lair':
        dest_list_1 = ([
            ["tungsten", "door", "doors"],
            ["room of last rites", "door", "doors"],
            ])

        possible_destinations['room of last rites'] = dest_list_1

    # The list of possible move words.
    move_lists = ([
                  ["move", "to"],
                  ["go", "to"],
                  ["travel", "to"],
                  ["leave", "to"],
                  ])

    door_list = ([
                ["door", "doors"],
                ])

    # generate invalid combinations. This creates combinations using the move
    # list and door/doors. Will generate combinations like "move door.". This
    # is not valid due to their being multiple doors in a room.
    invalid_list = []
    total_invalid_list = []

    # Combine the move_lists with door_list.
    for list_obj_1 in move_lists:
        for list_obj_2 in door_list:
            invalid_list.append(list_obj_1 + list_obj_2)

    # Generate the actual invalid combinations.
    for word_list in invalid_list:
        _gen_invalid = (itertools.combinations(word_list, i + 1)
                        for i in range(len(word_list)))

        all_invalid = itertools.chain(*_gen_invalid)

        list_all_invalid = list(all_invalid)

        total_invalid_list += list_all_invalid

    # Create a set of sentences that include spaces to check against. Uses the
    # combinations generated in the above for loop.
    invalid_combination = set(' '.join(i) for i in total_invalid_list)

    for key in possible_destinations:
        # List to hold the combinations of both movement commands and
        # destination variations.
        move_dest_list = []

        # Holds all valid combinations of input
        combination_lists = []

        # The specific destination list for a give room.
        dest_lists = possible_destinations[key]

        # Combine the movement list with each of the possible destination
        # lists.
        for list_obj_1 in move_lists:
            for list_obj_2 in dest_lists:
                move_dest_list.append(list_obj_1 + list_obj_2)

        # Generate all possible combinations of the words that make up the
        # move_dest_list.
        for i, word_list in enumerate(move_dest_list):
            _gen = (itertools.combinations(word_list, i + 1)
                    for i in range(len(word_list)))

            all_combinations_gen = itertools.chain(*_gen)

            combinations = list(all_combinations_gen)

            # Door descriptions require that the word door/doors or staircase
            # be in the command to travel to that door.
            if i % 2 == 0:
                # Must have word + door or word + doors or word + staircase.
                _gen_valid = (word_tuple for word_tuple in combinations
                              if (("door" in word_tuple and
                                   "doors" not in word_tuple) or
                                  ("doors" in word_tuple and
                                   "door" not in word_tuple) or
                                  ("staircase" in word_tuple)))

            # Room name descriptions must have at least part of the room name
            # in the command. They do not need door to be in the command
            # however.
            else:
                # Must have room name or form of room name
                _gen_valid = (word_tuple for word_tuple in combinations
                              if key in word_tuple or "entrance" in word_tuple)

            # Join all possible combinations into a set of sentences
            # representing the user commands.
            valid_combination = set(' '.join(i) for i in _gen_valid)

            # Add the valid combination sentences to the final list that we
            # are checking against
            combination_lists.append(valid_combination)

        # Check for valid match. Also checks against sentence.
        for word_list in combination_lists:
            if (user_input in word_list and
               user_input not in invalid_combination):
                return key

    return user_input


def verb_alias_check(command):
    """Check for aliases of 10 core verbs.

    Args:
        command (str): Corresponds to new_command2 in text_parser.py
            file. Is a string that is the user input.

    Returns:
        str: If an alias matches it returns one of the 10 core verbs the
            game uses. If an alias does not match it returns the unmodified
            command string as taken from text_parser.py

    """
    alias_dictionary = {}

    # Filled out dictionary for each of the 10 core verbs. The order of the
    # alias array matters. Multi-word aliases that have a single word
    # counterpart, such as sniff at and sniff, must appear before their single
    # word counterpart in the list. This is to prevent the function from
    # replacing the single word without replacing the additional word "at".
    alias_dictionary["take"] = ["grab", "get", "obtain", "steal", "pick up"]
    alias_dictionary["use"] = ["utilize"]
    alias_dictionary["drop"] = ["leave behind", "leave", "get rid of", "lose"]
    alias_dictionary["look at"] = ["inspect", "examine", "observe"]
    alias_dictionary["eat"] = ["consume", "devour", "ingest"]
    alias_dictionary["drink"] = ["swallow", "imbibe", "sip"]
    alias_dictionary["smell"] = ["sniff at", "sniff"]
    alias_dictionary["listen to"] = ["hear"]
    alias_dictionary["climb"] = ["climb up", "ascend up", "ascend", "go up",
                                 "scale up", "scale", "climb onto"]
    alias_dictionary["duck"] = ["crouch down", "crouch", "get down",
                                "squat down", "squat", "hunch down", "hunch",
                                "stoop down", "stoop", "duck down"]
    alias_dictionary["rotate"] = ["turn around", "turn", "pivot around",
                                  "pivot", "twist around", "twist",
                                  "revolve around", "revolve", "spin around",
                                  "spin",
                                  ]

    for key in alias_dictionary:
        for word in alias_dictionary[key]:
            command = command.replace(word, key)

    return command


def item_alias_check(command):
    """Check for item aliases.

    Args:
        command (str): Corresponds to new_command2 in text_parser.py
            file. Is a string that is the user input.

    Returns:
        str: If an alias matches it returns the item name that is used verbs
            by the feature and item handler. If an alias does not match it
            returns the unmodified command string as taken from text_parser.py

    """
    alias_dictionary = {}

    # Filled out dictionary for items. The order of the
    # alias array matters. Multi-word aliases that have a single word
    # counterpart, such as sniff at and sniff, must appear before their single
    # word counterpart in the list. This is to prevent the function from
    # replacing the single word without replacing the additional word "at".
    alias_dictionary['Quackers'] = ['rubber duck', 'quackers']
    alias_dictionary['box'] = ['lock box', 'emerald box']
    alias_dictionary['scrap'] = ['painting scrap']

    # If the user enters "key" as part of their command, but does not specify
    # the key type, this code will ask them to enter in the type.
    if ('key' in command and 'emerald' not in command and
        'golden' not in command and 'iron' not in command and
       'skull' not in command):
        user_input = input("Please enter the type of key (for example type "
                           "golden or emerald): ")
        print("")

        user_input.lower().strip()

        if "key" not in user_input:
            new_input = user_input + ' ' + 'key'

        command = command.replace('key', new_input)

    # Replace alias with item name used by the item_handler.
    for key in alias_dictionary:
        for word in alias_dictionary[key]:
            command = command.replace(word, key)

    return command
