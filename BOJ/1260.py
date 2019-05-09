# 백준알고리즘 1260번
# https://www.acmicpc.net/problem/1260

# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

nodes, links, start = map(int, input().split(" "))

table = [[0]*(nodes+1) for _ in range(nodes+1)]

for _ in range(links):
    i, j = map(int, input().split(" "))
    table[i][j] = 1
    table[j][i] = 1

visited = []


def dfs(target, visited):
    if target in visited:
        return 1

    visited.append(target)

    for i in range(len(table[target])):
        if table[target][i] == 1:
            dfs(i, visited)


dfs(start, visited)
print(" ".join(map(str, visited)))

visited=[]
queue=[]
queue.append(start)

while(len(queue) != 0):
    target=queue.pop(0)
    if target in visited:
        continue

    visited.append(target)

    for i in range(len(table[target])):
        if table[target][i] == 1:
            queue.append(i)

print(" ".join(map(str, visited)))