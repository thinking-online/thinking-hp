# -*- coding: utf-8 -*-
# 「縦書きにした時の構成（案）」の見本を作る。A5・縦書き。類書と同じ組み方（1行40字、1ページ16行）。
#   python3 -I scripts/build_mock_tate.py   → build/見本_縦書きの構成.html
#   node scripts/shot_mock_tate.js          → build/見本_縦書きの構成.png（行のずれ、はみ出しがあれば知らせる）
# 前提：改行は最低限（文をつなげて段落にする）。ブロックは、項目の頭・2コマ・3STEP・まとめの4つだけ。
# 2つの版を並べる：マックス版（今の文を削らない）と、削った版（320ページ）。
# 14番の文は、1本の長い帯に流して、16行ごとにページに切っている（HTMLの中のスクリプト）。本の組版と同じ流れ方になる。
# ページ数の目安は scripts/tate_model.py で数える。
import html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tate_model as M
ROOT = os.path.dirname(HERE)
NAME = "見本_縦書きの構成"
W, R = 40, 16
FW = str.maketrans("0123456789", "０１２３４５６７８９")


def vt(s):
    """縦書き用。2けたの数字は横に並べ、ほかの数字は全角にする。==…== は網かけ。"""
    s = html.escape(s, quote=False)
    s = re.sub(r"[0-9]+", lambda m: '<span class="tcy">%s</span>' % m.group(0) if len(m.group(0)) == 2 else m.group(0).translate(FW), s)
    s = s.replace("OK", '<span class="tcy">OK</span>')
    return re.sub(r"==(.+?)==", r"<mark>\1</mark>", s)


def P(s, cls=""):
    return '<p%s>%s</p>' % ((' class="%s"' % cls) if cls else "", vt(s))


def H(s):
    return "<h3>%s</h3>" % vt(s)


def ill(label, text, cls=""):
    return '<div class="ill %s"><span>%s</span><div>%s</div></div>' % (cls, label, text)


# ---------------------------------------------------------------- 14番の材料
HEAD = ('<div class="blk vhead"><div class="vlab"><b class="vno">14</b><span class="pill">頭のいい人が絶対やらないこと</span></div>'
        '<div class="vttl">黙って、じっと見つめて覚える</div></div>')
