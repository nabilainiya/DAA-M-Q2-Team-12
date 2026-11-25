"""Dijkstra: Priority Queue (heapq) + edge relaxation. Minimum total terrain cost."""
import heapq
from ..graph import neighbors, cost, rebuild


def dijkstra(grid, start, target):
    dist, parent, done, order = {start: 0}, {start: None}, set(), []
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if u in done:
            continue
        done.add(u)
        order.append(u)
        if u == target:
            break
        for v in neighbors(grid, u):
            nd = d + cost(grid, v)
            if nd < dist.get(v, float("inf")):
                dist[v], parent[v] = nd, u
                heapq.heappush(pq, (nd, v))
    return order, rebuild(parent, target)
