# 전국 주민등록 인구 및 세대 현황
# http://27.101.213.4/

# 전국도서관표준데이터
# https://www.data.go.kr/dataset/15013109/standard.do

# xlsx 를 읽기 위한 코드
import openpyxl

# 엑셀 파일 열기
wb = openpyxl.load_workbook('전국도서관표준데이터.xlsx')

# 활성 sheet 선택하기
ws = wb.active

i = 0
lib_cnt = {}

for row in ws.rows:
    # 어떤 정보가 들어 있는지 확인하기 위한 코드
    if i == 0:
        # print(', '.join(row))
        for k in row:
            print(k.value, end=',')

        print()  # 줄바꿈 한번 하기
        i += 1
        continue

    place = row[1].value

    if place in lib_cnt:
        lib_cnt[place] += 1
    else:
        lib_cnt[place] = 1

for key in sorted( list( lib_cnt.keys() )):
    print(key, lib_cnt[key])


