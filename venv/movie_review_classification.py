import pandas as pd
import numpy as np
from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import time

from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

driver = webdriver.Chrome(r"C:\Users\ijy91\Downloads\chromedriver_win32\chromedriver.exe")   # 크롬 웹 드라이버 경로 지정

driver.get("https://movie.naver.com/movie/bi/mi/point.nhn?code=161967")                      # 영화 '기생충'

driver.switch_to.frame(driver.find_element_by_id('pointAfterListIframe'))

review_list = []                    # 전체 리뷰 데이터
review_pos_word_list = []           # 평점 6점 이상의 긍정 리뷰 데이터

for page in range(0, 100):          # 1페이지에서 100페이지까지 == 1000개
    time.sleep(1)
    html_source = driver.page_source
    html_soup = BeautifulSoup(html_source, 'html.parser')
    html = html_soup.find('div', {'class': 'ifr_area basic_ifr'})
    review = html.find('div', {'class': 'score_result'}).find_all('li')

    for i in range(len(review)):
        star_score = review[i].find('div', {'class': 'star_score'}).find('em').text.strip()          # 평점
        review_text = review[i].find('div', {'class': 'score_reple'}).find('span').text.strip()      # 댓글
        if int(star_score) > 5:                     # 6점 이상인 경우 긍정, 5점 이하인 경우 부정으로 분류
            review_list.append((review_text, 'pos'))
            review_pos_word_list.append(review_text)
        else:
            review_list.append((review_text, 'neg'))

    if page == 0:
        driver.find_elements_by_xpath('//*[@class = "paging"]/div/a')[10].click()
    else:
        driver.find_elements_by_xpath('//*[@class = "paging"]/div/a')[11].click()

print(review_list)

from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

okt = Okt()

train = review_list # 학습시킬 데이터

def pos_tokenize(raw_sent):
    pos_sent = []

    sent = okt.pos(raw_sent, norm=True, stem=True)

    for tup in sent:
        word, tag = tup[0], tup[1]
        word_tag = word + '/' + tag
        pos_sent.append(word_tag)

    return ' '.join(pos_sent)

all_words = set()

train_features = []

for tup in train:
    sent, label = tup[0], tup[1]
    sent = pos_tokenize(sent)
    words = word_tokenize(sent)
    for word in words:
        all_words.add(word)

for tup in train:
    sent, label = tup[0], tup[1]
    sent = pos_tokenize(sent)
    words = word_tokenize(sent)
    tmp = {set_word: (set_word in words) for set_word in all_words}
    sent_tup = (tmp, label)
    train_features.append(sent_tup)

for i in range(len(train_features)):
    print(train_features[i])

classifier = nltk.NaiveBayesClassifier.train(train_features)
classifier.show_most_informative_features()

test_sent = '별로 재미없었어요' # 테스트 문장

test_sent = pos_tokenize(test_sent)
words = word_tokenize(test_sent)
test_feature = {set_word: (set_word in words) for set_word in all_words}

print('테스트 문장의 분류 결과 : ' + classifier.classify(test_feature))

from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

ko_doc = '\n'.join(review_pos_word_list)

ko_doc_noun = okt.nouns(ko_doc)

count_noun = Counter(ko_doc_noun)
count_noun.most_common(100)         # 가장 많이 나온 100개의 단어
stopword_list = ['관람객', '영화']    # 워드 클라우드에서 제외할 단어 리스트

for word in count_noun:
    if len(word) == 1:              # 단어의 길이가 1인 경우 제외 리스트에 추가
        stopword_list.append(word)

for stopword in stopword_list:
    if stopword in count_noun:
        count_noun.pop(stopword)

print(count_noun.most_common(100))

wc_img = WordCloud(background_color='white', max_words=2000,
                   font_path=r'C:\Windows\Fonts\NanumGothic.ttf')

wc_img = wc_img.generate_from_frequencies(count_noun)

plt.imshow(wc_img, interpolation="bilinear")
plt.axis("off")
plt.show()