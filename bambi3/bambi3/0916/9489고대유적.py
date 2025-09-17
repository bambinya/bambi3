T = int(input())
# 테스트케이스
for tc in range(1,T+1):

    N, M = map(int,input().split())
    # N개의줄에 데이터
    data = [list(map(int,input().split())) for _ in range(N)]

    # 구할려는 가장 긴 길이
    max_count = 0

    # 가로
    for i in range(N):
        count = 0
        for j in range(M):
            #i,j에서 1이면 count 1증가
            if data[i][j] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

    # 세로
    for j in range(M):
        count = 0
        for i in range(N):
            if data[i][j] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

    print(f"#{tc} {max_count}")