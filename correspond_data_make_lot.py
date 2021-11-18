from re import T
import pandas as pd

def check(lst, content):
    for word in lst:
        if word in content:
            return 1
    return 0

print("tsv読み込み中")
data = pd.read_csv("../other/data/test_questions_10000.tsv",delimiter="\t")


#region 変数定義
#tango_list = ['私','旦那','今','自分','子供','赤ちゃん','コメント','大丈夫','病院','ママ','気持ち','時間','息子','わたし','妊娠','娘','出産','実家']
genre_list = ['私','旦那','子ども','親']


watashi_words = ['私','わたし','自分','ママ']
danna_words = ['旦那','夫','パパ','主人']
kodomo_words = ['子供','息子','娘','子ども']
oya_words =['実家','親','姑','義']

column = ['id','content','time']
#endregion

print(column)
column.extend(genre_list)

#print(column)

df = pd.DataFrame(columns=column)

print(df)

for index,row in data.iterrows():
    #print(index)
    #print(type(index))
    #print(row)
    #print(type(row))
    tmp = pd.Series(index=column)
    tmp['id'] = row['id']
    tmp['content'] = row['content']
    aps = row['created'].split(' ')
    ap = aps[1]
    print(ap)
    bps = ap.split(':')
    bp = bps[0]
    print(bp)

    if bp < '06':
        tmp['time'] = 0
    elif bp < '12':
        tmp['time'] = 1
    elif bp < '18':
        tmp['time'] = 2
    else:
        tmp['time'] = 3

    #tmp['content'] = row['content']

    tmp['私'] = check(watashi_words,row['content'])
    tmp['旦那'] = check(danna_words,row['content'])
    tmp['子供'] = check(kodomo_words,row['content'])
    tmp['親'] = check(oya_words,row['content'])

    if tmp['私'] + tmp['旦那']+ tmp['子供'] + tmp['親'] > 0 :
        df = df.append(tmp,ignore_index=True)


senti_df = pd.read_csv("senti_10000.tsv",delimiter="\t")

senti_df = senti_df.iloc[:,1:3]

eva_df = pd.merge(senti_df, df, how='inner', on='id')

print(df)
print(senti_df)
print(eva_df)

#for index,row in eva_df.iterrows():
#    if row['score'] >= -0.3:
#        eva_df.at[index,'score'] = 1
#    else:
#        eva_df.at[index,'score'] = 0


eva_df.to_csv("result/sample5.csv")





"""
text = '今日は旦那と赤ちゃんと出かけました。あの人はわたしの気持ちなんてわからないから実家に帰りたーい。'

tmp = pd.Series(index=column)
tmp['category_id'] = 15
tmp['content'] = text
for word in tango_list:
    tmp[word] = word in text

print(tmp)

print(df.append(tmp,ignore_index=True))
"""