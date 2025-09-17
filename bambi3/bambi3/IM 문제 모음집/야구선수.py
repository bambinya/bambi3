T = int(input())

for tc in range(1,T+1):
    # N : 야구선수 인원
    # K : 허용가능한 실력
    N, K = map(int,input().split())
    # 야구선수들의 실력
    score = list(map(int,input().split()))

    max_player = 0

    # 실력 오름차순
    score.sort()

    for i in range(N):
        # 한명은 뽑으니까 1로 초기화
        player = 1
        for j in range(i+1,N):
            if score[j] - score[i] <= K:
                player += 1
            else:
                break
        max_player = max(max_player,player)

    print(f"#{tc} {max_player}")