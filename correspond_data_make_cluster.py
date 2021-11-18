from re import T
import pandas as pd

def check(lst, content):
    for word in lst:
        if word in content:
            return 1
    return 0

print("tsv読み込み中")
data = pd.read_csv("../question_plain_text_100000.csv")

print(data)

#region 変数定義
#tango_list = ['私','旦那','今','自分','子供','赤ちゃん','コメント','大丈夫','病院','ママ','気持ち','時間','息子','わたし','妊娠','娘','出産','実家']
genre_list = ['家族','病気','薬','赤ちゃん','植物','動物','病院','飲食','仕事','乗り物','身体','自然','時間','お金','教育','住宅','衣類','精神状態','場所','性格','人間','スピリチュアル','文字','五感','エネルギー','色','ネガティブ','妊婦','方角','交通','小物','栄養','数値','文化','個人情報']
kazoku_list=  ['うち', '旦那', '子', '家', 'ママ', '実家', '夫', '主人', '家族', '娘', '家事', '息子', '母', '義母', '義父', '実母', '妹', '義理', '祖母', '姉', '弟', 'お父さん', '親', '両親', '母親', '父', '兄弟', '父親', '親戚', '双子', '親子', '祖父', 'オバアちゃん', '母方', '父方', '孫', 'ひ孫', '曾孫', '玄孫', 'ばば', 'おば', 'お母さん', '奥さん', '長男', '長女', '次男', '年子', '次女', '三男', '三女', '内孫', '二女', '外孫'] 
byoki_list =  ['コロナ', '風邪', '陽性', '体調', '陰性', '安静', '喘息', '持病', '痔', '発作', '肺炎', '疾患', '疾病', '傷病' ,'病気', '風疹', '水痘', '麻疹', '疹' , '癌', 'がん', '大腸', '咽頭', '食道', '乳癌', '直腸', '胃癌', '肺癌' , '傷', '重症', 'ケガ', '外傷', 'けが', '裂傷', '重傷', '別状', '熱傷', 'アザ', 'あざ', '痣' , 'シミ', 'シワ', 'キズ', 'しわ', 'ヨレ', 'ジワ', 'アレルギー' , '症状', '逆子', '障害', '浮腫', '黄疸', '軽度', '重度', '吃音', '痒疹', '斜視' , '腹痛', '頭痛', '腰痛', '胃痛', '鼻炎', '歯痛', '胃炎' , '痛み', '陣痛', '咳', '鼻水', '食欲', '高熱', '微熱', '激痛', '鮮血', '眠気' , '肌', '湿疹', '汗疹', '毛穴', '炎症', '月経', '寝汗', '腋臭', '水虫'] 
kusuri_list =  ['薬', '座薬', '薬局', '軟膏', '錠', '整腸剤', '目薬', '乳液', '鉄剤', '坐薬', 'ピル', '下剤', '用量', '薬剤', '幻覚', '効能', '薬効', '薬物', '媚薬', '鎮痛'] 
akachan_list = ['一人っ子', 'お子さん', 'おっぱい', 'おむつ', 'オムツ','ベビーカー', '保育園', '育休', '有給', '休暇', '有休', '半休', 'ハイハイ', '抱っこ', '母乳', '子供', '幼稚園', '母子', '幼児', '年少', '赤ちゃん', '子ども', '男の子', '女の子', 'おもちゃ', '我が家', 'こども', 'とんとん', '生後', '産前', '療育', 'ベビー'] 
shokubutu_list = ['庭', '桜', '親木', '花', 'お花', '根', '畑', '豆', '葉', '株', '雑草', '芝生', '植物', '木材', '樹木', '森林', '牧草', '木々', '草木', '鬱蒼', '双葉', '二子', '森', '猪子', '一条', '取手', '芝', '小口', '水木']
dobutsu_list = ['犬', '猫', '動物', '象', '鳥', '子猫', 'ブタ', '羽', '恐竜', '蛾', '幼虫', '昆虫', '成虫', '蝶', '蝶々', '白蟻', 'カビ', '虫', '蚊', 'ダニ', '菌', 'コバエ', '蜂', '巣', '蜘蛛', '死骸']
byoin_list = ['整形外科', 'クリニック', '病院', '産院', '内科', '医者', '医師', '初診', '医療', '眼科', '外来', '転院', '歯医者']  
insyoku_list = ['もち', '麦茶', 'お湯','製茶', 'かき', 'もも', '牛乳', '離乳食','お菓子', '冷蔵庫', 'ごはん', '食べ物', 'おかず', 'ケーキ', '小さじ', 'うどん', '味噌汁', 'ご飯', 'バナナ', '夕飯', '弁当', '粥', '夕食', 'お昼', '献立', '食後', '白米', '昼食''野菜', '食材', '果物', '朝市', '惣菜', '食品', '味覚', '根菜', '豆類', '産直', '食料', '物資', '食糧', '乳汁', 'ミルク', '刺身', '生魚', '焼魚' ,'パン', '納豆', '豆腐', 'そば', '焼肉', 'ピザ', '餃子', '丼', '麺', '豆乳' , '海苔', '煎餅', '漬物', '昆布', '漬け', '筋子', '貝柱', '珍味', '蒲鉾', '漬' , '月齢', '素材', '材料', '小麦', '成分', '国産', '製品', '産', '原材料', '食塩', '鶏肉', '豚肉', '牛肉', '牛', '肉類', '挽肉', '赤身', '牛脂', '食肉', '和牛' , '鮭', '鯛', '釣り', '竿', '鱈子', 'サバ', '鯖', '真鯛', '旬', '干物', '肉', '骨', '脂肪', '鶏', '豚', '下味', '脂', '軟骨', '生肉', '脂身' ,'魚', '寿司', '鰻', 'エビ', '白身', 'タコ', 'イカ', 'うに', 'カニ', 'えび' , '油', '砂糖', '塩', '醤油', '酢', '食紅', '鰹節', 'ごま', '生姜', '黒糖' , '人参', '大根', '枝豆', '大葉', '茄子', '白菜', '芋', 'ネギ', 'ニラ', '冷奴', '卵', '採卵', '卵黄', '卵白', '黄身', '殻', '玉子', '雛鳥', '半熟', '親鳥']
shigoto_list =  ['印鑑', '実印', '判子', '認印', '朱肉', '一人', '上司', '社員', '社長', '職', '技手', '教授', '主任', '課長', '知事', '市長', '町長' '社歴', '会社', '化学', '社会', '企業', '国', '職業', '衛生', '国民', '人事', '事業', '役員', '会長', '総会', '会員', '会', '組合', '機関', '団体', '委員', '大会', '協会', '課', '本部', '市立', '県立', '区立', '町立', '府立', '正社員', '都', '杜', '府', '都立', '定職', '遠方', '県内', '隣県', '近県', '県南', '府県', '都県']  
norimono_list = ['バス', '電車', '便', '片道', '車内', '終電', '線路', '踏切', '無人', '切符', '区間', '車', '電動', '輪', '高速', '新車', '車種', '軌道', '車両', '馬力', '原付', '自転車']  
karada_list =  ['髪の毛', '汗', '血','鼠蹊', '鼠径', '目', '生理', '体', '身体', '栄養', '人間', '胎児', '命', '羊水'  , '手', '皮', '素手', '両手', '片手', '拳', '手袋', '内野', '外野', '旗'  , '頭', '足', '指', '耳', '腕', '全身', '手足', '爪', '脚', '親指'  , '顔', '鼻', '唇', '寝顔', '頬', '一重', 'まぶた', '口元', '目の下', '左目', '遠視', '乱視', '近視', '子宮', '乳', '乳首', '膣', '舌', '精子', '乳頭', '陰部', '筋肉', '肛門', '腹腔' , '喉', 'のど', '気管', '鼓膜', '声帯', '喉元', 'ノド', '咽' , '髪', '毛', '前髪', '髪型', 'ヘア', '眉毛', 'ハゲ', '毛根', '白髪', '髭', '胎嚢', '頸管', '胎芽', '絨毛', '臍帯', '掻爬', '穿刺', '痔核', '幽門', '結膜', '膀胱', '胆石', '結石', '胆汁', '胆嚢', '結腸', '胆道' , '歯', '虫歯', '前歯', '歯茎', '歯並び', '乳歯', '差し歯', '永久歯', '茶渋', 'むし歯' , '胃', '心臓', '腸', '肺', '胃腸', '血管', '内臓', '腎臓', '肝臓', '涙腺' , '脳幹', '小脳', '神経', '脳', '脊椎', '腰椎', '頚椎', '脊髄', '歯石', '口臭', '体臭' , '腹囲', '胸囲', '顎', '上唇', 'あご', '上顎', '小鼻', '口角', '頬骨', '鼻筋', '鼻翼', '咬筋', '膝', '肘', '膝下', 'ひざ', '靭帯', 'ひじ', 'ヒザ','膝', '頭皮', '地肌' , '骨盤', '恥骨', '背骨', '鼻骨', '坐骨', '尾骨', '仙骨', '腰骨', '頭骨', '肋骨', '鎖骨', '胸骨' , '頚', '頸' , 'お腹', '胸', '腰', '首', '腹', '背中', '下腹部', '尻', '肩', '股', '腓骨', '脛骨', '橈側', '橈骨', '嚢胞', '卵巣', '血腫', '乳腺', '筋腫', '腫瘍', '悪性', '腹水', '血栓', '良性', '卵胞', '黄体' , '血圧', '血糖', '水疱', '便通', '便通', '皮膚', '涎', '痰', '粘液', '唾液', '胃酸', '唾', '胃液', 'ツバ', '生唾', 'だ液', '囊', '目脂', '腟内', '臍の緒', '馬手', '二次', 'お下', '方体', '今体', '肋', '膜', '胎盤', '胚', '細胞', '上皮', '角質', '器官', '内皮', '多能', '表皮', '跡', '赤み', '腫れ', '傷口', '膿', '白斑', '痕', '傷跡', '斑点', 'べそ'] 
shizen_list = ['熱', '高温', '体温', '平熱', '温度', '湿度', '常温', '室温', '気温', '低温', '天気', '晴れ', '天候', '快晴', '晴天', '青空', '日和' , '雨', '梅雨', '湿気', '台風', '雷', '大雨', '雲', '雪', '水滴', '豪雨', '雨量', '降水'  , '外気', '冷風', '冷気', '熱風', '寒暖', '夏', '半袖', '冬', '秋', '冷房', '春', '季節', '夏場', '屋外', '真夏']
zikan_list = ['夜中', '夜間', '最初','休み', '土日', '連休', '時短', '祝日', '期限', '日程', '曜日', '休', '定時', '次', '初期', '最後', '後期', '段階', '直前', '最終', '中期', '時代', '初日', '月', '水', '年', '時点', '日', '祝', '火', '木', '金', '土', '間', '週', '半', '間隔', '期間', '程度', '周期', '日中']
okane_list = ['月割', '見積', 'ローン', 'お金', '金銭', '現金', '自費', '資金', 'タダ', '報酬', '同額', '大金', '自腹', '千円', '頭金', '金利', '利子', '利率', '利息', '年利', '元金', '元本'  , '紙幣', '札', '硬貨', '釣銭' , '底値', '元値', '高値', '安値', '買値', '元利' ,'敷金', '礼金', '敷', '礼', '保険', '銀行', '口座', '国保', '年金', '積立', '老後', '郵貯', '満額', '共済', '費用', '家賃', '料金', '食費', '予算', '月々', '税金', '全額', '学費', '月額', '家計', '財政', '相場', '経済', '所得', '治安', '特区', '物価', '情勢', '賃金', '資源', '政策', '給料', '年収', '時給', '職種', '副業', '月収', '基本給', '月給', '賞与', '労務']
kyoikuku_list = ['模試', '高校', '私立', '大学', '公立', '学生', '中学', '高卒', '塾', '卒', '先生'  , '絵本', '歌', '遊具', '曲', '絵', '玩具', '人形', '教材', '知育', '学研' , '学校', '教室', '学年', '学区', '部活', '生徒', '校区', '教員', '体育', '学級', '小学校' ]
jutaku_list =['リビング', 'エアコン', 'マイホーム', '風呂', 'トイレ','部屋', '寝室', '玄関', '室内', '物件', '世帯', '建売', '住宅', '個室', '新居', '居宅', '通所', '布団', '枕', '毛布', '寝具', '寝床', '羽毛', '蚊帳', '用布', '氷枕', '夜具', '電気', '機', '同軸', '電球', '家電', '宅内', '機種', '電源', '回線', '信号' , '床', '棚', '本体', '便座', '天井', '段差', '木製', '地面', '鉄棒', '柱', '椅子', '机', '家具', 'イス', '絨毯', '敷物', '脚立', 'ゴザ', '肘掛', 'ベッド', 'アパート', '窓', '壁', 'ドア', '扉', '網戸', '柵', '屋根', '半間', '外壁', '大工', '洋式', '和式']  
irui_list = ['服', '肌着', '靴', '洋服', '服装', '下着', '靴下', '水着', '長袖', '帽子', '着丈', '肩幅', '股下', '身幅', '股上', '実寸', '身丈', '産着', '被布', '祝着', '着物', '浴衣', '甚平', '唐織', '袴', '和装', '振袖', '留袖', '兵児帯', '草履', '夏物', '秋物', '冬物']  
seishin_list = ['心', '感情', '精神', '自己', '性欲', '情緒', '暴力', '我欲', '欲', '余裕', '気配', '気力', '満々', '余地', '余力','悪阻', 'うつ', '鬱', '激務', '不眠', '鬱病', '鬱々', '寛解', '拒食', '幻聴', 'ハート', 'ストレス']
basyo_list =['センター', '駅', '市内','プール', 'スーパー', '公園', '土地', '周辺', '近辺', '街', '都会', '広場', '墓', '絶壁', '地', '店', '店員', '店長', '旅館', '宿', '農家', '本屋', '客', '食堂', '全区', '区', '区内', '自治', '区民', '同市', '同区', '区長', '町会', '各区'] 
seikaku_list = ['怖気', 'やる気', '人見知り', 'わがまま', 'ご機嫌','淡白', '淡泊', '機嫌', '性格', '癇癪', '苛', '無口', '愛想', '利口', '頑', '礼儀', '高圧']  
ningen_list =['女', '男', '仲良し', 'お互い', '人', '他人', '自分', '本人', '相手', '女性', '男性', '彼氏', '独身', '年上', '男女', '女子', '既婚', '年下', '大人', '友達', '友人', '先輩', '仲', '同士', '同僚', '親友', '後輩', '知人', '仲間']  
spiritual_list = ['神社', '運', '腹帯', 'お寺', '神様', 'お札', '風水', '仏壇', '縁起', '厄払い', '夢占']  
moji_list = ['漫画', '作品', '物語', '人物', '胸糞', '表紙', '作家', '未読', '巻', '小説' , '画数', '字画', '異体', '総画', '部首', '書体', '字体', '言葉', '漢字', '文章', '文字', '英語', '単語', '歌詞', '敬語', '口頭', '言語', '母音', '声門', '子音', '鼻音', '唇音', '口蓋', '助詞'] 
gokan_list = ['音量', '音程', '鼻声', '歌声', '声量', '鼻歌', '低音', '曲調', '音色', '地声', '出汁', '風味', '後味', '水気', '甘み', '甘味', '塩味', '苦味', '酸味', '臭み', '声', '悲鳴', '音', '大声', '泣き声', '奇声', '拍手', '騒音', '物音', '足音', '鏡', '眼鏡', '視力', '顕微', '視界', '眼', '遠目', '対物', '肉眼', '目視'] 
energy_list = ['ガス', '水道', '栓', '蛇口', '管', '下水', '温水', '用水', '給湯', '上水', '水槽', '冷水', '氷水', '流水', '海水', '真水', '水圧', '水温', '塩水', '水流', '水位', '流量', '水量', '水質', '強火', '弱火', '中火', '予熱', '余熱', '熱性' ]  
color_list = ['茶色', '黒', '白', '赤', '黄色', '緑', '青', '緑色', '紫', '水色']  
neg_list =  ['口', '愚痴', '一言', '長文', '無言', '本音', '冗談', '悪口', '悪気', '弱音', 'イヤ', '限界', '最悪', '理想', '最高', '苦痛', '現実', '常識', '無知', '憂鬱']  
ninpu_list = ['つわり', '小児科', '新生児', '帝王切開', '産婦人科', '寝返り', '吐き気', '夜泣き', 'ホルモン', '経産婦']  
hogaku_list =['下', '周り', '横', '隣', '右', '後ろ', '左', '付近', '奥', '裏', '北方', '南部', '南', '北', '中部', '東', '東部', '北部', '西', '西部', '上', '先']  
kotsu_list =  ['道路', '私道', '歩道', '車道', '側溝', '公道', '縁石', '道幅', '路肩', '車間', '階段', '上り', '坂', '坂道', '登り', '昇り', '下り', '勾配', '階数'] 
komono_list =['綿棒', '蓋', '鍋', '缶', '瓶', '湯船', '容器', 'パンツ', 'マスク', 'スプーン', 'セット', 'シート', 'マット', '紐', '荷物', '財布', '袋', '鍵', '通帳', '水筒', '箱', '傘', '箸']
kanjo_list = ['大笑い', '怒り', '悪意', '不満', '殺意', '偏見', '罪悪', '不信', '鬱憤', '恨み', '敵意', '泣', '感じ', '気', '楽しみ', 'ショック', 'すき', '気持ち']  
eiyo_list= ['水分', '糖', '塩分', '果汁', '糖分', '脂質', '油分', '果糖', '糖度', '葉酸', '鉄分', '亜鉛'] 
suchi_list = ['サイズ', '打率', 'プラス', '体重', '量', '距離', '回数', '金額', '収入', '頻度', '人数', '確率', '数値', '検量']
bunka_list =['短冊', '粗品', '行事', '両家', '式', '葬儀', '法事', '葬式', '還暦', '喜寿', '米寿', '古希', 'お中元','内侍', '本陣', '無量', '冠者', '三方', '南都', '今上', '大安', '中道', '円座', '教派', '宗派', '女系', '男系','お盆', '初盆', '盆', '新盆', '花火']  
privacy_list = ['名前', '性別', '年齢', '名義', '住所', '苗字', '籍', '名字', '旧姓', '戸籍']
column = ['id','content','time']
#endregion

