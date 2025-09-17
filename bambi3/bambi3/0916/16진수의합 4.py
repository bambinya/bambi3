T = int(input())

for tc in range(1,T+1):
    N = int(input())
    char = input().strip()

    result = 0

    for ch in char:
        result += int(ch,16)

    print(f"#{tc} {result}")