import sys, importlib.util, html, re
S='/tmp/claude-0/-home-user-thinking-hp/fe35a45f-1f03-5054-8c22-5fcd44116fc2/scratchpad'
def esc(s): return html.escape(re.sub(r'\*\*|【推定】','',str(s)))
for y in [int(a) for a in sys.argv[1:]]:
    yy=str(y)[2:]; d=f'{S}/mjl{yy}/content'
    sys.path.insert(0,d+'/parts')
    for k in ('part1','part2'): sys.modules.pop(k,None)
    spec=importlib.util.spec_from_file_location('b',f'{d}/data/meiji-hogaku_{y}.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); sys.path.pop(0)
    B=m.BOOK; ov=B['overview']; P=B['parts']
    n=sum(len(p['questions']) for p in P); words=sum(p['body_words'] for p in P)
    official= y==2026
    diffq=[(p,q) for p in P for q in p['questions'] if '不一致' in q.get('checked','')]
    wq=[(p,q) for p in P for q in p['questions'] if any(k in q['type'] for k in ('記述','要約','日本語'))]
    ex_p,ex_q=(wq or diffq or [(P[0],P[0]['questions'][0])])[-1]
    steps=[re.sub(r'\*\*','',s) for s in ex_q.get('steps',[])][:3]
    h=[]
    h.append(f'<p>明治大学 法学部 {y}年度の英語を、全{n}問すべて解説したPDFです。</p>')
    h.append('<p>答えと短い解説が載っているだけの解答では、「なぜそれが答えなのか」は分かっても、「本番でどうやってそこにたどり着くのか」「なぜ自分は間違えたのか」までは分かりません。</p><p>この解説は、その2つに答えるために作りました。</p><ul><li>正解の根拠だけでなく、解く人が頭の中で何をどの順番で考えるか</li><li>誤答の選択肢が、なぜダメなのか</li><li>その誤答を選んでしまう人は、何ができていないのか</li></ul><p>を、1問ずつ書いています。</p>')
    h.append('<h2>この解説でわかること</h2><ul>'+''.join(f'<li>{t}</li>' for t in [f'{y}年度の明治法の英語が、どんな試験だったか（2つの長文の正体と、差がつく所）',f'全{n}問の正解と、その根拠の文（本文のどこにあるか・英文と訳・どの語句が決め手か）','各設問を解く手順（どこを見て、何に気づいて、どう決めるか）','誤答の選択肢がダメな理由と、それを選ぶ人の「思考のくせ」','記述（日本語の要約・説明や英語を書く問題）の解答例と、採点で見られる要点・減点される書き方','すべての選択肢の訳と、それが正解・不正解になる理由','本文の流れが一目で分かる「英文マップ」','段落ごとの全訳と、「つまりどういうことか」をかみくだいた説明','間違えた問題を「失点の型」で分けて、次に何をすればいいかが分かる復習の進め方'])+'</ul>')
    h.append(f'<h2>{y}年度 明治法の英語はこんな試験でした</h2><p>大問は2つで、合わせて約{words:,}語の長文を読みます。1題が長いのが明治法の特徴です。</p><ul>'+''.join(f'<li>大問{p["no"]}：{esc(p["title"])}</li>' for p in P)+'</ul>')
    h.append('<p>設問は、下線部の言い換え・英語の質問に答える問題・内容一致が中心で、記述もあります。本文を段落ごとに要約しながら読み、設問の根拠の段落をすばやく見つけられるかで差がつきます。</p>')
    for i,(lab,txt,_) in enumerate(ov['diff_points'][:3]):
        h.append(f'<h3>差がつく所{i+1}：{esc(lab)}</h3><p>{esc(txt)}</p>')
    h.append('<h2>中身（目次）</h2><ul><li>この年度の全体像（大問構成・時間配分・解く順番・差がつく所）</li><li>大問ごとに（I・II）：この文章の正体（一行で）／設問タイプと攻め方／英文マップ（段落の流れと、設問がどこにあるか）／設問ごとの解説（出題意図・解く手順：読む→気づく→絞る→確かめる・根拠の文と訳・全選択肢の訳と正誤の理由・その誤答を選ぶ人の思考）／全訳（段落ごとの全訳＋「つまり」のかみくだいた説明）</li><li>総まとめ（全問の解答一覧・失点の型別の復習の進め方・自己採点表）</li></ul><p>紙面はカラーで、正解・根拠の文・決め手の語句・罠が一目で分かるように色分けしています。</p>')
    h.append(f'<h2>たとえば、こんな解説です（大問{ex_p["no"]} {esc(ex_q["id"])} より）</h2><p>{esc(ex_q.get("target",""))}</p>'+(f'<p>{esc(ex_q.get("intent",""))}</p>' if ex_q.get('intent') else '')+'<p>解説では、次のような手順で答えにたどり着く過程を書いています。</p><ol>'+''.join(f'<li>{esc(s)}</li>' for s in steps)+f'</ol><p>このように、全{n}問で「どこを見れば決まるか」と「間違える人はどこを見ていないか」をセットで書いています。</p>')
    h.append('<h2>こんな人におすすめです</h2><ul><li>明治大学 法学部を受ける人</li><li>過去問を解いたけれど、答え合わせで終わってしまっている人</li><li>「なんとなく正解した問題」を、次も確実に取れるようにしたい人</li><li>長い英文で根拠の場所が見つけられず、時間が足りなくなる人</li></ul>')
    h.append(f'<h2>使い方</h2><ol><li>明治大学 法学部 {y}年度の英語の問題を用意して、印刷してください。この解説PDFには、問題文と英文の本文は入っていません（設問の下線部と短い引用だけを示しています）。問題は過去問題集などで入手してください。</li><li>時間を計って解きます。</li><li>総まとめの解答一覧で答え合わせをします。</li><li>間違えた問題、迷った問題から、設問ごとの解説を読みます。</li><li>全訳と英文マップで、本文の流れを確認します。</li><li>失点の型別の復習の進め方に沿って、次にやることを決めます。</li></ol>')
    if official:
        a=f'<p>選択問題・記述の正解は、明治大学が公表している解答と照合しています。設問ごとの配点は公表されていないため、自己採点表の配点は THINKING の推定です。</p>'
    else:
        a=f'<p>明治大学は、{y}年度の英語の解答を公表していません。この解説の正解は、THINKING が解答を見ずに解いた答えと、市販の解答を1問ずつ突き合わせて決めました。</p>'
        if diffq: a+='<p>'+'、'.join(f'大問{p["no"]} {esc(q["id"])}' for p,q in diffq)+'は、本文の根拠から市販の解答とは異なる答えを正解としています（理由は解説に書いています）。</p>'
        a+='<p>記述の解答例は THINKING が作成したものです。設問ごとの配点は公表されていないため、自己採点表の配点は THINKING の推定です。</p>'
    h.append('<h2>正解について</h2>'+a)
    h.append(f'<h2>料金</h2><ul><li>1年分（{y}年度）：550円 ← この記事です</li><li>3年分セット：990円（準備中）</li><li>5年分セット：1,490円（準備中）</li></ul>')
    h.append('<h2>明治法の対策をもっとしたい人へ</h2><p>THINKING では、明治大学 法学部の英語を大問ごとに鍛える問題集シリーズも作っています。過去問で見つかった弱点を、大問ごとの問題集で集中して練習できます。</p><p>問題集の詳細・質問・相談は、THINKING 公式LINEからどうぞ。<br>https://line.me/R/ti/p/@499yrupi</p>')
    h.append('<h2>よくある質問</h2><h3>問題文は入っていますか？</h3><p>入っていません。問題は各自で用意して、手元に置いて使ってください。</p><h3>スマホでも読めますか？</h3><p>PDFなので、スマホ・タブレット・パソコンのどれでも読めます。書き込みながら使う場合は、印刷するのがおすすめです。</p><h3>何ページありますか？</h3><p>PAGES ページです。</p><h3>他の年度はありますか？</h3><p>2022〜2026年度の5年分を作っています。3年分・5年分のセットも準備中です。</p>')
    free='<html><head><meta charset="utf-8"></head><body>\n'+'\n'.join(h)+'\n</body></html>\n'
    paid=open(f'{S}/wsc25/note/paid.html',encoding='utf-8').read().replace('早稲田大学 商学部 2025年度','明治大学 法学部 %d年度'%y).replace('90分で','時間を計って').replace('1〜2週間あけてから、もう一度90分で解いてください','1〜2週間あけてから、もう一度時間を計って解いてください')
    open(f'{S}/mjl{yy}/note/free.html','w',encoding='utf-8').write(free); open(f'{S}/mjl{yy}/note/paid.html','w',encoding='utf-8').write(paid)
    print(y,n,words,len(diffq),ex_q['id'], '早稲田' in paid, '90分' in paid)
