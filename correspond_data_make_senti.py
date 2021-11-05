import pandas as pd

def check(lst, content):
    for word in lst:
        if word in content:
            return 1
    return 0

print("tsv読み込み中")
data = pd.read_csv("data/test_questions_10000.tsv",delimiter="\t")



#region 変数定義
tango_list = ['私','旦那','今','自分','子供','赤ちゃん','コメント','大丈夫','病院','ママ','気持ち','時間','息子','わたし','妊娠','娘','出産','実家']
genre_list = ['家族','出産','子供','健康','私','お金']
kazoku_words = ['旦那','実家','姑','両親','義実家']
shussan_words = ['出産','妊娠','授乳','産後','離乳食','陣痛']
kenko_words = ['入院','病院','熱','風邪']
kodomo_words =['子供','赤ちゃん','息子','娘','子ども']
okane_words = ['お金','仕事']
watashi_words = ['私','わたし','自分']
column = ['category_id','content']
#endregion



print(column)
column.extend(genre_list)
column.extend(['sentiment'])

#print(column)

df = pd.DataFrame(columns=column)

print(df)

for index,row in data.iterrows():
    print(index)
    print(type(index))
    print(row)
    print(type(row))
    tmp = pd.Series(index=column)
    tmp['category_id'] = row['category_id']
    tmp['content'] = row['content']

    tmp['家族'] = check(kazoku_words,row['content'])
    tmp['出産'] = check(shussan_words,row['content'])
    tmp['子供'] = check(kodomo_words,row['content'])
    tmp['健康'] = check(kenko_words,row['content'])
    tmp['私'] = check(watashi_words,row['content'])
    tmp['お金'] = check(okane_words,row['content'])

    df = df.append(tmp,ignore_index=True)

df.to_csv("result/sample2.csv")





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