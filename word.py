import random

class Words:

    def __init__(self):
        self.word_list = self.get_word_list()
        # self.possible_beginnings =

    def get_word_list(self):
        with open("words_alpha.txt") as words:
            # returns the list of words without the whitespaces
            # we only want words in list that are >=3
            return [word.strip() for word in words.readlines() if word.strip() and len(word.strip()) >= 3]

    def get_dict_of_possible_words(self):
        dict_of_all_beginnings = {}
        # get the whole word list. We will now put it into a dictionary below organized by first two letters as keys
        list_of_words = self.get_word_list()
        for word in list_of_words:
            first_two_letters = word[:2]
            if first_two_letters not in dict_of_all_beginnings:
                # make a new list for those beginnings
                dict_of_all_beginnings[first_two_letters] = []
            else:
                # there is already a list in the dictionary, so we will just append the next word to the list
                dict_of_all_beginnings[first_two_letters].append(word)

        filtered_dict = {
            key: value_list for key, value_list in dict_of_all_beginnings.items() if len(value_list) >= 300}
        # only use the first 2 letters that actually have enough to go on -- did loop with counter and there are 174 options for this condition
        return filtered_dict

    def get_random_first_two_letters(self):
        filtered_dict = self.get_dict_of_possible_words()
        list_of_first_choices = list(filtered_dict.keys())
        choice_of_first_two_letters = random.choice(list_of_first_choices)
        return choice_of_first_two_letters

    def get_first_two_letters_for_all(self):
        pass
