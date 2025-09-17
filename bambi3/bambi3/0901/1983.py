for tc in range(1, T+1):
    
    # N : 학생 수 K : 알고 싶은 학생 번호
    N, K = map(int, input().split())

    # 평점
    grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    # 리스트에 총점수랑 학생번호를 넣고 순회해서 K번호를 찾으면 되지않나  

    # 평점에 있는 학생수
    students = N // 10

    # 총점,학생번호를 저장할 리스트
    score = []

    # 입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어진다
    # 학생수 N명만큼
    for student in range(N):
        # 중간, 기말, 과제 한줄로 입력
        middle, final, task = map(int, input().split())
        total_score = (middle * 0.35) + (final*0.45) + (task*0.2)
        # (총점, 학생번호) 튜플로 넣음
        score.append((total_score, student))

    # 높은>낮은 점수로 내림차순
    # reverse=True 를 쓰지않아 계속 오름차순이 되었음
    score.sort(reverse=True)

    for idx in range(N):
        # 학생 번호가 K면
        if score[idx][1] == K-1: # 인덱스는 0부터 시작이니까 -1    [idx][1] : 학생번호
            # 찾은 학생 평점 어딘지 계산
            score_idx = idx // students  
            print((f"#{tc} {grades[score_idx]}"))