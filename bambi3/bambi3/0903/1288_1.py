T = int(input())
# 테스트케이스
for tc in range(1, T+1):
    
    N = int(input())

    sheep = [] # 양을 세면서 본 숫자를 저장할 리스트

    #첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다
    k = 0 

    while True:
        k += 1

        sheep_num = N * k # 지금 세고있는 양 번호

        # sheep_num을 밑에서 쓰면 끝자리 번호를 구할때 k번째 양 번호가 사라지므로
        # 자리수를 확인할 때 쓸 임시 변수가 필요
        # 이 부분에서 틀렸음
        num = sheep_num

        # 각각 자리수를 뽑기 위해 반복
        while num > 0:
            # 일의자리까지 구해서 넣었던건지 확인하기
            # 10으로 나눈 나머지가 일의 자리와 같음
            num_i = num % 10
            # sheep에 없는 숫자면 sheep에 append
            if num_i not in sheep:
                sheep.append(num_i)
            #일의자리 빼고 다시 반복
            num //= 10
        # 0~9까지 다 모였으면 break
        if len(sheep) == 10:
            break
    # 출력이 잘못되어서 코드가 잘못된줄 알았는데
    # 문제에서 출력에 '몇 번' 양이 k가 아니라 양의 번호를 출력하는것이여서 계속 오류가 떴었음...
    # print(f"#{tc} {k}")
    print(f"#{tc} {k*N}")