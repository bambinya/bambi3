T = int(input())

di = [-1,1,0,0]
dj = [0,0,-1,1]

for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    max_count = 0

    # NxN 격자
    for i in range(N):
        for j in range(N):
            # 현재위치 시작위치 초기화
            ci, cj = i, j
            cnt = 0

            while True:
                cnt += 1
                min_num = 100000000
                # 다음위치, 정해지지 않았으니까 None
                next = None

                # 4방향탐색
                for d in range(4):
                    ni = ci + di[d]
                    nj = cj + dj[d]
                    # 범위 안이면
                    if 0 <= ni < N and 0 <= nj < N:
                        # 현재위치보다 더 작으면
                        if matrix[ni][nj] < matrix[ci][cj]:
                            # 최소값보다 더 작으면
                            if matrix[ni][nj] < min_num:
                                min_num = matrix[ni][nj]
                                next = (ni,nj)
                # 이동가능한 칸이 없다면 종료
                if next is None:
                    break
                else:
                    ci, cj = next

            max_count = max(max_count, cnt)
    print(f"#{tc} {max_count}")