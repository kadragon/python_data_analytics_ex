import csv

import matplotlib as mpl  # 기본 설정 만지는 용도
import matplotlib.pyplot as plt


# 지역명을 정돈하기 위한 함수
def region_name_short(region):
    region = region.replace('특별', '')
    region = region.replace('자치', '')
    region = region.replace('광역', '')
    region = region.replace('시', '')
    region = region.replace('도', '')
    region = region.replace('청', '')
    region = region.replace('라', '')
    region = region.replace('상', '')
    return region


# http://localdata.kr/devcenter/dataDown.do?menuNo=20001

# csv 파일 열기, 'r' 읽기 모드, 인코딩 방식은 utf-8
f = open('03_13_02_P.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(f)

# 그래프에서 마이너스 폰트 깨질 경우 대비
mpl.rcParams['axes.unicode_minus'] = False

# 한글 폰트 적용
plt.rcParams["font.family"] = 'NanumBarunGothic'

# 두개의 그래프를 그리기 위한 subplot 시작
fig = plt.figure()
fig.set_size_inches(19.20, 10.80)
ax1 = fig.add_subplot(2, 1, 1)  # (2, 1) 크기의 공간에 첫번째 그래프
ax2 = fig.add_subplot(2, 1, 2)  # (2, 1) 크기의 공간에 두번째 그래프

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
    place = region_name_short(place)

    # dictionary 사전에 정의 되어 있으면 1 증가
    # 아니면, 사전에 정의
    if place in theater_cnt:
        theater_cnt[place] += 1
    else:
        theater_cnt[place] = 1

# 그래프를 그리기 위한 데이터 수집용 리스트
x_title = []
y_value = []

for data in sorted(list(theater_cnt.keys())):
    x_title.append(data)
    y_value.append(theater_cnt[data])

# 막대 그래프 그리기
ax1.bar(x_title, y_value, width=0.5)
ax1.title.set_text('전국 영업중 상영관 수')
# ax1.set_xlabel('')
ax1.set_ylabel('상영관수')

# 전국 인구 데이터 2017년도 기준
m = open('M_2017.csv', 'r', encoding='euc-kr')
m_csv = csv.reader(m)

nation_count = 0  # 전국 인구수 저장
etc_count = {}  # 지역별 인구수 저장용 Dictionary

for i in m_csv:
    if i[0] == '전국':
        nation_count = int(i[1])
    if i[0][2:4] == '특별' or i[0][::-1][0:1] == '도' or i[0][2:4] == '광역':
        region = region_name_short(i[0])
        etc_count[region] = int(i[1])

# 그래프를 그리기 위한 데이터 저장용 List 선언
x_conv_title = []
y_conv_data = []

# 데이터 수집하기
for key in sorted(list(etc_count.keys())):
    x_conv_title.append(key)
    y_conv_data.append(etc_count[key] / theater_cnt[key])

ax2.bar(x_conv_title, y_conv_data, width=0.5)
ax2.title.set_text('상영관 1개당 인구수')
ax2.set_ylabel('인구수')

plt.show()

# 열었던 파일 제거
f.close()
m.close()
