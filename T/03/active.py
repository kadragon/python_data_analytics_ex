import csv
# 오늘 날짜를 구하기 위한 코드
from datetime import datetime

f = open('actor.csv', 'r', encoding='euc-kr')
csv_reader = csv.reader(f)


# 형식을 지정하여 오늘 날짜 구하기
# today = datetime.today().strftime("%Y-%m-%d")
# print(today)

# 년도와 월별 통계 구하기 오늘 날짜
today_year = datetime.today().year
today_month = datetime.today().month

# act_cnt = {}

# 첫행을 출력하기 위해서 사용하는 변수
i = 0

for line in csv_reader:
    # 첫줄 출력하기 그 이후에는 출력하지 않음
    # 첫줄에 각 분류가 어떻게 데이터가 들어가 있는지 헤더값이 적혀 있음
    if i < 2:
        print(line)
        i += 1
    else:
        # 올해 이번달 이후에 진행되는 모든 행사를 출력
        year, month, day = line[3].split('-')
        if int(year) * 100 + int(month) >= today_year * 100 + today_month:
            print("[%s] [%s] %s | %s"
                  % (line[3], line[1], line[0], line[20]))
            #
            # if line[20] != '':
            #     place = line[20].split()[0]
            #
            #     if place in act_cnt:
            #         act_cnt[place] += 1
            #     else:
            #         act_cnt[place] = 1

# for key in list(act_cnt.keys()):
#     print(key, act_cnt[key])
