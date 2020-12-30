from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

data_list = pd.date_range("2020-01-01", periods=100, freq='D') # 1월 1일부터 하루 간격으로 100일 동안

movie_title = []
movie_point = []
movie_date = []
print(data_list)
for today in tqdm(data_list):   # 진행 상황을 Progress Bar 형태로 나타냄
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=" + (today.strftime('%Y%m%d'))
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), "html.parser")

    titles = soup.find_all('div', {'class': 'tit5'})
    points = soup.find_all('td', {'class': 'point'})

    titles_text = []        # 영화 제목 리스트
    points_text = []        # 영화 평점 리스트
    date = []
    for t, p in zip(titles, points):
        titles_text.append(t.text.strip(' \n'))
        points_text.append(float(p.text))
        date.append(today)

    movie_title += titles_text
    movie_point += points_text
    movie_date += date

    #print(movie_title)
    #print(movie_point)
    #print(movie_date)

import matplotlib.pyplot as plt

frame = pd.DataFrame({'date': movie_date, 'title' : movie_title, 'point': movie_point})
frame_sort = frame.sort_values(by='date')   # 영화 평점 데이터 프레임을 날짜 순으로 내림차순
print(frame_sort)

input_title = input()
search_movie = frame.query("title == ['{}']".format(input_title))       # 입력 받은 영화 제목을 데이터 프레임에서 검색

plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
plt.figure(figsize=(12,8))
plt.title('2020-01-01부터 100일간 영화 {} 평점 그래프'.format(input_title)) # 그래프 제목을 입력 받은 영화 제목으로 함
plt.xlabel('날짜')
plt.ylabel('평점')
plt.plot(search_movie['date'],search_movie['point'])
plt.show()