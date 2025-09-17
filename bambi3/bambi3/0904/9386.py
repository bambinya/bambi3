T = int(input())

for tc in range(1,T+1):
    N = int(input())

    arr = input()
    # 1의 개수를 셀 변수
    count = 0
    # 연속한 1의 개수 최대값
    max_count = 0

    # arr 순회해서 1을 찾기
    for i in arr:
        # "1"이라면
        if i == "1":
            # count 를 1증가시킴
            count += 1

            if count > max_count:
                max_count = count

        # "0" 이라면 count 를 0으로 초기화
        else:
            count = 0

    print(f"#{tc} {max_count}")