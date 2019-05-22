import csv

# https://www.data.go.kr/dataset/3045278/fileData.do

# 데이터를 저장할 공간을 만들어 두기~
data = [0] * (2018 - 1987 + 1)

for year in [1987, 1990, 2000, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]:
    # csv 파일 1개씩 열기 | 'r' = read | encording utf-8 방식
    f = open('./서울시_미세먼지/일별평균대기오염도_' + str(year) + '.csv', 'r', encoding='utf-8')

    # csv 파일 열기
    # csv 파일이란? (comma-separated values)
    # 1, 2, 3, 4, 5 ',' 로 구분되어 있는 것

    # 측정일시, 측정소명, 이산화질소농도(ppm), 오존농도(ppm), 이산화탄소농도(ppm), 아황산가스(ppm), 미세먼지(㎍ / ㎥), 초미세먼지(㎍ / ㎥)
    # 20130101, 강남구, 0.04, 0.007, 0.5, 0.006, 38,
    csv_reader = csv.reader(f)

    for i in csv_reader:
        # 일자가 기록된게 아니라면 통계에서 제외
        if len(i[0]) != 8:
            continue

        # ex) i[0] 에 저장되어 있는 20130101 을 편집
        # i[0][0:4] > 2013
        # 연도 최초 데이터가 1987년도, 따라서 0으로 편집 (배열의 시작은 0)
        target = int(i[0][0:4]) - 1987

        # 월별로 데이터를 수집하기 위해서 내부 배열 선언
        if data[target] == 0:
            data[target] = [[0] * 13, [0] * 13]

        month = int(i[0][4:6])

        # 미세먼지 데이터가 있을때, 이를 각 달별로 저장하고 평균내기 위한 카운트 증가
        if i[6] != '':
            data[target][0][month] += int(i[6])
            data[target][1][month] += 1

    # 연 파일 닫기
    f.close()

# 최대값, 최소값 구하기 위한 값 찾기
max_pm = 0
max_date = ''
min_pm = 9999
min_date = ''

# 년도별, 월별 통계치를 이용해서 찾기
for year in range(1995 - 1987, 2019 - 1987):
    for month in range(1, 13):
        # 평균치 계산하기
        avg_pm = data[year][0][month] / data[year][1][month]

        # 최대치 찾기
        if max_pm < avg_pm:
            max_pm = avg_pm
            max_date = "%04d-%02d" % (year + 1987, month)

        # 최소치 찾기
        if min_pm > avg_pm:
            min_pm = avg_pm
            min_date = "%04d-%02d" % (year + 1987, month)

        # 매달 평균 데이터 출력하기
        # print("%04d-%02d: %4.2f" % (year+1987, month, avg_pm))

print("[MAX PM10] %s - %3.2f" % (max_date, max_pm))
print("[MIN PM10] %s - %3.2f" % (min_date, min_pm))
