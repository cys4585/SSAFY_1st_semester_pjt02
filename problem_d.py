import requests
from tmdb import URLMaker
from pprint import pprint


def recommendation(title):
    # url
    key = '59dde7bd14865cb45e54cd51d83d7ab7'
    url_maker = URLMaker(key)
    # movie id
    movie_id = url_maker.movie_id(title)
    # title에 해당하는 movie id가 없으면 리턴 
    if movie_id == None:
        return None
    # movie id를 통해 추천목록 url 얻기
    url = url_maker.get_url(category='movie', feature=f'{movie_id}/recommendations', language='ko')
    # 요청 -> 응답 -> 데이터 얻기
    response = requests.get(url)
    movies_list = response.json().get('results')
    # 반환할 빈 리스트 생성
    titles_list = []
    # 영화 하나씩 조사
    for i in range(len(movies_list)):
        # 영화 제목들을 모두 리스트에 추가
        titles_list.append(movies_list[i].get('title'))
    return titles_list

if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None
