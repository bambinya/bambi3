T = int(input())
 
for tc in range(1,T+1):
    # N : 돌의 수 M : 뒤집기 횟수
    N, M = map(int, input().split())
    # 돌의 상태
    stone = list(map(int,input().split()))
    # M개의 줄에 걸쳐 i,j가 주어진다
    for _ in range(M):
        i, j = map(int, input().split())
 
        for d in range(1, j+1):
            if 0 <= i-1-d and i-1+d < N:
                # stone[i-1-d] : 왼 stone[i-1+d]: 오
                # 왼,오가 같다면
                if stone[i-1-d] == stone[i-1+d]:
                    # 양쪽이 같으면 뒤집음
                    # 흰색이 0, 검정이 1이면 1에서 빼면 뒤집어짐
                    stone[i-1-d] = 1 - stone[i-1-d]
                    stone[i-1+d] = 1 - stone[i-1+d]
    print(f"#{tc}", *stone)
 
# 계속 if 0 <= i-1-d and i-1+d < N: 이부분을 빼먹어서
# 범위를 빼먹어서 runtime 에러가 계속뜸