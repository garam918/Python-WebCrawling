# Python-WebCrawling

## Selenium과 BeatifulSoup을 이용한 간단한 웹 크롤링 및 텍스트 마이닝

1) movie_grade_graph.py : 네이버 영화 평점 그래프 그리기
2) movie_review_classification.py : 한국어 영화 리뷰 데이터을 이용한 분류기 학습 및 워드 클라우드 그리기
3) youtube_review_crawling.py : 유튜브 댓글 수집

</br >

### movie_grade_graph

- 2020년 1월 1일부터 하루 간격으로 100일 동안의 영화 평점 데이터 수집
  - pd.data_range의 값을 수정해서 특정 기간, 날에 대한 데이터 수집 가능
- BeautifulSoup을 이용한 영화 평점 데이터 추출
- matplotlib.pyplot을 이용한 평점 그래프 그리기
  - 특정 영화 제목을 데이터 프레임에서 검색하여 그리기 가능

<img src="https://user-images.githubusercontent.com/62510764/105808832-dc207500-5feb-11eb-8e4f-a2547787f7c7.JPG" height=100% width="100%"></img>

</br >

### movie_review_classification

- selenium을 이용한 특정 영화의 리뷰 데이터 수집
- BeautifulSoup을 이용한 html 파싱으로 리뷰와 평점 추출
- nltk와 Okt를 이용한 리뷰의 자연어 처리 및 텍스트 분석, 형태소 분석
  - 테스트 문장이 긍정, 부정인지 판별
- wordcloud를 이용한 긍정 리뷰의 시각화

<img src="https://user-images.githubusercontent.com/62510764/105809104-72549b00-5fec-11eb-8bc5-71c8481ca561.JPG" height=100% width="100%"></img>

</br >

### youtube_review_crawling

- selenium을 이용한 특정 유튜브 영상의 댓글 데이터 수집
  - 소스 코드는 영상 1개만을 수집하지만 url 주소를 리스트에 넣을 경우 여러 유튜브 영상의 댓글 수집 가능

<img src="https://user-images.githubusercontent.com/62510764/105809233-a7f98400-5fec-11eb-8eb3-773340cb1167.gif" height=100% width="100%"></img>

</br >

## 설치 환경

- Pycharm
  - Python 3.8
- beautifulsoup4 4.6.0
- konlpy 0.5.2
- nltk 3.5
- pandas 1.2.0
- wordcloud 1.8.1
- matplotlib 3.2.0

</br >

## 유의할 점

- jupyter notebook에서 작성된 코드로 pycharm이나 다른 환경에서 실행이 가능하지만 matplotlib의 경우 최신 버전이 아닌 3.2.0 버전으로 해야 오류가 발생하지 않습니다
- konlpy의 경우
  1) JAVA 1.7 이상 설치
  2) JAVA_HOME Path 설정
  3) JPype1 (>=0.57) 설치
  - 이 세가지가 선행 되어야 하며 만약 importerror: dll load failed while importing _sqlite3 이 오류가 뜬다면 https://www.sqlite.org/download.html 에서 
  자신의 OS 환경에 맞는 파일을 다운 받은 후 system32 > dll 폴더에 넣어야 합니다.  
