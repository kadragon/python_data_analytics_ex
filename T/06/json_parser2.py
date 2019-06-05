import urllib.request
import json
from datetime import datetime


# https://www.data.go.kr/dataset/15000496/openapi.do
# https://www.data.go.kr/subMain.jsp?param=T1BFTkFQSUAxNTAwMDQ5Ng==#/L3B1YnIvcG90L215cC9Jcm9zTXlQYWdlL29wZW5EZXZHdWlkZVBhZ2UkQF4wMTJtMSRAXnB1YmxpY0RhdGFQaz0xNTAwMDQ5NiRAXnB1YmxpY0RhdGFEZXRhaWxQaz11ZGRpOjZiNmI2MWUyLWNmNWQtNDk3Zi04ZmQyLWMwYjg0ZWE5NTRjMl8yMDEzMDMwNDEwMDQkQF5vcHJ0aW5TZXFObz0yOTI4JEBebWFpbkZsYWc9dHJ1ZQ==

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


# 오늘 날짜를 8자리로 변환
today = datetime.today().year*10000 + datetime.today().month*100 + datetime.today().day

print(today)


serviceKey = "jjg9PodXGlwYYrfmH0VNL%2BmmUjU4h%2BNp4RxysfJihzOqGGN3mucbkB96AAFh0bUkAldnsSv6fWJXBarx8n9otw%3D%3D"

numOfRows = 1000
pageNo = 1
eventStartDate = 20190101

url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchFestival?" \
      "serviceKey=%s" \
      "&numOfRows=%d" \
      "&pageNo=%d" \
      "&arrange=A" \
      "&listYN=Y" \
      "&MobileOS=ETC" \
      "&MobileApp=AppTest" \
      "&eventStartDate=%d" \
      "&_type=json" % (serviceKey, numOfRows, pageNo, eventStartDate)


def gps_from_ip():
    with urllib.request.urlopen("http://ip-api.com/json") as url:
        data = json.loads(url.read().decode())

        return data['lat'], data['lon']

y, x = gps_from_ip()

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

    i = 0

    for data_row in data['response']['body']['items']['item']:
        if i == 0:
            print(data_row)

        if not data_row['eventstartdate'] <= today <= data_row['eventenddate']:
            continue

        if 'mapx' in data_row.keys() and 'mapy' in data_row.keys():
            if abs(float(data_row['mapx']) - x) > 0.5 or abs(float(data_row['mapy']) - y) > 0.5:
                continue

        i += 1
        region = region_name_short(data_row['addr1'].split()[0])

        if 'tel' in data_row.keys():
            data_row['tel'] = data_row['tel']
        else:
            data_row['tel'] = '연락처 정보 없음'

        print("%03d - [%d ~ %d] %s | %s | %s" % (i, data_row['eventstartdate'], data_row['eventenddate'], region, data_row['title'], data_row['tel']))
