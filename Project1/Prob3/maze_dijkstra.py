import numpy as np
import heapq


def dijkstra(maze: np.ndarray, ori: tuple, dest: tuple):
    m = len(maze[0])
    n = len(maze)
    confirmed = np.array([[0 for _ in range(m)] for _ in range(n)])
    dist = np.array([[-1 for _ in range(m)] for _ in range(n)])
    prev = np.empty(shape=(n, m), dtype=tuple)
    searched = set()
    step_infos = []
    dist[ori[1], ori[0]] = 0
    mov_x = [1, 0, -1, 0]
    mov_y = [0, -1, 0, 1]
    pq = []
    heapq.heappush(pq, (0, ori))
    step = 1

    def cur_path(ori: tuple, dest: tuple):
        back = dest
        path = [back]
        while back != ori:
            pt = prev[back[1], back[0]]
            path.append(pt)
            back = pt
        path.reverse()
        return path

    while pq:
        cur_dist, (x_cur, y_cur) = heapq.heappop(pq)
        confirmed[y_cur, x_cur] = 1
        step_infos.append((step, cur_path(ori, (x_cur, y_cur)), searched.copy()))
        step += 1
        if confirmed[dest[1], dest[0]] == 1:
            break

        for i in range(4):
            x_new, y_new = x_cur + mov_x[i], y_cur + mov_y[i]
            if (0 <= x_new < m and 0 <= y_new < n) and maze[y_new, x_new] == 0 and not confirmed[y_new, x_new]:
                if dist[y_new, x_new] == -1 or dist[y_new, x_new] > cur_dist + 1:
                    dist[y_new, x_new] = cur_dist + 1
                    prev[y_new, x_new] = (x_cur, y_cur)
                    searched.add((x_new, y_new))
                    heapq.heappush(pq, (dist[y_new, x_new], (x_new, y_new)))
    back = dest
    path = [back]
    while back != ori:
        pt = prev[back[1], back[0]]
        path.append(pt)
        searched.discard(pt)
        back = pt
    path.reverse()
    searched.discard(dest)
    return path, dist[dest[1], dest[0]], step_infos


if __name__ == '__main__':
    n, m = map(int, input().split(' '))  # N x M
    maze = np.ones((n, m), dtype=np.int8)
    for i in range(n):
        maze[i] = input().split(' ')

    path, dist, searched = dijkstra(maze, (0, 0), (m - 1, n - 1))
    print(path, dist, searched)
