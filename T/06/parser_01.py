# pip install beautifulsoup4
# pip install requests

import bs4
import requests


def get_html(url) -> str:
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어드려 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()

    return response.text


def get_news_info(q) -> None:
    """
    구글 뉴스 사이트에 접속해서 제목 찾기
    :param q: 주제
    """
    print("="*10, q, "="*10)
    html = get_html('https://news.google.com/search?q='+q+'&hl=ko&gl=KR&ceid=KR%3Ako')
    soup = bs4.BeautifulSoup(html, 'html.parser')

    news = soup.select('article h3')

    for i in news:
        print(i.text, "https://news.google.com/"+i.select('a')[0].get('href')[2:])


get_news_info('세종과학예술영재학교')
