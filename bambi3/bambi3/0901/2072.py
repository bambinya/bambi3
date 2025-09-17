T = int(input())

# 테스트 케이스
for tc in range(1, T+1):

    number = list(map(int, input().split()))

    # 홀수의 합 초기화
    total = 0

    # 리스트에서 하나씩 꺼내서 홀수 확인
    for i in number:
        # 홀수인지 확인 
        if i % 2 == 1:
            # 홀수라면 total에 i 더함
            total += i

    print(f"#{tc} {total}")