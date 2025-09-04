# 변수 초기화 까지만 작성하고 답을 참고하였음

T = int(input())

for tc in range(1,T+1):
    # 농장크기 N*N
    N = int(input())
    # 농장
    matrix = [list(map(int, input())) for _ in range(N)]

    # 수익
    money = 0

################################################################

    # d는 중앙에서 농장 끝까지의 거리
    # N은 항상 홀수
    d = N // 2

    # 농장 중앙의 좌표 
    center = (d,d)

    for r in range(N):        # 행
        for c in range(N):    # 열
            # 중앙에서 세로로 떨어진거리와 가로로 떨어진 거리 합이 d 보다작거나 같다면 마름모 안쪽
            if abs(r-d) + abs(c-d) <= d:
                # 값을 수익에 넣음
                money += matrix[r][c]
    print(f"#{tc} {money}")