HQ = P("家の玄関に、今、靴は何足、出ていますか？", "hq")
A = "数えている間、目は、どこを見ていましたか。この本から目を離して、上か、遠くを見たはずです。目を閉じた人も、いると思います。人は、何かを思い出そうとする時、目の前のものから、目を離します。目に入ってくるものが、じゃまになるからです。逆に言うと、==教材をじっと見つめている間、頭は、思い出していません。=="
B_FULL = "歴史のテストが、近づいています。「集中して、じっと見ていれば、頭に入るはず」。教科書を開いて、黙って、見つめます。目は、同じ行の上を、何度もすべっています。20分たって、教科書を閉じます。何が書いてあったか、言おうとしても、出てきません。"
B_CUT = "歴史のテストが、近づいています。教科書を開いて、黙って、見つめます。20分たって、教科書を閉じます。何が書いてあったか、言おうとしても、出てきません。"
C = "じっと見るのは、真面目な人ほどやります。静かで、集中しているように見えます。本人も、集中しているつもりです。でも、やっていることは「入れる」だけです。絶対法則02で書いた通り、点になるのは「思い出して、出す」ほうでした。"
D = "では、思い出す時、体をどう使えばいいのか。ここが、この項目の話です。使うのは、==目と、口==です。"
E = "イギリスのヨーク大学の研究者たちの実験です。映像を見てもらって、そのあと内容を思い出してもらいます。片方のグループには、目を開けたまま思い出してもらいました。もう片方には、目を閉じて思い出してもらいました。目を閉じたグループのほうが、==見たものも、聞いたものも、正確に思い出せました。=="
F = "理由は、単純です。目を開けていると、目の前のものが、ずっと頭に入ってきます。机の上、壁のポスター、窓の外。見るつもりがなくても、頭は、それを全部受け取っています。目を閉じると、それが止まります。そのぶん、頭を、思い出すことに使えます。"
G = "教材を見つめたまま「思い出そう」としても、目に答えが入ってきてしまいます。それは、思い出しているのではなく、見ているだけです。"
H1 = "もう1つは、口です。カナダのウォータールー大学の研究者たちの実験です。単語のリストを覚えてもらいます。半分の単語は、声に出して読む。もう半分は、黙って読む。あとでテストをすると、==声に出した単語のほうが、よく覚えていました。=="
I = "声に出すと、口が動きます。自分の声が、耳から入ってきます。黙って読む時は目だけですが、声に出すと、目と口と耳を使います。思い出す時の手がかりが、増えるんです。"
J = "そして、声にはもう1つ、いいところがあります。頭の中で言うと、言えたかどうかを、自分でごまかせます。声は、出てこなければ止まります。==ごまかせません。=="
XO = P("×　教材を開いたまま、黙って、見つめる", "xo x") + P("○　教材を閉じて、目も閉じて、声に出す", "xo o")
K = "本を閉じる。目を閉じる。声に出す。これで、1つの動作です。見つめる人は、教材に向かっています。頭のいい人は、教材から顔を上げています。自習室や図書館で、時々天井を見ている人がいますよね。あれは、さぼっているのではありません。思い出しています。"
K_CUT = "本を閉じる。目を閉じる。声に出す。これで、1つの動作です。見つめる人は、教材に向かっています。頭のいい人は、教材から顔を上げています。自習室や図書館で、時々天井を見ている人がいますよね。あれは、思い出しています。"
L = "電車の中や、図書館では、声が出せません。その時は、口だけ動かします。声ほどではありませんが、黙って眺めているよりは残ります。家に帰ったら、声に出します。家で黙って勉強するのは、もったいないです。"
T1, T2, T3, T4, T5 = ("見つめている間、頭は受け取っているだけです", "目を閉じると、思い出しやすくなります", "声に出すと、残りやすくなります",
                      "2つを、1つの動作にします", "声を出せない場所では")

KOMA = ('<div class="blk vkoma">'
        '<div class="k x"><span>伸びない人</span>' + ill("絵", "じっと見つめる") + '<b>見つめて覚える</b><i>じーっと見れば、入るはず</i></div>'
        '<div class="k o"><span>頭のいい人</span>' + ill("絵", "目を閉じて、<br>声に出す") + '<b>声に出して覚える</b><i>目を閉じて、言える？</i></div></div>')
STEPS = [("覚えたい所を読んだら、本を閉じて、顔を上げる", "見つめない。閉じる"),
         ("目を閉じて、書いてあったことを声に出す", "光合成は、葉で……えーと"),
         ("声が止まった所だけ見て、もう一度、言う", "ここで止まった。もう1回")]
SHEET = ('<div class="blk vsheet"><div class="sbox"><div class="sttl">頭のいい人の<br>『暗記のしかた』3STEP</div>'
         + "".join('<div class="st"><div class="lab">STEP <b>0%d</b></div><div class="do">%s</div><div class="say">「%s」</div></div>'
                   % (i, html.escape(h), html.escape(v)) for i, (h, v) in enumerate(STEPS, 1))
         + '<div class="king"><span>「できた」の基準</span><p>目を閉じたまま、止まらずに最後まで言えたらOK！</p></div></div></div>')
MATOME = ('<div class="blk vmatome"><div class="mbox"><p class="mlab">まとめ</p>' + P("見つめている間は、入れているだけ。", "one")
          + P("①　じっと見ても、思い出す回数は0のまま", "li") + P("②　目を閉じると、思い出しやすくなる", "li") + P("③　声に出すと、残りやすくなる", "li")
          + P("だから、見つめない。閉じて、声に出す。", "dk") + P("迷ったら、自分に聞きます。「目を閉じて、言える？」", "dk") + "</div></div>")

