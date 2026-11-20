import sys,importlib.util,json,os
d=sys.argv[1]; out=[]
for n in range(1,6):
    p=f"{d}/content/parts/part{n}.py"
    if not os.path.exists(p): continue
    sys.path.insert(0,f"{d}/content/parts")
    spec=importlib.util.spec_from_file_location(f"p{n}_{d}",p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    P=m.PART
    for q in P["questions"]:
        ch=[c.get("key") for c in q.get("choices",[])] if q.get("choices") else None
        out.append((P.get("no",P.get("roman",n)),q["id"],q.get("type",""),ch))
key={}
for x in out: key.setdefault(str(x[0]),[]).append(x)
with open(f"{d}/work/qids.txt","w") as f:
    for k,v in key.items():
        f.write(f"大問{k}:\n")
        for _,i,t,ch in v: f.write(f"  {i}  [{t}]" + (f"  選択肢キー: {','.join(map(str,ch))}" if ch else "  （記述・整序・抜き出し）") + "\n")
print(d,len(out))
