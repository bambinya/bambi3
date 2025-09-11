T = int(input())
# 테스트케이스
for tc in range(1, T + 1):

    N, Q = map(int, input().split())
    # 모두 0이 적힌 상자
    box = [0] * N
    # 문제에서 Q개의 줄의 i번째 줄에는 L, R이 주어진다
    for i in range(1, Q+1):
        L, R = map(int, input().split())

        # L번 상자부터 R번 상자까지
        for j in range(L-1, R):
            # 값을 i로 변경
            box[j] = i

    print(f"#{tc}", *box)