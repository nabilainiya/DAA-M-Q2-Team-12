import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tq.algorithms import bfs, dfs, dijkstra
from tq.game import Game
from tq.graph import path_cost
from tq.maps import LEVELS


class AlgorithmTests(unittest.TestCase):

    def test_wall_collision(self):
        g = Game.load(0)
        g.move(-1, 0)
        self.assertEqual(g.player, (1, 1))


if __name__ == "__main__":
    unittest.main()
