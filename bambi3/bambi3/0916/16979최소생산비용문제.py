T = int(input())


# idx : 공장번호
# selected : 선택한 제품 번호목록
# now_cost : 현재까지 비용 합
def perm(idx, selected, now_cost):
    global min_cost # 전역함수

    # 가지치기
    # 현재비용이 최소비용보다 크면 
    if now_cost >= min_cost:
        return

    # 종료 조건
    # 모든 공장에서 선택했으면
    if idx == N:
        # 최소 생산 비용
        min_cost = min(now_cost, min_cost)
        return

    # 재귀 호출
    # idx번 공장에서 제품 j 선택
    for j in range(N):
        # 이미 선택한 제품이 아니라면
        if j not in selected:
            selected.append(j)
            # j번 제품을 idx번 공장에서 생산했으니 비용 추가
            new_cost = now_cost + cost[j][idx]
            # 다음공장으로 감 idx+1, 생산한제품번호목록, 지금까지 생산비용
            perm(idx + 1, selected, new_cost)
            # 백트래킹 선택 생산 취소
            selected.pop()


for tc in range(1, T + 1):
    # 제품 / 공장 개수
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 100000000

    # 첫번째 공장부터, 아직 제품선택안한 상태, 지금까지 비용0부터
    perm(0, [], 0)

    print(f"#{tc} {min_cost}")