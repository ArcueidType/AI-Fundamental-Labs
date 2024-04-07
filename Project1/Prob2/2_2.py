import queue


def bfs(initial_state: str):
    dist = {initial_state: 0}
    opt_x = [0, 1, 0, -1]
    opt_y = [-1, 0, 1, 0]
    q = queue.Queue()
    q.put(initial_state)
    final_state = '12345678x'
    while not q.empty():
        cur_state = q.get()
        cur_dist = dist[cur_state]
        if cur_state == final_state:
            return cur_dist

        idx = cur_state.index('x')
        x_idx, y_idx = idx % 3, idx // 3

        for i in range(4):
            new_x, new_y = x_idx + opt_x[i], y_idx + opt_y[i]
            if new_x < 0 or new_x > 2 or new_y < 0 or new_y > 2:
                continue
            next_state = list(cur_state)
            next_state[idx], next_state[new_y * 3 + new_x] = next_state[new_y * 3 + new_x], next_state[idx]
            next_state = ''.join(next_state)
            if next_state not in dist:
                dist[next_state] = cur_dist + 1
                q.put(next_state)
    return -1


if __name__ == '__main__':
    initial = input().replace(' ', '')
    print(bfs(initial))
