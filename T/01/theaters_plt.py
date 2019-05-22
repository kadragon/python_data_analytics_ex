import csv

# 그래프를 그리는데 필요한 matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt

# http://localdata.kr/devcenter/dataDown.do?menuNo=20001

# csv 파일 열기, 'r' 읽기 모드, 인코딩 방식은 utf-8
f = open('03_13_02_P.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(f)

# dictionary 선언, 사전형
theater_cnt = {}

# 한줄씩 읽어서 처리해보자.
for line in csv_reader:
    # 영업상태구분코드가 01(영업중)이 아니면 패스
    if line[7] != '01':
        continue

    # 주소에서 첫번째만 분리하기
    # 제주특별자치도 서귀포시 월드컵로 31 (법환동)
    place = line[18].split()[0]

    # dictionary 사전에 정의 되어 있으면 1 증가
    # 아니면, 사전에 정의
    if place in theater_cnt:
        theater_cnt[place] += 1
    else:
        theater_cnt[place] = 1

# 한글 폰트 적용
plt.rcParams["font.family"] = 'NanumBarunGothic'

# 그래프를 그리기 위한 데이터 수집용 리스트
x_title = []  # 지역명 저장
y_value = []  # 데이터 저장

# 데이터 수집하기
for key in list(theater_cnt.keys()):
    # x 축은 도별 이름을 다 적으면 너무 기니까 2글자만 수집
    x_title.append(key[0:2])
    y_value.append(theater_cnt[key])

# 막대 그래프 그리기
plt.bar(x_title, y_value, width=0.5)
plt.legend()
plt.show()
