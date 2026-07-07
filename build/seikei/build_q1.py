# -*- coding: utf-8 -*-
"""
成蹊大学 経営学部 英語 — 大問Ⅰ 会話文空所補充 徹底攻略ドリル
（完全攻略マニュアル 第3部 大問タイプ別攻略ドリル ①）
学部別合格設計塾THINKING（合同会社ARC）

出典形式の再現: 2025年度 成蹊 大問Ⅰ
  = 1つの会話文に13空所。空所1〜6は Set A、7〜13は Set B の語群から一つずつ選ぶ。
    番号は各Set内で一度ずつ。不要な選択肢が各Setに2つ含まれる（Aは8択/6使用、Bは9択/7使用）。
本ドリルの英文・設問・選択肢はすべて完全オリジナル（過去問の転載なし）。

出力: kakomon/seikei-u/q1-dialogue-cloze.pdf
"""
import os, re
from html import escape as esc
from weasyprint import HTML

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "kakomon", "seikei-u", "q1-dialogue-cloze.pdf")
CIRC = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬"  # 1..13

def circ(n): return CIRC[n-1]

# =============================================================================
# 問題データ（データ駆動）
#   各 problem: setA/setB は「アルファベット順の選択肢リスト」
#   ans は blank番号(int) -> 正解の語(str)。正解語は必ず該当Setに含まれること。
# =============================================================================
PROBLEMS = [
{
 "id":"EX01", "level":"標準", "min":7, "title":"新しいクラブ",
 "scene":"サラ (Sara) とトム (Tom) が、新しく入ったクラブについて話している。",
 "lines":[
  ("Sara","Hi Tom. Someone told me you [[1]] a new club last week. Is that true?"),
  ("Tom","Yeah, I finally [[2]] to join the photography club. I'd been [[3]] about it for months."),
  ("Sara","Nice! How's it [[4]] so far?"),
  ("Tom","Really well. The other members are all friendly, and the club is [[5]] popular this year."),
  ("Sara","I've been [[6]] for a club too, but there are so many that I can't choose."),
  ("Tom","You should just [[7]] one and try it. You can always change later."),
  ("Sara","That's true. Do you think the photography club would [[8]] me as a beginner?"),
  ("Tom","Of course. Half the members had never [[9]] a camera before joining."),
  ("Sara","Really? That [[10]] a lot to me. I was worried I wasn't good enough."),
  ("Tom","Don't worry about that. What [[11]] is that you enjoy it."),
  ("Sara","Okay, you've [[12]] me. I'll come to the next meeting."),
  ("Tom","Great. I'm sure you won't [[13]] it."),
 ],
 "setA":["able","decided","doing","going","joined","looking","pretty","thinking"],
 "setB":["accept","choose","convinced","held","learned","matters","means","realize","regret"],
 "ans":{1:"joined",2:"decided",3:"thinking",4:"going",5:"pretty",6:"looking",
        7:"choose",8:"accept",9:"held",10:"means",11:"matters",12:"convinced",13:"regret"},
 "exp":{
  1:("流れ・時制","last week があるので過去形。「クラブに入った」joined。"),
  2:("文法","finally｜過去形＋to do。「（ようやく）入ろうと決めた」decided to join。"),
  3:("コロケーション","had been ＋ -ing。think about ～「～について考える」の thinking。"),
  4:("イディオム","How's it going?「調子はどう？」定型。doing は不可。"),
  5:("品詞・語法","形容詞 popular を強める副詞は pretty「かなり」のみ（able は形容詞で不可）。"),
  6:("コロケーション","have been ＋ -ing。look for ～「～を探す」の looking。"),
  7:("流れ","命令的な提案「一つ選んでみたら」＝choose。accept は空所8で使う。"),
  8:("流れ","「初心者の私を受け入れてくれる？」accept me。choose は使用済み。"),
  9:("文法","had never ＋過去分詞。hold a camera「カメラを持つ／扱う」の held。"),
  10:("イディオム","That means a lot to me.「それは私にとって大きな意味がある」。"),
  11:("構文","What matters is that ...「大事なのは～ということ」。means は空所10で使用済み。"),
  12:("流れ","「あなたに説得された（から行く）」you've convinced me。"),
  13:("流れ","won't ＋原形。「後悔しないよ」won't regret it。"),
 },
 "distractorNote":"Set A 不要: able / doing（able は「〜できる」で文が成立せず、doing は going の紛らわしい罠）。"
                  "Set B 不要: learned / realize（意味・語法上どの空所にも入らない）。",
 "trans":"サラ「トム、先週新しいクラブに入ったって聞いたけど、本当？」／トム「うん、ついに写真部に入ることにしたんだ。"
         "何ヶ月も考えてたからね」／サラ「いいね！今のところ調子はどう？」／トム「すごくいいよ。メンバーはみんな親切だし、"
         "今年は部がかなり人気なんだ」／サラ「私もクラブを探してるんだけど、多すぎて選べなくて」／トム「とりあえず一つ選んで"
         "試してみたら。あとで変えられるし」／サラ「確かに。写真部は初心者の私でも受け入れてくれるかな？」／トム「もちろん。"
         "メンバーの半分は入る前カメラを触ったこともなかったよ」／サラ「そうなの？それを聞いて安心した。下手すぎるかもって"
         "心配だったの」／トム「気にしないで。大事なのは楽しむことだよ」／サラ「わかった、説得されたよ。次のミーティング行く」"
         "／トム「よかった。きっと後悔しないよ」",
},
{
 "id":"EX02", "level":"標準", "min":7, "title":"カフェのアルバイト",
 "scene":"ニナ (Nina) とレオ (Leo) が、レオの新しいアルバイトについて話している。",
 "lines":[
  ("Nina","Leo, someone said you [[1]] working at the café last month. Is that right?"),
  ("Leo","Yeah. I [[2]] to apply because I needed some experience. How's it [[3]], you ask? Actually, pretty good."),
  ("Nina","Were you [[4]] on your first day?"),
  ("Leo","A little. I was [[5]] worried about making mistakes, and I'm still [[6]] to the early schedule."),
  ("Nina","So, what [[7]] you to apply there?"),
  ("Leo","A friend [[8]] the place to me. She said the manager really [[9]] the staff well."),
  ("Nina","That [[10]] a big difference. A good manager is hard to [[11]]."),
  ("Leo","Definitely. Working there has already [[12]] me a lot, and it's [[13]] me want to do my best."),
 ],
 "setA":["adjusting","advice","going","nervous","pretty","spoken","started","wanted"],
 "setB":["find","found","gives","led","made","makes","recommended","taught","treats"],
 "ans":{1:"started",2:"wanted",3:"going",4:"nervous",5:"pretty",6:"adjusting",
        7:"led",8:"recommended",9:"treats",10:"makes",11:"find",12:"taught",13:"made"},
 "exp":{
  1:("語法","start ＋ -ing「〜し始める」。started working。wanted は working を続けられない。"),
  2:("文法","過去形＋to do。「応募しようと思った」wanted to apply。"),
  3:("イディオム","How's it going?「調子はどう？」。"),
  4:("品詞","be動詞の後は形容詞。「緊張した？」nervous。"),
  5:("品詞・語法","worried（形容詞）を強める副詞は pretty のみ。"),
  6:("コロケーション","be still ＋ -ing。adjust to ～「～に慣れる」の adjusting。"),
  7:("語法","what ＋ V ＋ 人 ＋ to do「何が人に～させたか」。lead 人 to do の led。"),
  8:("語法","recommend A to B「AをBに勧める」。led は空所7で使用済み。"),
  9:("流れ・時制","現在の話。treat ～ well「～を大切に扱う」の treats。"),
  10:("イディオム","make a difference「違いを生む／重要だ」の makes。"),
  11:("語法","hard to ＋原形。「見つけるのが難しい」find。found（過去/設立）は形が不適。"),
  12:("流れ","has already ＋過去分詞。teach 人 a lot「多くを教える」の taught。"),
  13:("語法","it's（＝it has）＋過去分詞。make 人 do の made（makes は使用済み）。"),
 },
 "distractorNote":"Set A 不要: advice / spoken（名詞・不適切な過去分詞でどの空所にも入らない）。"
                  "Set B 不要: found / gives（found は原形 find（空所11）の形違いの罠、gives は make a difference 等の定型に合わず不要）。",
 "trans":"ニナ「レオ、先月カフェで働き始めたって聞いたけど本当？」／レオ「うん。経験が欲しくて応募しようと思ったんだ。"
         "調子はどうかって？実は結構いいよ」／ニナ「初日は緊張した？」／レオ「少しね。ミスするのがかなり心配だったし、"
         "まだ早番のシフトに慣れてる途中なんだ」／ニナ「そこに応募した決め手は？」／レオ「友達がその店を勧めてくれてね。"
         "店長がスタッフをすごく大切にしてくれるって」／ニナ「それは大きいね。いい店長ってなかなかいないから」／レオ「本当に。"
         "もう働きながらたくさん学んだし、もっと頑張ろうって気にさせてくれるんだ」",
},
{
 "id":"EX03", "level":"やや難", "min":8, "title":"グループ発表の準備",
 "scene":"マヤ (Maya) とダニエル (Daniel) が、授業のグループ発表の準備について話している。",
 "lines":[
  ("Maya","Daniel, have you [[1]] the slides yet?"),
  ("Daniel","Almost. I'm still [[2]] on the last two. The handout?"),
  ("Maya","I [[3]] care of that this morning. It just needs [[4]] once more."),
  ("Daniel","Perfect. And how's everything else [[5]]?"),
  ("Maya","It's [[6]] along nicely. We're almost ready."),
  ("Daniel","Good. Honestly, are you [[7]] about presenting in front of everyone?"),
  ("Maya","A bit. I think we should [[8]] the whole thing once more before Friday."),
  ("Daniel","I agree. Practice always helps. Do you [[9]]?"),
  ("Maya","Definitely. By the way, can you [[10]] the questions at the end? You're better at that."),
  ("Daniel","Sure, I'll [[11]] that part. And that's a good [[12]] — we should decide who does what."),
  ("Maya","Great. Then I'm [[13]] we'll do fine. Let's meet tomorrow."),
 ],
 "setA":["arrived","checking","coming","finished","going","spoken","took","working"],
 "setB":["agree","handle","listen","luck","nervous","point","practice","ready","sure"],
 "ans":{1:"finished",2:"working",3:"took",4:"checking",5:"going",6:"coming",
        7:"nervous",8:"practice",9:"agree",10:"handle",11:"handle",12:"point",13:"sure"},
 # 注: 11は handle を2回使えないため再設計（下記 fix 参照）
 "exp":{},  # placeholder; 下で上書き
 "distractorNote":"",
 "trans":"",
},
{
 "id":"EX04", "level":"標準", "min":7, "title":"届かない荷物",
 "scene":"エマ (Emma) とライアン (Ryan) が、オンライン注文した商品が届かない件について話している。",
 "lines":[
  ("Emma","Ryan, I [[1]] a jacket from an online shop last week, but it hasn't [[2]] yet."),
  ("Ryan","Really? How long have you been [[3]]?"),
  ("Emma","Five days. Maybe they sent it to the [[4]] address. Did you try [[5]] the package?"),
  ("Ryan","Not yet. It was [[6]] to come on Monday, right?"),
  ("Emma","Yes. What should I do?"),
  ("Ryan","You should [[7]] the seller first. Ask for a [[8]], or ask them to [[9]] it."),
  ("Emma","Good idea. I'll message them now."),
  ("Ryan","Wait — let me check the tracking page. What [[10]]? ... Oh, your order was [[11]] at customs."),
  ("Emma","Oh, that explains it."),
  ("Ryan","Yeah. Please be [[12]]. It should arrive [[13]]."),
 ],
 "setA":["arrived","missing","ordered","sent","supposed","tracking","waiting","wrong"],
 "setB":["angry","contact","delayed","happened","patient","refund","replace","soon","written"],
 "ans":{1:"ordered",2:"arrived",3:"waiting",4:"wrong",5:"tracking",6:"supposed",
        7:"contact",8:"refund",9:"replace",10:"happened",11:"delayed",12:"patient",13:"soon"},
 "exp":{
  1:("流れ","order A from an online shop「ネット店で注文する」。last week で過去形 ordered。"),
  2:("文法","hasn't ＋過去分詞（現在完了）。自動詞 arrive の arrived「まだ届いていない」。"),
  3:("コロケーション","have been ＋ -ing。wait「待つ」の waiting。"),
  4:("品詞・流れ","the ＋形容詞＋名詞。「間違った住所」the wrong address。"),
  5:("語法","try ＋ -ing「試しに～する」。track the package の tracking。"),
  6:("イディオム","be supposed to do「～するはずだ」の supposed。"),
  7:("流れ","should ＋原形。「まず売り手に連絡する」contact。"),
  8:("品詞","冠詞 a の後は名詞。ask for a refund「返金を求める」。"),
  9:("語法","ask them to ＋原形。「交換してもらう」replace it。"),
  10:("イディオム","What happened?「何があった？」過去形。"),
  11:("文法","was ＋過去分詞（受動）。「税関で止められた／遅れた」delayed。"),
  12:("品詞","be ＋形容詞。「辛抱強く待って」be patient。angry は意味が逆で不可。"),
  13:("品詞","動詞 arrive を修飾する副詞。「まもなく届く」soon。"),
 },
 "distractorNote":"Set A 不要: missing / sent（missing は名詞前で意味不成立、sent は現在完了の受動になっておらず不可）。"
                  "Set B 不要: angry / written（angry は文意に反し、written はどの空所にも語法上入らない）。",
 "trans":"エマ「ライアン、先週ネットでジャケットを注文したのに、まだ届かないの」／ライアン「本当？どれくらい待ってるの？」"
         "／エマ「5日。間違った住所に送られたのかも。荷物を追跡してみた？」／ライアン「まだ。月曜に届くはずだったよね？」"
         "／エマ「そう。どうすればいい？」／ライアン「まず売り手に連絡した方がいい。返金を求めるか、交換してもらうか」"
         "／エマ「いい考え。今メッセージ送る」／ライアン「待って、追跡ページを見てみる。何があったんだ…ああ、"
         "君の注文、税関で止まってるよ」／エマ「なるほど、それでか」／ライアン「うん。辛抱強く待って。まもなく届くはず」",
},
{
 "id":"EX05", "level":"やや難", "min":8, "title":"留学の相談",
 "scene":"オリビア (Olivia) とサム (Sam) が、来年の留学について話している。",
 "lines":[
  ("Olivia","Guess what — I'm [[1]] on studying abroad next year!"),
  ("Sam","That's exciting! Where?"),
  ("Olivia","I've been [[2]] about Canada or Australia, but I haven't [[3]] yet. It's [[4]] to choose."),
  ("Sam","Australia might be [[5]] because of the flights. But I'm more [[6]] in Canada myself."),
  ("Olivia","Same here. The main [[7]] is that I want to [[8]] my English there."),
  ("Sam","Makes sense. When do you have to [[9]]?"),
  ("Olivia","The [[10]] is in October, so I can't [[11]] it."),
  ("Sam","Can your family [[12]] it, though? Studying abroad isn't cheap."),
  ("Olivia","We've saved for years, so it's [[13]] the cost. This is my dream."),
 ],
 "setA":["cheaper","decided","going","hard","interested","planning","thinking","worried"],
 "setB":["afford","apply","deadline","enjoy","improve","miss","money","reason","worth"],
 "ans":{1:"planning",2:"thinking",3:"decided",4:"hard",5:"cheaper",6:"interested",
        7:"reason",8:"improve",9:"apply",10:"deadline",11:"miss",12:"afford",13:"worth"},
 "exp":{
  1:("語法","plan on ＋ -ing「～するつもり」の planning。going on は不可。"),
  2:("コロケーション","have been ＋ -ing。think about ～ の thinking。"),
  3:("文法","haven't ＋過去分詞。「まだ決めていない」decided。"),
  4:("語法","It's ＋形容詞＋to do。「選ぶのが難しい」hard。"),
  5:("品詞","might be ＋比較級。「（航空券のぶん）より安いかも」cheaper。"),
  6:("コロケーション","be interested in ～「～に興味がある」の interested。"),
  7:("品詞・流れ","The main reason is that ...「主な理由は～」。名詞 reason。"),
  8:("語法","want to ＋原形。improve my English「英語を伸ばす」。"),
  9:("流れ","have to ＋原形。「（いつ）出願するか」apply。"),
  10:("流れ","「（出願）締切は10月」the deadline。reason は空所7で使用済み。"),
  11:("語法","can't ＋原形。miss the deadline「締切を逃す」の miss。"),
  12:("流れ","「家族はその費用を出せる？」can ... afford it。"),
  13:("イディオム","be worth ＋名詞「～の価値がある」の worth。"),
 },
 "distractorNote":"Set A 不要: going / worried（going は plan on の後に来られず、worried はどの空所にも意味上入らない）。"
                  "Set B 不要: enjoy / money（enjoy は文意に合わず、money はどの空所の語法にも入らない）。",
 "trans":"オリビア「聞いて、来年留学するつもりなの！」／サム「いいね！どこに？」／オリビア「カナダかオーストラリアで"
         "考えてるんだけど、まだ決めてないの。選ぶのが難しくて」／サム「航空券のぶんオーストラリアの方が安いかもね。"
         "でも僕自身はカナダの方が興味あるな」／オリビア「私も。主な理由は、そこで英語を伸ばしたいから」／サム「なるほど。"
         "いつまでに出願するの？」／オリビア「締切が10月だから、逃せないの」／サム「でも家族はその費用を出せるの？"
         "留学は安くないよ」／オリビア「何年も貯めてきたから、その価値はある。これは私の夢なの」",
},
]

