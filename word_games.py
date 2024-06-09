import time
import matplotlib.pyplot as plt

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
        print("You will be given the first two letters of a word and you will have 15 seconds to type as many combinations of words as you can.")
        time.sleep(2)
        print("Good luck!")
        time.sleep(2)
        confirmation = input("Please Confirm That You Understand the Instructions by Typing 'ok'\n").lower()

        while confirmation != "ok":
            confirmation = input("Type 'ok' To Show Confirmation of Instructions\n").lower()
        if confirmation == "ok":
            return "Great! "
        return "Invalid Input."

    # below is for calculating the score based on correct and incorrect words
    def get_current_score(self):
        score = 0
        correct_words_count = 0
        incorrect_words_count = 0

        for word in self.current_word_list:
            if word in self.words.word_list:
                correct_words_count += 1
                self.list_of_correct_words.append(word)
            else:
                incorrect_words_count += 1
                self.list_of_incorrect_words.append(word)
        total_words = incorrect_words_count + correct_words_count
        if total_words == 0:
            return score == 0
        score = (correct_words_count / total_words) * 100  # to make it out of 100
        return round(score, 2)

    # using matplotlib:
    def display_results_for_round(self, score):
        # getting length of each word
        length_of_each_word = [len(word) for word in self.list_of_correct_words]

        # Next, we will make a set to have a list of all lengths there are with no repeats. These are the possible values.
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
        other_possible_words = ", ".join(self.available_words[:10])
        plt.title(f"{self.player.name.title()}'s Score: {score} -- Total Correct Words: {len(self.list_of_correct_words)}\nList of Correct Words: {correct_words_text}\nList of Incorrect Words: {incorrect_words_text}\nOther Words You Could've Used: {other_possible_words}")
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
        total_seconds = 15

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