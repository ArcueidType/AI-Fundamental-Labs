"""
待补充代码：对搜索过的格子染色
"""
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from maze_dijkstra import dijkstra
from maze_astar import a_star
from maze_dfs import dfs
from maze_bfs import bfs


def visualize_maze_with_path(maze, algorithm: str):
    match algorithm:
        case 'a_star':
            path, _, step_infos = a_star(maze, (1, 0), (33, 34))
        case 'dijkstra':
            path, _, step_infos = dijkstra(maze, (1, 0), (33, 34))
        case 'bfs':
            path, _, step_infos = bfs(maze, (1, 0), (33, 34))
        case 'dfs':
            path, _, step_infos = dfs(maze, (1, 0), (33, 34))

    fig = plt.figure(figsize=(10, 10 * len(maze) / len(maze[0])))

    maze[path[0][1]][path[0][0]] = -1
    plt.imshow(maze, cmap='tab20c_r', interpolation='nearest')  # 使用灰度色图，并关闭插值

    plt.plot(path[0][0], path[0][1], marker='o', markersize=10, color='saddlebrown')
    plt.plot(path[-1][0], path[-1][1], marker='*', markersize=10, color='saddlebrown')
    # 设置坐标轴刻度和边框
    plt.xticks(range(len(maze[0])))
    plt.yticks(range(len(maze)))
    plt.gca().set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
    plt.grid(which="minor", color="black", linestyle='-', linewidth=2)

    plt.axis('on')  # 显示坐标轴

    def ani(frame):
        _, cur_path, cur_searched = step_infos[frame]

        for x, y in cur_searched:
            maze[y][x] = -1

        path_y, path_x = zip(*cur_path)
        plt.cla()
        plt.plot(path_y, path_x, marker='o', markersize=3, color='sandybrown', linewidth=3)
        plt.plot(path[0][0], path[0][1], marker='o', markersize=10, color='saddlebrown')
        plt.plot(path[-1][0], path[-1][1], marker='*', markersize=10, color='saddlebrown')
        plt.xticks(range(len(maze[0])))
        plt.yticks(range(len(maze)))
        plt.gca().set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
        plt.gca().set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
        plt.grid(which="minor", color="black", linestyle='-', linewidth=2)

        plt.axis('on')  # 显示坐标轴
        plt.imshow(maze, cmap='tab20c_r', interpolation='nearest')
        return []

    ani = animation.FuncAnimation(fig=fig, func=ani, frames=len(step_infos), interval=1, blit=True, repeat=False)
    # ani.save(algorithm + '.gif', writer='pillow', fps=24)
    plt.show()

# maze = np.array([
#     [0 for _ in range(15)],
#     [0 for _ in range(15)],
#     [0, 0, *(1 for _ in range(11)), 0, 0],
#     [*(0 for _ in range(12)), 1, 0, 0],
#     [*(0 for _ in range(12)), 1, 0, 0],
#     [*(0 for _ in range(12)), 1, 0, 0],
#     [*(0 for _ in range(12)), 1, 0, 0],
#     [*(0 for _ in range(12)), 1, 0, 0],
#     [*(0 for _ in range(12)), 1, 0, 0],
#     [*(0 for _ in range(12)), 1, 0, 0],
#     [*(0 for _ in range(12)), 1, 0, 0],
#     [*(0 for _ in range(12)), 1, 0, 0],
#     [0, 0, *(1 for _ in range(11)), 0, 0],
#     [0 for _ in range(15)],
#     [0 for _ in range(15)]
# ])


if __name__ == '__main__':
    maze = np.load('maze.npy')
    visualize_maze_with_path(maze, 'a_star')

    # maze = np.load('maze.npy')
    # visualize_maze_with_path(maze, 'dijkstra')

    # maze = np.load('maze.npy')
    # visualize_maze_with_path(maze, 'dfs')

    # maze = np.load('maze.npy')
    # visualize_maze_with_path(maze, 'bfs')
