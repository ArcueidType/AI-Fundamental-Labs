from queue import Queue


def bfs(graph, origin, dest):
    q = Queue()

    dist = [-1] * (dest + 1)
    dist[origin] = 0
    q.put(origin)
    while not q.empty():
        cur = q.get()
        for node in graph[cur]:
            if dist[node] == -1:
                dist[node] = dist[cur] + 1
                q.put(node)
    return dist[dest]


if __name__ == '__main__':
    dest, line_nums = map(int, input('').split(' '))
    graph = [[] for _ in range(dest + 1)]
    for i in range(line_nums):
        o, d = map(int, input('').split(' '))
        graph[o].append(d)

    dist = bfs(graph, 1, dest)
    print(dist)
