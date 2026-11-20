import sys, importlib, pprint, re
from collections import Counter
S='/tmp/claude-0/-home-user-thinking-hp/fe35a45f-1f03-5054-8c22-5fcd44116fc2/scratchpad'
y=int(sys.argv[1]); yy=str(y)[2:]; D=f'{S}/mjl{yy}/content'
sys.path.insert(0,D+'/parts')
parts=[importlib.import_module(m).PART for m in ('part1','part2')]
official = y==2026
TOTAL=70; REVIEW=6
def pts(q): 
    m=re.match(r'(\d+)',str(q.get('points','1'))); return int(m.group(1)) if m else 1
def written(q): return any(k in q['type'] for k in ('記述','要約','書く','日本語','英語1語'))
rows=[]; plan=[]; diff=[]; nq=0; nm=0; nw=0; tot=0; words=0
avail=TOTAL-REVIEW; bw=sum(p['body_words'] for p in parts)
for i,p in enumerate(parts):
    qs=p['questions']; c=Counter(); w=0
    for q in qs:
        if written(q): w+=1
        else: c[q['type'].split('（')[0]]+=1
    m=len(qs)-w; nq+=len(qs); nm+=m; nw+=w; sp=sum(pts(q) for q in qs); tot+=sp; words+=p['body_words']
    mins=round(avail*p['body_words']/bw)
    if i==len(parts)-1: mins=avail-sum(int(r[5][:-1]) for r in rows)
    src=p['source'].split('（大学の冊子')[0]
    rows.append([p['no'], f"{p['title']}（{src}）", f"約{p['body_words']}語", f"マーク{m}（"+"、".join(f"{k}{v}" for k,v in c.items())+"）"+(f"＋記述{w}" if w else ""), f"{sp}【推定】", f"{mins}分"])
    plan.append([str(i+1), f"大問{p['no']}", f"{mins}分", p['types_note'][0][:80] if p.get('types_note') else "設問の順に、根拠の段落を絞りながら読む。"])
    for q in qs:
        if ('不一致' in q.get('checked','')) or written(q):
            diff.append([f"大問{p['no']} {q['id']}（{q['type']}）", q.get('intent','')[:120], "解説の「解く手順」どおりに、根拠の段落を特定してから答える。"+("（市販の解答と答えが異なる問題。解説に理由あり）" if '不一致' in q.get('checked','') else "")])
