T = int(input())

A = {"A":10, "B":11, "C":12, "D":13, "E":14, "F": 15}

for tc in range(1,T+1):
    N = int(input())
    char = input().strip()

    # 구해야하는 합
    result = 0

    for i in range(len(char)):
        if char[i] in A:
            result += A[char[i]]
        else:
            result += int(char[i])

    print(f"#{tc} {result}")

