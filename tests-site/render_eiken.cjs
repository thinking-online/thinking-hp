const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs=require('fs'),path=require('path');
const ROOT='/home/user/thinking-hp',OUT=path.join(ROOT,'test-pdfs');
const books=process.argv.slice(2);
(async()=>{
 const b=await chromium.launch();const pg=await b.newPage();let i=0;
 for(const book of books){
   const base=path.join(ROOT,'test',book);
   const ranges=fs.readdirSync(base).filter(d=>fs.statSync(path.join(base,d)).isDirectory());
   const dir=path.join(OUT,book);fs.mkdirSync(dir,{recursive:true});
   for(const range of ranges){
     const f=path.join(base,range,'index.html');
     await pg.goto('file://'+f,{waitUntil:'load'});
     await pg.pdf({path:path.join(dir,`${book}_${range}.pdf`),format:'A4',printBackground:true,margin:{top:'14mm',bottom:'14mm',left:'12mm',right:'12mm'}});
     i++;if(i%20===0)console.log(i);
   }
 }
 await b.close();console.log('DONE',i);
})().catch(e=>{console.error(e);process.exit(1)});
