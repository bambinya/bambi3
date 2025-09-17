T = int(input())
# 테스트케이스
for tc in range(1, T+1):
    # 반지름 N
    N = int(input())
    # 원안에 포함되는 격자점의 개수
    count = 0
    
    # 사분면중 하나에서 값들 구해서 곱하기
    for x in range(0,N+1):
        for y in range(0,N+1):
            # x^2 + y^2 <= N^2 라면
            if x**2 + y**2 <= N**2:
                # (0,0) 이면 count 1증가
                if x == 0 and y == 0:
                    count += 1
                # (0,y) (x,0) 축에 위치하면 2배
                elif x == 0 or y == 0:
                    count += 2
                # 나머지는 4배
                else:
                    count += 4
    print(f"#{tc} {count}")