"""Grid = graph: walkable tile = vertex, 4-direction move = edge.
Cost of a step = cost of the tile entered."""
DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
COST = {".": 1, ":": 2, "~": 3}


def neighbors(grid, u):
    for dr, dc in DIRS:
        r, c = u[0] + dr, u[1] + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] != "#":
            yield (r, c)


def cost(grid, u):
    return COST[grid[u[0]][u[1]]]


def rebuild(parent, target):
    """Reconstruct path from the parent map; None if target was never reached."""
    if target not in parent:
        return None
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return path[::-1]


def path_cost(grid, path):
    return sum(cost(grid, u) for u in path[1:])
