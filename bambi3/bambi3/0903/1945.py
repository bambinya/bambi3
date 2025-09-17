T = int(input())
for tc in range(1,T+1):

    N = int(input())
    # 2,3,5,7,11 지수 저장할 리스트
    numbers = [0, 0, 0, 0, 0]

    # while문으로 반복해서 나머지가 0이 아니면 다음 숫자로 넘어가서 나누기?
    # N 이 1이 되기 전까지 반복
    while N != 1:
        # N을 2로나눈 나머지가 0이면
        if N % 2 == 0:
            numbers[0] += 1
            # 나누기2한 몫
            N //= 2
            # 다시 위로가서 반복
            continue
        # N을 3로나눈 나머지가 0이면
        if N % 3 == 0:
            numbers[1] += 1
            N //= 3
            continue
        # N을 5로나눈 나머지가 0이면
        if N % 5 == 0:
            numbers[2] += 1
            N //= 5
            continue
        # N을 7로나눈 나머지가 0이면
        if N % 7 == 0:
            numbers[3] += 1
            N //= 7
            continue
        # N을 11로나눈 나머지가 0이면
        if N % 11 == 0:
            numbers[4] += 1
            N //= 11
            continue
        # 안나누어떨어지면 종료
        break
    print(f"#{tc}", *numbers) #공백으로 출력