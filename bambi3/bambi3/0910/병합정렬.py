def merge(left, right):
    # 전역변수 count
    global count
    # 왼쪽 마지막원소가 오른쪽 마지막 원소보다 크다면
    # count 1증가
    if left[-1] > right[-1]:
        count += 1
    # 두 리스트를 병합한 결과를 넣을 리스트
    result = [0] * (len(left) + len(right))
    l = r = 0
    # 비교할 대상이 있을때까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1
    # 왼쪽 리스트에 남은걸 result에 넣음
    while l < len(left):
        result[l+r] = left[l]
        l += 1
    # 오른쪽 리스트에 남은걸 result에 넣음
    while r < len(right):
        result[l+r] = right[r]
        r += 1
    return result
 
def merge_sort(li):
    if len(li) == 1:
        return li
    # 절반씩 분할
    mid = len(li) // 2
    # 리스트 앞쪽 반
    left = li[:mid]
    # 리스트 뒤쪽 반
    right = li[mid:]
 
    left_list = merge_sort(left)
    right_list = merge_sort(right)
 
    merged_list = merge(left_list, right_list)
    return merged_list
 
 
T = int(input())
for tc in range(1,T+1):
    # N : 정수의 개수
    N = int(input())
    arr = list(map(int,input().split()))
 
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수
    count = 0
 
    sorted_arr = merge_sort(arr)
    print(f"#{tc} {sorted_arr[N//2]} {count}")