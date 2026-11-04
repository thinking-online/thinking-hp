# -*- coding: utf-8 -*-
"""四六判・縦組み・2色刷りの見本。book/ で実行。出力 build/見本_四六判.html"""
import io, os

NAVY = "#15467E"
GRAY = "#8a8a8a"

CSS = f"""
@page {{ size: 127mm 188mm; margin: 0; }}
* {{ box-sizing: border-box; margin:0; padding:0; }}
body {{ background:#fff; }}
.page {{ width:127mm; height:188mm; position:relative; overflow:hidden;
        break-after:page; background:#fff; }}
.page:last-child {{ break-after:auto; }}

/* 版面　天20 地22 小口16 ノド18 */
.area {{ position:absolute; top:20mm; bottom:22mm; left:16mm; right:18mm;
        writing-mode: vertical-rl; font-family:"Noto Serif CJK JP", serif;
        font-size:9.5pt; line-height:1.8; color:#111; }}
.area.wide {{ left:14mm; right:14mm; }}

.hashira {{ position:absolute; top:11mm; left:16mm; font-size:6.5pt; color:{GRAY};
           font-family:"Noto Sans CJK JP",sans-serif; letter-spacing:.08em; }}
.nombre {{ position:absolute; bottom:11mm; right:18mm; font-size:7pt; color:{GRAY};
          font-family:"Noto Sans CJK JP",sans-serif; }}

.tcy {{ text-combine-upright: all; }}

/* 項目の扉部分 */
.opener {{ inline-size:100%; margin-inline-end:6mm; }}
.num {{ font-family:"Noto Sans CJK JP",sans-serif; font-weight:700;
       font-size:30pt; color:{NAVY}; line-height:1;
       text-combine-upright: all; margin-block-end:4mm; }}
.ttl {{ font-size:15pt; font-weight:500; line-height:1.55; letter-spacing:.02em; }}

.xo {{ inline-size:100%; background:#eef3f9; border-block-start:2px solid {NAVY};
      padding:5mm 3.5mm; margin-inline-end:6mm; font-size:8.6pt; line-height:2.1; }}
.xo .x {{ color:#555; }}
.xo .o {{ color:{NAVY}; }}
.tag {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:7pt; color:{GRAY};
       letter-spacing:.1em; margin-block-start:3mm; }}

p {{ text-indent:1em; margin:0; }}
p.noind {{ text-indent:0; }}
p + p {{ margin-inline-start:0; }}
.sp {{ block-size:1em; }}

h2 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:10.5pt; font-weight:700;
     margin-inline-end:4mm; border-block-start:3px solid {NAVY};
     padding-block-start:2.5mm; inline-size:100%; }}
h3 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:9.5pt; font-weight:700;
     color:{NAVY}; margin-inline-end:2.5mm; inline-size:100%; }}

/* 頭のなかの2つの囲み */
.minds {{ display:flex; flex-direction:row; gap:5mm; inline-size:100%; }}
.mind {{ padding:4mm 3.5mm; font-size:8.6pt; line-height:2.0; inline-size:100%; }}
.mind.ng {{ border:1px solid #d5d5d5; background:#fafafa; }}
.mind.ok {{ border:1px solid {NAVY}; background:#f2f6fb; }}
.mind .cap {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:7.5pt;
             font-weight:700; color:{GRAY}; margin-block-end:2.5mm; }}
.mind.ok .cap {{ color:{NAVY}; }}
.mind p {{ text-indent:0; }}

/* 手順 */
.step {{ margin-inline-end:2mm; }}
.stepno {{ font-family:"Noto Sans CJK JP",sans-serif; font-weight:700; color:{NAVY};
          font-size:9pt; }}

/* まとめ囲み */
.sum {{ border:1px solid {NAVY}; padding:4.5mm 3.5mm; font-size:9pt; line-height:1.95;
      inline-size:100%; margin-inline-start:4mm; }}
.sum .lbl {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:7.5pt;
            font-weight:700; color:{NAVY}; }}
.sum p {{ text-indent:0; }}

/* 図 */
.area.figb {{ bottom:88mm; }}
.figbox {{ position:absolute; left:13mm; right:13mm; bottom:20mm; height:62mm;
          writing-mode:horizontal-tb; font-family:"Noto Sans CJK JP",sans-serif; }}
.figcap {{ font-size:7pt; color:{GRAY}; margin-bottom:1.5mm; letter-spacing:.06em; }}
.figbox svg {{ width:100%; height:calc(100% - 5mm); display:block; }}
.illu {{ position:absolute; }}

/* 章扉 */
.tobira {{ position:absolute; top:42mm; bottom:50mm; left:16mm; right:18mm;
          writing-mode: vertical-rl; font-family:"Noto Serif CJK JP",serif; }}
.tobira .aori {{ font-size:8.5pt; color:{GRAY}; margin-inline-end:6mm; }}
.tobira .cno {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:8pt;
               color:{NAVY}; letter-spacing:.1em; margin-block-end:3mm; }}
.tobira .ct1 {{ font-size:13pt; color:#333; margin-inline-end:4mm; line-height:1.6; }}
.tobira .ct2 {{ font-size:22pt; font-weight:600; letter-spacing:.04em; }}
.tobira .bar {{ position:absolute; inset-block:0; inset-inline-end:-6mm;
               border-inline-start:3px solid {NAVY}; }}

/* 目次 */
.toc {{ font-size:9pt; line-height:1.75; }}
.toc .chead {{ inline-size:100%; margin-inline-end:7mm; }}
.toc .chead .cno {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:7.5pt;
                   color:{NAVY}; margin-block-end:2mm; }}
.toc .chead .cname {{ font-size:14pt; font-weight:600; letter-spacing:.03em; }}

.item {{ margin-inline-end:5mm; inline-size:100%; position:relative; }}
.item .l1 {{ font-size:9.5pt; }}
.item .l1 .n {{ font-family:"Noto Sans CJK JP",sans-serif; font-weight:700;
               color:{NAVY}; font-size:9pt; text-combine-upright:all;
               margin-block-end:1.2mm; }}
.item .l2 {{ font-size:7.8pt; color:#666; margin-inline-start:1.5mm; }}
.item .l3 {{ font-size:7.8pt; color:{NAVY}; margin-inline-start:1.5mm; }}
.item .pg {{ position:absolute; inset-inline-end:0; inset-block-start:1mm;
            font-family:"Noto Sans CJK JP",sans-serif; font-size:7pt; color:{GRAY};
            text-combine-upright:all; }}
"""

