# -*- coding: utf-8 -*-
# 「頭のいい人が絶対にやらない『◯◯』」に入れる言葉を、1項目につき3つずつ、1ページ目のカードの形で並べる。
#   python3 -I scripts/build_sanpattern.py            → build/やらない言葉_3パターン_50.html
#   node scripts/shot_page.js やらない言葉_3パターン_50   → PNG と PDF
# 言葉の中の「|」は、長い言葉を2行に分ける場所（カードの中だけ。下の説明には出ない）。
import io, html, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plan_v2 as plan

CAND = {   # A＝これまでの本命、B・C＝別案
 "01": ["みんなと同じ勉強", "とりあえず、|みんなと同じ", "定番の勉強法"],
 "02": ["読み返し", "読むだけ勉強", "何度も読む"],
 "03": ["スラスラ進む勉強", "ラクな勉強", "自分に合う|勉強法探し"],
 "04": ["がむしゃら勉強", "とにかく頑張る", "時間で勝負"],
 "05": ["一夜漬け", "まとめやり", "テスト前の|まとめ勉強"],
 "06": ["完璧主義", "完璧待ち", "100点になってから"],
 "07": ["聞くだけ授業", "授業の|聞きっぱなし", "受け身の授業"],
 "08": ["板書の丸写し", "全部ノートに写す", "写すだけノート"],
 "09": ["小テストの|やりっぱなし", "小テストの|ポイ捨て", "点だけ見て終わり"],
 "10": ["全部に全力", "宿題ぜんぶ全力", "言われた通り全部"],
 "11": ["覚えてから解く", "インプット待ち", "まず全部読む"],
 "12": ["にらめっこ暗記", "見つめるだけ暗記", "黙って暗記"],
 "13": ["まとめノート作り", "きれいなノート", "蛍光ペンだらけ"],
 "14": ["1個ずつ暗記", "バラバラ暗記", "丁寧すぎる暗記"],
 "15": ["わかったつもり", "うなずくだけ", "説明できないまま|次へ"],
 "16": ["イチからやり直し", "忘れてから復習", "最初から覚え直し"],
 "17": ["1教科ぶっ通し", "今日は数学だけ", "同じ教科の連続"],
 "18": ["わかるまで粘る", "30分の長考", "ねばり勝負"],
 "19": ["○つけて終わり", "マルで満足", "正解したら次へ"],
 "20": ["問題文の|読み飛ばし", "見切り発車", "途中で解き始める"],
 "21": ["時間無制限の|演習", "ノータイマー", "解けるまで解く"],
 "22": ["頭の中だけで|考える", "書かずに考える", "脳内勉強"],
 "23": ["なんとなく○", "なんとなくできた", "あいまい○"],
 "24": ["ただの解き直し", "もう1回解くだけ", "解き直しの|繰り返し"],
 "25": ["1問ずつ直し", "全部直し", "上から順に直す"],
 "26": ["次は気をつける", "うっかりで|片づける", "ケアレスミス扱い"],
 "27": ["『わかった』の放置", "わかったの過信", "わかったまま|放っておく"],
 "28": ["やる気まかせの|目標", "気分で立てる目標", "テンション目標"],
 "29": ["毎日2時間宣言", "高すぎるノルマ", "毎日◯時間ルール"],
 "30": ["明日の自分まかせ", "盛りすぎ計画", "理想の計画"],
 "31": ["時間ができたら|勉強", "まとまった|時間待ち", "スキマ時間の|スルー"],
 "32": ["意地の完走", "もったいないから|最後まで", "合わない参考書の|完走"],
 "33": ["やる気チャージ", "合格体験記めぐり", "モチベ動画めぐり"],
 "34": ["過去問の温存", "過去問は最後", "実力がついてから|過去問"],
 "35": ["ながら勉強", "音楽ききながら|勉強", "BGM勉強"],
 "36": ["スマホ我慢", "スマホとの|我慢くらべ", "触らないと決める"],
 "37": ["キリのいい|ところまで", "休憩なし勉強", "ノンストップ勉強"],
 "38": ["無理やり朝型", "朝活チャレンジ", "早起き宣言"],
 "39": ["徹夜", "睡眠けずり", "夜ふかし勉強"],
 "40": ["まず片づけ", "片づけてから|スタート", "片づけ待ち"],
 "41": ["自己暗示", "『自分はできる』の|言い聞かせ", "ポジティブの|ゴリ押し"],
 "42": ["ひとり反省会", "自分責め", "自分へのダメ出し"],
 "43": ["点数くらべ", "友達との比べっこ", "人と比べて|落ち込む"],
 "44": ["考えないようにする", "不安のぐるぐる", "不安の我慢"],
 "45": ["前日に|新しい問題集", "前日の新規開拓", "前日の悪あがき"],
 "46": ["落ち着け、|落ち着け", "無理に落ち着く", "落ち着こうとする"],
 "47": ["1番から順番に", "大問1から解く", "順番どおり"],
 "48": ["AIに丸投げ", "AIの答えコピペ", "答えだけ聞く"],
 "49": ["自力しばり", "AI禁止", "AIはズル、の|思いこみ"],
 "50": ["全部わかりません", "ざっくり質問", "丸ごと質問"],
}
import re
ABC = "ABC"
def E(s):
    return re.sub(r"(?<![0-9])([0-9]{2,3})(?![0-9])", r'<span class="tcy">\1</span>', html.escape(s))

