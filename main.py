import argparse
from game import TicTacToe

def main():
    parser = argparse.ArgumentParser(description="Play Tic Tac Toe in the terminal.")
    parser.add_argument('--player1', type=str, default='Player 1', help='Name of Player 1')
    parser.add_argument('--player2', type=str, default='Player 2', help='Name of Player 2')
    args = parser.parse_args()

    game = TicTacToe(args.player1, args.player2)
    game.play_game()

if __name__ == "__main__":
    main()