def page(hashira, nombre, inner, cls="area"):
    h = f'<div class="hashira">{hashira}</div>' if hashira else ''
    n = f'<div class="nombre">{nombre}</div>' if nombre else ''
    return f'<div class="page">{h}<div class="{cls}">{inner}</div>{n}</div>'

P = []

# ------------------------------------------------ 1 章扉
P.append(f'''<div class="page">
<div class="tobira">
  <div class="bar"></div>
  <div class="aori">覚えた、を信じないところから始まる</div>
  <div class="ct1">頭のいい人が、絶対にやらないこと</div>
  <div class="cno">第<span class="tcy">5</span>章</div>
  <div class="ct2">覚えるとき</div>
</div></div>''')

# ------------------------------------------------ 2 項目の1ページ目
inner = '''
<div class="opener">
  <div class="num">23</div>
  <div class="ttl">単語を、<br>1語10回ずつ書いて覚える</div>
  <div class="tag">やり方</div>
</div>
<div class="xo">
  <p class="x">×「10回書けば、さすがに覚える」</p>
  <p class="o">○「見て、隠して、出す。これで1周」</p>
</div>
<p class="noind">英語の小テストが明日あります。範囲は30語。</p>
<p>ノートを開いて、1語ずつ書いていきます。</p>
<p class="noind">　　available available available available ……</p>
<p>10回書きました。次の単語に移ります。</p>
<p>30語かける10回で、300回。1時間かかりました。手が疲れました。</p>
<p>翌日の小テスト。30問中、18問正解でした。</p>
<p>1時間かけて、12問落としています。</p>
'''
P.append(page('第5章　覚えるとき', '112', inner))