def kw_html(w):
    parts = w.split("|")
    if len(parts) == 1:
        n = len(w)
        k = 17 if n <= 5 else 13 if n <= 7 else 10.5 if n <= 9 else 9.6 if n <= 10 else 8.8
        return f'<div class="kw" style="font-size:{k}cqw">「{E(w)}」</div>'
    m = max(len(parts[0]), len(parts[1])) + 1
    k = max(8.5, min(13, 116 / m))
    return f'<div class="kw two" style="font-size:{k:.1f}cqw">「{E(parts[0])}<br>{E(parts[1])}」</div>'

def card(no, i, w):
    plain = w.replace("|", "")
    return (f'<button type="button" class="card" id="c{no}{ABC[i]}" data-no="{no}" data-k="{ABC[i]}" data-w="{html.escape(plain)}" aria-pressed="false">'
            f'<span class="pg"><span class="no"><span>法則</span><b>{no}</b></span>'
            f'<span class="decl"><span class="lead">頭のいい人が絶対にやらない</span>{kw_html(w).replace("<div", "<span").replace("</div>", "</span>")}</span>'
            f'<span class="then"><i></i>じゃあ、何をする？</span></span>'
            f'<span class="cap"><em>{ABC[i]}</em>{html.escape(plain)}</span></button>')

blocks, nav = [], []
for ci, (ch_no, ch_title, ch_sub, items) in enumerate(plan.CHAPTERS, 1):
    its = []
    for no, law, title, x, o, src in items:
        cards = "".join(card(no, i, w) for i, w in enumerate(CAND[no]))
        its.append(f'<section class="it" data-no="{no}"><header><b>{no}</b><span>今のタイトル：{html.escape(title)}</span></header>'
                   f'<div class="trio">{cards}</div></section>')
    nav.append(f'<a href="#ch{ci}">{html.escape(ch_no)}<small>{items[0][0]}〜{items[-1][0]}</small></a>')
    blocks.append(f'<h2 id="ch{ci}"><span>{html.escape(ch_no)}</span>{html.escape(ch_sub)}</h2><div class="grid">{"".join(its)}</div>')

