def quicksort(A, l, r):
    if l < r:
        # 기준 원소를 정함
        p = partition(A, l, r)
        # 기준 원소 왼쪽 부분 정렬
        quicksort(A, l, p - 1)
        # 기준 원소 오른쪽 부분 정렬
        quicksort(A, p + 1, r)
 
def partition(A, l, r):
    p = A[l]  # 기준 원소
    # 앞, 뒤에서부터 찾기위한 인덱스
    i, j = l, r
 
    # i, j가 교차하기 전까지
    while i <= j:
        # i반 인덱스에 있는 원소가 p보다 작으면 자기자리
        # +1씩 하면서 다음 찾기
        while i <= j and A[i] <= p:
            i += 1
        # j번 인덱스에 있는 원소가 p보다 크면 자기자리
        # -1씩 하면서 다음 찾기
        while i <= j and A[j] >= p:
            j -= 1
        # i가 j보다 작으면 p보다 큰게 i에있고 작은게 j에있음
        # 서로 바꾸기
        if i < j:
            A[i], A[j] = A[j], A[i]
 
    # 기준 원소를 가운데로 이동
    A[l], A[j] = A[j], A[l]
    return j
 
# 메인 프로그램
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
 
    quicksort(A, 0, N-1)
 
    print(f"#{tc} {A[N//2]}")