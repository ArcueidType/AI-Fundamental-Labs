import heapq


def reachable(x, y):
    if 0 <= x < 3 and 0 <= y < 3:
        return True
    else:
        return False


def dijkstra(initial_state: str):
    visited = {}
    opt_x = [0, 1, 0, -1]
    opt_y = [-1, 0, 1, 0]
    pq = [(0, initial_state)]
    visited[initial_state] = True
    final_state = '12345678x'
    while pq:
        cur_dist, cur_state = heapq.heappop(pq)
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
            if next_state not in visited:
                visited[''.join(next_state[:9])] = True
                heapq.heappush(pq, (cur_dist + 1, next_state))
    return -1


if __name__ == '__main__':
    initial = input().replace(' ', '')
    print(dijkstra(initial))
