import sys
from tq.algorithms import bfs, dfs, dijkstra
from tq.game import Game
from tq.graph import path_cost
from tq.maps import LEVELS
from tq.render import render_grid
from tq.term import getkey, show

MOVES = {"up": (-1, 0), "w": (-1, 0), "down": (1, 0), "s": (1, 0),
         "left": (0, -1), "a": (0, -1), "right": (0, 1), "d": (0, 1)}
B = lambda t: f"\x1b[1m{t}\x1b[0m"
HOW = f"""{B('INSTRUCTIONS')}

 Gerak: WASD atau tombol panah (4 arah). Wall (#) tidak bisa dilewati.
 Treasure ($) diambil otomatis saat diinjak.
 Exit terkunci (X) sampai semua treasure terkumpul, lalu menjadi E.
 Skor = (100 x treasure) + 500 selesai + 200 bonus jika tanpa Restart.
 Terrain: grass . = 1, sand : = 2, swamp ~ = 3.
 Algorithm Assistant hanya memberi saran; kamu tetap bebas bergerak.

 (tekan tombol apa saja)"""
ALGO = f"""{B('ALGORITHM INFORMATION')}

 BFS      Queue. Jalur dengan LANGKAH paling sedikit (bobot dianggap sama).
 DFS      Stack + backtracking. Menjelajah area dan menemukan treasure,
          bukan untuk jalur terpendek.
 Dijkstra Priority Queue. Jalur dengan BIAYA terrain minimum; bisa memilih
          jalur lebih panjang demi menghindari swamp. Coba di Level 3!

 (tekan tombol apa saja)"""
LEGEND = (" @ pemain  $ treasure  X/E exit  # wall  . grass(1)  : sand(2)  ~ swamp(3)"
          "  o dijelajahi  * jalur akhir")
CONTROLS = " WASD/panah gerak | 1 BFS  2 DFS  3 Dijkstra | T ganti target | C bersihkan | R restart | M menu"


def draw(g, viz, info, target):
    visited, path = viz if viz else ((), ())
    show(f"{B(LEVELS[g.level][0])}   Treasure {len(g.got)}/{len(g.treasures)}   Skor {g.score}"
         f"   Langkah {g.steps}   Exit: {'TERBUKA' if g.exit_open else 'terkunci'}\n\n"
         f"{render_grid(g, visited, path)}\n\n {g.msg}\n"
         f" {info or 'Tekan 1/2/3 untuk menjalankan BFS/DFS/Dijkstra dari posisimu.'}\n\n"
         f"{LEGEND}\n Target algoritma: {target[0]} (DFS tidak memakai target)\n{CONTROLS}")


def animate(g, n, target):
    name = {1: "BFS", 2: "DFS", 3: "Dijkstra"}[n]
    found = None
    if n == 2:
        order, found = dfs(g.grid, g.player, g.remaining())
        path = []
    else:
        order, path = (bfs if n == 1 else dijkstra)(g.grid, g.player, target[1])
    frames = [("v", u) for u in order] + [("p", u) for u in (path or [])]
    visited, final = set(), set()
    for kind, u in frames:
        (visited if kind == "v" else final).add(u)
        draw(g, (visited, final), f"{name}: node dikunjungi {len(visited)}", target)
        k = getkey(0.04)
        if k == "p":
            draw(g, (visited, final), f"{name}: PAUSE - tekan tombol apa saja", target)
            getkey()
        elif k == "c":
            return None, ""
    info = f"{name}: node dikunjungi {len(visited)}"
    if n == 2:
        info += " | treasure ditemukan: " + (" ".join(map(str, found)) or "-") + " | DFS bukan shortest path"
    elif path:
        info += f" | langkah {len(path) - 1} | biaya {path_cost(g.grid, path)}"
    else:
        info += " | tidak ada jalur"
    return (visited, final), info


def play(level, reset_used=False):
    g, tidx, viz, info = Game.load(level, reset_used), 0, None, ""
    while True:
        targets = g.targets()
        tidx %= len(targets)
        draw(g, viz, info, targets[tidx])
        k = getkey()
        if k in MOVES:
            g.move(*MOVES[k])
            if g.won:
                show(f"{B('LEVEL SELESAI!')}  {LEVELS[level][0]}\n\n{render_grid(g)}\n\n"
                     f" Treasure  : {len(g.got)}/{len(g.treasures)}\n Langkah   : {g.steps}\n"
                     f" Skor akhir: {g.score}{'' if g.reset_used else '  (termasuk bonus tanpa reset)'}\n\n"
                     " [r] Play Again   [m] Back to Menu")
                while (k := getkey()) not in ("r", "m"):
                    pass
                return "again" if k == "r" else "menu"
        elif k in ("1", "2", "3"):
            viz, info = animate(g, int(k), targets[tidx])
        elif k == "t":
            tidx, viz, info = tidx + 1, None, ""
        elif k == "c":
            viz, info = None, ""
        elif k == "r":
            return "restart"
        elif k == "m":
            return "menu"


def choose_level():
    show(f"{B('PILIH LEVEL')}\n\n" + "\n".join(f" [{i + 1}] {n}" for i, (n, _) in enumerate(LEVELS)) + "\n [b] Kembali")
    while True:
        k = getkey()
        if k == "b":
            return None
        if k and k.isdigit() and 1 <= int(k) <= len(LEVELS):
            return int(k) - 1


def main():
    sys.stdout.write("\x1b[?25l")
    try:
        while True:
            show(f"{B('TREASURE QUEST')} - A Multiple Treasure Hunt Adventure\n\n"
                 " [1] Play Game\n [2] Instructions\n [3] Algorithm Information\n [q] Keluar")
            k = getkey()
            if k == "1":
                level = choose_level()
                result = "again" if level is not None else "menu"
                while result in ("again", "restart") and level is not None:
                    result = play(level, reset_used=(result == "restart"))
            elif k in ("2", "3"):
                show(HOW if k == "2" else ALGO)
                getkey()
            elif k == "q":
                break
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\x1b[?25h\n")


if __name__ == "__main__":
    main()