# マックス版：今の14番の文を、1字も削らない。文をつなげて段落にしただけ
MAX = (HEAD + HQ + P("思い浮かべて、数えてみてください。", "c") + P("……", "c")
       + P(A) + P(B_FULL) + H(T1) + P(C) + P(D) + H(T2) + P(E) + P(F) + P(G) + H(T3) + P(H1) + P(I) + P(J)
       + H(T4) + XO + P(K) + H(T5) + P(L) + KOMA + SHEET + MATOME)
# 削った版：4ページに入るように、削った
CUT = (HEAD + HQ + P("思い浮かべて、数えてみてください。……", "c")
       + P(A) + P(B_CUT) + H(T1) + P(C + D) + H(T2) + P(E) + P(F) + H(T3) + P(H1) + P(I) + P(J)
       + H(T4) + XO + P(K_CUT) + KOMA + SHEET + MATOME)


def count(*parts):
    return len(re.sub(r"\s|==", "", "".join(parts)))


N_MAX = count("家の玄関に、今、靴は何足、出ていますか？思い浮かべて、数えてみてください。……", A, B_FULL, T1, C, D, T2, E, F, G, T3, H1, I, J, T4,
              "×教材を開いたまま、黙って、見つめる○教材を閉じて、目も閉じて、声に出す", K, T5, L)
N_CUT = count("家の玄関に、今、靴は何足、出ていますか？思い浮かべて、数えてみてください。……", A, B_CUT, T1, C, D, T2, E, F, T3, H1, I, J, T4,
              "×教材を開いたまま、黙って、見つめる○教材を閉じて、目も閉じて、声に出す", K_CUT)

# ---------------------------------------------------------------- 全体のページ（目安。scripts/tate_model.py で数えた行から）
its = M.items(W)
ITEMS_MAX = sum(M.pages_for(r, R) for _, _, r in its)
BODY = sum(c for _, c, _ in its)
OTH = M.others(W, R)
CH1 = sum(p for _, p in OTH["第1章の項目"])
# 前付けと巻末は、形が決まっているものがあるので、手で置く（目次は1項目1行、参考文献は小さい字、など）
FRONT = [("扉", 2), ("巻頭の10秒", 8), ("目次", 6), ("はじめに", 12), ("この本の使い方", 4)]
BACK = [("45を、1枚に", 4), ("6つの言葉", 3), ("保護者の方へ", 2), ("参考文献", 5), ("おわりに", 4), ("奥付など", 2)]
DOORS = sum(p for h, p in OTH["章の扉と導入"] if h != "第1章")
COLS = sum(p for _, p in OTH["コラム"])
n_front, n_back = sum(p for _, p in FRONT), sum(p for _, p in BACK)
n_ch1 = 3 + CH1 + 1                     # 章の扉と導入3 ＋ 6項目 ＋ コラム1
n_col = COLS - 1
OTHER = n_front + n_ch1 + DOORS + n_col + n_back
TOTAL_MAX = OTHER + ITEMS_MAX
plan, ITEMS_CUT, CUTCH = M.fit(its, R, 320 - OTHER)
SIX = sorted(k for k in plan if plan[k] == 6)
SPARE = 320 - OTHER - ITEMS_CUT
BASE = sum(__import__("math").ceil(M.body_rows(M.B.body(kk), W, merge=False, gap=0.5) / R) + 3 for kk, _, _ in its)


def bar(rows, total, scale):
    cells = "".join('<div class="%s" style="flex:%d">%s%s</div>' % (c, n, ("<b>%d</b>" % n) if n >= 6 else "", name if n >= 24 else "") for name, n, c in rows if n)
    return '<div class="bar" style="width:%.1f%%">%s</div>' % (100.0 * total / scale, cells)


