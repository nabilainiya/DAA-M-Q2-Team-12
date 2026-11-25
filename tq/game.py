from dataclasses import dataclass, field
from .maps import LEVELS


@dataclass
class Game:
    level: int
    grid: list
    player: tuple
    treasures: list
    exit: tuple
    reset_used: bool = False
    got: set = field(default_factory=set)
    score: int = 0
    steps: int = 0
    won: bool = False
    msg: str = "Kumpulkan semua treasure, lalu menuju Exit."

    @classmethod
    def load(cls, level, reset_used=False):
        grid, treasures, player, exit_ = [], [], None, None
        for r, row in enumerate(LEVELS[level][1]):
            cells = []
            for c, ch in enumerate(row):
                if ch == "S":
                    player, ch = (r, c), "."
                elif ch == "T":
                    treasures.append((len(treasures) + 1, (r, c)))
                    ch = "."
                elif ch == "E":
                    exit_, ch = (r, c), "."
                cells.append(ch)
            grid.append(cells)
        return cls(level, grid, player, treasures, exit_, reset_used)

    @property
    def exit_open(self):
        return len(self.got) == len(self.treasures)

    def remaining(self):
        return {pos for i, pos in self.treasures if i not in self.got}

    def targets(self):
        t = [(f"Treasure {i}", pos) for i, pos in self.treasures if i not in self.got]
        return t + [("Exit", self.exit)]

    def move(self, dr, dc):
        r, c = self.player[0] + dr, self.player[1] + dc
        if not (0 <= r < len(self.grid) and 0 <= c < len(self.grid[r])) or self.grid[r][c] == "#":
            self.msg = "Menabrak wall!"
            return
        self.player, self.steps, self.msg = (r, c), self.steps + 1, ""
        for i, pos in self.treasures:
            if pos == self.player and i not in self.got:
                self.got.add(i)
                self.score += 100
                self.msg = f"Treasure {i} didapat! +100"
        if self.player == self.exit:
            left = len(self.treasures) - len(self.got)
            if left:
                self.msg = f"Exit terkunci. Masih ada {left} treasure."
            else:
                self.won = True
                self.score += 500 + (0 if self.reset_used else 200)
