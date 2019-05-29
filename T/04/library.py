# pip install openpyxl

import csv

# matplotlib 그래프 그리기 위해서 필요한 것 가져오기
import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# xlsx 를 읽기 위한 코드,
import openpyxl

# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

# 한글 폰트 적용
# https://programmers.co.kr/learn/courses/21/lessons/950
nanum_font_list = [(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]

if len(nanum_font_list) > 0:
    plt.rcParams["font.family"] = nanum_font_list[0][0]
else:
    print("나눔 폰트가 설치되어 있지 않습니다. 한글이 정상적으로 출력되지 않을 수 있습니다.")
    plt.rcParams['font.family'] = 'Gulim'


# 그래프를 그리기 위한 설정
fig = plt.figure()
fig.set_size_inches(10.80 / 3 * 2, 19.20 / 3 * 2)
plt.style.use('seaborn-deep')  # 미리 구성되어 있는 Theme


# subplot 그리기 위한 설정
ax1 = fig.add_subplot(3, 1, 1)  # (3, 1) 크기의 공간에 첫번째 그래프
ax2 = fig.add_subplot(3, 1, 2)  # (3, 1) 크기의 공간에 두번째 그래프
ax3 = fig.add_subplot(3, 1, 3)  # (3, 1) 크기의 공간에 세번째 그래프


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


# 엑셀 파일 열기
wb = openpyxl.load_workbook('전국도서관표준데이터.xlsx')

# sheet 의 이름 목록을 구함
# gsn = wb.sheetnames

# 활성 sheet 선택하기
ws = wb.active

# 장소 카운트 및 장서수 카운트를 위한 값
place_cnt = {}
book_cnt = {}


# 라인을 한바퀴씩 돌면서 값 찾기
for r in ws.rows:
    # r[1] 에 시도명 | r[12] - 장서수, r[13] - 연속간행물, r[14] - 비도서
    if r[1].value == '시도명':
        continue

    # 지역명 정리하기
    place = region_name_short(r[1].value)

    # 장서수 계산하기
    if place in place_cnt:
        place_cnt[place] += 1
        book_cnt[place] += (int(r[12].value))  # + int(r[13].value) + int(r[14].value))
    else:
        place_cnt[place] = 1
        book_cnt[place] = (int(r[12].value))  # + int(r[13].value) + int(r[14].value))


# 지역 정렬
place_list = sorted(list(place_cnt.keys()))

# 첫번째 그래프에 넣을 x, y 값 저장할 List
x_value = place_list
y_value = []

for key in x_value:
    y_value.append(place_cnt[key])

# 막대 그래프 그리기 (도서관)
ax1.bar(x_value, y_value, width=0.7)
ax1.title.set_text('전국 도서관 수')
ax1.set_ylabel('도서관 수')


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
y_conv_data = []
book_conv_data = []

# 데이터 수집하기
for key in x_value:
    y_conv_data.append(etc_count[key] / place_cnt[key])
    book_conv_data.append(book_cnt[key] / etc_count[key] * 10000)

# 막대 그래프 그리기 (인구수)
ax2.bar(x_value, y_conv_data, width=0.7)
ax2.title.set_text('도서관 1개당 인구수')
ax2.set_ylabel('인구수 (2017)')


# 막대 그래프 그리기 (장서)
ax3.bar(x_value, book_conv_data, width=0.7)
ax3.title.set_text('인구 만명당 장서 수')
ax3.set_ylabel('장서수 (도서)')

plt.show()
