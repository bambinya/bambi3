T =int(input())

for tc in range(1,T+1):
    # D: 전면부 사이 거리
    # A: 기차A속력
    # B: 기차 B 속력
    # F: 파리의 속력
    D, A, B, F = map(int, input().split())

    # 거리 = 시간*속력
    result = F * (D / (A+B))

    print(f"#{tc} {result}")