import heapq


def h(state):
    value = 0
    for i in range(len(state)):
        if state[i] != 'x':
            ori = ord(state[i]) - ord('1')
            value += abs(i // 3 - ori // 3) + abs(i % 3 - ori % 3)
    return value


def a_star(initial_state):
    final_state = '12345678x'
    dist = {}
    prev = {}
    pq = []
    dist[initial_state] = 0
    opt_x = [0, 1, 0, -1]
    opt_y = [-1, 0, 1, 0]
    opt = ['u', 'r', 'd', 'l']
    heapq.heappush(pq, (h(initial_state), initial_state))
    while pq:
        _, cur_state = heapq.heappop(pq)
        if cur_state == final_state:
            break

        idx = cur_state.index('x')
        x_idx, y_idx = idx % 3, idx // 3

        for i in range(4):
            new_x, new_y = x_idx + opt_x[i], y_idx + opt_y[i]
            if new_x < 0 or new_x > 2 or new_y < 0 or new_y > 2:
                continue
            chars = list(cur_state)
            chars[idx], chars[new_y * 3 + new_x] = chars[new_y * 3 + new_x],  chars[idx]
            next_state = ''.join(chars)
            if next_state not in dist or dist[next_state] > dist[cur_state] + 1:
                dist[next_state] = dist[cur_state] + 1
                prev[next_state] = (opt[i], cur_state)
                heapq.heappush(pq, (dist[next_state] + h(next_state), next_state))

    path = ''
    while final_state != initial_state:
        opt, final_state = prev[final_state]
        path += opt
    return path[::-1]


if __name__ == '__main__':
    initial = input().replace(' ', '')
    rev_num = 0
    state = initial.replace('x', '')
    for i in range(8):
        for j in range(i):
            if state[i] > state[j]:
                rev_num += 1
    if rev_num & 1:
        print('unsolvable')
    else:
        print(a_star(initial))
