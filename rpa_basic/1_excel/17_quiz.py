# - 출석 10
# - 퀴즈1 10
# - 퀴즈2 10
# - 중간고사 20
# - 기말고사 30
# - 프로젝트 20
# -------------
# - 총합 100

# 1. 퀴즈2 점수를 전부 10으로 수정
# 2. H열에 총점 (SUM 이용), I열에 성적 정보 출력
# - 총점 90 이상 A, 80 이상 B, 70 이상 C, 나머지 D
# 3. 출석이 5 미만인 학생은 총점 상관없이 F
# 4. 최종 파일명 : scores.xlsx

from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(['학번', '출석', '퀴즈1', '퀴즈2', '중간고사', '기말고사', '프로젝트'])

scores = [
(1,10,8,5,14,26,12),
(2,7,3,7,15,24,18),
(3,9,5,8,8,12,4),
(4,7,8,7,17,21,18),
(5,7,8,7,16,25,15),
(6,3,5,8,8,17,0),
(7,4,9,10,16,27,18),
(8,6,6,6,15,19,17),
(9,10,10,9,19,30,19),
(10,9,8,8,20,25,20)
]

for s in scores:
    ws.append(s)

# 1. 퀴즈2 점수를 전부 10으로 수정
for cell in ws['D']:
    if isinstance(cell.value, int): # int형 데이터만
        cell.value = 10

# 2. H열에 총점 (SUM함수 이용), I열에 성적 정보 출력
ws['H1'] = '총점'
ws['I1'] = '성적'

# a, b, c, d, e, f, g, h, i
# 1, 2, 3, 4, 5, 6, 7, 8, 9
for idx, score in enumerate(scores, start=2): # start=2 : idx가 2부터 시작

    # H열에 함수 적용
    ws.cell(row=idx, column=8).value = "=SUM(B{}:G{})".format(idx, idx)
    # =SUM(B2:G2)
    # =SUM(B3:G3) ...

    # I열에 성적 적용
    # - 총점 90 이상 A, 80 이상 B, 70 이상 C, 나머지 D
    # evaluate 가 안되어있기 때문에 수식을 사용하지 않고 따로 총점 값을 만듦
    sum_val = sum(score[1:]) - score[3] + 10 # 총합 - 퀴즈2 + 10 (퀴즈2 점수를 10점으로 값을 구해야 하기 때문에)

    grade = None
    if sum_val >= 90:
        grade = 'A'
    elif sum_val >= 80:
        grade = 'B'
    elif sum_val >= 70:
        grade = 'C'
    else:
        grade = 'D'
    
    # 3. 출석이 5 미만인 학생은 총점 상관없이 F
    if score[1] < 5:
        grade = 'F'
    
    ws.cell(row=idx, column=9).value = grade # I열에 성적 정보

wb.save("scores.xlsx")
