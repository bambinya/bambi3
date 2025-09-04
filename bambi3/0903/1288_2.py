# 정답 참고

T = int(input())
# 테스트케이스
for tc in range(1, T+1):
    N = int(input())
 
    # 0~9까지 중복이 안되는 set 사용
    nums_set = set()
 
    # 몇번째 배수를 셀지
    i = 1
 
    # 0~9까지 숫자가 다 들어갈때까지 반복함
    while len(nums_set) < 10:
        # N*i 는 양 번호
        # 문자열로 받아서 한글자씩 순회함
        for j in str(N*i):
            nums_set.add(j) # 문자열 순회로 빈 집합에 원소(0~9) 더하기
        # 길이가 10 == 0~9까지 다 들어감
        # 다 들어갔으면 break
        if len(nums_set) == 10:
            break
        # 다음배수확인
        i += 1
 
    print(f"#{tc} {i*N}")