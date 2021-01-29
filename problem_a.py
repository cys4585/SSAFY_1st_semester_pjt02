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