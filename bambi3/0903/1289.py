# 정답을 참고하였음
T = int(input())

for tc in range(1, T+1):
    # 문자열str은 불변 리스트는 변경 할수있음
    origin = list(input()) # 원래 메모리 비트

    # 메모리 길이 
    n = len(origin)

    # 바꿀 메모리, 모두 0으로 초기화함
    mem = ["0"] * n

    # 원래 상태로 바꿀때 바꾼 비트 개수
    cnt = 0

    # 맨 앞부터 비트를 바꿔 본다 0 또는 1로
    # 0 또는 1로 바꾸면 그 뒤에있는 비트도 똑같이 다 바꿔준다.
    for i in range(n):

        ith_char = origin[i]
        # 원래 값에 i번째랑 지금i번째 다르면 바꿈
        if ith_char != mem[i]:
            # i 번째 비트를 바꿨다?? => i+1 번째 비트부터 n-1 번째 비트까지 다 바꿔줘야한다.
            # 바꿀때마다 cnt 1 증가
            cnt += 1
            # 문제 메모리 bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리의 끝까지 덮어씌운다.
            # i이후도 전부 바꿈
            for j in range(i, n):
                mem[j] = ith_char
        # 비교해서 원래값과 같다면 반복을 멈추고 break
        if mem == origin:
            break
    print(f"#{tc} {cnt}")
