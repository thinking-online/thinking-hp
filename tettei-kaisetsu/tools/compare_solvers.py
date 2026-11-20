import sys,os,glob,runpy,importlib.util,re,json
def norm(s): return re.sub(r"[^a-z0-9]","",str(s).lower())
def book(d):
    out={}
    for n in range(1,6):
        p=f"{d}/content/parts/part{n}.py"
        if not os.path.exists(p): continue
        sys.path.insert(0,f"{d}/content/parts")
        spec=importlib.util.spec_from_file_location(f"b{n}{d}",p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        P=m.PART; no=str(P.get("no",P.get("roman",n)))
        for q in P["questions"]:
            out[("大問"+no,q["id"])]=(q.get("answer"),q.get("answer_display"),bool(q.get("choices")))
    return out
res={}
for d in sys.argv[1:]:
    B=book(d); sols={os.path.basename(f)[6:-3]:runpy.run_path(f)["ANS"] for f in sorted(glob.glob(f"solve/{d}/solve_*.py"))}
    rows=[]
    for (dai,qid),(ans,disp,mc) in B.items():
        r={"q":f"{dai} {qid}","book":ans if mc else (disp or ans),"mc":mc,"s":{}}
        for k,S in sols.items():
            e=S.get(dai,{}).get(qid)
            if e is None:
                e=next((v.get(qid) for kk,v in S.items() if norm(kk)==norm(dai) and qid in v),None)
            r["s"][k]=e
        rows.append(r)
    print(f"===== {d}  solvers={list(sols)}  設問={len(rows)}")
    for r in rows:
        flags=[]
        for k,e in r["s"].items():
            if e is None: flags.append(f"{k}:欠"); continue
            a=e.get("a")
            same = (str(a).strip().lower()==str(r["book"]).strip().lower()) if r["mc"] else (norm(a)==norm(r["book"]) or norm(a) in norm(r["book"]))
            if not same: flags.append(f"{k}≠:{a}({e.get('conf')})")
            elif e.get("conf")!="高": flags.append(f"{k}={e.get('conf')}")
        if flags: print(f"  {r['q']:<18} 本={str(r['book'])[:40]:<40} | "+"  ".join(flags))
