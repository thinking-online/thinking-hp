const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'); const path = require('path');
const ROOT='/home/user/thinking-hp';
const OUT=path.join(ROOT,'test-pdfs');
function walk(d,out){ for(const e of fs.readdirSync(d,{withFileTypes:true})){ const p=path.join(d,e.name); if(e.isDirectory()) walk(p,out); else if(e.name==='index.html') out.push(p);} return out;}
const all=walk(path.join(ROOT,'test'),[]);
// keep only depth-3 test pages: test/<book>/<range>/index.html
const pages=all.filter(p=>{const rel=path.relative(ROOT,p).split(path.sep); return rel.length===4;});
(async()=>{
  const b=await chromium.launch();
  const pg=await b.newPage();
  let i=0;
  for(const f of pages){
    const rel=path.relative(path.join(ROOT,'test'),f).split(path.sep); // [book, range, index.html]
    const book=rel[0], range=rel[1];
    const dir=path.join(OUT,book); fs.mkdirSync(dir,{recursive:true});
    const out=path.join(dir,`${book}_${range}.pdf`);
    await pg.goto('file://'+f,{waitUntil:'load'});
    await pg.pdf({path:out,format:'A4',printBackground:true,margin:{top:'14mm',bottom:'14mm',left:'12mm',right:'12mm'}});
    i++; if(i%25===0) console.log(`${i}/${pages.length}`);
  }
  await b.close();
  console.log('DONE',i,'pdfs');
})().catch(e=>{console.error(e);process.exit(1)});
