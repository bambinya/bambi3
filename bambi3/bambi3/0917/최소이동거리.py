# 최단거리문제 >> 다익스트라로 풀어보기

import heapq

INF = int(1e9)

T = int(input())

for tc in range(1, T + 1):
    # N : 연결지점 0부터 N번(정점)
    # E : 도로 구간 (간선) 개수
    N, E = map(int, input().split())
    # 정점 번호가 0~N이므로 N+1개임 
    V = N + 1 

    # 인접리스트
    # g[i] = [(i번에서 연결된 지점, 구간 거리(가중치)), ...]
    g = [[] for _ in range(V)]

    for i in range(E):

        # s: 시작 #: 끝 # w: s에서  e가는 구간거리, 가중치
        s, e, w = map(int, input().split())
        # 인접리스트에 넣음
        g[s].append((e, w))

    INF = 1e9

    D = [INF] * V

    # start : 시작정점
    def dijkstra(start):
        # 항상 가중치 작은 정점을 꺼내기 가능함
        heap = []
        heapq.heappush(heap, (0, start))

        D[start] = 0

        while heap:
            # (최소가중치, 정점번호) 꺼냄
            # 최소 거리를 꺼냄
            w, v = heapq.heappop(heap)

            # 꺼낸 거리가 더 크면 더 이어갈 필요가없음
            if w > D[v]:
                continue

            # nv : v와 인접한 정점번호, nw : 그때 거리(가중치)
            for nv, nw in g[v]:
                # nv로 가는 새로운 거리 = v까지 최단거리 + v~nv까지 거리
                new_distance = w + nw
                # 새 거리가 이전 계산한 거리보다 작다면 힙에 추가
                if new_distance < D[nv]:
                    D[nv] = new_distance
                    heapq.heappush(heap, (new_distance, nv))

    dijkstra(0)
    print(f"#{tc} {D[N]}")