# 전국 주민등록 인구 및 세대 현황
# http://27.101.213.4/

# 전국도서관표준데이터
# https://www.data.go.kr/dataset/15013109/standard.do

# xlsx 를 읽기 위한 코드
import openpyxl


# 엑셀 파일 열기
wb = openpyxl.load_workbook('전국도서관표준데이터.xlsx')

# sheet 의 이름 목록을 구함
# gsn = wb.sheetnames

# 활성 sheet 선택하기
ws = wb.active


for row in ws.rows:
    for k in row:
        print(k.value, end=',')

    print()