import os
import json
import time
from colorama import init, Fore, Style
from utils import save_game_history

init(autoreset=True)

class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [' '] * 9
        self.current_player = player1
        self.other_player = player2
        self.symbols = {player1: 'X', player2: 'O'}
        self.scores = {player1: 0, player2: 0}

    def print_board(self):
        print(Fore.YELLOW + "\nCurrent Board:")
        for i in range(0, 9, 3):
            print(Fore.GREEN + f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print(Fore.BLUE + "---|---|---")

    def is_winner(self, symbol):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        return any(all(self.board[i] == symbol for i in cond) for cond in win_conditions)

    def is_draw(self):
        return ' ' not in self.board

    def switch_players(self):
        self.current_player, self.other_player = self.other_player, self.current_player

    def display_scores(self):
        print(Fore.CYAN + f"\n🎯 Current Scoreboard:")
        for player, score in self.scores.items():
            print(f"{player}: {score} wins")

    def play_game(self):
        play_again = True

        while play_again:
            self.board = [' '] * 9
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.display_scores()
                self.print_board()

                start_time = time.time()
                try:
                    move = int(input(f"{self.current_player} ({self.symbols[self.current_player]}), choose your move (1-9): ")) - 1
                    time_taken = time.time() - start_time

                    if time_taken > 15:
                        print(Fore.RED + "⏱️ You took too long! Move faster next time.")

                    if self.board[move] != ' ':
                        print(Fore.RED + "⚠️ Position already taken. Try again.")
                        time.sleep(1)
                        continue
                except (ValueError, IndexError):
                    print(Fore.RED + "❌ Invalid input. Please enter a number from 1 to 9.")
                    time.sleep(1)
                    continue

                self.board[move] = self.symbols[self.current_player]

                if self.is_winner(self.symbols[self.current_player]):
                    self.print_board()
                    print(Fore.GREEN + f"\n🎉 {self.current_player} wins!")
                    self.scores[self.current_player] += 1
                    save_game_history(self.current_player, self.other_player, self.symbols[self.current_player])
                    break
                elif self.is_draw():
                    self.print_board()
                    print(Fore.MAGENTA + "\nIt's a draw!")
                    save_game_history(self.current_player, self.other_player, "Draw")
                    break
                else:
                    self.switch_players()

            # Ask to play again
            replay = input(Fore.YELLOW + "\n🔁 Do you want to play another round? (y/n): ").lower()
            if replay != 'y':
                play_again = False
                print(Fore.CYAN + "\nThanks for playing! Final Scores:")
                self.display_scores()
