T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = list(map(int,input().split()))
    # 포탈 횟수
    total = 0
    # 현재 위치
    idx= 0
    # 방문 체크
    visited = [0]*(N-1)

    # 마지막 방까지 반복
    while idx < N-1:
        total += 1

        if idx == 0:
            idx = 1
        # 방문한적없으면
        elif visited == 0:
            # 방문체크해주고
            visited = 1
            # 방이동
            idx = room[idx] - 1
        else:
            # 방문한적 있으면
            # 한칸 +1 방으로 이동
            idx += 1
    print(f"#{tc} {total}")