# --- EX03 は blank11 が handle 重複だったため、ここで正しく再定義（handle→take）---
PROBLEMS[2]["ans"] = {1:"finished",2:"working",3:"took",4:"checking",5:"going",6:"coming",
                      7:"nervous",8:"practice",9:"agree",10:"handle",11:"take",12:"point",13:"sure"}
PROBLEMS[2]["setB"] = ["agree","handle","listen","luck","nervous","point","practice","ready","sure","take"]
# Set B が10個になるので blank数(7)＋不要2＝9 に合わせて調整: take を入れ、listen を除外
PROBLEMS[2]["setB"] = ["agree","handle","luck","nervous","point","practice","ready","sure","take"]
PROBLEMS[2]["lines"] = [
  ("Maya","Daniel, have you [[1]] the slides yet?"),
  ("Daniel","Almost. I'm still [[2]] on the last two. The handout?"),
  ("Maya","I [[3]] care of that this morning. It just needs [[4]] once more."),
  ("Daniel","Perfect. And how's everything else [[5]]?"),
  ("Maya","It's [[6]] along nicely. We're almost ready."),
  ("Daniel","Good. Honestly, are you [[7]] about presenting in front of everyone?"),
  ("Maya","A bit. I think we should [[8]] the whole thing once more before Friday."),
  ("Daniel","I agree. Practice always helps. Do you [[9]]?"),
  ("Maya","Definitely. By the way, can you [[10]] the questions at the end? You're better at that."),
  ("Daniel","Sure, I'll [[11]] that part. And that's a good [[12]] — let's decide who does what."),
  ("Maya","Great. Then I'm [[13]] we'll do fine. Let's meet tomorrow."),
]
PROBLEMS[2]["ans"] = {1:"finished",2:"working",3:"took",4:"checking",5:"going",6:"coming",
                      7:"nervous",8:"practice",9:"agree",10:"handle",11:"take",12:"point",13:"sure"}
