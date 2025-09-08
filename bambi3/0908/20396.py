T = int(input())
 
for tc in range(1, T+1):
    # N : 돌의 개수
    # M : 뒤집는횟수
    N, M = map(int, input().split())
    # 돌 상태
    stone = list(map(int, input().split()))
    # m개의 줄에 걸쳐
    for _ in range(M):
        # i,j 입력
        i, j = map(int, input().split())
 
        # i 번째부터 j개의 돌
        # 1 <= i
        # i부터 i+j 까지
        # 0부터니까 i-1 , i+j-1 해야함
        # runtime error
        for d in range(i-1, i+j-1):
            if d < N:
                stone[d] = stone[i-1]
            else:
                break
    print(f"#{tc}", *stone)