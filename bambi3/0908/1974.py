T = int(input())  # 테스트 케이스 개수
 
for tc in range(1, T + 1):
    # 9x9 퍼즐
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    # 겹치는 숫자 없을경우 1을 정답으로, 아니면 0
    result = 1 
 
    #  행 
    for i in range(9):
        check = [0] * 9
        for j in range(9):
            num = puzzle[i][j]
            # 이미 있는 숫자면 result 0
            if check[num-1] == 1:
                result = 0
            check[num-1] = 1
 
    #  열 
    for j in range(9):
        check = [0] * 9
        for i in range(9):
            num = puzzle[i][j]
            if check[num-1] == 1:
                result = 0
            check[num-1] = 1
 
    # 3X3 격자
    for i in range(0, 9, 3):       # 시작 행: 0, 3, 6
        for j in range(0, 9, 3):   # 시작 열: 0, 3, 6
            check = [0] * 9
            # 3x3 순회
            for x in range(3):
                for y in range(3):
                    num = puzzle[i+x][j+y]
                    # 중복확인 이미 있는 숫자면
                    if check[num-1] == 1:
                        result = 0
                    check[num-1] = 1
 
    print(f"#{tc} {result}")
 
    # 푸는 방법은 생각했지만 코드로 구현하는데 어려움을 겪어 정답을 참고했습니다