PROBLEMS[2]["exp"] = {
  1:("文法","have you ＋過去分詞。「スライドはもう終わった？」finished（took は have you took と言えず不可）。"),
  2:("コロケーション","be still ＋ -ing。work on ～「～に取り組む」の working。"),
  3:("イディオム","take care of ～「～を片付ける／担当する」の took（過去）。"),
  4:("語法","need ＋ -ing「～される必要がある（＝受動）」。check の checking「確認が要る」。"),
  5:("イディオム","How's everything going?「全部順調？」の going。"),
  6:("イディオム","come along「（物事が）進む」の coming。going は空所5で使用済み。"),
  7:("品詞","be ＋形容詞。「緊張してる？」nervous。"),
  8:("流れ","should ＋原形。「本番前にもう一度練習する」practice。"),
  9:("流れ","相手の意見への同意を求める「そう思わない？」Do you agree?"),
  10:("語法","「最後の質問に対応できる？」handle the questions。"),
  11:("流れ","「その部分は僕が引き受ける」I'll take that part（take は「担当する」）。handle は使用済み。"),
  12:("品詞・イディオム","a good point「いい指摘」の point（名詞）。"),
  13:("品詞","be ＋形容詞。I'm sure (that) ...「きっと～だと思う」の sure。"),
}
PROBLEMS[2]["distractorNote"] = ("Set A 不要: arrived / spoken（自動詞 arrived は目的語を取れず、spoken も語法上どの空所にも入らない）。"
  "Set B 不要: luck / ready（good luck! の luck や ready は、それぞれの空所の文脈・語法に合わない）。")
