from aliases import *
from scroll_print import *


def get_input():
    """Get raw user input.

    Returns:
        str: Raw user input.

    """
    user_input = input("Type some text: ")
    print("")

    return user_input


def parse_input(input, current_room):
    """Divide input into recognizable components.

    Args:
        input (str): Raw user input.

    Returns:
        dictionary(str, str): Dictionary of command mapped to the item or
            feature that the command is acting on.

    """
    # citation: https://www.nltk.org/ helped with the idea of tokens
    # categories for command words
    assigned_tokens = {
        'verb': None,
        'item': None,
        'feature': None,
        'direction': None,
        'standard_action': None,
        'error': None
    }

    # arrays with parts of speech
    direction_array = [
                       # General Directions
                       'north', 'east', 'south', 'west',

                       # Floor 1
                       'fortress entrance', 'entrance hall', 'mess hall',
                       'store room', 'kitchen',

                       # Floor 2
                       'washroom', 'smoking room', 'sleeping chambers',
                       'supplies closet', 'sauna room',

                       # Floor 3
                       'tower hall', 'archives', 'reading room',
                       'room of last rites', 'final lair'
                       ]

    standard_action_array = ['help', 'look', 'gamemenu', 'game menu',
                             'inventory', 'stats', 'get stats', 'my stats',
                             'player stats', 'savegame', 'loadgame',
                             'save game', 'load game']

    verb_array = ['take', 'use', 'drop', 'look at', 'eat', 'drink', 'smell',
                  'listen to', 'climb', 'duck', 'rotate', 'equip']

    item_array = [
                  # Room 1
                  'sword',

                  # Room 2
                  'golden key',

                  # Room 3
                  'bread',

                  # Room 4
                  'letter', 'jar',

                  # Room 5
                  'oven mitt', 'acidic ooze',

                  # Room 6
                  'Quackers',

                  # Room 7
                  'emerald key',

                  # Room 8
                  'healing potion', 'book',

                  # Room 9
                  'rapier',

                  # Room 10

                  # Room 11
                  'charcoal',

                  # Room 12
                  'scrap', 'mythril tongs',

                  # Room 13
                  'iron key',

                  # Room 14
                  'skull key'

                  # Room 15
                    ]

    feature_array = [
                     # Room 1
                     'body', 'door', 'cloak', 'bag',

                     # Room 2
                     'writing', 'rope', 'rubble',

                     # Room 3
                     'engraving', 'armor', 'plates',

                     # Room 4
                     'box', 'broom', 'shelves', 'carcass', 'vines',

                     # Room 5
                     'fish', 'sink',

                     # Room 6
                     'tub', 'fountain',

                     # Room 7
                     'humidor', 'ashtray', 'smoke', 'chair',

                     # Room 8
                     'bed', 'window',

                     # Room 9
                     'towels', 'shampoo',

                     # Room 10
                     'machinery', 'mirror', 'vent',

                     # Room 11
                     'ceiling', 'painting', 'table', 'ruby', 'charcoal',
                     'dagger',

                     # Room 12
                     'fireplace', 'chandelier', 'cobwebs',

                     # Room 13
                     'tome', 'couch', 'raven',

                     # Room 14
                     'bones', 'handprint', 'cage', 'fairy',

                     # Room 15
                     'evelyn',
                     ]

    # this takes user input and puts it all into lowercase
    command = input.lower().strip()
    command = item_preposition_handler(command)
    # ##### PRINT STATEMENT FOR TESTING #####
    # print("You typed: ", command)

    # ignore certain words when parsing string
    ignored_words = ['a', 'an', 'the']

    # clean the string to ignore certain words
    def remove_ignored_words(command):
        new_string = []
        for word in command.split():
            if word not in ignored_words:
                new_string.append(word)
        new_command = ' '.join(new_string)

        # ##### PRINT STATEMENT FOR TESTING #####
        # print("Here is the cleaned version: ", new_command)
        return new_command

    # run function to clean input string
    new_command2 = remove_ignored_words(command)

    # ##### PRINT STATEMENT FOR TESTING #####
    # print("new command: {}".format(new_command2))

    # variables to check if we already have a complete command and if we have
    # an invalid scenario
    done = False
    invalid = False

    # check if the command is for a standard game action
    for action in standard_action_array:
        if new_command2 == action:
            # print("Doing the action of:", action)
            assigned_tokens['standard_action'] = action
            done = True

    # check if the command indicates a direction to move in
    if done is False:
        room_name = current_room.get_name()

        new_command2 = move_alias_check(room_name, new_command2)

        for dest in direction_array:
            if new_command2 == dest or new_command2 == "go " + dest or\
               new_command2 == "go to " + dest or new_command2 == "move "\
               + dest or new_command2 == "move to " + dest or new_command2\
               == "walk " + dest or new_command2 == "walk to " + dest or\
               new_command2 == "run " + dest or new_command2 == "run to" +\
               dest or new_command2 == "travel " + dest or\
               new_command2 == "travel to " + dest:
                # ##### PRINT STATEMENT FOR TESTING #####
                # print("Moving to the ", dest)
                assigned_tokens['direction'] = dest
                done = True

    new_command2 = verb_alias_check(new_command2)
    new_command2 = item_alias_check(new_command2)
    new_command2 = feature_alias_check(new_command2)

    # split each word in the string to be an element in an array
    clean_text = new_command2.split()
    command_length = len(clean_text)

    # CHECK FOR VERBS
    if done is False:

        # for each item in the verb array
        for verb_phrase in verb_array:
            verb_match = False

            # get the length of the verb or verb phrase
            verb_split = verb_phrase.split()
            verb_length = len(verb_split)

            # iterate through each word in the user input string
            for index, token in enumerate(clean_text):
                # if the verb is one word and matches a word in user input,
                # we have a verb match
                if token == verb_split[0] and verb_length == 1:
                    verb_match = True

                # if the verb is multi-words, keep seeing if there is a full
                # match
                elif token == verb_split[0] and verb_length > 1:

                    # mark the index where it matched
                    start_count = index
                    i = 0

                    # from where the first word matched, iterate through the
                    # user input to see if it matches the full verb phrase
                    verb_match = True
                    for user_word in range(start_count,
                                           start_count+verb_length-1, 1):
                        # next word in verb phrase matches
                        if clean_text[user_word] == verb_split[i]:
                            i = i+1
                        else:
                            verb_match = False

            # if the verb/phrase matches and no verb is assigned, mark it as
            # the verb of the sentence
            if verb_match is True:
                if assigned_tokens['verb'] is None:
                    assigned_tokens['verb'] = verb_phrase

                # if there was already a verb, then this sentence has too
                # many verbs
                # to process
                else:
                    assigned_tokens['error'] = "You input too many verbs!"
                    invalid = True
                    # assigned_tokens['verb'] = None

    # WE NEED TO HAVE A FAILURE HERE -- commands must have verbs unless
    # they are a direction or standard action!
    if done is False and assigned_tokens['verb'] is None:
        assigned_tokens['error'] = ("You need a recognized verb, or least a "
                                    "destination or standard game action, "
                                    "like \"help\"!")
        invalid = True

    # CHECK FOR ITEMS

    if done is False and invalid is False:

        for item_phrase in item_array:
            item_match = False
            item_split = item_phrase.split()
            item_length = len(item_split)  # get the length of that item

            # iterate through each word in the user input string
            for index, token in enumerate(clean_text):

                # if the item is one word and matches a word in user input,
                # we have a item match
                if token == item_split[0] and item_length == 1:
                    item_match = True

                # if the item is multi-words, keep seeing if there is a full
                # match
                elif token == item_split[0] and item_length > 1:

                    # mark the index where it matched
                    start_count = index
                    i = 0

                    # from where the first word matched, iterate through
                    # the user input to see if it matches the full item/phrase
                    item_match = True
                    for user_word in range(start_count,
                                           start_count+item_length-1, 1):
                        # next word in verb phrase matches
                        if clean_text[user_word] == item_split[i]:
                            i = i+1
                        else:
                            item_match = False
            # if the item/phrase matches and no item is assigned, mark
            # it as the item of the sentence
            if item_match is True:
                if assigned_tokens['item'] is None:
                    assigned_tokens['item'] = item_phrase

                # if there was already an item, then this sentence has too many
                # items to process
                else:
                    assigned_tokens['error'] = "You input too many items!"
                    invalid = True
                    # assigned_tokens['item'] = None

    # CHECK FOR FEATURES
    if done is False and invalid is False:

        for feature_phrase in feature_array:
            feature_match = False
            feature_split = feature_phrase.split()
            feature_length = len(feature_split)  # get the length of that item

            # iterate through each word in the user input string
            for index, token in enumerate(clean_text):

                # if the feature is one word and matches a word in user input,
                # we have a feature match
                if token == feature_split[0] and feature_length == 1:
                    feature_match = True

                # if the feature is multi-words, keep seeing if there is a full
                # match
                elif token == feature_split[0] and feature_length > 1:

                    # mark the index where it matched
                    start_count = index
                    i = 0

                    # from where the first word matched, iterate through the
                    # user input to see if it matches the full feature/phrase
                    feature_match = True

                    for user_word in range(start_count,
                                           start_count+feature_length-1, 1):
                        # next word in feature phrase matches
                        if clean_text[user_word] == feature_split[i]:
                            i = i+1
                        else:
                            feature_match = False
            # if the feature/phrase matches and no feature is assigned,
            # mark it as the feature of the sentence
            if feature_match is True:
                if assigned_tokens['feature'] is None:
                    assigned_tokens['feature'] = feature_phrase

                # if there was already a feature, then this sentence has too
                # many features to process
                else:
                    assigned_tokens['error'] = "You input too many features!"
                    invalid = True
                    # assigned_tokens['feature'] = None

    # Check for extra, unrecognized words in input
    numTokens = 0

    # Used to track cases where feature and item have the same name.
    prevValue = ""

    if "on" in clean_text:
        command_length -= 1

    # if there is not already an error with the input
    if done is False and assigned_tokens['error'] is None:
        # count how many assigned tokens in input
        for key, value in assigned_tokens.items():
            # Checks against feature and item having the same name. Will not
            # Count twice in this case.
            if value is not None and value != prevValue:
                # count the number of words in the token
                numTokens = numTokens + len(value.split())

                if key == 'item' or key == 'feature':
                    prevValue = value

        # if the number of recognized words is not equal to
        # length of the user input, there are extra words
        # print(numTokens)
        # print(command_length)
        if numTokens != command_length:
            assigned_tokens['error'] = ("You input extra and/or unrecognized "
                                        "words!")
            invalid = True

    # ##### PRINT STATEMENT FOR TESTING #####
    # print("\n{}".format(assigned_tokens.items()))

    return assigned_tokens