# ------------------------------------------------ 3 本文つづき
inner = '''
<h2>書いている間、単語帳を見ています</h2>
<p>10回書くとき、ほとんどの人は単語帳を見ています。</p>
<p>見ながら書いているあいだ、頭は何をしているか。</p>
<p>文字の形を、目から手に移しています。これは、写す作業です。</p>
<p>思い出していません。1回もです。</p>
<p>手は300回動きました。頭は0回です。</p>
<h2>前に配った教材で、こう書きました</h2>
<p class="noind">　　書いて覚えるより、見て覚えるほうが速い。</p>
<p>あれは、半分合っていて、半分足りませんでした。</p>
<p>正確には、こうです。</p>
<p class="noind">　　見て、隠して、出す。</p>
<p>見るだけだと、速いけれど残りません。見たあとに隠して、出せたかどうかを確かめる。ここまでで1周です。</p>
'''
P.append(page('23　単語を、1語10回ずつ書いて覚える', '113', inner))

# ------------------------------------------------ 4 頭のなか
inner = '''
<h2>頭のなか</h2>
<div class="minds">
  <div class="mind ng">
    <div class="cap">ノートに向かって、伸びない人</div>
    <p>「available、available……」</p>
    <p>（単語帳を見ながら書く）</p>
    <p>「あと7回」</p>
    <p>「次、consist」</p>
    <p>（また見ながら書く）</p>
  </div>
  <div class="mind ok">
    <div class="cap">同じとき、頭のいい人</div>
    <p>「10個、見る」</p>
    <p>（30秒見る）</p>
    <p>（単語帳を閉じる）</p>
    <p>「available ……利用できる、だ」</p>
    <p>「consist ……」</p>
    <p>「……出てこない」</p>
    <p>「飛ばして次。indicate ……示す」</p>
    <p>（10個書いて、開く）</p>
    <p>「出なかったのは、consist と obtain の2個か」</p>
    <p>「この2個だけ、もう1回見る」</p>
  </div>
</div>
'''
P.append(page('23　単語を、1語10回ずつ書いて覚える', '116', inner))

# ------------------------------------------------ 5 やり方＋まとめ
inner = '''
<h2>やり方</h2>
<h3>1　10個だけ見る</h3>
<p>30個を一気に見ないでください。10個ずつです。見る時間は30秒。覚えようとしなくていいです。眺めるだけ。</p>
<h3>2　閉じて、10個書く</h3>
<p>出てこないものは、飛ばします。粘らないでください。10秒で次に行きます。</p>
<h3>3　開いて、出なかったものだけ印をつける</h3>
<p>出たものは、もう見ません。終わりです。</p>
<div class="sum">
  <p>見ながら書くのは、写す作業。思い出していない。<br>
  10回見ながら書くより、1回思い出して書くほうが残る。しかも速い。</p>
  <p>&nbsp;</p>
  <p><span class="lbl">この場面を見つけた問い</span>　いま、閉じて出せるか？</p>
  <p><span class="lbl">今日やること</span>　今日覚える単語のうち10個を、30秒見てから、閉じて書いてみる。</p>
</div>
'''
P.append(page('23　単語を、1語10回ずつ書いて覚える', '118', inner))

# ------------------------------------------------ 6-7 目次
def toc_item(n, t, x, o, pg):
    return (f'<div class="item"><div class="l1"><span class="n">{n}</span>　{t}</div>'
            f'<div class="l2">×「{x}」</div><div class="l3">○「{o}」</div>'
            f'<div class="pg">{pg}</div></div>')