PROBLEMS[2]["trans"] = ("マヤ「ダニエル、スライドはもう終わった？」／ダニエル「ほぼね。最後の2枚に取り組んでる。配布資料は？」"
  "／マヤ「今朝片付けたよ。あと一度確認が要るだけ」／ダニエル「完璧。他は全部順調？」／マヤ「いい感じに進んでる。"
  "もうすぐ準備完了」／ダニエル「よし。正直、みんなの前で発表するの緊張してる？」／マヤ「少しね。金曜の前に一度"
  "通しで練習した方がいいと思う」／ダニエル「賛成。練習はいつも効くよ。そう思わない？」／マヤ「もちろん。ところで、"
  "最後の質問対応をお願いできる？あなたの方が得意だから」／ダニエル「いいよ、そこは引き受ける。あ、それいい指摘だね—"
  "誰が何をやるか決めよう」／マヤ「いいね。じゃあきっとうまくいくよ。明日会おう」")

# =============================================================================
# 構造検証（機械的ミスの検出）
# =============================================================================
def validate():
    for p in PROBLEMS:
        na = sum(1 for b in p["ans"] if b<=6)
        nb = sum(1 for b in p["ans"] if b>=7)
        assert na==6, f"{p['id']}: Set A blanks={na}"
        assert nb==7, f"{p['id']}: Set B blanks={nb}"
        assert len(p["setA"])==8, f"{p['id']}: setA options={len(p['setA'])}"
        assert len(p["setB"])==9, f"{p['id']}: setB options={len(p['setB'])}"
        assert p["setA"]==sorted(p["setA"]), f"{p['id']}: setA not alpha"
        assert p["setB"]==sorted(p["setB"]), f"{p['id']}: setB not alpha"
        usedA=[p["ans"][b] for b in range(1,7)]
        usedB=[p["ans"][b] for b in range(7,14)]
        assert len(set(usedA))==6, f"{p['id']}: Set A answer reused {usedA}"
        assert len(set(usedB))==7, f"{p['id']}: Set B answer reused {usedB}"
        for b,w in p["ans"].items():
            bank = p["setA"] if b<=6 else p["setB"]
            assert w in bank, f"{p['id']} blank{b}: '{w}' not in bank"
        # 本文の空所数
        text=" ".join(t for _,t in p["lines"])
        marks=set(int(x) for x in re.findall(r"\[\[(\d+)\]\]", text))
        assert marks==set(range(1,14)), f"{p['id']}: blanks in text={sorted(marks)}"
    print("validate: OK")