CSS = """
/* 配置の考え方：1項目＝カード3枚（A・B・C）。カードは本の1ページ目そのままの形。大きな言葉だけを見比べて、押して選ぶ */
:root {
  --bg:#f3f5f8; --surface:#ffffff; --fg:#151a22; --muted:#5d6878; --line:#d5dbe4; --band:#e7ecf3;
  --accent:#15467e; --accent-soft:#e2ebf7; --on-accent:#ffffff;
  --paper:#ffffff; --paper-ink:#14171c; --paper-accent:#15467e;
  --sans:"Noto Sans JP","Noto Sans CJK JP","Hiragino Sans","Yu Gothic",sans-serif;
  --serif:"Noto Serif JP","Noto Serif CJK JP","Hiragino Mincho ProN","Yu Mincho",serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg:#12161c; --surface:#1a2029; --fg:#e8ecf2; --muted:#9aa6b6; --line:#323c49; --band:#232c38;
  --accent:#8db8ee; --accent-soft:#1f3350; --on-accent:#0f1620;
  --paper:#eceef2; --paper-ink:#14171c; --paper-accent:#15467e; color-scheme:dark } }
:root[data-theme="dark"] {
  --bg:#12161c; --surface:#1a2029; --fg:#e8ecf2; --muted:#9aa6b6; --line:#323c49; --band:#232c38;
  --accent:#8db8ee; --accent-soft:#1f3350; --on-accent:#0f1620;
  --paper:#eceef2; --paper-ink:#14171c; --paper-accent:#15467e; color-scheme:dark }
* { box-sizing:border-box; }
body { background:var(--bg); color:var(--fg); font-family:var(--sans); font-size:15px; line-height:1.75; margin:0; }
.wrap { max-width:1080px; margin:0 auto; padding-block:26px 120px;
  padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); }
h1 { font-family:var(--serif); font-weight:900; font-size:clamp(24px,4.2vw,34px); line-height:1.35; margin:0 0 6px; text-wrap:balance; }
.lede { color:var(--muted); margin:0 0 6px; max-width:46em; }
.nav { display:flex; flex-wrap:wrap; gap:8px; margin:14px 0 0; }
.nav a { display:inline-flex; gap:8px; align-items:baseline; padding:5px 12px; border:1px solid var(--line); background:var(--surface); color:var(--accent); font-weight:700; font-size:13.5px; text-decoration:none; }
.nav a small { color:var(--muted); font-weight:400; font-size:11.5px; }
.nav a:focus-visible { outline:3px solid var(--accent); outline-offset:2px; }
h2 { scroll-margin-top:12px; font-size:14px; font-weight:700; background:var(--band); padding:7px 14px; margin:30px 0 14px; letter-spacing:.04em; }
h2 span { color:var(--accent); margin-right:12px; }
.grid { display:grid; grid-template-columns:minmax(0,1fr); gap:30px; }
.it { min-width:0; }
.it header { display:flex; align-items:baseline; gap:12px; margin-bottom:9px; }
.it header b { font-family:var(--serif); font-weight:900; font-size:26px; color:var(--accent); line-height:1; font-variant-numeric:tabular-nums; }
.it header span { font-size:13.5px; color:var(--muted); line-height:1.5; min-width:0; }
.trio { display:grid; grid-template-columns:repeat(3, minmax(0,300px)); gap:14px; align-items:start; }

.card { display:block; width:100%; min-width:0; padding:0; margin:0; border:0; background:none; color:inherit; font:inherit; text-align:left; cursor:pointer; }
.card:focus-visible { outline:3px solid var(--accent); outline-offset:3px; }
.pg { display:block; aspect-ratio:127/188; max-width:100%; container-type:inline-size; position:relative; background:var(--paper); color:var(--paper-ink);
      border:1px solid var(--line); overflow:hidden; line-height:1.8; }
.pg .no { position:absolute; top:9cqw; right:9cqw; text-align:center; color:var(--paper-accent); line-height:1; }
.pg .no span { display:block; font-size:3.4cqw; letter-spacing:.3em; padding-left:.3em; margin-bottom:1.2cqw; }
.pg .no b { display:block; font-size:12cqw; font-weight:900; border-top:.9cqw solid var(--paper-accent); padding-top:1.4cqw; }
.pg .decl { position:absolute; top:12cqw; right:27cqw; height:128cqw; writing-mode:vertical-rl; display:block; }
.pg .lead { display:block; font-size:5.5cqw; font-weight:700; letter-spacing:.06em; margin-left:3cqw; }
.pg .kw { display:block; font-weight:900; line-height:1.2; letter-spacing:.03em; text-orientation:upright; }
.pg .tcy { text-combine-upright:all; -webkit-text-combine:horizontal; }
.pg .kw.two { line-height:1.25; }
.pg .then { position:absolute; left:9cqw; bottom:10cqw; writing-mode:vertical-rl; font-size:6cqw; font-weight:700; color:var(--paper-accent); letter-spacing:.06em; }
.pg .then i { display:inline-block; width:.6cqw; height:12cqw; background:var(--paper-accent); margin-bottom:2.4cqw; }
.cap { display:flex; gap:8px; align-items:baseline; margin-top:8px; font-size:15px; line-height:1.45; font-weight:700; }
.cap em { font-style:normal; flex:none; width:1.7em; height:1.7em; line-height:1.65em; text-align:center; font-size:12px; border:1px solid var(--accent); color:var(--accent); border-radius:50%; }

/* 選んだカード */
.it.has .card:not(.on) { opacity:.42; }
.card.on .pg { outline:3px solid var(--accent); outline-offset:-1px; }
.card.on .cap em { background:var(--accent); color:var(--on-accent); }

.result { margin-top:40px; border-top:1px solid var(--line); padding-top:18px; }
.result h3 { font-family:var(--serif); font-size:18px; margin:0 0 4px; }
.result p { color:var(--muted); font-size:13.5px; margin:0 0 10px; }
#out { width:100%; min-height:170px; font:13px/1.7 var(--sans); padding:10px 12px; border:1px solid var(--line); background:var(--surface); color:var(--fg); resize:vertical; }
.bar { position:fixed; left:0; right:0; bottom:0; z-index:20; background:var(--surface); border-top:1px solid var(--line);
       padding-top:10px; padding-bottom:calc(10px + env(safe-area-inset-bottom, 0px));
       padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); }
.barin { max-width:1048px; margin:0 auto; display:flex; align-items:center; gap:10px; flex-wrap:wrap; }
#cnt { font-weight:700; font-variant-numeric:tabular-nums; margin-right:auto; }
.btn { font:inherit; font-size:13.5px; font-weight:700; padding:7px 14px; border:1px solid var(--accent); background:var(--accent); color:var(--on-accent); cursor:pointer; }
.btn.sub { background:transparent; color:var(--accent); }
.btn:focus-visible { outline:3px solid var(--accent); outline-offset:2px; }
#msg { font-size:13px; color:var(--muted); min-width:7em; }
@media (max-width:560px) { .trio { gap:7px; } .cap { font-size:12px; gap:5px; } .it header span { font-size:12px; } .it header b { font-size:22px; } }
@media print {
  body { font-size:11px; } .wrap { max-width:none; padding-block:0; }
  .bar, .result, .nav { display:none; } .it { break-inside:avoid; } h2 { break-after:avoid; }
  .grid { gap:10px; } .trio { grid-template-columns:repeat(3, 50mm); gap:5mm; } .cap { font-size:11px; }
}
"""