items_r = [
    ("23","単語を、1語10回ずつ書いて覚える","10回書けば、さすがに覚える","見て、隠して、出す。これで1周","112"),
    ("24","なぜそうなるのかを聞かずに、そのまま覚える","そういうものだと、覚えておこう","なぜ？　を1回だけ、自分に聞く","119"),
    ("25","なぜを持たずに、語呂だけで覚える","語呂なら、すぐ覚えられる","語呂は、意味を入れたあとの道具","125"),
    ("26","似ている3つを、それぞれ丸ごと覚える","3つとも、しっかり覚えよう","違うところ1か所だけ、覚える","131"),
    ("27","覚えたことを、自分の中だけで確かめる","頭の中で言えたから、覚えてる","人に説明する。声に出すと、穴が出る","137"),
]
items_l = [
    ("28","友達と教え合うのを、おしゃべりで終える","一緒にやると、はかどる気がする","お互いに、問題を5問ずつ出し合う","143"),
    ("29","「わかった」を、テストの日まで信じる","あそこは、もうできるから大丈夫","できるかどうかは、出してから決める","148"),
    ("30","忘れてから、最初から覚え直す","もう全部忘れた。1からやり直しだ","忘れる前に、間をあけてもう1回出す","154"),
    ("31","解説を読んで納得したら、次の問題へ進む","なるほど、わかった。次いこう","解説を閉じて、白紙に解き直す","160"),
    ("32","出てこなかったら、すぐ答えをめくる","わからないものは、考えても無駄","10秒だけ出そうとする。粘らない","166"),
]

inner = ('<div class="chead"><div class="cno">第<span class="tcy">5</span>章</div>'
         '<div class="cname">覚えるとき</div></div>'
         + "".join(toc_item(*i) for i in items_r))
P.append(page(None, None, f'<div class="toc">{inner}</div>', cls="area wide"))

inner = "".join(toc_item(*i) for i in items_l)
P.append(page(None, None, f'<div class="toc">{inner}</div>', cls="area wide"))


# ============================================================ 図
FIG_A = '''<svg viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
<style>
 .lbl{font:13px "Noto Sans CJK JP",sans-serif;fill:#111}
 .sm {font:11px "Noto Sans CJK JP",sans-serif;fill:#666}
 .nv {font:13px "Noto Sans CJK JP",sans-serif;fill:#15467E;font-weight:700}
 .gy {font:13px "Noto Sans CJK JP",sans-serif;fill:#999;font-weight:700}
 .bx {fill:#fff;stroke:#bbb;stroke-width:1.2}
 .bxn{fill:#f2f6fb;stroke:#15467E;stroke-width:1.4}
 .bxg{fill:#f7f7f7;stroke:#ccc;stroke-width:1.2;stroke-dasharray:4 3}
 .ar {stroke:#999;stroke-width:1.4;fill:none;marker-end:url(#a1)}
 .arn{stroke:#15467E;stroke-width:1.6;fill:none;marker-end:url(#a2)}
</style>
<defs>
<marker id="a1" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
<path d="M0,0 L7,3.5 L0,7 z" fill="#999"/></marker>
<marker id="a2" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
<path d="M0,0 L7,3.5 L0,7 z" fill="#15467E"/></marker>
</defs>

<text x="4" y="22" class="gy">×</text>
<text x="22" y="22" class="sm">見ながら、10回書く</text>
<rect class="bx" x="22"  y="34" width="66" height="34" rx="3"/>
<text x="55" y="56" class="lbl" text-anchor="middle">単語帳</text>
<line class="ar" x1="92" y1="51" x2="118" y2="51"/>
<rect class="bx" x="122" y="34" width="46" height="34" rx="3"/>
<text x="145" y="56" class="lbl" text-anchor="middle">目</text>
<line class="ar" x1="172" y1="51" x2="198" y2="51"/>
<rect class="bx" x="202" y="34" width="46" height="34" rx="3"/>
<text x="225" y="56" class="lbl" text-anchor="middle">手</text>
<rect class="bxg" x="122" y="78" width="126" height="26" rx="3"/>
<text x="185" y="96" class="sm" text-anchor="middle">頭　ここを通っていない</text>
<text x="268" y="47" class="sm">手　300回</text>
<text x="268" y="65" class="sm">頭　　0回</text>

<line x1="0" y1="120" x2="400" y2="120" stroke="#e2e2e2" stroke-width="1"/>

<text x="4" y="146" class="nv">○</text>
<text x="22" y="146" class="sm">見て、隠して、出す</text>
<rect class="bxn" x="22"  y="156" width="66" height="30" rx="3"/>
<text x="55" y="176" class="lbl" text-anchor="middle">単語帳</text>
<line class="arn" x1="92" y1="171" x2="118" y2="171"/>
<rect class="bxn" x="122" y="156" width="46" height="30" rx="3"/>
<text x="145" y="176" class="lbl" text-anchor="middle">目</text>
<line class="arn" x1="172" y1="171" x2="198" y2="171"/>
<rect class="bxn" x="202" y="156" width="46" height="30" rx="3"/>
<text x="225" y="176" class="nv" text-anchor="middle">頭</text>
<line class="arn" x1="252" y1="171" x2="278" y2="171"/>
<rect class="bxn" x="282" y="156" width="46" height="30" rx="3"/>
<text x="305" y="176" class="lbl" text-anchor="middle">手</text>
<text x="338" y="168" class="sm">手　10回</text>
<text x="338" y="183" class="sm">頭　10回</text>
</svg>'''