# =============================================================================
# デザインシステム
# =============================================================================
CSS = """
:root{
  --navy:#16263f; --navy-deep:#0e1a2e; --navy-soft:#1c3354;
  --gold:#b8954a; --gold-light:#d9c08a; --gold-deep:#9a7a36;
  --vermilion:#c8431f; --ink:#1f2933; --gray:#5b6672;
  --paper:#ffffff; --washi:#f7f4ee; --washi-2:#f1ece1; --line:#d8d2c4; --teal:#1e7a4f;
}
@page{
  size:A4; margin:19mm 15mm 16mm 15mm;
  @bottom-center{content:counter(page); font-family:"Noto Sans CJK JP"; font-size:8.5pt; color:#8a8273;}
  @top-left{content:"成蹊大学 経営学部 英語 大問Ⅰ 会話文空所補充 徹底攻略ドリル"; font-family:"Noto Sans CJK JP"; font-size:7.4pt; color:#a89f8c; letter-spacing:.03em;}
  @top-right{content:"学部別合格設計塾THINKING"; font-family:"Noto Serif CJK JP"; font-size:7.3pt; letter-spacing:.12em; color:#b8954a;}
}
@page cover{ margin:0; @bottom-center{content:none;} @top-left{content:none;} @top-right{content:none;} }

*{ box-sizing:border-box; }
body{ font-family:"Noto Serif CJK JP", serif; font-size:10pt; line-height:1.85; color:var(--ink); margin:0; padding:0; }
p{ margin:0 0 .7em; text-align:justify; }
strong{ font-weight:700; }
.sans{ font-family:"Noto Sans CJK JP", sans-serif; }

/* 表紙 */
.cover{ page:cover; position:relative; width:210mm; height:297mm; overflow:hidden;
  background:linear-gradient(150deg, var(--navy-deep) 0%, var(--navy) 55%, var(--navy-soft) 100%); color:#fff; }
.cover .frame{ position:absolute; inset:12mm; border:0.6pt solid rgba(217,192,138,.38); }
.cover .frame2{ position:absolute; inset:13.4mm; border:0.4pt solid rgba(217,192,138,.20); }
.cover .brandtop{ position:absolute; top:20mm; left:0; right:0; text-align:center;
  font-family:"Noto Sans CJK JP"; font-size:9.5pt; letter-spacing:.42em; color:var(--gold-light); text-indent:.42em; }
.cover .seal{ position:absolute; top:20mm; right:20mm; writing-mode:vertical-rl; border:1pt solid var(--gold-light);
  color:var(--gold-light); font-family:"Noto Serif CJK JP"; font-weight:700; font-size:12pt; letter-spacing:.34em;
  padding:7mm 3.2mm; line-height:1; background:rgba(14,26,46,.28); }
.cover .center{ position:absolute; top:99mm; left:20mm; right:20mm; }
.cover .kicker{ font-family:"Noto Sans CJK JP"; font-size:11pt; letter-spacing:.28em; color:var(--gold-light); margin-bottom:7mm; text-indent:.28em; }
.cover h1{ font-family:"Noto Serif CJK JP"; font-weight:900; font-size:36pt; line-height:1.28; margin:0; letter-spacing:.02em; }
.cover h1 .q{ color:var(--gold-light); }
.cover .rule{ height:2.4pt; width:64mm; background:var(--gold); margin:8mm 0 7mm; }
.cover .subject{ font-family:"Noto Sans CJK JP"; font-size:14pt; letter-spacing:.16em; color:#eef2f7; }
.cover .voltag{ display:inline-block; margin-top:9mm; border:0.8pt solid var(--gold-light); padding:2.4mm 6mm;
  font-family:"Noto Sans CJK JP"; font-size:11pt; letter-spacing:.12em; color:var(--gold-light); }
.cover .subtitle{ margin-top:6mm; font-size:12pt; color:#d7dee7; letter-spacing:.05em; }
.cover .philo{ position:absolute; bottom:36mm; left:20mm; right:20mm; text-align:center;
  font-family:"Noto Serif CJK JP"; font-size:11pt; color:#cfd7e1; letter-spacing:.10em; }
.cover .lock{ position:absolute; bottom:20mm; left:20mm; right:20mm; text-align:center; }
.cover .lock .mark{ font-family:"Noto Serif CJK JP"; font-weight:900; font-size:15pt; letter-spacing:.10em; color:#fff; }
.cover .lock .arc{ font-family:"Noto Sans CJK JP"; font-size:8.2pt; letter-spacing:.30em; color:var(--gold-light); margin-top:3mm; }

/* 章扉・見出し */
.chapter-open{ break-before:page; margin:0 0 7mm; }
.chapter-open.first{ break-before:auto; }
.chapter-open .band{ background:var(--navy); color:#fff; padding:6.5mm 7mm 6mm; border-left:3pt solid var(--gold); }
.chapter-open .cno{ font-family:"Noto Sans CJK JP"; font-size:9pt; letter-spacing:.30em; color:var(--gold-light); }
.chapter-open .ctitle{ font-family:"Noto Serif CJK JP"; font-weight:900; font-size:18pt; margin-top:2.5mm; line-height:1.3; }
.chapter-open .clead{ font-size:9.4pt; color:var(--gray); margin-top:4mm; line-height:1.8; }
h2.sec{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:12.5pt; color:var(--navy); margin:8mm 0 3.5mm;
  padding-bottom:1.8mm; border-bottom:1.6pt solid var(--gold); break-after:avoid; }
h3.sub{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:10.4pt; color:var(--navy-soft); margin:6mm 0 2.5mm;
  padding-left:3mm; border-left:3pt solid var(--gold-light); break-after:avoid; }
.lead{ font-size:9.8pt; color:#333; margin-bottom:4mm; }

/* 枠 */
.box{ padding:4mm 5mm; margin:4mm 0; border-radius:1.2mm; break-inside:avoid; }
.box .bt{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9.6pt; margin-bottom:2mm; letter-spacing:.04em; }
.box p{ font-size:9.2pt; line-height:1.75; }
.box.warn{ background:#fbf1ee; border:0.5pt solid #e6bcae; border-left:3pt solid var(--vermilion); }
.box.warn .bt{ color:var(--vermilion); }
.box.ok{ background:#eef6f1; border:0.5pt solid #b7d9c6; border-left:3pt solid var(--teal); }
.box.ok .bt{ color:var(--teal); }
.box.gold{ background:var(--washi); border:0.5pt solid var(--gold-light); border-left:3pt solid var(--gold); }
.box.gold .bt{ color:var(--gold-deep); }
.box.navy{ background:var(--washi-2); border:0.5pt solid var(--line); border-left:3pt solid var(--navy); }
.box.navy .bt{ color:var(--navy); }

ol.steps{ margin:2mm 0 3mm; padding-left:5.6mm; }
ol.steps li{ font-size:9.4pt; line-height:1.7; margin-bottom:1.6mm; }
ol.steps li b{ font-family:"Noto Sans CJK JP"; color:var(--navy); }

/* 問題ヘッダ */
.phead{ break-inside:avoid; break-after:avoid; margin:0 0 3mm; display:flex; align-items:center; gap:3mm;
  border-bottom:1.6pt solid var(--navy); padding-bottom:2mm; }
.phead .id{ font-family:"Noto Sans CJK JP"; font-weight:900; font-size:13pt; color:#fff; background:var(--navy);
  padding:1mm 3.2mm; border-radius:1mm; letter-spacing:.03em; }
.phead .tt{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:12pt; color:var(--navy); }
.phead .meta{ margin-left:auto; font-family:"Noto Sans CJK JP"; font-size:8.4pt; color:var(--gray); }
.phead .meta .lv{ color:var(--gold-deep); font-weight:700; }
.scene{ font-size:9.2pt; color:var(--gray); margin:0 0 3mm; }
.instr{ font-size:8.8pt; color:var(--ink); background:var(--washi); border:0.4pt solid var(--line);
  padding:2.6mm 3.4mm; border-radius:1mm; margin:0 0 4mm; line-height:1.7; }

/* 会話 */
.dlg{ margin:0 0 4mm; }
.dlg .ln{ display:flex; gap:2.5mm; margin-bottom:2.2mm; break-inside:avoid; font-family:"Noto Serif CJK JP"; }
.dlg .sp{ flex:0 0 17mm; font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9.3pt; color:var(--navy-soft); text-align:right; }
.dlg .tx{ flex:1; font-size:9.9pt; line-height:1.95; }
.blank{ display:inline-block; min-width:9mm; text-align:center; border:0.7pt solid var(--navy);
  border-radius:.8mm; padding:0 1.4mm; font-family:"Noto Sans CJK JP"; font-weight:700; font-size:8.8pt;
  color:var(--navy); background:#fff; line-height:1.5; vertical-align:baseline; }

/* 選択肢バンク */
.banks{ display:flex; gap:5mm; margin:2mm 0 0; break-inside:avoid; }
.bank{ flex:1; border:0.5pt solid var(--line); border-radius:1.2mm; overflow:hidden; }
.bank .bh{ background:var(--navy-soft); color:#fff; font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9pt;
  padding:1.8mm 3mm; letter-spacing:.04em; }
.bank .bg{ padding:2.6mm 3mm; column-count:2; column-gap:4mm; }
.opt{ font-family:"Noto Serif CJK JP"; font-size:9.3pt; line-height:1.85; break-inside:avoid; }
.opt .cn{ font-family:"Noto Sans CJK JP"; color:var(--gold-deep); font-weight:700; margin-right:.6mm; }

/* 解答解説 */
.akey{ break-inside:avoid; margin:1mm 0 4mm; border:0.5pt solid var(--line); border-radius:1.2mm; overflow:hidden; }
.akey .kh{ background:var(--teal); color:#fff; font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9pt; padding:1.6mm 3mm; }
.akey .kg{ display:flex; flex-wrap:wrap; padding:2.4mm 3mm; gap:1.4mm 2mm; }
.akey .k{ font-family:"Noto Sans CJK JP"; font-size:8.9pt; background:var(--washi); border:0.4pt solid var(--line);
  border-radius:.8mm; padding:.6mm 2mm; white-space:nowrap; }
.akey .k b{ color:var(--navy); }
.akey .k .w{ color:var(--teal); font-weight:700; }

table.exp{ width:100%; border-collapse:collapse; margin:2mm 0 3mm; font-size:8.9pt; break-inside:auto; }
table.exp th{ background:var(--navy); color:#fff; font-family:"Noto Sans CJK JP"; font-weight:500; padding:2mm 2.4mm; text-align:left; }
table.exp td{ padding:2mm 2.4mm; border:0.4pt solid var(--line); vertical-align:top; line-height:1.6; }
table.exp tr:nth-child(even) td{ background:var(--washi); }
table.exp .bn{ text-align:center; font-family:"Noto Sans CJK JP"; font-weight:700; color:var(--navy); white-space:nowrap; }
table.exp .aw{ font-family:"Noto Sans CJK JP"; font-weight:700; color:var(--teal); white-space:nowrap; }
table.exp .tg{ font-family:"Noto Sans CJK JP"; font-size:7.8pt; color:var(--gold-deep); white-space:nowrap; }
.transbox{ font-size:8.8pt; color:#3a3a3a; background:var(--washi); border:0.4pt solid var(--line);
  border-radius:1mm; padding:3mm 3.6mm; margin:3mm 0 2mm; line-height:1.85; break-inside:avoid; }
.transbox .tl{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:8.6pt; color:var(--navy); margin-bottom:1.5mm; }

ul.check{ list-style:none; margin:2.5mm 0; padding:0; }
ul.check li{ font-family:"Noto Sans CJK JP"; font-size:9.2pt; line-height:1.7; padding-left:6mm; position:relative; margin-bottom:1.6mm; }
ul.check li::before{ content:"\\2610"; position:absolute; left:0; color:var(--gold-deep); font-size:10.5pt; }
.divider-note{ font-size:8pt; color:var(--gray); border-top:0.4pt solid var(--line); padding-top:2mm; margin-top:6mm; }

table.data{ width:100%; border-collapse:collapse; margin:3mm 0 4mm; font-size:8.9pt; }
table.data th{ background:var(--navy); color:#fff; font-family:"Noto Sans CJK JP"; font-weight:500; padding:2.2mm 2.6mm; text-align:left; }
table.data td{ padding:2mm 2.6mm; border:0.4pt solid var(--line); vertical-align:top; line-height:1.6; }
table.data tr:nth-child(even) td{ background:var(--washi); }
table.data .em{ font-family:"Noto Sans CJK JP"; font-weight:700; color:var(--navy); }
"""

