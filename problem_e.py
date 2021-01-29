import requests
from tmdb import URLMaker
from pprint import pprint


def credits(title):
    # movie id 얻기
    key = '59dde7bd14865cb45e54cd51d83d7ab7'
    url_maker = URLMaker(key)
    movie_id = url_maker.movie_id(title)
    # movie id 없으면 None 리턴
    if movie_id == None:
        return None
    # credit 관련 url 얻기
    url = url_maker.get_url(category='movie', feature=f'{movie_id}/credits')
    # 요청 응답 / 데이터 얻기
    response = requests.get(url)
    data = response.json()

    # 데이터를 담을 빈 리스트 생성
    cast_list = []
    crew_list = []
    # cast 정보 하나씩 조사
    for cast in data.get('cast'):
        # cast id 10 미만인 배우 이름만 담기
        if cast.get('cast_id') < 10:
            cast_list.append(cast.get('name'))
    # crew 정보 하나씩 조사
    for crew in data.get('crew'):
        # department가 Directing인 이름만 담기
        if crew.get('department') == 'Directing':
            crew_list.append(crew.get('name'))
            
    # cast정보와 crew 정보를 dictionary에 담기
    result = {
        'cast' : cast_list,
        'crew' : crew_list
    }
    return result
    

if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None