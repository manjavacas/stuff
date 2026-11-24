import copy

EMPTY = " "
PLAYERS = ("X", "O")


def other(symbol: str) -> str:
    """Return the opponent's symbol."""
    return "O" if symbol == "X" else "X"


class Board:
    """Tic-tac-toe board. It is the single source of truth for whose turn it is."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.last_player: str | None = None  # who made the last move
        self.last_move: tuple[int, int] | None = None

    def copy(self) -> "Board":
        """Independent copy, safe to mutate in simulations."""
        return copy.deepcopy(self)

    def make_move(self, row: int, col: int) -> None:
        """Place the current player's symbol and pass the turn.

        Raises ValueError if the move is illegal or the game is already over.
        """
        if self.is_terminal():
            raise ValueError("The game is already over")
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError(f"Move out of the board: {(row, col)}")
        if self.board[row][col] != EMPTY:
            raise ValueError(f"Cell already occupied: {(row, col)}")
        self.board[row][col] = self.current_player
        self.last_player = self.current_player
        self.last_move = (row, col)
        self.current_player = other(self.current_player)

    def check_winner(self) -> str | None:
        """Return the winning symbol, or None if nobody has won (yet)."""
        b = self.board
        lines = (
            [b[i] for i in range(3)]  # rows
            + [[b[0][i], b[1][i], b[2][i]] for i in range(3)]  # columns
            + [[b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]]  # diagonals
        )
        for line in lines:
            if line[0] != EMPTY and line[0] == line[1] == line[2]:
                return line[0]
        return None

    def is_full(self) -> bool:
        return all(cell != EMPTY for row in self.board for cell in row)

    def is_terminal(self) -> bool:
        return self.check_winner() is not None or self.is_full()

    def get_available_moves(self) -> list[tuple[int, int]]:
        if self.check_winner() is not None:
            return []
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == EMPTY]

    def result(self, symbol: str) -> float:
        """Result of a finished game from `symbol`'s point of view.

        1.0 = win, 0.0 = loss, 0.5 = draw.
        """
        if not self.is_terminal():
            raise ValueError("The game is not over")
        winner = self.check_winner()
        if winner is None:
            return 0.5
        return 1.0 if winner == symbol else 0.0

    def __str__(self) -> str:
        return "\n-+-+-\n".join("|".join(row) for row in self.board)

    def print_board(self) -> None:
        print(self)
        print()
