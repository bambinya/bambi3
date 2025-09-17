T = int(input())
for tc in range(1,T+1):
 
    N = int(input())
 
    A = list(map(int, input().split()))
 
    # 최댓값
    # 단조 증가하는 수가 없다면 -1을 출력
    max_num = -1
 
    for i in range(N):
        # 0부터 시작하면 중복이 될수도있음
        # i < j 이므로
        for j in range(i+1, N):
            # 두 수 곱 , 문제에서 Ai x Aj
            mul_num = A[i] * A[j]
            # 굡을 문자열로 변환
            s = str(mul_num)
 
            for d in range(1, len(s)):
                # 뒤에 숫자가 더 작으면 단조 증가 아님 break
                if s[d] < s[d-1]:
                    break
            else:
                # mul_num가 단조 증가면 최대값 비교
                if mul_num > max_num:
                    max_num = mul_num
    print(f"#{tc} {max_num}")
 
    # max_num = 0 으로 초기화를 하여 테스트케이스가 41개 맞음
    # 증가하는 수가 없다면 -1을 출력해야함
    # max_num = -1 로바꿈
    # 두 수를 탐색할때 for i in range(N) , for j in range(N) 둘다 
    # 범위를 N으로 하여 오류가 발생했음 . gpt.의 도움을 받음