def rows_for(items_pages, spare=0):
    return [("前付け", n_front, "c1"), ("第1章", n_ch1, "c2"), ("章の扉と導入", DOORS, "c3"), ("07〜45番の項目", items_pages, "c4"),
            ("コラム", n_col, "c6"), ("巻末・おわりに", n_back, "c7"), ("予備", spare, "c8")]


CSS = """
*{box-sizing:border-box}
html{font-family:"Noto Sans CJK JP","Noto Sans JP",sans-serif;color:#16181d;background:#e8e6e1}
body{margin:0;padding:34px 40px 60px;width:1180px;position:relative;overflow-x:hidden}
h1{font-size:24px;font-weight:900;color:#15467e;margin:0 0 10px}
.lead{font-size:13px;line-height:1.9;margin:0 0 4px;color:#333}
h2{font-size:17px;font-weight:900;margin:44px 0 6px;display:flex;align-items:center;gap:12px}
h2 .n{background:#15467e;color:#fff;border-radius:6px;padding:1px 12px;font-size:14px}
.note{font-size:12.5px;line-height:1.9;color:#333;margin:0 0 14px}
.vname{font-size:13.5px;font-weight:900;margin:14px 0 2px}
.vname small{font-weight:400;font-size:12px;color:#444;margin-left:10px}
.bar{display:flex;height:58px;border-radius:8px;overflow:hidden;margin:4px 0 4px;background:#fff}
.bar div{display:flex;flex-direction:column;justify-content:center;align-items:center;font-size:11px;line-height:1.35;color:#fff;font-weight:700;white-space:nowrap;overflow:hidden}
.bar b{font-size:15px}
.c1{background:#7a8594}.c2{background:#15467e}.c3{background:#5d7fa8}.c4{background:#a4500a}.c6{background:#6b8f5a}.c7{background:#7a8594}.c8{background:#b9bec7}
.leg{display:flex;gap:18px;flex-wrap:wrap;font-size:11.5px;margin:6px 0 4px}
.leg i{display:inline-block;width:11px;height:11px;border-radius:2px;margin-right:5px;vertical-align:-1px}
table{border-collapse:collapse;background:#fff;font-size:12.5px;margin-top:8px}
th,td{border:1px solid #cfd4dc;padding:6px 12px;text-align:left;line-height:1.6;vertical-align:top}
th{background:#eef1f6;font-weight:700}
td.num{text-align:right;font-weight:700;white-space:nowrap}
td.nw{white-space:nowrap}
tr.hl td{background:#fdf6e9}
/* 見開き */
.sp{margin:16px 0 26px}
.sphead{font-size:13.5px;font-weight:700;margin-bottom:8px;display:flex;align-items:center;gap:12px}
.tagc{background:#15467e;color:#fff;border-radius:99px;padding:1px 14px;font-size:12px}
.pages{display:flex;background:#fff;width:1008px;box-shadow:0 1px 4px rgba(0,0,0,.15)}
.page{width:504px;height:714px;position:relative;border-right:1px solid #e3e3e3;background:#fff}
.page:last-child{border-right:0}
.chip{position:absolute;top:18px;right:44px;background:#15467e;color:#fff;font-size:10.5px;border-radius:4px;padding:1px 10px;line-height:1.7}
.folio{position:absolute;bottom:22px;left:0;right:0;text-align:center;font-size:10px;color:#888}
.win{position:absolute;top:96px;left:44px;width:416px;height:528px;overflow:hidden}
.ghost{background:#f3f2ef;display:flex;align-items:center;justify-content:center}
.gtext{font-size:13px;color:#888;text-align:center;line-height:1.9}
.measure{position:absolute;left:-30000px;top:0}
/* 縦書きの帯。1行は幅26px、40字で高さ528px */
.vt{writing-mode:vertical-rl;height:528px;font-family:"Noto Serif CJK JP","Noto Serif JP",serif;font-size:13.2px;line-height:26px;text-align:justify;line-break:strict;color:#16181d}
.vt p{margin:0;text-indent:1em}
.vt p.c,.vt p.hq{text-indent:0}
.vt p.hq{font-family:"Noto Sans CJK JP",sans-serif;font-weight:900;font-size:14px;color:#15467e}
.vt h3{font-family:"Noto Sans CJK JP",sans-serif;font-weight:900;font-size:13.6px;line-height:26px;color:#15467e;margin:0 26px 0 0}
.vt p.xo{text-indent:2em;font-family:"Noto Sans CJK JP",sans-serif;font-size:12.6px}
.vt p.x{color:#555}.vt p.o{font-weight:700;color:#15467e}
.vt mark{background:#d5e4f7;color:inherit}
.tcy{text-combine-upright:all}
.spacer{height:528px}
.blk{height:528px}
/* 項目の頭（3行ぶん＝78px） */
.vhead{width:78px;padding-left:12px}
.vlab{line-height:24px;font-family:"Noto Sans CJK JP",sans-serif;font-size:10.5px;font-weight:700;color:#15467e}
.vno{display:inline-block;writing-mode:horizontal-tb;width:24px;height:24px;line-height:24px;text-align:center;background:#15467e;color:#fff;font-size:13px;border-radius:4px;margin-bottom:8px}
.pill{background:#e3ecf7;border-radius:12px;padding:8px 5px}
.vttl{line-height:42px;font-family:"Noto Sans CJK JP",sans-serif;font-size:25px;font-weight:900;color:#15467e;letter-spacing:.02em}
/* 絵の枠 */
.ill{border:1.5px dashed #9aa0a8;background:#f0efeb;border-radius:4px;position:relative;display:flex;align-items:center;justify-content:center;text-align:center;color:#666;font-size:10px;line-height:1.6}
.ill span{position:absolute;top:4px;left:5px;background:#7a7f87;color:#fff;font-size:8.5px;border-radius:3px;padding:0 6px;line-height:1.6}
/* 2コマ（6行ぶん＝156px）。中は横書き */
.vkoma{writing-mode:horizontal-tb;width:156px;padding:0 8px;display:flex;flex-direction:column;gap:8px;font-family:"Noto Sans CJK JP",sans-serif;line-height:1.5}
.vkoma .k{flex:1;border-radius:8px;padding:6px 4px 8px;text-align:center;display:flex;flex-direction:column}
.vkoma .x{background:#eceef2}.vkoma .o{background:#e3ecf7;border:1px solid #15467e}
.vkoma span{font-size:9.5px;color:#555}
.vkoma .ill{flex:1;margin:4px 2px 6px;background:#fff}
.vkoma b{display:block;font-size:14px;font-weight:900}
.vkoma i{display:block;font-style:normal;font-size:9px;white-space:nowrap}
/* 3STEPと基準（7行ぶん＝182px）。中は横書き */
.vsheet{writing-mode:horizontal-tb;width:182px;padding:0 6px;font-family:"Noto Sans CJK JP",sans-serif;text-align:left}
.sbox{height:100%;border:1.5px solid #15467e;border-radius:8px;padding:10px 10px 10px;display:flex;flex-direction:column;justify-content:space-between}
.sttl{font-size:12.5px;font-weight:900;line-height:1.5;border-bottom:2px solid #15467e;padding-bottom:5px}
.st{border-bottom:1px solid #dfe3ea;padding-bottom:9px}
.lab{display:inline-block;background:#15467e;color:#fff;border-radius:99px;font-size:9px;font-weight:700;padding:0 10px;line-height:1.7}
.lab b{font-size:11px}
.do{font-size:11.5px;font-weight:700;line-height:1.6;margin:5px 0 5px}
.say{display:inline-block;border:1px solid #15467e;border-radius:8px;padding:1px 6px;font-size:9.5px;line-height:1.7;letter-spacing:-.02em}
.king{background:#e3ecf7;border-radius:6px;padding:8px 9px}
.king span{display:inline-block;background:#15467e;color:#fff;border-radius:99px;font-size:9px;font-weight:700;padding:0 9px;line-height:1.8}
.king p{margin:4px 0 0;font-size:11px;font-weight:700;line-height:1.6;text-indent:0}
/* まとめ（7行ぶん＝182px）。中は縦書き */
.vmatome{width:182px;padding-right:4px}
.mbox{height:100%;background:#f1f4f9;border-radius:8px;padding:14px 6px;line-height:25px}
.mbox p{text-indent:0;line-height:25px}
.mbox .mlab{line-height:16px;font-family:"Noto Sans CJK JP",sans-serif;font-size:9.5px;font-weight:700;color:#15467e}
.mbox .one{font-family:"Noto Sans CJK JP",sans-serif;font-weight:900;font-size:14px}
.mbox .li{text-indent:1em}
"""

