import time
import matplotlib.pyplot as plt
# import threading
from winsound import Beep
import random


class Words:

    def __init__(self):
        self.word_list = self.get_word_list()

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
            key: value_list for key, value_list in dict_of_all_beginnings.items() if len(value_list) >= 600}
        # only use the first 2 letters that actually have enough to go on
        return filtered_dict

    def get_random_first_two_letters(self):
        filtered_dict = self.get_dict_of_possible_words()
        list_of_first_choices = list(filtered_dict.keys())
        choice_of_first_two_letters = random.choice(list_of_first_choices)
        return choice_of_first_two_letters

class Player:

    def __init__(self):
        self.name = input("Welcome to the game! Please Enter Your Name to Start:\n")
        self.list_of_scores = []

    def __str__(self):
        return self.name

    def add_score_to_list(self, number):
        score = round(number, 2)
        self.list_of_scores.append(score)

    def get_highest_score(self):
        try:
            return max(self.list_of_scores)
        except ValueError:
            return "Oops! No scores yet."
        


class Sound:
    def __init__(self):
        self.playing = False

    def play_tick_tock(self):
        start_time = time.time()
        total_seconds = 30
        
        self.playing = True
        while time.time() - start_time < total_seconds:
            Beep(600,100)
            Beep(800,100) #higher frequency sound 
           
    
    def stop_sound(self):
        self.playing = False

    def play_alarm(self):
        for _ in range(5):
            Beep(2500,500)
            time.sleep(0.05)
    
class WordGame:

    def __init__(self, player, words):
        self.player = player
        self.words = words
        self.current_word_list = []  # to hold words for the round
        self.current_score = self.get_current_score()
        self.list_of_correct_words = []
        self.list_of_incorrect_words = []
        self.instructions = self.get_instructions()
        # self.sound = Sound() # make instance of sound class

    def get_instructions(self):
        print(f"Welcome, {self.player}.")
        time.sleep(1)
        print("The following are instructions on how to play:")
        time.sleep(2)
        print("You will be given the first two letters of a word and you will have 30 seconds to type as many combinations of words as you can.")
        time.sleep(2)
        print("Good luck!")
        time.sleep(2)
        confirmation = input(
            "Please Confirm That You Understand the Instructions by Typing 'ok'\n").lower()

        while confirmation != "ok":
            confirmation = input(
                "Type 'ok' To Show Confirmation of Instructions\n")
        if confirmation == "ok":
            return "Great! "
        return "Great!"

    def get_current_score(self):
        score = 0
        correct_words_count = 0
        incorrect_words_count = 0

        for word in self.current_word_list:
            if word in self.words.get_word_list():
                correct_words_count += 1
                self.list_of_correct_words.append(word)
            else:
                incorrect_words_count += 1
                self.list_of_incorrect_words.append(word)
        total_words = incorrect_words_count + correct_words_count
        if total_words == 0:
            return score == 0
        score = (correct_words_count / total_words) * 100  # out of 100
        return round(score, 2)

    
    def display_results_for_round(self, score):
        # getting length of each word
        length_of_each_word = [len(word)
                               for word in self.list_of_correct_words]

        # Next, we will make a set to have a list of all lengths there are
        set_of_all_lengths_used = set(length_of_each_word)

        # Next, we will put it in a dictionary

        length_count_dict = {}

        for length in set_of_all_lengths_used:
            count_of_each = length_of_each_word.count(length)
            length_count_dict[length] = count_of_each

        plt.bar(length_count_dict.keys(), length_count_dict.values())
        plt.xlabel("Word Length")
        plt.ylabel("Number of Words With That Length")
        correct_words_text = ", ".join(self.list_of_correct_words)
        incorrect_words_text = ", ".join(self.list_of_incorrect_words)
        plt.title(f"{self.player.name.title()}'s Score: {score}\nTotal Correct Words: {len(self.list_of_correct_words)}\nList of Correct Words: {correct_words_text}\nList of Incorrect Words: {incorrect_words_text}\nOther Words You Could've Used: {self.available_words[:10]}")
        plt.show()

    def display_end_results(self):
        plt.figure(figsize=(10, 5))
        # num+1 so that it doesn't start at zero
        y = self.player.list_of_scores
        x = [num+1 for num in range(len(y))]

        plt.plot(x, y, marker='o')
        plt.title(f"{self.player.name}'s Scores Over Time\nHighest Score: {self.player.get_highest_score()}")
        plt.xlabel('Game Number')
        plt.ylabel('Score')
        plt.ylim(0, 100)
        plt.show()

    def start_game(self):
        random_starting_letters = self.words.get_random_first_two_letters()
        # in general, the available dict words
        available_dict_words = self.words.get_dict_of_possible_words()
        # just get the words for these starting letters
        self.available_words = available_dict_words[random_starting_letters]

        print("Ready...")
        time.sleep(1)
        print("Set...")
        time.sleep(1)
        print("Go!")

        start_time = time.time()
        total_seconds = 30

        # tick_tock_sound_thread = threading.Thread(target=self.sound.play_tick_tock)
        # tick_tock_sound_thread.start() # start thread

        while (time.time() - start_time < total_seconds):  # while 30 seconds haven't elapsed yet
            # player will keep on getting the same first letter and they could input anything else for the rest
            # this is to make is a complete word
            word = input(f"Enter a word that begins with {random_starting_letters} ({round(total_seconds - (time.time() - start_time), 0)} seconds left): \n{random_starting_letters}")
            starting_letters = random_starting_letters # reset every time 
            starting_letters += word

            if starting_letters not in self.current_word_list:  # so no doubles
                self.current_word_list.append(starting_letters)

        # self.sound.stop_sound()
        # tick_tock_sound_thread.join() #make sure thread finishes before continuing with main and having alarm sound


        print("Time is up!\n\n")
        # self.sound.play_alarm()

        time.sleep(1)
        score = self.get_current_score()
        self.player.add_score_to_list(score)
        if score <= 50:
            print(f"Oops! You only got {score}. Play again. ")
        elif score < 90:
            print(f"Good job! You scored {score} points.")
        else:
            print(f"Congrats! You scored {score}.")

        time.sleep(1)
        print("\n\nCorrect Words:")
        for wrd in self.list_of_correct_words:
            print(wrd)
        time.sleep(2)
        print("\n\nIncorrect Words:")
        for wrd in self.list_of_incorrect_words:
            print(wrd)
        time.sleep(2)
        print("\n\nSome Other Words That You Could Have Used:")
        for idx, wrd in enumerate(self.available_words):
            print(wrd)
            if idx == 10:
                break
        print("\n\n")
        time.sleep(2)

        self.display_results_for_round(score)

        # reset lists for each round
        self.current_word_list = []
        self.list_of_correct_words = []
        self.list_of_incorrect_words = []


def main():

    player = Player()
    word = Words()
    game = WordGame(player, word)

    print(game.instructions)

    while True:
        game.start_game()

        continue_playing_or_not = input(
            "Do you want to play again? (yes/no):\n")

        while continue_playing_or_not not in ["yes", "no"]:
            continue_playing_or_not = input(
                "Invalid response. Please enter 'yes' if you would like to cotinue playing and 'no' if you would like to stop\n")
        if continue_playing_or_not == "no":
            print(f"Thank you for playing, {player.name}. Your high score is {
                  player.get_highest_score()}")
            game.display_end_results()
            break


if __name__ == "__main__":
    main()
