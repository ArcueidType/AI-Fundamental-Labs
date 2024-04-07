def extract_min(pq):
    min_key = 0
    for i, k in enumerate(pq):
        if i == 0:
            min_key = k
            continue
        if pq[k] < pq[min_key]:
            min_key = k
    node = min_key
    min_value = pq[min_key]
    pq.pop(min_key)
    return node, min_value


def dijkstra(graph, ori, dest):
    pq = {ori: 0}
    dist = [-1] * (dest + 1)
    while pq:
        cur, cur_dist = extract_min(pq)
        dist[cur] = cur_dist
        for node, weight in graph[cur]:
            if dist[node] == -1:
                if node in pq.keys():
                    if cur_dist+weight < pq[node]:
                        pq[node] = cur_dist + weight
                else:
                    pq[node] = cur_dist + weight
    return dist[dest]


if __name__ == '__main__':
    dest, line_nums = map(int, input('').split(' '))
    graph = [[] for _ in range(dest + 1)]
    for i in range(line_nums):
        o, d, w = map(int, input('').split(' '))
        graph[o].append((d, w))

    min_dist = dijkstra(graph, 1, dest)
    print(min_dist)