JS = r"""
const COL = 26, R = 16, PW = COL * R;
function paginate(id) {
  const src = document.getElementById(id);
  for (const el of [...src.children]) {
    const e = src.getBoundingClientRect().right, b = el.getBoundingClientRect();
    const start = Math.round(e - b.right), end = Math.round(e - b.left);
    let push = 0;
    if (el.classList.contains('blk')) { if (Math.floor(start / PW) !== Math.floor((end - 1) / PW)) push = (Math.floor(start / PW) + 1) * PW - start; }
    else if (el.tagName === 'H3') { if (end % PW === 0) push = COL; }
    if (push) { const sp = document.createElement('div'); sp.className = 'spacer'; sp.style.width = push + 'px'; src.insertBefore(sp, el); }
  }
  const total = Math.round(src.getBoundingClientRect().width);
  return { src, total, pages: Math.ceil(total / PW) };
}
function build(box) {
  const { src, total, pages } = paginate(box.dataset.src);
  const labels = JSON.parse(box.dataset.labels), tags = JSON.parse(box.dataset.tags);
  const mk = (k) => {
    const p = document.createElement('div');
    if (k >= pages) { p.className = 'page ghost'; p.innerHTML = '<div class="gtext">' + box.dataset.after + '</div>'; return p; }
    p.className = 'page';
    p.innerHTML = '<div class="chip">' + (k + 1) + 'ページ目　' + (labels[k] || '') + '</div><div class="win"></div><div class="folio">' + (k + 1) + '</div>';
    const c = src.cloneNode(true); c.removeAttribute('id');
    c.style.cssText = 'position:absolute;top:0;width:' + total + 'px;right:' + (-k * PW) + 'px';
    p.querySelector('.win').appendChild(c);
    return p;
  };
  for (let k = 0; k < pages; k += 2) {
    const sp = document.createElement('div'); sp.className = 'sp';
    sp.innerHTML = '<div class="sphead"><span class="tagc">' + (tags[k / 2] || '') + '</span>見開き' + (k / 2 + 1) + '　　右＝' + (k + 1) + 'ページ目　／　左＝'
      + (k + 1 < pages ? (k + 2) + 'ページ目' : '次の項目') + '</div><div class="pages"></div>';
    sp.querySelector('.pages').append(mk(k + 1), mk(k));
    box.appendChild(sp);
  }
  box.dataset.total = total; box.dataset.pages = pages;
}
document.fonts.ready.then(() => { document.querySelectorAll('.sps').forEach(build); document.body.dataset.done = '1'; });
"""


