T = int(input())
# 상하좌우 대각선
dx = [-1,-1,-1,0,0,1,1,1]  # 8방향 (행 이동)
dy = [-1,0,1,-1,1,-1,0,1]  # 8방향 (열 이동)

for tc in range(1, T+1):
    # N : 보드의 한 변의 길이
    # M : 돌을 놓는 횟수
    N, M = map(int, input().split())

    # N*N보드판
    matrix = [[0] * N for _ in range(N)]

    # 중앙에 4개 돌을 놓고 시작
    # 1 : 흑돌 2 : 백돌
    C  = N//2
    matrix[C-1][C-1] = 2  # 백돌
    matrix[C][C] = 2      # 백돌
    matrix[C-1][C] = 1    # 흑돌
    matrix[C][C-1] = 1    # 흑돌

    for i in range(M):
        # 행, 열, 색
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        matrix[x][y] = color

        # 8방향 탐색
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            # 뒤집을 다른색 돌 저장할 배열
            stone = []
            # 범위안에 있는 동안 반복
            while 0 <= nx < N and 0 <= ny < N:
                # 돌이없으면 멈춤
                if matrix[nx][ny] == 0:
                    break
                # 같은 돌을 만나면       
                elif matrix[nx][ny] == color:
                    # 지금까지 만난 다른돌 뒤집음
                    for px, py in stone:
                            matrix[px][py] = color
                    break
                else:
                    # 다른 돌이면 나중에 뒤집을수도 있으니까 저장해둠
                    stone.append((nx, ny))

                    # 다음칸으로 
                    nx += dx[d]
                    ny += dy[d]

    # 흑돌, 백돌 개수
    black = 0
    white = 0
    # N*N격자 순회해서 흑돌 백돌 찾음
    for i in range(N):
        for j in range(N):
            # 1이면 흑돌 +1
            if matrix[i][j] == 1:
                black += 1
            # 0이면 백돌 +1
            elif matrix[i][j] == 2:
                white += 1
            
    print(f"#{tc} {black} {white}")
        