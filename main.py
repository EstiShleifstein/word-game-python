from players import Player
from words import Words
from word_games import WordGame


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
