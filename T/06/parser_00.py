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


def get_movies_info() -> None:
    """
    현재 상영작 영화 정보 보기
    """
    html = get_html('http://www.cgv.co.kr/movies/')
    soup = bs4.BeautifulSoup(html, 'html.parser')

    movie_list = soup.select('div.sect-movie-chart li div.box-contents')

    i = 1

    for movie in movie_list:
        movie_name = movie.find('a').text.strip()
        movie_ticket = movie.select('div.score strong span')[0].text

        print("[%02d] %s %s" % (i, movie_name, movie_ticket))
        i += 1


get_movies_info()
