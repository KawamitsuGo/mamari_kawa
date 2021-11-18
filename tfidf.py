import re
import MeCab
from collections import Counter
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import glob
import numpy as np
import math
import mpmath
mpmath.mp.dps = 100


tagger = MeCab.Tagger("-Ochasen")

df = pd.read_csv("../question_plain_text_100000.csv")
#df = pd.read_csv("../other/data/test_answers_100.tsv",delimiter='\t')

file = open('../ja.text8', 'r')  #読み込みモードでオープン
wiki = file.read()

print(df)

wakaches = []

wakachi_list = []

i = 0

for index,row in df.iterrows():
    tweet_keitaiso = tagger.parse(row['content'])

    words_keitaiso_array = tweet_keitaiso.split('\n')
    for word_keitaiso in words_keitaiso_array:
        wakachi_list.append(re.split('[\t,]', word_keitaiso))

    i = i + 1
    print(i)

wakachi_selected = ""

print("名詞形容詞の出力")

l = len(wakachi_list)
i = 0

for wakachi in wakachi_list:
    if(wakachi[0] not in ('EOS', '') and (wakachi[3] == '名詞-一般' or wakachi[3] == '名詞-固有名詞一般' or wakachi[3] == '名詞-形容動詞語幹')):
        wakachi_selected = wakachi_selected + " " + wakachi[0]
    if(wakachi[0] not in ('EOS', '') and (wakachi[3] == '形容詞-自立' or wakachi[3] == '形容詞-非自立')):
        wakachi_selected = wakachi_selected + " " + wakachi[2]
    per = i*100/l
    print(str(per)+'%終わり')
    i = i + 1





sample = pd.array([wakachi_selected,wiki])

# TfidfVectorizer
vec_tfidf = TfidfVectorizer()

print("ベクトル化")
# ベクトル化
X = vec_tfidf.fit_transform(sample)

print("tfidfの実行")
#tfidf実行
print("doing tfidf...")
table_tfidf = pd.DataFrame(X.toarray(), columns=vec_tfidf.get_feature_names())

print(table_tfidf)


table_rank = table_tfidf.mean(axis=0) 
table_rank = table_rank.sort_values(ascending=False) 
#table_rank = table_rank.iloc[0:20] 

table_rank.to_csv("tfidf.csv")



"""
#region
#形態素解析
for file in csv_files:
    print(file)
    f = open(file,'r',encoding = "utf-8",errors = "ignore")
    tweets = f.read()

    tweets_array = tweets.split('\n')

    wakachi_list = []

    for tweet in tweets_array:
        tweet_keitaiso = tagger.parse(tweet)

        words_keitaiso_array = tweet_keitaiso.split('\n')
        for word_keitaiso in words_keitaiso_array:
            wakachi_list.append(re.split('[\t,]', word_keitaiso))

    wakachi_selected = ""

    #品詞での振り分け
    for wakachi in wakachi_list:
        if(wakachi[0] not in ('EOS', '') and (wakachi[3] == '名詞-一般' or wakachi[3] == '名詞-固有名詞一般' or wakachi[3] == '名詞-形容動詞語幹')):
            wakachi_selected = wakachi_selected + " " + wakachi[0]
        if(wakachi[0] not in ('EOS', '') and (wakachi[3] == '形容詞-自立' or wakachi[3] == '形容詞-非自立')):
            wakachi_selected = wakachi_selected + " " + wakachi[2]

    wakaches.append(wakachi_selected)

sample = pd.array(wakaches)

#endregion



# TfidfVectorizer
vec_tfidf = TfidfVectorizer()

# ベクトル化
X = vec_tfidf.fit_transform(sample)

#tfidf実行
print("doing tfidf...")
table_tfidf = pd.DataFrame(X.toarray(), columns=vec_tfidf.get_feature_names(),index=csv_files)

#理科大のデータだけを抽出
table_daigaku = table_tfidf.query('index.str.contains("/rikadai_tw/")')



#大学のトップ20単語を出力
print("sorting list...")
table_rank = table_daigaku.mean(axis=0) 
table_rank = table_rank.sort_values(ascending=False) 
table_rank = table_rank.iloc[0:20] 
list1 = table_rank.index.values 

#共起度分析
print("calculating co_occurence...")
coocr(list1)


"""