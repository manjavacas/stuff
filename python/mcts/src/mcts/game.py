from mcts.board import Board
from mcts.players import Player

import tqdm


class Game:
    def __init__(self, board: Board, player1: Player, player2: Player, verbose: bool = True):
        if {player1.symbol, player2.symbol} != {"X", "O"}:
            raise ValueError("Players must have the symbols 'X' and 'O'")
        self.board = board
        self.players = {player1.symbol: player1, player2.symbol: player2}
        self.verbose = verbose

    def play(self) -> str:
        """Play one game. Return the winning symbol or "Draw". X always starts."""
        self.board.reset()
        if self.verbose:
            self.board.print_board()
        while not self.board.is_terminal():
            player = self.players[self.board.current_player]
            # The player gets a copy so it can't corrupt the real board.
            move = player.get_move(self.board.copy())
            self.board.make_move(*move)
            if self.verbose:
                self.board.print_board()
        return self.board.check_winner() or "Draw"


def play_many(player_x: Player, player_o: Player, n_games: int) -> dict[str, int]:
    """Play n_games silently and count the results."""
    game = Game(Board(), player_x, player_o, verbose=False)
    results = {"X": 0, "O": 0, "Draw": 0}
    for _ in tqdm.tqdm(range(n_games), desc=f"Playing {n_games} games"):
        results[game.play()] += 1
    return results
