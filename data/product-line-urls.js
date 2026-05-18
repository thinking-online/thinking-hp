/**
 * 大学・学部別マニュアル専用 LINE URL（slug → LIFF）
 *
 * ※ data/line-url.js の一括変更の対象外。各 product-*.html から読み込む。
 * ※ 新しいマニュアルページを追加するときは、ここに slug を登録し、
 *    該当 HTML で applyProductLineUrl("slug") を呼ぶ。
 */
window.THINKING_PRODUCT_LINE_URLS = {
  "kangaku-english":
    "https://liff.line.me/1656043253-rkMxPZMQ/landing?follow=%40499yrupi&lp=QBjnFI&liff_id=1656043253-rkMxPZMQ",
};

/** @param {string} [slug] product data の slug */
window.getThinkingLineUrl = function (slug) {
  if (slug && window.THINKING_PRODUCT_LINE_URLS && window.THINKING_PRODUCT_LINE_URLS[slug]) {
    return window.THINKING_PRODUCT_LINE_URLS[slug];
  }
  return window.THINKING_LINE_LIFF_URL || "#";
};

/**
 * 商品ページ用: 専用 URL があれば THINKING_LINE_LIFF_URL を上書き（ヘッダー・フッター含む）
 * @param {string} slug
 * @returns {string}
 */
window.applyProductLineUrl = function (slug) {
  var url = window.getThinkingLineUrl(slug);
  if (slug && window.THINKING_PRODUCT_LINE_URLS && window.THINKING_PRODUCT_LINE_URLS[slug]) {
    window.THINKING_LINE_LIFF_URL = url;
  }
  return url;
};
