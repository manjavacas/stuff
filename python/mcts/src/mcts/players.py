import random
from math import log
from mcts.board import Board
from dataclasses import dataclass, field
from typing import Protocol

class Player(Protocol):
    symbol: str

    def get_move(self, board: Board) -> tuple[int, int]:
        ...

class RandomPlayer:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def get_move(self, board: Board) -> tuple[int, int]:
        return random.choice(board.get_available_moves())


class MCTSPlayer:
    @dataclass
    class State:
        board: Board
        parent: "MCTSPlayer.State | None" = None
        move: tuple[int, int] | None = None
        children: list["MCTSPlayer.State"] = field(default_factory=list)
        v: float = 0.0
        n: int = 0
            
    def __init__(self, symbol: str, iterations: int = 1000):
        self.symbol = symbol
        self.iterations = iterations

    def ucb1(self, state: 'MCTSPlayer.State') -> float:
        if state.n == 0:
            return float('inf')
        exploitation = state.v / state.n
        exploration = 2 * (log(state.parent.n / state.n)** 0.5)
        return exploitation + exploration

    def rollout(self, state: "MCTSPlayer.State") -> str | None:
        board = state.board.copy()         
        while not board.is_terminal():
            board.make_move(*random.choice(board.get_available_moves()))
        return board.check_winner() 
        
    def backpropagate(self, state: 'MCTSPlayer.State', result: str | None) -> None:
        while state is not None:
            state.n += 1
            if result is None:
                state.v += 0.5
            elif result == state.board.last_player:
                state.v += 1
            state = state.parent

    def get_move(self, board: Board) -> tuple[int, int]:
        # Implementation of MCTS
        root = self.State(board=board)
        for _ in range(self.iterations):
            current = root
            # SELECTION
            while current.children:
                current = max(current.children, key=lambda child: self.ucb1(child))
            # EXPANSION
            if current.n > 0 and not current.board.is_terminal():
                for move in current.board.get_available_moves():
                    new_board = current.board.copy()
                    new_board.make_move(*move)
                    current.children.append(self.State(board=new_board, parent=current, move=move))
                current = random.choice(current.children)
            # SIMULATION
            result = self.rollout(current)
            # BACKPROPAGATION
            self.backpropagate(current, result)
            
        return max(root.children, key=lambda c: c.v / c.n if c.n else float("-inf")).move