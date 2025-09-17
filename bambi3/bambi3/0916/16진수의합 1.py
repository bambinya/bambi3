T = int(input())

for tc in range(1,T+1):
    # N : 숫자 개수
    N = int(input())
    char = input().strip()

    # 합
    result = 0

    # 한글자씩 꺼냄
    for i in range(len(char)):
        # result에 char[i] 10진수로 바꾸고 더함
        result += int(char[i], 16)

    print(f"#{tc} {result}")