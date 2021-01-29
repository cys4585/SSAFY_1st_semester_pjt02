# pjt02

### problem A - 영화 개수 카운트 기능 구현

- TMDB에 request를 하기위한 url 문자열을 만든다.
- tmdb.py에 있는 URLMaker클래스와 get_url()메소드를 이용해서 간단히 만들 수 있었다.
  - 인스턴스 생성시 api-key를 넘긴다.
  - get_url() 메소드를 이용해 url 문자열을 완성시킨다.
    - get_url() 메소드의 매개변수 중 catecory, feature는 default값으로 각각 movie, popular가 있기 때문에 따로 인자값을 주지 않아도, 자동으로 영화 목록 url이 만들어진다.
- response = requests.get(url)을 통해 요청을 보내고 리턴값을 response에 담아준다.
- data = response.json()을 통해 응답받은 정보를 코드에서 사용할 수 있도록 바꿔준다.
- data 정보 중에서, 'results'에 해당하는 value인 list가 내가 필요로하는 정보이다.
- problem A에서 원하는 영화의 수를 리턴해야하기 때문에 len(data.get('results'))를 리턴한다.

```python
import requests
from tmdb import URLMaker


def popular_count():
    key = '59dde7bd14865cb45e54cd51d83d7ab7'
    url_maker = URLMaker(key)
    # movie popular 데이터가 있는 url 가져오기
    url = url_maker.get_url()

    # 해당 url로 요청 보내고 응답받기
    response = requests.get(url)
    # 응답받은 데이터 받기
    data = response.json()
    
    # 데이터 중에서 'results : [영화list]' 꼴로 들어있음.
    # [영화list]의 길이를 리턴
    return len(data.get('results'))

if __name__ == '__main__':
    print(popular_count())
```

- 처음 시작할 때, URLMaker클래스와 메소드의 내용을 자세하게 이해할 필요가 있다. 



### problem B - 영화 평점 조사해서 목록 출력

- problem A 와 동일하게 url 및 data를 가젼온다.
- data의 영화정보는 'result' key에 해당하는 value값(list)이다.
  - 영화정보를 movies_list에 담는다.
- return을 위한 빈 list를 생성하고, for문을 이용해 영화를 하나씩 조사한다.
  - vote_average가 8이상이면 list에 영화정보(dictionary)를 담는다.
- for문이 끝나면 평점이 8이상인 모든 영화가 list에 담겨져 있다. 이 list를 리턴한다.

```python
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

```



### problem C - 영화 목록 중 평점이 높은 5개 영화만 추출

- url 및 data 가져오는 법은 동일하다.
- sorted() 함수를 쓰기 어려워 2중 for문으로 해결했다.
  - 5개 영화를 담을 빈리스트를 만들어둔다.
  - 평점이 가장 높은 영화를 pop하는 작업을 5번 반복한다.
  - 평점이 가장 높은 영화를 pop하는 과정
    - 가장 높은 평점을 구하기 위한 변수와 그 영화의 위치를 저장할 변수를 생성한다.
    - 영화정보가 담겨있는 list를 for문을 통해 반복한다.
      - 평점이 가장 큰 영화정보의 index를 변수에 저장한다.
    - 반복문이 종료되면 index를 저장한 변수를 통해 list.pop()을 하고, 빈리스트에 담는다.
    - pop을 했기 때문에 평점이 가장 큰 영화는 다음 반복에서 제외된다.

```python
import requests
from tmdb import URLMaker
from pprint import pprint


def ranking():
    # url
    key = '59dde7bd14865cb45e54cd51d83d7ab7'
    url_maker = URLMaker(key)
    url = url_maker.get_url()
    # data
    response = requests.get(url)
    data = response.json()
    movies_list = data.get('results')
    # 반환할 list 생성 (상위 5개 영화)
    top_five = []
    # 5번 반복
    for _ in range(5):
        # 가장 높은 평점을 구하기 위한 변수
        max_vote_average = 0
        # 가장 높은 평점인 영화의 인덱스를 저장하기 위한 변수
        max_movie_index = 0
        # 영화 리스트 수 만큼 반복
        for i in range(len(movies_list)):
            # 영화의 평점이 평점 변수보다 높으면 평점 변수, 해당 영화의 인덱스를 변경
            if movies_list[i].get('vote_average') > max_vote_average:
                max_vote_average = movies_list[i].get('vote_average')
                max_movie_index = i
        # 반복이 끝나면 가장 높은 평점을 기록한 영화의 인덱스를 알 수 있음
        # 리스트에서 그 인덱스에 해당하는 데이터를 pop()을 통해 꺼내고
        # 리턴할 list에 추가
        top_five.append(movies_list.pop(max_movie_index))

    return movies_list

if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())
```

- sorted() 함수를 통해 해결하는 방법도 공부해봐야겠다.

```python
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
	
    # movies_list를 정렬한다.
    # key(vote_average)에 해당하는 value을 기준으로
    # value가 높은 순으로
    movies_list = sorted(movies_list, key=itemgetter('vote_average'), reverse=True)
    top_five = []
    for i in range(5):
        top_five.append(movies_list[i])
    return top_five

if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())
```

- operator 모듈에 있는 itemgetter 함수를 이용해서 list 안에 있는 dictionary의 특정 value값을 비교할 수 있었다.



### problem D - 제목을 기준으로 추천영화 목록 출력하기

- TMDB에 요청할 url을 수정해야한다.
  - 추천영화 목록 url은 /movie/{movie_id}/recommendations 꼴로 만들어야한다.
  - 먼저 얻어온 title을 통해 movie_id를 얻어야 한다.
    - URLMaker클래스의 movie_id() 메소드를 이용해 간편하게 movie_id를 얻을 수 있다.
    - movie_id가 None이라면 : 얻어온 title이 tmdb 데이터에 없다는 뜻 -> None을 리턴한다.
  - get_url() 메소드에 ('movie', f'{movie_id}/recommendations', language='ko')를 준다.
    - get_url() 메소드의 **kwargs 매개변수가 있어, key=value 형식으로 원하는 만큼 인자를 넘길 수 있다.
  - for 반복문을 통해 영화의 제목들을 list에 담아서 리턴한다.

```python
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

```

- url 요청하는게 어려웠다. TMDB 홈페이지에 GET Recommendations 에 대한 내용이 상세하게 나와있어서 마음을 가라앉히고 천천히 살펴보니 해결이 되었다.
- 모르는 내용도 침착하게 찾아보면 해결이 가능하다.



### problem E - Credit URL 요청 (배우, 감독이름 얻기)

- Get Credits에 대한 내용을 살펴봤다.
  - /movie/{movie_id}/credits 형식으로 url 요청이 가능하다.
  - id, cast, crew 정보들이 담겨있다.
    - cast, crew 안에 각각 name, cast_id, department등의 데이터들이 담겨있다.
- movie_id() 메소드로 movie_id를 얻고, get_url() 메소드로 url를 만들어 request했다.
- response 정보를 json으로 만들어 cast, crew를 각각 조사했다.
- cast_list를 만들어 cast_id가 10 미만인 경우에 name을 추가했다.
- crew_list를 만들어 department가 Directing인 경우에 name을 추가했다.
- dictionary를 만들어 cast_list와 crew_list를 각각 'cast', 'crew' key의 value로 담아서 리턴했다.

```python
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
```

