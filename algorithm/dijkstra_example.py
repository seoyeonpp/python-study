import algorithm
import heapq



@algorithm.helper.time_logger
def dijkstra(graph, start):
    # 시간복잡도 O((V + E) log V)
    # 모든 노드의 거리를 무한대로 초기화, 아직 도달하지 못했다는 의미 (도달하지 않은 노드는 무한히 멀다고 가정하기 때문. 0으로 초기화한다면 알고리즘이 거리 갱신을 안함! )
    # float('inf') 는 양의 무한대 (다익스트라, 플로이드, DP등에서 최댓값 초기화 용도로 사용)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0 # 시작 노드의 거리는 0

    print("초기 거리:", distances)

    # 우선순위 큐에 (거리, 노드) 형태로 저장
    # 우선순위 큐를 초기화: (현재까지의 거리, 노드) 형태
    # 시작 노드를 거리 0으로 큐에 넣음
    queue = [(0,start)]

    while queue: # 큐가 빌때까지 (모든 노드를 확인할때까지)
        current_distance, current_node = heapq.heappop(queue) # 가장 짧은 거리의 노드를 꺼냄 / heapq 덕분에 자동으로 가장 가까운 노드가 먼저 나옴.
        print("현재 노드:", current_node, "현재 거리:", current_distance)
        # 이미 더 짧은 거리로 처리된 적 있으면 무시
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]: # 현재 노드에 연결된 모든 이웃 노드(neighbor)와 간선 가중치(weight) 탐색
            distance = current_distance + weight # 현재 노드를 거쳐서 이웃 노드로 가는 새 distance 계산

            if distance < distances[neighbor]: # 이웃 노드까지 더 짧은 거리를 찾았다면
                distances[neighbor] = distance # 최단 거리 정보 업데이트
                heapq.heappush(queue, (distance, neighbor)) # 갱신된 이웃 노드를 우선순위 큐에 다시 넣음, 다음에 이 노드에서 또 이웃 탐색

    return distances # 모든 노드까지의 최단 거리를 딕셔너리로 반환


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

if __name__ == "__main__":
    start_node = 'A'
    result = dijkstra(graph, start_node)
    print(result)