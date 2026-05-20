/**
 * Smart Study English LP — LINE 導線（用途別）
 * 質問・相談会: lp=SIF9cb / 申し込み: lp=sd1BHd
 */
window.SSE_LINE_CONSULT_URL =
  "https://liff.line.me/1656043253-rkMxPZMQ/landing?follow=%40499yrupi&lp=SIF9cb&liff_id=1656043253-rkMxPZMQ";

window.SSE_LINE_APPLY_URL =
  "https://liff.line.me/1656043253-rkMxPZMQ/landing?follow=%40499yrupi&lp=sd1BHd&liff_id=1656043253-rkMxPZMQ";

window.sseConsultUrl = function sseConsultUrl() {
  return window.SSE_LINE_CONSULT_URL || "#";
};

window.sseApplyUrl = function sseApplyUrl() {
  return window.SSE_LINE_APPLY_URL || "#";
};
