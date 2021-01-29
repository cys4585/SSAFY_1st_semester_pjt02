import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    key = '59dde7bd14865cb45e54cd51d83d7ab7'
    url_maker = URLMaker(key)
    # movie popular 데이터가 있는 url 가져오기
    url = url_maker.get_url()

    # 요청 -> 응답으로 데이터 가져오기
    response = requests.get(url)
    data = response.json()
    # 영화 리스트 가져오기
    movies_list = data.get('results')
    # 리턴할 빈리스트 생성
    result = []
    # 영화 하나씩 조사
    for m in movies_list:
        # 평점이 8 이상이면
        if m.get('vote_average') >= 8:
            # 리스트에 해당 영화 데이터 담기
            result.append(m)
    return result

if __name__ == '__main__':
    pprint(vote_average_movies())    
