import heapq


def dijkstra(graph, origin, dest):
    pq = [(0, origin)]
    dist = [-1] * (dest + 1)

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        if dist[cur_node] != -1:
            continue

        dist[cur_node] = cur_dist
        for node, weight in graph[cur_node]:
            if dist[node] == -1:
                heapq.heappush(pq, (cur_dist+weight, node))

    return dist[dest]


if __name__ == '__main__':
    dest, line_nums = map(int, input('').split(' '))
    graph = [[] for _ in range(dest + 1)]
    for i in range(line_nums):
        o, d, w = map(int, input('').split(' '))
        graph[o].append((d, w))

    min_dist = dijkstra(graph, 1, dest)
    print(min_dist)
