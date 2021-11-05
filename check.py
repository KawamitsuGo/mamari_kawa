import pandas as pd

df = pd.read_csv("sample.csv")

tango_list = ['私','旦那','今','自分','子供','赤ちゃん','コメント','大丈夫','病院','ママ','気持ち','時間','息子','わたし','妊娠','娘','出産','実家']


for tango in tango_list:
    print(df[tango].unique())
