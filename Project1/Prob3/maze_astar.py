import numpy as np
import heapq


def h1(cur_pos: tuple, dest_pos: tuple):
    x_cur, y_cur = cur_pos[0], cur_pos[1]
    x_dest, y_dest = dest_pos[0], dest_pos[1]
    value = abs(y_dest - y_cur) + abs(x_dest - x_cur)
    return value


def h2(cur_pos: tuple, dest_pos: tuple):
    x_cur, y_cur = cur_pos[0], cur_pos[1]
    x_dest, y_dest = dest_pos[0], dest_pos[1]
    value = abs(y_dest - y_cur) ** 2 + abs(x_dest - x_cur) ** 2
    return value


def a_star(maze: np.ndarray, ori: tuple, dest: tuple, h):
    m = len(maze[0])
    n = len(maze)
    dist = np.array([[-1 for _ in range(m)] for _ in range(n)])
    prev = np.empty(shape=(n, m), dtype=tuple)
    searched = set()
    step_infos = []
    dist[ori[1], ori[0]] = 0
    mov_x = [1, 0, -1, 0]
    mov_y = [0, -1, 0, 1]
    pq = []
    heapq.heappush(pq, (h(ori, dest), ori))
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
        _, (x_cur, y_cur) = heapq.heappop(pq)
        step_infos.append((step, cur_path(ori, (x_cur, y_cur)), searched.copy()))
        step += 1
        if (x_cur, y_cur) == dest:
            break
        cur_dist = dist[y_cur, x_cur]
        for i in range(4):
            x_new, y_new = x_cur + mov_x[i], y_cur + mov_y[i]
            if (0 <= x_new < m and 0 <= y_new < n) and maze[y_new, x_new] == 0:
                if dist[y_new, x_new] == -1 or dist[y_new, x_new] > cur_dist + 1:
                    dist[y_new, x_new] = cur_dist + 1
                    prev[y_new, x_new] = (x_cur, y_cur)
                    searched.add((x_new, y_new))
                    heapq.heappush(pq, (dist[y_new, x_new] + h((x_new, y_new), dest), (x_new, y_new)))
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
    path, dist, searched = a_star(maze, (0, 0), (m - 1, n - 1), h2)
    print(path, dist, searched)
