import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tq.algorithms import bfs, dfs, dijkstra
from tq.game import Game
from tq.graph import path_cost
from tq.maps import LEVELS

class AlgorithmTests(unittest.TestCase):
    def test_bfs_vs_dijkstra_level3(self):
        g = Game.load(2)
        target = g.treasures[0][1]
        _, p_bfs = bfs(g.grid, g.player, target)
        _, p_dij = dijkstra(g.grid, g.player, target)
        self.assertEqual(len(p_bfs) - 1, 8)
        self.assertEqual(path_cost(g.grid, p_bfs), 14)
        self.assertEqual(path_cost(g.grid, p_dij), 12)
        self.assertGreater(len(p_dij), len(p_bfs))

    def test_all_targets_reachable_and_dfs_finds_all(self):
        for i in range(len(LEVELS)):
            g = Game.load(i)
            order, found = dfs(g.grid, g.player, g.remaining())
            self.assertEqual(set(found), g.remaining())
            self.assertIn(g.exit, order)

    def test_full_playthrough_score(self):
        for i in range(len(LEVELS)):
            g = Game.load(i)
            for t in [p for _, p in g.treasures] + [g.exit]:
                for u in bfs(g.grid, g.player, t)[1][1:]:
                    g.move(u[0] - g.player[0], u[1] - g.player[1])
            self.assertTrue(g.won)
            self.assertEqual(g.score, 100 * len(g.treasures) + 700)

    def test_wall_collision(self):
        g = Game.load(0)
        g.move(-1, 0)
        self.assertEqual(g.player, (1, 1))


if __name__ == "__main__":
    unittest.main()
