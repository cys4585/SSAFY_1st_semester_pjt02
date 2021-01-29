import requests
from tmdb import URLMaker
from pprint import pprint
from operator import itemgetter

def ranking():
    # url
    key = '59dde7bd14865cb45e54cd51d83d7ab7'
    url_maker = URLMaker(key)
    url = url_maker.get_url()
    # data
    response = requests.get(url)
    data = response.json()
    movies_list = data.get('results')

    # # 반환할 list 생성 (상위 5개 영화)
    # top_five = []
    # # 5번 반복
    # for _ in range(5):
    #     # 가장 높은 평점을 구하기 위한 변수
    #     max_vote_average = 0
    #     # 가장 높은 평점인 영화의 인덱스를 저장하기 위한 변수
    #     max_movie_index = 0
    #     # 영화 리스트 수 만큼 반복
    #     for i in range(len(movies_list)):
    #         # 영화의 평점이 평점 변수보다 높으면 평점 변수, 해당 영화의 인덱스를 변경
    #         if movies_list[i].get('vote_average') > max_vote_average:
    #             max_vote_average = movies_list[i].get('vote_average')
    #             max_movie_index = i
    #     # 반복이 끝나면 가장 높은 평점을 기록한 영화의 인덱스를 알 수 있음
    #     # 리스트에서 그 인덱스에 해당하는 데이터를 pop()을 통해 꺼내고
    #     # 리턴할 list에 추가
    #     top_five.append(movies_list.pop(max_movie_index))

    movies_list = sorted(movies_list, key=itemgetter('vote_average'), reverse=True)
    top_five = []
    for i in range(5):
        top_five.append(movies_list[i])
    return top_five

if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())