FIG_B = '''<svg viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
<style>
 .t {font:12px "Noto Sans CJK JP",sans-serif;fill:#111}
 .s {font:10px "Noto Sans CJK JP",sans-serif;fill:#777}
 .n {font:12px "Noto Sans CJK JP",sans-serif;fill:#15467E;font-weight:700}
 .no{font:22px "Noto Sans CJK JP",sans-serif;fill:#15467E;font-weight:700}
 .bk{fill:#fff;stroke:#999;stroke-width:1.3}
 .sl{fill:#15467E}
 .ln{stroke:#ccc;stroke-width:1}
 .ar{stroke:#15467E;stroke-width:1.6;fill:none;marker-end:url(#b1)}
</style>
<defs><marker id="b1" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
<path d="M0,0 L7,3.5 L0,7 z" fill="#15467E"/></marker></defs>

<text x="4" y="20" class="no">1</text>
<text x="24" y="20" class="t">30秒、見る</text>
<rect class="bk" x="24" y="30" width="96" height="62" rx="3"/>
<line class="ln" x1="72" y1="30" x2="72" y2="92"/>
<text x="48" y="52" class="s" text-anchor="middle">available</text>
<text x="96" y="52" class="s" text-anchor="middle">利用できる</text>
<text x="48" y="72" class="s" text-anchor="middle">consist</text>
<text x="96" y="72" class="s" text-anchor="middle">成り立つ</text>

<line class="ar" x1="128" y1="61" x2="152" y2="61"/>

<text x="160" y="20" class="no">2</text>
<text x="180" y="20" class="t">隠して、出す</text>
<rect class="bk" x="160" y="30" width="96" height="62" rx="3"/>
<line class="ln" x1="208" y1="30" x2="208" y2="92"/>
<text x="184" y="52" class="s" text-anchor="middle">available</text>
<text x="184" y="72" class="s" text-anchor="middle">consist</text>
<rect class="sl" x="208" y="30" width="48" height="62" rx="0"/>
<text x="232" y="66" style="font:11px 'Noto Sans CJK JP',sans-serif;fill:#fff" text-anchor="middle">隠す</text>

<line class="ar" x1="264" y1="61" x2="288" y2="61"/>

<text x="296" y="20" class="no">3</text>
<text x="316" y="20" class="t">印をつける</text>
<rect class="bk" x="296" y="30" width="96" height="62" rx="3"/>
<line class="ln" x1="344" y1="30" x2="344" y2="92"/>
<text x="320" y="52" class="s" text-anchor="middle">available</text>
<text x="368" y="52" class="s" text-anchor="middle">出た　○</text>
<text x="320" y="72" class="s" text-anchor="middle">consist</text>
<text x="368" y="72" class="n" text-anchor="middle">出ない ●</text>

<line x1="0" y1="112" x2="400" y2="112" stroke="#e2e2e2"/>
<text x="4" y="134" class="t">出たものは、もう見ない。●のついたものだけ、もう1回。</text>
<text x="4" y="156" class="s">1セット　2分弱。30語なら3セットで、20分。</text>
</svg>'''

