import csv

import matplotlib as mpl  # 기본 설정 만지는 용도
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 적용
# https://programmers.co.kr/learn/courses/21/lessons/950
nanum_font_list = [(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]

if len(nanum_font_list) > 0:
    plt.rcParams["font.family"] = nanum_font_list[0][0]
else:
    plt.rcParams["font.family"] = "Gulim"


# http://localdata.kr/devcenter/dataDown.do?menuNo=20001

# csv 파일 열기, 'r' 읽기 모드, 인코딩 방식은 utf-8
f = open('03_13_02_P.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(f)

tm_list = []

x_max = 0
y_max = 0

for data in csv_reader:
    # 영업상태구분코드가 01(영업중)이 아니면 패스
    if data[7] != '01':
        continue

    # 첫줄 컬럼이거나, 좌표 정보가 없을 경우 제외
    if data[26] in ['좌표정보(X)', '']:
        continue

    # 좌표 데이터 이상으로 ']' 가 입력 된경우 제거
    # 197428.923002637, 452041.177877529
    # 중부 TM 좌표
    data[27] = data[27].replace(']', '')

    # 기준점을 0으로 맞추고, 단위를 줄임
    data[26] = (round(float(data[26])) - 132878) // 5000
    data[27] = (round(float(data[27])) + 27615) // 5000

    # 좌표계 추가
    tm_list.append([data[26], data[27]])

    # 최대값 찾아서 넣기
    if x_max < data[26]:
        x_max = data[26]
    if y_max < data[27]:
        y_max = data[27]

# 지역별 상영관 수 저장하기
tm = []
for _ in range(y_max + 1):
    tmp = [0] * (x_max + 1)
    tm.append(tmp)

for x, y in tm_list:
    tm[y_max - y][x] += 5

# 그래프에서 마이너스 폰트 깨질 경우 대비
mpl.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(7.5, 14), dpi=300)
plt.imshow(tm, cmap='coolwarm', interpolation='nearest')
plt.title('전국 상영관 위치')
plt.axis('off')
plt.show()

# 열었던 파일 제거
f.close()