# =============================================================================
# レンダリング
# =============================================================================
def cover():
    return """
<section class="cover">
  <div class="frame"></div><div class="frame2"></div>
  <div class="brandtop">学部別合格設計塾 THINKING</div>
  <div class="seal">大問一</div>
  <div class="center">
    <div class="kicker">成蹊大学 経営学部 英語</div>
    <h1>大問<span class="q">Ⅰ</span> 会話文<br>空所補充<br><span style="font-size:22pt;">徹底攻略ドリル</span></h1>
    <div class="rule"></div>
    <div class="subject">Set A / Set B 型 完全対応・成蹊型オリジナル演習</div>
    <div class="voltag">第 3 部 ①</div>
    <div class="subtitle">大問タイプ別攻略ドリル</div>
  </div>
  <div class="philo">受験は、根性じゃなく、設計。</div>
  <div class="lock">
    <div class="mark">学部別合格設計塾 THINKING</div>
    <div class="arc">GOUDOU KAISHA ARC &nbsp;/&nbsp; JUKENNO OUSAMA</div>
  </div>
</section>
"""

def render_dialogue(p):
    rows=""
    for sp,tx in p["lines"]:
        h=esc(tx)
        for n in range(1,14):
            h=h.replace(f"[[{n}]]", f'<span class="blank">{n}</span>')
        rows+=f'<div class="ln"><div class="sp">{esc(sp)}:</div><div class="tx">{h}</div></div>'
    return f'<div class="dlg">{rows}</div>'