# イラスト（線画）。学研側のイラストレーターに渡す方向性のサンプル
ILLU = '''<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
<g fill="none" stroke="#15467E" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="52" cy="30" r="14"/>
<path d="M30 76 q0-22 22-22 q22 0 22 22"/>
<path d="M12 78 h96"/>
<path d="M12 78 l-2 26 M108 78 l2 26"/>
<path d="M62 70 l24 -6"/>
<path d="M60 62 l26 -8 l8 10 l-26 8 z" fill="#f2f6fb"/>
<path d="M73 56 l8 10"/>
</g>
<path d="M86 30 l0 10 M92 24 l7 7 M96 40 l9 4"
      stroke="#15467E" stroke-width="2" stroke-linecap="round" fill="none" opacity=".45"/>
</svg>'''

# ============================================================ 図を入れたページを差し込む
def figpage(hashira, nombre, inner, cap, svg):
    return (f'<div class="page"><div class="hashira">{hashira}</div>'
            f'<div class="area figb">{inner}</div>'
            f'<div class="figbox"><div class="figcap">{cap}</div>{svg}</div>'
            f'<div class="nombre">{nombre}</div></div>')

# 3ページ目（本文つづき）を、図つきに差し替え
inner3 = """
<h2>書いている間、単語帳を見ています</h2>
<p>10回書くとき、ほとんどの人は単語帳を見ています。</p>
<p>見ながら書いているあいだ、頭は何をしているか。文字の形を、目から手に移しています。これは、写す作業です。</p>
<p>思い出していません。1回もです。手は300回動きました。頭は0回です。</p>
"""
P[2] = figpage('23　単語を、1語10回ずつ書いて覚える', '113', inner3,
               '図　同じ10分で、頭が動いた回数', FIG_A)

# 5ページ目（やり方）を、図つきに差し替え
inner5 = """
<h2>やり方</h2>
<p>30個を一気に見ないでください。10個ずつです。見る時間は30秒。覚えようとしなくていいです。眺めるだけ。</p>
<p>そのあと閉じて、10個書きます。出てこないものは飛ばします。粘らないでください。10秒で次に行きます。</p>
<p>開いて、出なかったものだけに印をつけます。出たものは、もう見ません。</p>
"""
P[4] = figpage('23　単語を、1語10回ずつ書いて覚える', '117', inner5,
               '図　1セットの流れ', FIG_B)

# 章扉にイラストを入れる
P[0] = P[0].replace('</div></div>',
    '</div><div class="illu" style="bottom:24mm;left:18mm;width:30mm;height:30mm;'
    'opacity:.9">' + ILLU + '</div></div>')

# まとめページを追加（6ページ目として挿入）
inner6 = """
<h2>これをやると、何が残るか</h2>
<p>「覚えていない単語のリスト」が残ります。</p>
<p>10回ずつ書いた人の手元には、300個の文字が残ります。どれを覚えていて、どれを覚えていないかは、わかりません。</p>
<p>閉じて出した人の手元には、8個の印が残ります。テストの5分前に見るのは、この8個です。</p>
<div class="sum">
  <p>見ながら書くのは、写す作業。思い出していない。<br>
  10回見ながら書くより、1回思い出して書くほうが残る。しかも速い。</p>
  <p>&nbsp;</p>
  <p><span class="lbl">この場面を見つけた問い</span>　いま、閉じて出せるか？</p>
  <p><span class="lbl">今日やること</span>　今日覚える単語のうち10個を、<br>30秒見てから、閉じて書いてみる。</p>
</div>
"""
P.insert(5, page('23　単語を、1語10回ずつ書いて覚える', '118', inner6))

html = f'<meta charset="utf-8"><title>見本</title><style>{CSS}</style>' + "".join(P)
os.makedirs("build", exist_ok=True)
io.open("build/見本_四六判.html","w",encoding="utf-8").write(html)
print("ok", len(P), "ページ")
