from re import T
import pandas as pd

def check(lst, content):
    for word in lst:
        if word in content:
            return 1
    return 0

print("tsv読み込み中")
data = pd.read_csv("../../Sotsuron/test_questions_10000.tsv",delimiter="\t")


#region 変数定義
#tango_list = ['私','旦那','今','自分','子供','赤ちゃん','コメント','大丈夫','病院','ママ','気持ち','時間','息子','わたし','妊娠','娘','出産','実家']
genre_list = ['家族','出産','子供','健康','私','お金']
kazoku_words = ['旦那','実家','姑','両親','義実家','義母','親戚','義理','夫婦','親','義父','祖母']
shussan_words = ['出産','妊娠','授乳','産後','離乳食','陣痛','母乳','オムツ','おっぱい','保育園','つわり','インフルエンザ']
kenko_words = ['入院','病院','熱','風邪','体重','薬','咳']
kodomo_words =['子供','赤ちゃん','息子','娘','子ども','子','抱っこ',]
okane_words = ['お金','仕事']
watashi_words = ['私','わたし','自分']
column = ['category_id','time','score']
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
    tmp['category_id'] = row['category_id']
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

    tmp['家族'] = check(kazoku_words,row['content'])
    tmp['出産'] = check(shussan_words,row['content'])
    tmp['子供'] = check(kodomo_words,row['content'])
    tmp['健康'] = check(kenko_words,row['content'])
    tmp['私'] = check(watashi_words,row['content'])
    tmp['お金'] = check(okane_words,row['content'])
    

    if tmp['家族'] + tmp['出産']+ tmp['子供'] + tmp['健康'] + tmp['私'] + tmp['お金'] > 1 :
        df = df.append(tmp,ignore_index=True)


senti_df = pd.read_csv("senti.tsv",delimiter="\t")

eva_df = pd.merge(df, senti_df, how='inner', on=['word', 'speech'])



df.to_csv("result/sample4.csv")





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