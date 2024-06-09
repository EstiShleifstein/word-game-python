import random

class Words:

    def __init__(self):
        self.word_list = self.get_word_list()
        self.first_begginings = self.get_list_of_all_first_beginnings()

    def get_word_list(self):
        with open("words_alpha.txt") as words:
            # returns the list of words without the whitespaces
            # we only want words in list that are >=3
            return [word.strip() for word in words.readlines() if word.strip() and len(word.strip()) >= 3]

    def get_dict_of_possible_words(self):
        dict_of_all_beginnings = {}
        # We will now put it into a dictionary below organized by first two letters as keys
        for word in self.word_list:
            first_two_letters = word[:2]
            if first_two_letters not in dict_of_all_beginnings:
                # make a new list for those beginnings
                dict_of_all_beginnings[first_two_letters] = []
            else:
                # there is already a list in the dictionary, so we will just append the next word to the list
                dict_of_all_beginnings[first_two_letters].append(word)

        filtered_dict = {key: value_list for key, value_list in dict_of_all_beginnings.items() if len(value_list) >= 600}
        # only use the first 2 letters that actually have enough to go on -- at least 600 words
        return filtered_dict
    
    def get_list_of_all_first_beginnings(self):
        filtered_dict = self.get_dict_of_possible_words()
        list_of_first_options = list(filtered_dict.keys()) # getting just the keys = all of the possible combinations
        return list_of_first_options

    def get_random_first_two_letters(self):
        list_of_first_options = self.get_list_of_all_first_beginnings()
        choice_of_first_two_letters = random.choice(list_of_first_options)
        self.first_begginings.remove(choice_of_first_two_letters) # so there are no repeats during the game
        return choice_of_first_two_letters

