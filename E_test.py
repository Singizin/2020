from collections import deque


def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    print(visited)
    return visited


start = 1
goal = 2

if __name__ == '__main__':
    graph = [[0, 0, 1, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [1, 0, 0, 1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0]]
    bfs(1, 7, graph)
