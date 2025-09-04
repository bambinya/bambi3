# Ai, Bj 까지만 만들고 못풀어서 gpt

T = int(input()) 
# 테스트 케이스
for tc in range(1, T+1):
    # N,M : 숫자 수
    N, M = map(int, input().split())
    # Ai, Bj
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # Ai가 항상 더 짧거나 같도록 해야함
    # 범위 M-N+1이 음수가 되면 안됨
    if N > M:
        Ai, Bj = Bj, Ai 
        N, M = M, N

    # 최대 합 초기화
    max_sum = 0

    # Ai가 Bj에 겹치는 구간
    for i in range(M - N + 1):
        sum = 0

        # 겹치는 구간 곱 합 계산
        for j in range(N):  # j: Ai의 인덱스
            sum += Ai[j] * Bj[i + j]  # Ai[j]와 Bj[i+j] 곱해서 sum에 더함

        # 현재 합이 최대합보다 크면 바꿈
        if sum > max_sum:
            max_sum = sum

    print(f"#{tc} {max_sum}")