JS = r"""
(function () {
  var KEY = 'yaranai-3pattern-v1', sel = {};
  try { sel = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { sel = {}; }
  var out = document.getElementById('out'), cnt = document.getElementById('cnt'), msg = document.getElementById('msg');
  function save() { try { localStorage.setItem(KEY, JSON.stringify(sel)); } catch (e) {} }
  function render() {
    var lines = [], n = 0;
    document.querySelectorAll('.it').forEach(function (it) {
      var no = it.dataset.no, k = sel[no];
      it.classList.toggle('has', !!k);
      it.querySelectorAll('.card').forEach(function (c) {
        var on = c.dataset.k === k;
        c.classList.toggle('on', on); c.setAttribute('aria-pressed', on ? 'true' : 'false');
        if (on) { lines.push(no + ' ' + k + '　' + c.dataset.w); n++; }
      });
    });
    out.value = lines.join('\n');
    cnt.textContent = '選んだ数　' + n + ' / 50';
  }
  document.querySelectorAll('.card').forEach(function (c) {
    c.addEventListener('click', function () {
      var no = c.dataset.no;
      if (sel[no] === c.dataset.k) delete sel[no]; else sel[no] = c.dataset.k;
      save(); render(); msg.textContent = '';
    });
  });
  document.getElementById('copy').addEventListener('click', function () {
    if (!out.value) { msg.textContent = 'まだ選んでいません'; return; }
    function fallback() { out.focus(); out.select(); msg.textContent = '下の枠を選びました。コピーしてください'; out.scrollIntoView({ block: 'center' }); }
    try { navigator.clipboard.writeText(out.value).then(function () { msg.textContent = 'コピーしました'; }, fallback); } catch (e) { fallback(); }
  });
  document.getElementById('clear').addEventListener('click', function () { sel = {}; save(); render(); msg.textContent = '選び直せます'; });
  render();
})();
"""

doc = f"""<title>やらない言葉の3パターン</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&family=Noto+Serif+JP:wght@700;900&display=swap">
<style>{CSS}</style>
<div class="wrap">
<h1>やらない言葉の3パターン</h1>
<p class="lede">50項目それぞれ、頭のいい人が絶対にやらない「◯◯」に入れる言葉を、3つずつ並べました。カードは、各項目の1ページ目（四六判・縦書き）の形です。</p>
<p class="lede">気に入ったカードを押すと、選べます。選んだものは、下の「選んだ言葉」にたまります。</p>
<nav class="nav" aria-label="章へ飛ぶ">{"".join(nav)}</nav>
{"".join(blocks)}
<div class="result"><h3>選んだ言葉</h3><p>カードを押すと、ここに「番号　記号　言葉」が並びます。そのままコピーして送れます。</p>
<textarea id="out" readonly aria-label="選んだ言葉の一覧"></textarea></div>
</div>
<div class="bar"><div class="barin"><span id="cnt">選んだ数　0 / 50</span><span id="msg" role="status"></span>
<button type="button" class="btn sub" id="clear">選び直す</button><button type="button" class="btn" id="copy">選んだ言葉をコピー</button></div></div>
<script>{JS}</script>
"""
io.open("build/やらない言葉_3パターン_50.html", "w", encoding="utf-8").write(doc)
print("ok", sum(len(v) for v in CAND.values()), "枚")