def render_bank(title, opts):
    items="".join(f'<div class="opt"><span class="cn">{circ(i+1)}</span>{esc(w)}</div>' for i,w in enumerate(opts))
    return f'<div class="bank"><div class="bh">{title}</div><div class="bg">{items}</div></div>'

def render_problem(p):
    instr=('次の会話文の空所に入る語句として最も適切なものを、空所 <b>1〜6</b> については Set A、'
           '空所 <b>7〜13</b> については Set B の中からそれぞれ一つずつ選びなさい。'
           'なお、Set A と Set B 内の番号はどちらも一度ずつしか使えず、不要な選択肢がそれぞれ二つずつ含まれている。')
    return f"""
<section>
  <div class="phead">
    <span class="id">演習 {p['id'][-2:]}</span>
    <span class="tt">{esc(p['title'])}</span>
    <span class="meta"><span class="lv">{esc(p['level'])}</span>　目標 {p['min']}分</span>
  </div>
  <div class="scene">場面：{esc(p['scene'])}</div>
  <div class="instr">{instr}</div>
  {render_dialogue(p)}
  <div class="banks">
    {render_bank("Set A （空所 1〜6）", p['setA'])}
    {render_bank("Set B （空所 7〜13）", p['setB'])}
  </div>
</section>
"""

def render_answer(p):
    # 正解キー
    keys=""
    for b in range(1,14):
        w=p["ans"][b]; bank=p["setA"] if b<=6 else p["setB"]; num=bank.index(w)+1
        keys+=f'<span class="k"><b>{b}</b> <span class="w">{circ(num)} {esc(w)}</span></span>'
    # 解説表
    rows=""
    for b in range(1,14):
        w=p["ans"][b]; bank=p["setA"] if b<=6 else p["setB"]; num=bank.index(w)+1
        tag,txt=p["exp"][b]
        rows+=(f'<tr><td class="bn">{b}</td><td class="aw">{circ(num)} {esc(w)}</td>'
               f'<td class="tg">{esc(tag)}</td><td>{txt}</td></tr>')
    return f"""
<section>
  <div class="phead">
    <span class="id">演習 {p['id'][-2:]}</span>
    <span class="tt">解答・解説 — {esc(p['title'])}</span>
    <span class="meta">全13空所</span>
  </div>
  <div class="akey"><div class="kh">正解キー</div><div class="kg">{keys}</div></div>
  <table class="exp">
    <tr><th style="width:8%">空所</th><th style="width:16%">正解</th><th style="width:14%">根拠</th><th>解説</th></tr>
    {rows}
  </table>
  <div class="box warn" style="margin-top:3mm;"><div class="bt">不要な選択肢（各Set2つ）</div><p>{p['distractorNote']}</p></div>
  <div class="transbox"><div class="tl">日本語訳</div>{esc(p['trans'])}</div>
</section>
"""

