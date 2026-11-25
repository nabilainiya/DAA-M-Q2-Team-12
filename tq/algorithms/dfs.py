"""DFS: Stack + backtracking. Explores the reachable area and records treasures.
Not a shortest-path algorithm."""
from ..graph import neighbors


def dfs(grid, start, treasures):
    stack, seen, order, found = [start], set(), [], []
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        order.append(u)
        if u in treasures:
            found.append(u)
        stack.extend(v for v in list(neighbors(grid, u))[::-1] if v not in seen)
    return order, found
