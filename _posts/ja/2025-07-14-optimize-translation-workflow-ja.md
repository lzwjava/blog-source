---
audio: false
generated: true
lang: ja
layout: post
title: 最適化翻訳：パラグラフハッシュ法
translated: true
type: note
---

### 翻訳ワークフローの最適化に関する考察

あなたの目標は明確です：Jekyllのブログ投稿（Markdownで記述）を8言語に翻訳する際、変更または新しい段落のみを再翻訳し、変更のないものはキャッシュすることで、AIトークンの使用量を最小限に抑えることです。編集にはMarkdownを使い続け、コアコンテンツにデータベース/JSON/YAMLを使用するのは避け、コードブロック（翻訳すべきでないもの）のような特別な要素を処理したいと考えています。段落ベースのアプローチは理にかなっています。なぜなら、それはあなたの執筆と編集の方法に沿っており、文レベルよりも段落レベルの方が、翻訳が文脈的に正確になる可能性があるからです。

主な課題：
- **変更の特定**: バージョン管理の差分がない場合、何が新規/変更/未変更かを検出する方法が必要です。段落のハッシュ化（正規化された英語テキストにSHA-256を使用するなど）は効率的でステートレスです—古いバージョンを完全に保存する必要はありません。
- **Markdown構造の処理**: コードブロック、ヘッダー、リスト、またはその他の構文が問題を引き起こす可能性があるため、単に `\n\n` で分割することはできません。単純な正規表現ベースの分割器は基本的な投稿には機能するかもしれませんが、構造を保存し翻訳不可能な部分をスキップするには、軽量なMarkdownパーサーの方が優れています。
- **キャッシュ**: ファイルベースでシンプルに保ち（例：JSONファイルまたはファイルのディレクトリ）、データベースを避けます。言語ごと、段落ハッシュごとにキャッシュします。
- **トークンの節約**: 長い投稿では、マイナーな編集で使用量を80〜90%削減できる可能性があります。影響を受ける段落のみがAI APIにヒットするためです。
- **エッジケース**: 追加/削除された段落（新しいハッシュ化で対応）；マイナーな調整（例：タイポ修正）は、空白/句読点を正規化しない限り再翻訳をトリガーします；コードブロックやインラインコードは除外する必要があります；段落が並び替えられると、ハッシュは一致しませんが、それを「新規」として扱えば問題ありません。
- **統合**: Jekyllワークフロー（例：bashスクリプトやGitフック経由）で、これをビルド前スクリプトとして実行します。翻訳されたMarkdownファイルを別々に生成するなら、Jekyllプラグインは必要ありません。

これは、文レベル（AIにとって文脈が不正確）や投稿全体（節約にならない）よりも優れています。YAML/JSONは確かにアイデアを書くには煩雑です—Markdownにこだわりましょう。

### 提案する最善の方法：キャッシュとMarkdownを考慮したパーシングを伴う段落ハッシュ化

Pythonスクリプトを使用して：
1. 英語のMarkdownを「翻訳可能な単位」（段落、コードブロック、必要に応じてヘッダーなどを除く）にパースします。
2. 各単位の英語テキストをハッシュ化します（正規化、例：余分な空白を除去）。
3. ハッシュ/言語による既存の翻訳について、ファイルベースのキャッシュを確認します。
4. 不足しているものをAIツール（例：DeepSeek/Mistral API）経由で翻訳します。
5. 新しい翻訳をキャッシュします。
6. 翻訳不可能な部分を保存しながら、翻訳されたMarkdownファイルを再構築します。

**これが最善である理由**:
- **シンプルでオーバーヘッドが少ない**: データベースなし、単なるファイル。AI呼び出しを除き、ローカル/オフラインで実行。
- **柔軟性**: コードブロックをスキップすることで処理可能。他のMarkdown要素（例：ヘッダーが短い場合は翻訳しない）に拡張可能。
- **コスト効率**: 新規/変更された段落に対してのみ支払い。10段落の投稿で1つを編集すると、約90%のトークンを節約。
- **保守性**: 英語のMarkdownを自然に編集；スクリプトが残りを処理。
- **必要なツール**: Python（おそらく所持）。ライブラリ：`hashlib`（ハッシュ化用に組み込み）、`markdown` または `mistune`（パーシング用、必要な場合；「特別な構文なし」の場合は正規表現からシンプルに開始）。

#### ステップバイステップの実装

1. **セットアップ**:
   - `translations_cache.json` ファイル（またはスケーラビリティのために `cache/` のようなハッシュ.jsonファイルのディレクトリ）を作成。
   - 構造： `{ "hash1": { "fr": "翻訳テキスト", "es": "...", ... }, "hash2": { ... } }`
   - これをブログリポジトリ（機密性の高い場合はgit-ignore）または別のディレクトリに保存。
   - スクリプト内であなたの8言語をリストします（例：['fr', 'es', 'de', ...]）。

