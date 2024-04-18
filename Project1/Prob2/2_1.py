import queue


def dfs(state: list):
    global visited
    global stack

    opt_x = [0, 1, 0, -1]
    opt_y = [-1, 0, 1, 0]
    idx = state.index('x')
    x_idx, y_idx = idx % 3, idx // 3

    for i in range(4):
        new_x, new_y = x_idx + opt_x[i], y_idx + opt_y[i]
        if new_x < 0 or new_x > 2 or new_y < 0 or new_y > 2:
            continue
        next_state = list(cur_state)
        next_state[idx], next_state[new_y * 3 + new_x] = next_state[new_y * 3 + new_x], next_state[idx]
        next_state = ''.join(next_state)
        if next_state not in visited:
            stack.put(next_state)
            visited[next_state] = True


if __name__ == '__main__':
    initial = input().split(' ')
    visited = {}
    stack = queue.LifoQueue()
    stack.put(initial)
    visited[''.join(initial)] = True

    while True:
        if stack.empty():
            print(0)
            break
        cur_state = stack.get(block=True)
        if cur_state == '12345678x':
            print(1)
            break
        dfs(cur_state)
