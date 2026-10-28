/* プレビュー用の仮データ（?preview=1 のときだけ読み込む。本番では使わない）
 * 例: /kakomon-portal/?preview=1&role=guest
 * 権限の絞り込みは GAS の filterCatalog_ と同じ考え方で再現している。 */
window.MOCK_BOOT = function () {
  var role = (location.search.match(/[?&]role=(\w+)/) || [])[1] || "student";
  var today = new Date();
  var recent = new Date(today.getTime() - 3 * 86400000).toISOString().slice(0, 10);

  var books = [
    ["b0001", "MARCH", "明治大学", "めいじ", "明治 全学部統一入試", "全学部統一入試（全学部・3科目／4科目方式）", "明大", false, 10],
    ["b0002", "MARCH", "明治大学", "めいじ", "明治 商学部", "学部別入試・英語4技能試験活用方式", "明大", false, 20],
    ["b0003", "MARCH", "明治大学", "めいじ", "明治 法学部", "学部別入試", "明大", false, 30],
    ["b0004", "MARCH", "立教大学", "りっきょう", "立教 文学部", "文学部独自日程（2/11）", "", true, 40],
    ["b0005", "MARCH", "中央大学", "ちゅうおう", "中央 法学部", "学部別選抜（一般方式・共通テスト併用方式）", "中大", false, 50],
    ["b0006", "関関同立", "同志社大学", "どうししゃ", "同志社 全日程", "全学部日程・学部個別日程（文系・理系すべて）", "", false, 60],
    ["b0007", "関関同立", "立命館大学", "りつめいかん", "立命館 全日程", "全学統一・学部個別配点・薬学・共通テスト併用・後期分割", "", false, 70],
    ["b0008", "関関同立", "関西大学", "かんさい", "関西大学 全学日程", "全学日程1・2（全学部・文系・理系）", "関大", false, 80],
    ["b0009", "日東駒専", "東洋大学", "とうよう", "東洋 全日程", "一般入試 前期・中期・後期（全学部）", "", false, 90],
    ["b0010", "日東駒専", "専修大学", "せんしゅう", "専修 全学部・前期", "スカラシップ・全国入試・全学部入試・前期", "", false, 100],
    ["b0011", "産近甲龍", "近畿大学", "きんき", "近畿大学 全学部（医学部除く）", "一般前期A・B・後期・共通テスト併用・公募推薦", "近大", false, 110],
    ["b0012", "産近甲龍", "龍谷大学", "りゅうこく", "龍谷 全日程", "一般 前期・中期・後期・公募推薦（2教科型）", "", false, 120]
  ].map(function (r) { return { id: r[0], g: r[1], u: r[2], uy: r[3], n: r[4], cov: r[5], kw: r[6], s: r[7], p: true }; });

  var std = [
    ["戦略編", "Vol.0 全体戦略・分析編"],
    ["大問別", "大問1・2 長文読解"],
    ["大問別", "大問3 長文空所補充"],
    ["大問別", "大問4 整序英作文"],
    ["大問別", "大問5 文法・語法"],
    ["大問別", "大問6 会話文"],
    ["単語帳", "必修英単語・熟語帳"],
    ["模試", "総合模試 第1回"],
    ["模試", "総合模試 第2回"]
  ];
  var items = [];
  books.forEach(function (b, bi) {
    std.forEach(function (s, i) {
      items.push({ b: b.id, k: s[0], t: s[1], f: "mock-" + b.id + "-" + i, p: true, d: i === 8 && bi % 3 === 0 ? recent : "2026-09-01" });
    });
  });

  var bought = { b0002: true };
  var allowed = function (b) {
    if (role === "staff" || role === "student") return true;
    if (b.s) return true;
    return role === "buyer" && !!bought[b.id];
  };
  var open = {};
  var outBooks = books.map(function (b) {
    var ok = allowed(b);
    if (ok) open[b.id] = true;
    return { id: b.id, g: b.g, u: b.u, uy: b.uy, n: b.n, cov: b.cov, kw: b.kw, s: b.s, L: !ok, h: false };
  });
  return {
    user: { name: "テスト 太郎", role: role },
    cfg: { title: "THINKING 合格部屋", buyUrl: "https://lin.ee/yJ8MFVb", lineUrl: "https://lin.ee/yJ8MFVb", campusUrl: "#", newDays: 14 },
    catalog: {
      groups: ["MARCH", "関関同立", "日東駒専", "産近甲龍", "その他"],
      kinds: ["戦略編", "大問別", "単語帳", "模試", "解説", "その他"],
      books: outBooks,
      items: items.filter(function (it) { return open[it.b] || it.k === "戦略編"; }),
      // 大学の画像：明治・立教などは img/uni/ の本物、中央だけシート（ドライブ）経由の見本。ほかは画像がないときの枠
      unis: {
        "明治大学": { c: "学部ごとに出題がまったく違う。受ける学部の1冊から始めよう" },
        "中央大学": { i: sampleImage("#24365a", "#F6F4EF", "CHUO") }
      }
    },
    etag: "mock",
    favs: role === "guest" ? [] : ["b0002", "b0006"]
  };
};

/* プレビュー用の見本画像（16:9 の SVG） */
function sampleImage(bg, fg, word) {
  var svg = '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">'
    + '<rect width="1600" height="900" fill="' + bg + '"/>'
    + '<circle cx="1320" cy="180" r="260" fill="' + fg + '" opacity=".18"/>'
    + '<text x="120" y="560" font-family="Georgia,serif" font-size="220" font-weight="700" fill="' + fg + '">' + word + '</text></svg>';
  return "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
}
