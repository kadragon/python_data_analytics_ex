import csv

# http://localdata.kr/devcenter/dataDown.do?menuNo=20001

# csv 파일 열기, 'r' 읽기 모드, 인코딩 방식은 utf-8
f = open('03_13_02_P.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(f)

# dictionary 선언, 사전형
theater_cnt = {}
cnt = 0

# 한줄씩 읽어서 처리해보자.
for line in csv_reader:
    # 영업상태구분코드가 01(영업중)이 아니면 패스
    if line[7] != '01':
        continue

    # 메가박스중앙(주) 동대문점 8관
    theater_name = line[21][0:4]  # 메가박스

    # 주소에서 첫번째만 분리하기
    # 제주특별자치도 서귀포시 월드컵로 31 (법환동)
    place = line[18].split()[0]

    # dictionary 사전에 정의 되어 있으면 1 증가
    # 아니면, 사전에 정의
    if place in theater_cnt:
        theater_cnt[place] += 1
    else:
        theater_cnt[place] = 1

# .keys()는 내부에 선언되어 있는 값 반환.
for key in list(theater_cnt.keys()):
    print(key, theater_cnt[key])

f.close()