plan.append([str(len(parts)+1),"見直し・予備",f"{REVIEW}分","記述の字数・語数、マークずれを確認。"])
diff=diff[:5]
_wl={('日本語' if '日本語' in q['type'] else '英語') for p in parts for q in p['questions'] if written(q)}
WLANG='日本語や英語' if len(_wl)==2 else (next(iter(_wl)) if _wl else '')
book={
 "id": f"meiji-hogaku_{y}", "univ":"明治大学","faculty":"法学部","year":y,"subject":"英語",
 "cover_color":"#3b2a5e","cover_sub":"","footer_note":"",
 "howto":["問題冊子を印刷して手元に置いてください。この解説には問題文・英文本文を載せていません。設問の下線部と短い引用だけを示します。",
   "まず時間を計って通して解き、総まとめの解答一覧で採点してから、各大問の解説を読んでください。各大問は「この文章の正体 → 設問タイプと攻め方 → 英文マップ → 設問ごとの解説 → 全訳」の順です。",
   "落とした設問は、総まとめの「失点の型別の復習動線」で型（A〜E）に分け、型ごとに復習します。",
   ("正解は大学が公表した解答と照合しています。" if official else "大学はこの年度の解答を公表していません。正解は、市販の解答と、THINKINGで別に解いた答えを照合して決めました。")+"【推定】と書いた箇所は、公表資料で確かめられなかったTHINKINGの判断です（配点など）。"],
 "overview":{
   "lead": f"大問2つ。Iは{parts[0]['title']}、IIは{parts[1]['title']}。総語数は約{words:,}語と、1題が長い。設問は下線部の言い換え・英問英答・内容一致が中心で、{WLANG}で書く記述も含む。本文を段落ごとに要約しながら読み、設問の根拠の段落を素早く特定できるかで差がつく。",
   "exam_line": f"【試験時間】{TOTAL}分（要確認）　【大問数】2　【解答数】{nq}（マーク{nm}＋記述{nw}）　【配点】自己採点用に合計{tot}点（マーク各1点・記述各3点として。設問ごとの配点は非公表のため【推定】）",
   "structure_head":["大問","素材（出典）","語数","設問数","配点","目安時間"],
   "structure_cls":["c key nowrap","","c nowrap","","c nowrap","c nowrap"],
   "structure":rows,"time_plan":plan,"diff_points":diff,
   "notes":["※ 試験時間は大学の募集要項で確認してください。",
            "※ 設問ごとの配点は大学が公表していません。自己採点表の配点（マーク各1点・記述各3点）はTHINKINGの【推定】です。",
            "※ 語数は概算（±10％程度）です。"]},
 "parts":"__PARTS__",
 "summary":{"lead":"まず自己採点。落とした設問を「型」（A〜E）で分けて、型ごとに復習する。知識の不足ではなく、どの手がかりを見落としたかで分けるのがこの本の方針です。",
   "total_points":f"{tot}【推定】",
   "answer_notes":[("※ 全設問の解答は、大学公表の解答と照合しています。" if official else f"※ 大学はこの年度の解答を公表していません。全{nq}設問の正解は、市販の解答と、THINKINGで別に解いた答えを1問ずつ照合して決めました。")]
      +[f"※ 大問{p['no']} {q['id']}は、市販の解答と異なる答えを正解としています（理由は解説に書いています）。" for p in parts for q in p['questions'] if '不一致' in q.get('checked','')]
      +["※ 記述の解答例は THINKING が作成したものです（大学公表の解答例がある場合は、それを示したうえで要点を解説しています）。","※ 配点は設問ごとに公表されていないため、THINKINGの【推定】です（マーク各1点・記述各3点）。"],
   "review_lead":"該当設問は、各設問の解説で付けた失点の型を集めたものです（1つの設問に複数の型が付くことがあります）。自分が落とした設問がどの型に多いかを数え、多い型の「次にやること」から始めてください。",
   "miss_types":[
     {"key":"A","name":"前後一文の手がかりを見落とした","lack":"答えは下線部・空所の外にある、という前提。直前・直後の一文、特に言い換えと呼応の語","action":"間違えた設問の前後一文に印をつけ、根拠になる語を書き出してから選び直す"},
     {"key":"B","name":"別の箇所・別の人物から答えを持ってきた","lack":"「本文に書いてある」と「この設問の根拠である」を分けること。設問文の人物・主体・時点の確認","action":"選んだ誤答の出どころの段落番号と人物を書き、設問が指す段落・人物と比べる"},
     {"key":"C","name":"向き・程度・数字を取り違えた","lack":"大小・肯否・因果・程度・割合の照合","action":"選択肢の述語と数字に＋／−や割合を書き込み、本文と向き・程度だけを照合し直す"},
     {"key":"D","name":"字面・連想で選んだ","lack":"同じ語が入っているだけの選択肢を先に疑う習慣。文脈の中での意味の確認","action":"誤答の語と正解の語を並べ、文脈で置き換えて意味が通るかを確かめる"},
     {"key":"E","name":"文の骨格・記述の要点を確かめなかった","lack":"品詞・語法・構文、記述で求められている要点と字数","action":"間違えた文を S・V・O／C・M に区切り直す。記述は要点を箇条書きにしてから字数内にまとめ直す"}],
   "closing":[]},
 "sources":[{"name":"大学公表の解答","status":"照合済み" if official else "公表なし","note":"大学公表の解答と照合。" if official else "市販の解答と、THINKINGで別に解いた答えを照合して決定。"},
   {"name":"配点","status":"【推定】","note":"設問ごとの配点は非公表。マーク各1点・記述各3点としてTHINKINGが推定。"},
   {"name":"試験時間","status":"要確認","note":"募集要項で確認してください。"}],
 "copyright":["本書は学習用の解説です。設問・英文の著作権は出題者・原著者に帰属します。和訳・解説はTHINKINGによるオリジナルです。"]}
src = f'''"""明治大学 法学部 {y}年度 英語｜THINKINGの徹底解説シリーズ（mkbook_meiji.py で生成）"""
import sys
from pathlib import Path
_PARTS_DIR = Path(__file__).resolve().parent.parent / "parts"
if str(_PARTS_DIR) not in sys.path:
    sys.path.insert(0, str(_PARTS_DIR))
from part1 import PART as PART1  # noqa: E402
from part2 import PART as PART2  # noqa: E402

BOOK = ''' + pprint.pformat(book, width=180, sort_dicts=False).replace("'__PARTS__'", "[PART1, PART2]") + "\n"
open(f'{D}/data/meiji-hogaku_{y}.py','w',encoding='utf-8').write(src)
print(y, nq, nm, nw, tot, [r[5] for r in rows], len(diff))
