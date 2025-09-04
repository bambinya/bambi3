T = int(input())

for tc in range(1, T+1):
    # K : 한번 충전으로 이동할 수 있는 최대거리
    # N : 종점
    # M : 충전소
    K, N, M = map(int, input().split())
    # 충전소
    charge = list(map(int, input().split()))
    # 현재위치
    current = 0
    # 충전한횟수
    charge_count = 0
    # 충전소까지 한번에 못갈 때 반복
    while current + K < N:
        # 최소한 몇 번 충전해야하는지 구해야하니까
        # 최대한 멀리있는 충전소까지 가서 충전해야함
        # 멀리있는 충전소를 구할려면 최대거리 K에서부터 찾으면됨
        # k에서 -1씩 하면서 충전소있는지 봄
        for i in range(K, 0, -1):
            # 움직였을때 충전소가있으면 이동하고 충전한 횟수를 1증가시킴
            if current + i in charge:
                current += i
                charge_count += 1
                break
        # 충전소가 없으면 ??
        # 들여쓰기 잘못함
        # 왜 charge_count = 0 가 들어갈까
        else:
            # 처음 갔을때 충전한번하고 그 뒤로 충전소가 안나와서 멈출수도 있으니까
            # charge_count 를 0으로 해줘야함
            charge_count = 0
            break
    print(f"#{tc} {charge_count}")