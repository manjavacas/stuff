from mcts.board import Board
from mcts.game import Game, play_many
from mcts.players import RandomPlayer, MCTSPlayer


def main() -> None:
    p1 = RandomPlayer("X")
    p2 = MCTSPlayer("O")

    # One verbose game to see what happens
    print("Playing one game...")
    winner = Game(Board(), p1, p2).play()
    print(f"Winner: {winner}\n")

    # Many silent games to measure strength
    n = 1000
    results = play_many(p1, p2, n)
    print(f"{n} games -> X: {results['X']}  O: {results['O']}  Draw: {results['Draw']}")


if __name__ == "__main__":
    main()
