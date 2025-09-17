T = int(input())

A = {"A":10, "B":11, "C":12, "D":13, "E":14, "F": 15}

for tc in range(1,T+1):
    N = int(input())
    char = input().strip()

    result = 0

    for ch in char:
        if ch in A:
            result += A[ch]

        else:
            result += int(ch)

    print(f"#{tc} {result}")