2. **Markdownのパーシング**:
   - 単純なケース（段落＋コードブロック）の場合：行ごとの処理を使用して、フェンスで囲まれたコードブロック (``````` または `~~~`) およびインデントされたコード（>3スペース）を検出。
   - 連続した非コード、非空白行のブロックとして「段落」を収集。
   - より良い方法：Pythonの `markdown` ライブラリを使用してHTMLに変換し、テキストを抽出しますが、再構築には情報が失われます。代わりに、`mistune`（高速なMarkdownパーサー）を使用してAST（抽象構文木）を取得し、走査して翻訳可能なノード（例：'paragraph'ノード）を変更できるようにします。
   - 必要に応じて `mistune` をインストール（ただし、あなたの環境には基本が含まれていると仮定；ローカルでpipできると想定）。

3. **ハッシュ化**:
   - 正規化： `text.strip().lower()` または単に `.strip()` を使用して、意図的な編集を見逃す可能性はありますが、空白の変更を無視します（希望する場合）。
   - ハッシュ： `hashlib.sha256(normalized.encode()).hexdigest()`

4. **翻訳**:
   - AI APIラッパーを使用（例：DeepSeekの場合："Translate this paragraph to French: {text}" のようなプロンプトを送信）。
   - 可能であればバッチ処理しますが、段落は小さいので逐次処理でも問題ありません。

5. **再構築**:
   - コード/ヘッダーをそのままに、翻訳可能なブロックをキャッシュされた/新しい翻訳に置き換えてMarkdownを再構築。

6. **スクリプト実行**:
   - 実行： `python translate_blog.py path/to/english.md`
   - 出力： `path/to/fr.md`, `path/to/es.md` など。
   - Jekyllの場合：これらを言語プレフィックスを付けて `_posts/` に配置するか、`jekyll-polyglot` のような多言語プラグインを使用して処理。

#### サンプルPythonスクリプト

以下は、行ごとのパーシングを使用した基本的なバージョンです（組み込み以外の外部ライブラリなし）。単純なMarkdown（空白行で区切られた段落、フェンスで囲まれたコードブロック）を想定しています。複雑な構文には `mistune` にアップグレードしてください。

```python
import hashlib
import json
import os
import sys
# AI翻訳関数があると仮定；あなたのDeepSeek/Mistral API呼び出しに置き換えてください
def ai_translate(text, lang):
    # プレースホルダー：API呼び出し結果を返す
    return f"Translated to {lang}: {text}"  # 実際のAPIに置き換え

CACHE_FILE = 'translations_cache.json'
LANGUAGES = ['fr', 'es', 'de', 'it', 'pt', 'zh', 'ja', 'ko']  # あなたの8言語

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=4)

def compute_hash(text):
    normalized = text.strip()  # 正規化をカスタマイズ
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()

def parse_markdown(md_text):
    lines = md_text.splitlines()
    blocks = []
    current_block = []
    in_code = False
    for line in lines:
        if line.strip().startswith('```') or line.strip().startswith('~~~'):
            in_code = not in_code
            if current_block:
                blocks.append(('text', '\n'.join(current_block)))
                current_block = []
            blocks.append(('code', line))
            continue
        if in_code:
            blocks.append(('code', line))
        else:
            if line.strip():  # 非空白
                current_block.append(line)
            else:
                if current_block:
                    blocks.append(('text', '\n'.join(current_block)))
                    current_block = []
    if current_block:
        blocks.append(('text', '\n'.join(current_block)))
    return blocks

def translate_post(english_md_path):
    with open(english_md_path, 'r') as f:
        md_text = f.read()
    
    blocks = parse_markdown(md_text)
    cache = load_cache()
    
    for lang in LANGUAGES:
        translated_blocks = []
        for block_type, content in blocks:
            if block_type == 'code':
                translated_blocks.append(content)
            else:  # text
                h = compute_hash(content)
                if h not in cache:
                    cache[h] = {}
                if lang not in cache[h]:
                    translation = ai_translate(content, lang)
                    cache[h][lang] = translation
                translated_blocks.append(cache[h][lang])
        
        # 改行で再結合
        translated_md = '\n\n'.join(translated_blocks)  # Markdownフォーマット用に調整
        output_path = english_md_path.replace('.md', f'_{lang}.md')
        with open(output_path, 'w') as f:
            f.write(translated_md)
    
    save_cache(cache)
    print("Translations updated.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py path/to/english.md")
    else:
        translate_post(sys.argv[1])
```

**使用方法**:
- `ai_translate` をあなたのAPIロジックに置き換えてください。
- 編集後に投稿ファイルで実行。
- ヘッダー/リストの場合：`parse_markdown` を拡張して（例：`#` または `-` で始まる行を別々のブロックとして）検出。
- 投稿に画像/リンクがある場合：それらはテキストブロック内にあるため変更されません。
- 正規化のヒント：マイナーな句読点の変更を無視したい場合は、ハッシュ化前にそれらを取り除くために正規表現を使用。

#### 拡張機能
- **Git統合**: `git diff` を使用して変更された行を事前に特定しますが、ハッシュ化の方がシンプルです。
- **バッチ翻訳**: APIがサポートしていれば、複数の新しい段落を一度に送信。
- **エラーハンドリング**: 失敗したAPI呼び出しを再試行；翻訳を検証。
- **高度なパーシング**: `mistune` をpipし、そのレンダラーを使用してカスタマイズ（例：'code_block'ノードをスキップ）。
- **テスト**: SHA-256ではハッシュ衝突は稀；サンプル投稿でテスト。

これは、あなたのワークフローを複雑にすることなくトークンを節約するはずです。あなたのMarkdownがより複雑な場合は、これから始めて反復してください。API統合に調整やヘルプが必要な場合はお知らせください！