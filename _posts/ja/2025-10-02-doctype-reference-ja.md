---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter DOCTYPE宣言リファレンス
translated: true
type: note
---

### 概要
これはCodeIgniterフレームワーク（オープンソースのWebアプリケーションフレームワーク）のPHP配列で、様々なマークアップ言語に対するDOCTYPE宣言を定義しています。DOCTYPEは文書型宣言であり、HTML文書で使用されるマークアップ言語のバージョンと標準をブラウザやバリデータに伝えます。これにより適切なレンダリングと検証が保証されます。これらの宣言は公式のW3C標準に基づいています。以下では、目的と典型的な使用例を含め、テーマ別にグループ化して各々を説明します。

### XHTML Doctypes
XHTML（eXtensible HyperText Markup Language）はXMLとして再構成されたHTMLであり、より厳格な構文（例：閉じタグの必須化、要素の小文字化）を強制します。
- **xhtml11**: XHTML 1.1を宣言します。モジュラー機能を備えた最新のXHTMLバージョンで、高度なWebアプリ向けです。厳格でXML準拠。フレームやレガシー要素のないモダンでセマンティックなWebページに使用されます。
- **xhtml1-strict**: XHTML 1.0 Strict。非推奨要素（例：`<font>`）を含まない、クリーンでセマンティックなマークアップを強制します。後方互換性を必要とする標準準拠サイトに理想的です。
- **xhtml1-trans**: XHTML 1.0 Transitional。HTML 3.2/4.0からの移行を容易にするため、一部のレガシーHTML要素を許可します。新旧のマークアップが混在する既存サイトで有用です。
- **xhtml1-frame**: XHTML 1.0 Frameset。`<frameset>`によるフレームレイアウトをサポートします。ユーザビリティ問題とSEO上の欠点により、モダンなWebデザインでは廃止されています。
- **xhtml-basic11**: XHTML Basic 1.1。モバイルデバイスやシンプルなアプリケーション向けの軽量プロファイルで、フォームやスタイルシートなどの高度な機能を除外しています。

### HTML Doctypes
HTMLはWebページの標準マークアップ言語で、緩い標準から厳格な標準へ進化してきました。
- **html5**: モダンなHTML5 DOCTYPE。シンプルで将来性があり、すべてのブラウザで標準モードでパースされます。マルチメディア、API、セマンティック要素（例：`<article>`、`<header>`）をサポート。新しいWebサイトに推奨されます。
- **html4-strict**: HTML 4.01 Strict。非推奨要素なしでセマンティックな厳密さを強制します。厳格な準拠を必要とするレガシープロジェクトで使用されます。
- **html4-trans**: HTML 4.01 Transitional。許可的で、段階的な更新のためにレガシータグを許可します。標準への移行中の古いサイトで一般的です。
- **html4-frame**: HTML 4.01 Frameset。フレームページ用で、読み込みの遅さとアクセシビリティ問題により現在は非推奨です。

### MathML Doctypes
MathML（Mathematical Markup Language）は、Web上で数学表記を表示できるようにします。
- **mathml1**: MathML 1.0。XML形式での基本的な数式レンダリング。シンプルな数式を含む教育ツールや文書で使用されます。
- **mathml2**: MathML 2.0。複雑な数学をサポートする機能強化、他のマークアップとのより良い統合。モダンな数学Web表示の基盤です。

### SVG Doctypes
SVG（Scalable Vector Graphics）は、Webグラフィックスのためのベクター画像をXMLで定義します。
- **svg10**: SVG 1.0。基本的な2Dベクターグラフィックス。静的なイラストに使用されます。
- **svg11**: SVG 1.1。アニメーションとフィルターを備えた完全な2Dグラフィックス。動的なWebグラフィックスの標準です。
- **svg11-basic**: SVG 1.1 Basic。機能を抑えたモバイル向けサブセット。デバイス上の軽量SVG用です。
- **svg11-tiny**: SVG 1.1 Tiny。携帯電話などの低電力デバイス向け最小プロファイル。基本的な形状とアニメーションをサポートします。

### 複合Doctypes
これらはリッチなマルチメディアコンテンツのために複数の標準を組み合わせます。
- **xhtml-math-svg-xh**: MathML 2.0およびSVG 1.1を組み込んだXHTML 1.1。テキスト、数式、グラフィックスが混在する文書（例：科学論文）向けです。
- **xhtml-math-svg-sh**: 上記と同様ですが、SVG（`<svg:svg>`）をルートとします。XHTMLとMathMLが埋め込まれたSVG主体の文書向けです。
- **xhtml-rdfa-1**: RDFa 1.0（Resource Description Framework in attributes）を組み込んだXHTML。メタデータ豊富なサイトのためのセマンティックWebデータ埋め込みを強化します。
- **xhtml-rdfa-2**: RDFa 1.1を組み込んだXHTML。HTML属性でのデータ連携のための改良版RDFa。Web of dataアプリケーションで使用されます。

### 使用上の注意
- これらはCodeIgniterに事前定義されており、`doctype()`ヘルパー関数を通じて簡単に挿入できます。
- モダンなWeb開発では、柔軟性とブラウザサポートの点でHTML5（`html5`）が好まれます。古いDOCTYPE（例：HTML 4やフレーム版）は大部分が時代遅れです。
- W3C仕様（例：w3.org/TR/html5/、w3.org/TR/xhtml11/）によって裏付けられており、一貫したパースを保証します：ブラウザはこれらを使用して標準モードまたは互換モードをトリガーし、レイアウトとスクリプトに影響を与えます。最適な検証（W3C Validatorなどのツール経由）のために、プロジェクトのマークアップニーズに基づいて選択してください。CodeIgniterで作業している場合は、ビューで配列キーを使用して宣言を出力します。