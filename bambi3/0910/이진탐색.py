def binary_search(A, target):
    left = 0 
    right = len(A) - 1
    # 방향 0: 없음, -1: 왼쪽, 1: 오른쪽
    last = 0
    # while문부터 진행이 되지않아 정답을 참고하였습니다.
    while left <= right:
        # 인덱스 중간
        mid = (left + right) // 2
        # 중간값과 target이 같으면 조건o 
        if A[mid] == target:
            return 1  # 조건 만족
        # target이 중간값보다 작으면 왼쪽 찾음
        if target < A[mid]:
            # 이전 방향이 왼쪽이라면 왼쪽-오른쪽 아니여서 조건x 
            if last == -1:
                return 0         
            last = -1
            right = mid - 1
        else:
            # target이 중간값보다 크면 오른쪽 찾음
            # 이전 방향이 오른쪽이면 왼쪽-오른쪽 아니여서 조건x
            if last == 1:
                return 0           # 조건 불만족
            last = 1
            left = mid + 1
 
    return 0
 
T = int(input())  # 테스트 케이스 수
 
for tc in range(1, T + 1):
    # N : A 리스트 길이
    # M : B 리스트 길이
    N, M = map(int, input().split())
    A = list(map(int, input().split()))                
    B = list(map(int, input().split()))
    # 정렬
    A.sort()
 
    #  양쪽구간을 번갈아 선택하게 되는 숫자의 개수
    cnt = 0
    for i in B:
        cnt += binary_search(A, i)
 
    print(f"#{tc} {cnt}")