def sps(src, labels, tags, after):
    return ('<div class="sps" data-src="%s" data-labels=\'%s\' data-tags=\'%s\' data-after="%s"></div>'
            % (src, json.dumps(labels, ensure_ascii=False), json.dumps(tags, ensure_ascii=False), after))


def main():
    scale = max(TOTAL_MAX, 320)
    leg = "".join('<span><i class="%s"></i>%s</span>' % (c, n) for n, _, c in rows_for(0, 1))
    six = "　".join(SIX)
    out = ['<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>見本　縦書きにした時の構成</title><style>' + CSS + "</style></head><body>",
           "<h1>見本　縦書きにした時の構成（案）</h1>",
           '<p class="lead">A5・縦書き。組み方は、類書（A5判・384ページ）と同じにしました：1行40字、1ページ16行。色は、黒と青の2色で作っています。点線の枠は、イラストが入る場所です。</p>',
           '<p class="lead">決まりは2つです。(1) 改行は最低限。文をつなげて、段落にする。(2) ブロックは、項目の頭・2コマ・3STEP・まとめの4つだけ。質問ページは、1ページ使わず、項目の頭に入れる。</p>',
           '<h2><span class="n">1</span>2つの版の、全体のページ数（目安）</h2>',
           '<p class="vname">マックス版　約%dページ<small>今の文を、1字も削らない。項目は、新しいページから始める（1項目 5〜9ページ）</small></p>' % (round(TOTAL_MAX, -1)),
           bar(rows_for(ITEMS_MAX), TOTAL_MAX, scale),
           '<p class="vname">削った版　320ページ<small>07〜45番を、4ページ×%d個 と 6ページ×%d個にそろえる。項目は、いつも見開きの右から始まる</small></p>' % (len(plan) - len(SIX), len(SIX)),
           bar(rows_for(ITEMS_CUT, SPARE), 320, scale),
           '<div class="leg">%s</div>' % leg,
           "<table><tr><th>版</th><th>改行</th><th>ブロック</th><th>07〜45番</th><th>全体</th><th>07〜45番の本文（今 約%s字）から削る量</th></tr>" % format(round(BODY, -2), ","),
           "<tr><td>何も変えずに、縦書きにする</td><td class='nw'>今のまま</td><td>質問ページ・3STEPに1ページずつ、2コマ・まとめに半ページずつ</td><td class='num'>約%dページ</td><td class='num'>%dページ以上</td><td>0</td></tr>" % (round(BASE, -1), round(OTHER + BASE, -1)),
           "<tr class='hl'><td>マックス版</td><td class='nw'>最低限</td><td class='nw'>4つだけ</td><td class='num'>%dページ</td><td class='num'>約%dページ</td><td>0</td></tr>" % (ITEMS_MAX, round(TOTAL_MAX, -1)),
           "<tr class='hl'><td>削った版</td><td class='nw'>最低限</td><td class='nw'>4つだけ</td><td class='num'>%dページ</td><td class='num'>320ページ</td><td>約%s字（約%d%%）。4ページの項目は、本文 約1,000〜1,200字まで。6ページの項目は、約1,800〜2,100字まで</td></tr>"
           % (ITEMS_CUT, format(int(round(CUTCH, -3)), ","), round(100 * CUTCH / BODY)),
           "</table>",
           '<p class="note" style="margin-top:8px">前付け %d、第1章 %d（6項目で%d）、章の扉と導入 %d、コラム %d、巻末・おわりに %d は、2つの版で同じです（合わせて%dページ。第1章と前付けは、削っていません）。<br>'
           '削った版で、6ページにする項目（本文が長い順に選んだ場合）：%s</p>' % (n_front, n_ch1, CH1, DOORS, n_col, n_back, OTHER, six),
           '<h2><span class="n">2</span>削った版　14番を、4ページで組んだ見本</h2>',
           '<p class="note">見開き2つで、1項目が終わります。本文は 約%s字（今の14番は 約%s字。最後の節「声を出せない場所では」と、ほか3か所、合わせて約%d字を削りました）。<br>'
           '右ページの頭に、番号と題。すぐ下に、問い。3ページ目の終わりに2コマ、4ページ目に3STEPとまとめ。</p>' % (format(N_CUT, ","), format(N_MAX, ","), N_MAX - N_CUT),
           sps("srcCut", ["項目の頭 ＋ 問い → 本文", "本文", "本文 ＋ 2コマ", "3STEP ＋ できた基準 ＋ まとめ"], ["つかむ → わかる", "わかる → やる"], "次の項目（15番）の<br>1ページ目"),
           '<h2><span class="n">3</span>マックス版　14番を、削らずに流した見本（5ページ）</h2>',
           '<p class="note">今の14番の文（約%s字）を、1字も削っていません。文をつなげて、段落にしただけです。5ページになります。3STEPがページをまたがないように送るので、4ページ目の左が少し空きます（王様の一言を置けます）。次の項目は、次のページから始めます。</p>' % format(N_MAX, ","),
           sps("srcMax", ["項目の頭 ＋ 問い → 本文", "本文", "本文", "本文の終わり ＋ 2コマ", "3STEP ＋ できた基準 ＋ まとめ"], ["つかむ → わかる", "わかる", "やる"], "次の項目（15番）の<br>1ページ目"),
           '<h2><span class="n">4</span>ブロックを、どう小さくしたか</h2>',
           "<table><tr><th>ブロック</th><th>前の見本（A5・横書き）</th><th>この見本（A5・縦書き）</th></tr>"
           "<tr><td>質問ページ</td><td>問いと合わせて、1ページ</td><td>項目の頭に入れる（3行ぶん）。番号・「頭のいい人が絶対やらないこと」・題</td></tr>"
           "<tr><td>2コマ</td><td>ページの3分の1</td><td>6行ぶん（ページの3分の1強）。上が伸びない人、下が頭のいい人</td></tr>"
           "<tr><td>3STEP・できた基準</td><td>まとめと合わせて、1ページ。STEPごとに絵</td><td>7行ぶん。絵はなし。中は横書き</td></tr>"
           "<tr><td>まとめ</td><td>（上と同じページ）</td><td>7行ぶん。一言・3つ・だから・自分への問い</td></tr>"
           "<tr><td>×と○の2行、型などの囲み</td><td>箱にする</td><td>箱にしない。本文の中に、字下げで置く</td></tr>"
           "<tr><td>小見出し</td><td>1行と少し</td><td>2行ぶん（前を1行あける）</td></tr></table>",
           '<p class="note" style="margin-top:26px">数え方：14番は、実際に文字を流して、16行ごとにページに切りました。全体のページ数は、07〜45番の本文を同じ決まりで行に直して数えた目安です（<code>scripts/tate_model.py</code>）。第1章・前付け・巻末は、文字を流していません。<br>'
           '字を少し小さくして、1行44字・1ページ18行にすると、マックス版は約360ページ、320ページに収める時に削る量は約1万2千字になります。本の大きさ、字の大きさ、色の数、イラストの数は、まだ決まっていないので、ページ数は目安です。</p>',
           '<div class="measure"><div class="vt" id="srcCut">%s</div><div class="vt" id="srcMax">%s</div></div>' % (CUT, MAX),
           "<script>" + JS + "</script></body></html>"]
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    with open(os.path.join(ROOT, "build", NAME + ".html"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("14番　マックス版 %d字／削った版 %d字" % (N_MAX, N_CUT))
    print("全体　ほか %d（前付け%d 第1章%d 扉%d コラム%d 巻末%d）／マックス版 07〜45番 %d → 全体 %d／削った版 07〜45番 %d（6ページ %d個）予備 %d、削る %d字／何も変えない 07〜45番 %d"
          % (OTHER, n_front, n_ch1, DOORS, n_col, n_back, ITEMS_MAX, TOTAL_MAX, ITEMS_CUT, len(SIX), SPARE, CUTCH, BASE))


if __name__ == "__main__":
    main()
