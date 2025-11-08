---
audio: false
generated: false
image: false
lang: ja
layout: post
title: AI統合を促進するために企業はAIコンテキストを提供すべき
translated: true
type: post
---

Greptime DBの友人がいて、その製品を既存のシステムに迅速に統合する方法について考えている。

## コンテキスト

1つのアプローチは、より多くのAIコンテキストを提供することです。Greptime DBは、ChatGPTのようなAIツールと互換性のある方法でドキュメントを整理することで、統合プロセスを簡素化できます。

Greptime DBは[https://greptime.com](https://greptime.com)でドキュメントを提供していますが、ChatGPTやDeepSeekのようなツールがドキュメントのすべてのページを効率的に処理できるかどうか疑問に思います。さらに、豊富な情報がGitHubリポジトリ、イシュー、内部ドキュメント、公開ドキュメント、その他明示的にドキュメント化されていない隠れた知識に散らばっています。

これを解決するために、Greptime DBは複数の専用GPTを作成する必要があるかもしれません。例えば、次のようなプロンプトを作成できます：

```

### Greptime Docs:
公式ドキュメントはこちらでご覧いただけます：[https://docs.greptime.com](https://docs.greptime.com)

* [クイックスタートガイド](https://docs.greptime.com/getting-started/quick-start)
* [ユーザーガイド](https://docs.greptime.com/user-guide/overview)
* [デモ](https://github.com/GreptimeTeam/demo-scene)
* [FAQ](https://docs.greptime.com/faq-and-others/faq)

### リポジトリURL:
GreptimeDBリポジトリのルートからの主要ディレクトリとファイル：

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)

追加の主要ファイル：

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)

ユーザーの質問に回答する前に、これらのリソースを検索してください。

```

これにより、ユーザーはドキュメントに基づいて質問に回答するGPTベースのチャットボットと対話でき、より正確な回答が得られます。

このGPTを作成します：[https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

この質問には回答できませんでした、

```
`greptimedb/src/query/src/query_engine/context.rs`について教えてください
```

## エージェント

`greptimedb-agent`というツールを想像しています。これは統合プロセスを簡素化します。

次のような簡単なコマンドを実行すると想像してください：

```bash
pip install greptimedb-agent
greptimedb-agent
```

`greptimedb-agent`は、現在のシステムの情報（マシンの詳細や既存のコードなど）を収集し、コンテキストを理解して、Greptime DBを最適に統合する方法を決定します。

このコマンドは、Greptime DBを統合するために自動的にコードを更新し、数ステップで現在のデータベースをGreptime DBにシームレスに置き換えます。