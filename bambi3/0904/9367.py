T = int(input())
for tc in range(1,T+1):
    # N : 당근 개수
    N = int(input())
    # 당
    C = list(map(int, input().split()))

    # 당근의 최대 개수
    carrot_max = 1
    
    count = 1

    for i in range(1,N):
        # 앞에 당근보다 커진다면 count 를 1증가
        if C[i] > C[i-1]:
            count += 1
        # 안커지면 count 1로 다시 초기화
        else:
            count = 1

        if count > carrot_max:
            carrot_max = count
    
    print(f"#{tc} {carrot_max}")

# for i in range(N)으로 했을때 테스트 케이스 10개중 9개만 맞음
# N으로 하면 c[0] > c[-1] 로 첫번째랑 마지막을 비교하게 되므로
# for i in range(1,N) 이 되어야함