print(column)
column.extend(genre_list)

#print(column)

df = pd.DataFrame(columns=column)

print(df)

i = 0

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
    #print(ap)
    bps = ap.split(':')
    bp = bps[0]
    #print(bp)

    if bp < '06':
        tmp['time'] = 0
    elif bp < '12':
        tmp['time'] = 1
    elif bp < '18':
        tmp['time'] = 2
    else:
        tmp['time'] = 3

    #tmp['content'] = row['content']


    tmp['家族']= check(kazoku_list,row['content'])
    tmp['病気'] = check(byoki_list,row['content'])
    tmp['薬']= check(kusuri_list,row['content'])
    tmp['赤ちゃん']= check(akachan_list,row['content'])
    tmp['植物'] = check( shokubutu_list,row['content'])
    tmp['動物'] = check( dobutsu_list,row['content'])  
    tmp['病院'] = check( byoin_list,row['content'])  
    tmp['飲食'] = check( insyoku_list,row['content'])  
    tmp['仕事'] = check( shigoto_list,row['content'])  
    tmp['乗り物'] = check( norimono_list,row['content'])
    tmp['身体'] = check( karada_list,row['content'])  
    tmp['自然'] = check( shizen_list,row['content'])  
    tmp['時間'] = check( zikan_list,row['content'])  
    tmp['お金'] = check( okane_list,row['content'])  
    tmp['教育'] = check( kyoikuku_list,row['content']) 
    tmp['住宅'] = check( jutaku_list,row['content'])  
    tmp['衣類'] = check( irui_list,row['content'])  
    tmp['精神状態'] = check( seishin_list,row['content'])  
    tmp['場所'] = check(basyo_list,row['content'])  
    tmp['性格'] = check( seikaku_list,row['content'])  
    tmp['人間'] = check( ningen_list,row['content'])  
    tmp['スピリチュアル'] = check( spiritual_list,row['content'])  
    tmp['文字'] = check( moji_list,row['content'])  
    tmp['五感'] = check( gokan_list,row['content'])  
    tmp['エネルギー'] = check( energy_list,row['content'])  
    tmp['色'] = check( color_list,row['content'])  
    tmp['ネガティブ'] = check( neg_list,row['content'])  
    tmp['妊婦'] = check( ninpu_list,row['content'])  
    tmp['方角'] = check( hogaku_list,row['content'])  
    tmp['交通'] = check( kotsu_list,row['content'])  
    tmp['小物'] = check( komono_list,row['content'])
    tmp['栄養'] = check( eiyo_list,row['content'])  
    tmp['数値'] = check( suchi_list,row['content'])  
    tmp['文化'] = check( bunka_list,row['content'])  
    tmp['個人情報'] = check( privacy_list,row['content'])

    if tmp['家族']+ tmp['病気']+ tmp['薬']+    tmp['赤ちゃん']+    tmp['植物']+    tmp['動物']+    tmp['病院']+    tmp['飲食']+    tmp['仕事']+    tmp['乗り物']+    tmp['身体']+    tmp['自然']+    tmp['時間']+    tmp['お金']+    tmp['教育']+    tmp['住宅']+    tmp['衣類']+    tmp['精神状態']+    tmp['場所']+    tmp['性格']+    tmp['人間']+    tmp['スピリチュアル']+    tmp['文字']+    tmp['五感']+    tmp['エネルギー']+    tmp['色']+    tmp['ネガティブ']+    tmp['妊婦']+    tmp['方角']+    tmp['交通']+    tmp['小物']+    tmp['栄養']+    tmp['数値']+    tmp['文化']+    tmp['個人情報']> 1 :
        df = df.append(tmp,ignore_index=True)

    i = i+ 1
    print(i)


senti_df = pd.read_csv("senti_cluster_100000.tsv",delimiter="\t")

senti_df = senti_df.iloc[:,1:3]

eva_df = pd.merge(senti_df, df, how='inner', on='id')

print(df)
print(senti_df)
print(eva_df)

for index,row in eva_df.iterrows():
    if row['score'] >= 0:
        eva_df.at[index,'score'] = 1
    else:
        eva_df.at[index,'score'] = 0


eva_df.to_csv("result/sample_chukan.csv")





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