# =============================================================================
# 前付け・攻略・巻末
# =============================================================================
def intro():
    return """
<section>
  <div class="chapter-open first">
    <div class="band">
      <div class="cno">大問Ⅰ 徹底攻略 &nbsp;/&nbsp; TYPE A DRILL</div>
      <div class="ctitle">「Set型・会話補充」を、手順で刈り取る</div>
      <div class="clead">成蹊の大問Ⅰは、13の空所を2つの語群（Set A・Set B）から埋める会話補充。1問1問の難度は高くないが、"不要選択肢"と"連鎖ミス"で崩れる受験生が後を絶たない。本書は解く手順を固定し、確実に満点近くを取りにいくための実戦ドリルである。</div>
    </div>
  </div>
  <p class="lead">まず大問Ⅰの正体を数字で押さえる。ここは<strong>速く確実に取り切る「取り所」</strong>だ（全体戦略は第1部を参照）。</p>
  <table class="data">
    <tr><th style="width:20%">項目</th><th>中身</th></tr>
    <tr><td class="em">形式</td><td>1つの会話文に空所13。空所1〜6は Set A、7〜13は Set B の語群から選ぶ。</td></tr>
    <tr><td class="em">選択肢</td><td>Set A ＝ 8択で6使用（不要2）／Set B ＝ 9択で7使用（不要2）。番号は各Set内で一度ずつ。</td></tr>
    <tr><td class="em">語の性質</td><td>選択肢は単語・短い語句。品詞・活用形・コロケーションで正解が一つに決まる設計。</td></tr>
    <tr><td class="em">狙われる力</td><td>会話の流れ＋文法枠＋定型表現（イディオム／コロケーション）の三点セット。</td></tr>
  </table>

  <h2 class="sec">なぜ崩れるのか ― 3つの罠</h2>
  <div class="box warn"><div class="bt">罠① 不要選択肢を"使い切ろう"としてしまう</div>
    <p>各Setに正解より2つ多い選択肢がある。「全部使うはず」と思い込むと、無理な空所にねじ込んで玉突きで崩れる。<strong>不要は必ず2つ残る</strong>と最初から知っておく。</p></div>
  <div class="box warn"><div class="bt">罠② 品詞・活用形を無視して"意味だけ"で選ぶ</div>
    <p>makes と making、find と found のような形違いが同じSetに並ぶ。空所の前後（be動詞・完了形・to・needs＋-ing など）を見れば形は一つに絞れる。意味の前に<strong>形</strong>を見る。</p></div>
  <div class="box warn"><div class="bt">罠③ 連鎖ミス ― 1つのズレが全体を倒す</div>
    <p>番号は一度ずつ。1箇所を誤った語で埋めると、正解の語が別の空所で足りなくなり連鎖崩壊する。<strong>確信度の高い空所から固定</strong>し、迷う空所は最後に回す。</p></div>

  <h2 class="sec">5ステップ解法 ― これを毎回まわす</h2>
  <ol class="steps">
    <li><b>① 品詞タグ付け</b>：先に選択肢群を名詞／動詞（原形・過去・過去分詞・-ing）／形容詞・副詞に仕分ける。</li>
    <li><b>② 文法枠で候補を絞る</b>：空所の直前直後を見る。be＋□→形容詞/-ing、have＋□→過去分詞、to＋□→原形、needs＋□→-ing、冠詞a＋□→名詞。</li>
    <li><b>③ 確信空所から固定</b>：イディオム・コロケーション（How's it going? / look for / a lot / be supposed to など）で一発で決まる空所を先に埋める。</li>
    <li><b>④ 会話の論理で意味を確定</b>：賛否・因果・言い換えの流れで、残りの意味を詰める。</li>
    <li><b>⑤ 不要2つを検算</b>：使わなかった選択肢がちょうど2つか、各Setで確認。合わなければどこかで連鎖ミス。</li>
  </ol>

  <div class="box gold"><div class="bt">覚えておく会話の定型（本ドリルで反復する）</div>
    <p>How's it going?（調子はどう）／ look for ～（探す）／ think about ～（考える）／ be supposed to do（～のはず）／ make a difference（重要だ）／ mean a lot（大きな意味を持つ）／ What matters is ...（大事なのは）／ take care of ～（片付ける）／ be worth ～（価値がある）／ can't afford ～（～する余裕がない）。</p></div>

  <div class="box navy"><div class="bt">本ドリルの使い方</div>
    <p>演習は<strong>問題編</strong>（演習01〜05）→<strong>解答解説編</strong>の順。まず時間を計って問題編を解き、答え合わせは解説編でまとめて行う。各空所には「根拠」（流れ／文法／コロケーション等）を明示した。<strong>なぜその形・その語なのか</strong>を言語化できるまで反復すれば、本番の大問Ⅰは"作業"になる。英文・設問・選択肢はすべて成蹊の形式を再現した完全オリジナルで、過去問の転載はない。</p></div>
</section>
"""

def problem_section_header():
    return """
<section>
  <div class="chapter-open">
    <div class="band">
      <div class="cno">PART 1 &nbsp;/&nbsp; PROBLEMS</div>
      <div class="ctitle">問題編 ― 演習 01〜05</div>
      <div class="clead">時間を計って解く。1題ずつ、目標時間内で。答えは書き込まず、解答解説編でまとめて照合する。連鎖ミスを避けるため、確信空所から固定すること。</div>
    </div>
  </div>
</section>
"""

def answer_section_header():
    return """
<section>
  <div class="chapter-open">
    <div class="band">
      <div class="cno">PART 2 &nbsp;/&nbsp; ANSWERS &amp; EXPLANATIONS</div>
      <div class="ctitle">解答解説編 ― 演習 01〜05</div>
      <div class="clead">正解の"根拠"を毎回言語化する。形（品詞・活用）→ コロケーション → 会話の流れ、の順で確認し、不要選択肢2つがなぜ残るかまで説明できるようにする。</div>
    </div>
  </div>
</section>
"""

def outro():
    return """
<section>
  <div class="chapter-open">
    <div class="band">
      <div class="cno">仕上げ &nbsp;/&nbsp; WRAP-UP</div>
      <div class="ctitle">大問Ⅰ 習熟チェックリスト</div>
      <div class="clead">5題を解き終えたら、次の項目を自分の言葉で説明できるか確認する。できなければ、その罠に当たる空所へ戻る。</div>
    </div>
  </div>
  <ul class="check">
    <li>Set A＝8択で6使用、Set B＝9択で7使用、不要が各2つ残る ― と即答できる</li>
    <li>be＋□／have＋□／to＋□／needs＋□／a＋□ で、入る品詞・活用を反射的に絞れる</li>
    <li>How's it going? / look for / be supposed to / make a difference などの定型を"見た瞬間"に埋められる</li>
    <li>makes↔making、find↔found のような形違いの罠を、前後の形で切れる</li>
    <li>確信空所から固定し、迷う空所を最後に回す手順が身についている</li>
    <li>解き終わりに「不要2つ」を検算して連鎖ミスを自己検出できる</li>
  </ul>
  <div class="box ok"><div class="bt">得点イメージ</div>
    <p>大問Ⅰは13マーク。ここを手順化して<strong>10〜12マーク</strong>を安定させれば、前半の"取り所"として大きな貯金になる（第1部の合格点設計を参照）。1問1分弱で処理し、浮いた時間を長文（大問Ⅱ・Ⅲ）に回すのが勝ち筋だ。</p></div>
  <div class="box gold"><div class="bt">次の一手</div>
    <p>会話補充の地力は語彙・定型表現の量に比例する。第2部（語彙・語法・テーマ対策大全）でコロケーションと同義語のネットワークを厚くし、本ドリルを反復せよ。設計＋反復が、大問Ⅰを"落とさない大問"に変える。</p></div>
  <div class="divider-note">
    学部別合格設計塾THINKING（合同会社ARC）／成蹊大学 経営学部 英語 大問Ⅰ 会話文空所補充 徹底攻略ドリル。
    本書の英文・設問・選択肢はすべて成蹊の出題形式を再現した完全オリジナルであり、実際の過去問の転載は一切ない。
  </div>
</section>
"""

def build():
    validate()
    problems="".join(render_problem(p) for p in PROBLEMS)
    answers="".join(render_answer(p) for p in PROBLEMS)
    html=f"""<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
{cover()}
{intro()}
{problem_section_header()}
{problems}
{answer_section_header()}
{answers}
{outro()}
</body></html>"""
    os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
    HTML(string=html).write_pdf(os.path.abspath(OUT))
    print("WROTE", os.path.abspath(OUT))

if __name__=="__main__":
    build()
