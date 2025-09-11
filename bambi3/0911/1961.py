# 90도 회전시키는 함수
def rotate(arr):
    # N*N 배열
    arrx = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 행 아래에서 위로 뒤집고 i열에 넣음
            arrx[i][j] = arr[N-1-j][i]

    return arrx

T = int(input())
# 테스트케이스
for tc in range(1,T+1):
    N = int(input())
    # N*N 배열
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 90도돌림
    arr90 = rotate(arr)
    # 90도에서 90도 돌림
    arr180 = rotate(arr90)
    # 180도에서 90도 돌림
    arr270 = rotate(arr180)

    print(f"#{tc}")

    for i in range(N):
        # 돌린 행을 문자열로 변환
        # 문자열로 바꾸고 join 해서 'xxx'로 바꿈
        a = ''.join(map(str, arr90[i]))
        b = ''.join(map(str, arr180[i]))
        c = ''.join(map(str, arr270[i]))

        # 한 줄에 공백으로 구분하여 출력
        print(f"{a} {b} {c}")