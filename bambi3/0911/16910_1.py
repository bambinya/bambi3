T = int(input())
# 테스트케이스
for tc in range(1, T+1):
    # 반지름 N
    N = int(input())
    # 원안에 포함되는 격자점의 개수
    count = 0
    # x축 좌표 -N~N까지
    for x in range(-N, N+1):
        # y축 좦 -N~N까지
        for y in range(-N, N+1):
            # x^2 + y^2 <= N^2 라면
            if x**2 + y**2 <= N**2:
                count += 1
    print(f"#{tc} {count}")
