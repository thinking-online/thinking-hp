/**
 * SUMMER LOCK-ON LP — LINE 導線
 * 申込時は「夏期特訓 参加」と送信してもらう運用
 */
window.SUMMER_LINE_APPLY_URL =
  "https://liff.line.me/1656043253-rkMxPZMQ/landing?follow=%40499yrupi&lp=summer26&liff_id=1656043253-rkMxPZMQ";

window.getSummerLineUrl = function () {
  return window.SUMMER_LINE_APPLY_URL || window.THINKING_LINE_LIFF_URL || "#";
};
