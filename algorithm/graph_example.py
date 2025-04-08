import algorithm
from collections import deque

"""
그래프 알고리즘 예제 코드
"""
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

@algorithm.helper.time_logger
def dfs(graph, node, visited):
    # 깊이 우선 탐색 (DFS)
    # 스택 or 재귀
    # 한번 길을 정하면 계속 파고듦
    # 방문 순서가 직관적이지 않을 수 있다.
    if node not in visited: # 방문하지 않은 노드일때만
        print(node, end=' ')
        visited.add(node) # 방문 기록에 추가
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

@algorithm.helper.time_logger
def bfs(graph, start):
    # → A 꺼냄, B, C 추가 → queue = [B, C]
    # → B 꺼냄, D, E 추가 → queue = [C, D, E]
    # → C 꺼냄, F 추가   → queue = [D, E, F]
    # → D 꺼냄 → 끝
    # → E 꺼냄, G 추가   → queue = [F, G]
    # → F 꺼냄 → 끝
    # → G 꺼냄 → 끝
    # bfs는 선입선출이 핵심이라서 큐를 사용
    visited = set() # set은 빠른 조회 O(n)
    queue = deque([start]) # 맨 처음에 start 넣고 시작

    while queue: # 큐가 비어있지 않을때까지 반복
        node = queue.popleft() # 맨 앞 큐 꺼내고,
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node]) # 인접 노드들을 큐에 추가

if __name__=="__main__":
    dfs(graph, 'A', set())
    bfs(graph, 'A')
