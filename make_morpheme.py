import re
import MeCab
from collections import Counter
import pandas as pd
import glob
import numpy as np
import math
from collections import Counter


#ファイル読み込み

#region start 
df = pd.read_csv("../Sotsuron/data/test_questions_10000.tsv",delimiter='\t')
tagger = MeCab.Tagger("-Ochasen")
wakaches = []
columns = ['id','word','speech','speech_']
result = pd.DataFrame(columns = columns)
i = 0
#endregion

def make_tmp (id,word,speech,speech_):
            tmp = pd.Series(index=columns)
            tmp['id'] = row['id']
            tmp['word'] = wakachi[2]
            tmp['speech'] = hinshi
            tmp['speech_'] = hinshi_detail
            return tmp


#形態素解
for index,row in df.iterrows():
    wakachi_list = []

    tweet_keitaiso = tagger.parse(row['content'])
    words_keitaiso_array = tweet_keitaiso.split('\n')
    for word_keitaiso in words_keitaiso_array:
        wakachi_list.append(re.split('[\t,]', word_keitaiso))

    #print(wakachi_list)

    #品詞での振り分け
    for wakachi in wakachi_list:
        if(wakachi[0] not in ('EOS')):
            hinshis = wakachi[3].split('-')
            hinshi = hinshis[0]
            if len(hinshis) > 1 :
                hinshi_detail = hinshis[1]
            else:
                hinshi_detail = ""
            if (hinshi == "名詞") and (hinshi_detail == ("一般"or "副詞可能" or "サ変接続" or "形容動詞語幹")) :
                tmp = make_tmp(row['id'],wakachi[2],hinshi,hinshi_detail)
                result = result.append(tmp,ignore_index=True)
            elif (hinshi == "動詞"or"形容詞") and (hinshi_detail == "自立"):
                tmp = make_tmp(row['id'],wakachi[2],hinshi,hinshi_detail)
                result = result.append(tmp,ignore_index=True)

    i = i + 1
    print(i)

result.to_csv("result/morphome.tsv",sep='\t')






