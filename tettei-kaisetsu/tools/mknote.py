import sys, importlib.util, html
S='/tmp/claude-0/-home-user-thinking-hp/fe35a45f-1f03-5054-8c22-5fcd44116fc2/scratchpad'
def load(y):
    d=f'{S}/wsc{str(y)[2:]}/content'
    sys.path.insert(0,d+'/parts')
    spec=importlib.util.spec_from_file_location(f'b{y}',f'{d}/data/waseda-shogaku_{y}.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k in ['part1','part2','part3','part4','part5']: sys.modules.pop(k,None)
    sys.path.pop(0); return m.BOOK
EX={
2024:("大問I 設問4（和文英訳）","会話の中の「5分前まで何も聞いていませんでした」を、hear を使って7語の英語にする問題です。",
 ["ポイントは、1語目が解答用紙にすでに印刷されていることです。そこを見落とすと主語を二重に書いてしまい、語数もずれます。","さらに、過去完了や否定の形にすると8語になってしまい、7語に収まる言い方は限られます。解説では、語数を指で数えながら until を使って組み立てる手順と、よくある減点例を並べています。"]),
2023:("大問I 設問3（補充・仮定法）","「（応募が）1つも届かなかったとしても、私は驚かなかったでしょう」という日本語に合うよう、英文の括弧に語を入れる問題です。",
 ["決め手は、日本語の「〜だったとしても」「〜だっただろう」から、過去の事実と反対のことを仮定する形（仮定法過去完了）だと先に決めることです。","形が決まれば、主節の would not have been と、if 節の had not received any が括弧の数どおりに入ります。解説では、括弧ごとに入る語とその理由、よくある書き間違い（did not の形・been の抜けなど）を示しています。"]),
2022:("大問V 設問5（数字の当てはめ）","報告書の本文の4つの空所に入る数字の組み合わせを、選択肢から選ぶ問題です。",
 ["1つの空所だけで選ぶと、ほかの空所と矛盾する組み合わせが残ります。","決め手は、「1ポイントだけ上がって15に」のように確実に決まる空所から先に決め、残りの選択肢を条件で消していく順番です。解説では、この消去の手順を1段ずつ示しています。"]),
}
ANS={
2024:["早稲田大学は、2024年度の英語の解答を公表していません。この解説の正解は、市販の解答と、THINKINGで別に解いた答えを1問ずつ照合して決めました。",
      "1問（大問V 設問4）だけは、本文の読み方によって答えが分かれる問題です。この解説では THINKING の判断を正解として示したうえで、もう一つの読み方の根拠も同じ重さで説明しています。配点も公表されていないため、自己採点表の配点は THINKING の推定です。"],
2023:["早稲田大学は、2023年度の英語の解答を公表していません。この解説の正解は、市販の解答と、THINKINGで別に解いた答えを1問ずつ照合して決めました（全問一致）。",
      "配点も公表されていないため、自己採点表の配点は THINKING の推定です。"],
2022:["早稲田大学は、2022年度の英語の解答を公表していません。この解説の正解は、市販の解答と、THINKINGで別に解いた答えを1問ずつ照合して決めました。",
      "大問I 設問4は2通りの書き方を正解として示しています。また大問IV 設問1-1は、本文の根拠から市販の解答とは異なる答えを正解としています（理由は解説に書いています）。配点も公表されていないため、自己採点表の配点は THINKING の推定です。"],
}
def strip(s): return s.replace('**','').replace('【推定】','')
for y in (2024,2023,2022):
    B=load(y); ov=B['overview']
    n=sum(len(p['questions']) for p in B['parts'])
    words=ov['lead'].split('総語数は約')[1].split('語')[0] if '総語数は約' in ov['lead'] else ''
    items=''.join(f'<li>大問{r[0]}：{html.escape(strip(r[1]))}</li>' for r in ov['structure'])
    diffs=''.join(f'<h3>差がつく所{i+1}：{html.escape(strip(d[0]))}</h3><p>{html.escape(strip(d[1]))}</p><p>分かれ目は、{html.escape(strip(d[2]))}</p>' for i,d in enumerate(ov['diff_points'][:3]))
    t,lead,ps=EX[y]
    exam_line=strip(ov['exam_line']).replace('【試験時間】','').replace('　',' ')
    free=open(f'{S}/wsc25/note/free.html',encoding='utf-8').read()
    a=free.index('<h2>2025年度'); b=free.index('<h2>中身（目次）</h2>')
    sec=f'<h2>{y}年度 早稲田商の英語はこんな試験でした</h2><p>90分で、5つの大問・約{words}語を読みます。{html.escape(strip(ov["lead"]).split("。",1)[1])}</p><ul>{items}</ul><p>たとえば次のような所で、取れる人と取れない人が分かれます。</p>{diffs}'
    free=free[:a]+sec+free[b:]
    a=free.index('<h2>たとえば、こんな解説です'); b=free.index('<h2>こんな人におすすめです</h2>')
    ex=f'<h2>たとえば、こんな解説です（{t} より）</h2><p>{lead}</p>'+''.join(f'<p>{p}</p>' for p in ps)+f'<p>このように、全{n}問で「どこを見れば決まるか」と「間違える人はどこを見ていないか」をセットで書いています。</p>'
    free=free[:a]+ex+free[b:]
    a=free.index('<h2>正解について</h2>'); b=free.index('<h2>料金</h2>')
    free=free[:a]+'<h2>正解について</h2>'+''.join(f'<p>{p}</p>' for p in ANS[y])+free[b:]
    free=free.replace('2025年度',f'{y}年度').replace('全63問',f'全{n}問')
    free=free.replace('<li>大問Vの抜き出し（9〜14語）で、どこを抜けば正解になるか</li>','<li>記述（整序・補充・抜き出しなど）の組み立て方と、よくある減点例</li>')
    free=free.replace('<li>整序（並べ替え）の組み立て方と、不要語・印刷済みの語の扱い</li>','<li>整序（並べ替え）の不要語・加える語・印刷済みの語の扱い</li>')
    free=free.replace(f'<p>{y}年度の解説もあります。','<p>2026年度・2025年度の解説もあります。')
    free=free.replace('2026年度の解説もあります。','2026年度・2025年度の解説もあります。')
    free=free.replace('<li>1年分（'+str(y)+'年度）：550円 ← この記事です</li>','<li>1年分（'+str(y)+'年度）：550円 ← この記事です</li>')
    d=f'{S}/wsc{str(y)[2:]}/note'
    open(d+'/free.html','w',encoding='utf-8').write(free)
    paid=open(f'{S}/wsc25/note/paid.html',encoding='utf-8').read().replace('2025年度',f'{y}年度')
    open(d+'/paid.html','w',encoding='utf-8').write(paid)
    print(y,n,words, '2025' in free)
