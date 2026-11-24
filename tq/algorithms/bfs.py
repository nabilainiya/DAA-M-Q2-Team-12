"""BFS: Queue + visited + parent. Fewest steps on an unweighted grid."""
from collections import deque
from ..graph import neighbors, rebuild


def bfs(grid, start, target):
    queue, parent, order = deque([start]), {start: None}, []
    while queue:
        u = queue.popleft()
        order.append(u)
        if u == target:
            break
        for v in neighbors(grid, u):
            if v not in parent:
                parent[v] = u
                queue.append(v)
    return order, rebuild(parent, target)
