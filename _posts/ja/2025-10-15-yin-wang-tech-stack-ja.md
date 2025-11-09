---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 陰王ブログ技術スタック分析
translated: true
type: note
---

ウェブサイト（https://www.yinwang.org/、タイトル「当然我在扯淡」）はカスタム構築されたブログのようです。提供されたHTMLソースに基づく分析：

- **フレームワーク**: 主に **Vue.js**（おそらくバージョン3）で構築されています。Vue固有の属性（`data-v-app`、スコープCSS用の`data-v-[hash]`）、コンポーネント参照（`HomeView`、`PostView`、Vue Routerによるナビゲーション処理の`router-link-active`）から判明
- **ビルドツール**: バンドルと開発に **Vite** を使用。ファビコン（`/vite.svg`）、ハッシュ化されたファイル名のモジュール先読みスクリプト（例：`/assets/index-DS_1rR7p.js`）、Viteの出力に典型的なアセット構造から確認可能
- **スタイリング**: ユーティリティファーストのクラスに **Tailwind CSS** を採用（例：`bg-gray-50 dark:bg-gray-900`、`flex items-center`、`sm:px-4`などのレスポンシブ接頭辞）
- **その他の特徴**: サーバーサイドレンダリングの指標は見られない（Nuxt.jsの痕跡なし）ため、静的サイトまたはクライアントサイドレンダリングのSPAと推測。投稿、タグ、ページネーションから、個人ブログ向けのシンプルなカスタム設定であり、投稿コンテンツにはMarkdownを使用している可能性が高い

**完全な手書きHTMLではなく**—Vueコンポーネントとテンプレートからビルドプロセス中に自動生成されたHTMLです。コアロジック（ルーティング、コンポーネント）はJS/TSでコーディングされていますが、最終出力は最適化された静的ファイルです。HugoやJekyllのような本格的な静的サイトジェネレーターの証拠はなく、軽量なVue + Viteプロジェクトと言えます。

[当然我在扯淡](https://www.yinwang.org/)