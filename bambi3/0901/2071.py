T = int(input())
#테스트 케이스
for tc in range(1, T+1):
    # 수 입력받음
    number = list(map(int, input().split()))
    # 수의 총합 초기화
    total = 0

    for i in number:
        total += i # total에 i를 더함

    # 평균 구하기
    avg = total / 10
    # 반올림 하는 함수 round
    result = round(avg)

    print(f"#{tc} {result}")

# round 함수 몰랐음