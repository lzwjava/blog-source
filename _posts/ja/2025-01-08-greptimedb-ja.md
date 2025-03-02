---
audio: false
generated: false
lang: ja
layout: post
title: 企業は統合を容易にするためにAIコンテキストまたはエージェントを提供すべき
translated: true
---

Greptime DB で働いている友人がいて、彼らの製品を既存のシステムに迅速に統合する方法について考えていました。

## コンテキスト

一つの潜在的なアプローチは、より多くのAIコンテキストを提供することです。Greptime DBは、ChatGPTのようなAIツールと互換性のある方法でドキュメントを整理し、統合プロセスを効率化することができます。

Greptime DBは[https://greptime.com](https://greptime.com)にドキュメントを提供していますが、ChatGPTやDeepSeekのようなツールがそのドキュメントのすべてのページを効率的に処理できるかどうか疑問に思います。さらに、GitHubリポジトリ、イシュー、内部ドキュメント、公開ドキュメント、そして明示的に文書化されていない隠れた知識など、多くの情報が広く散在しています。

この問題に対処するため、Greptime DB はいくつかの専門的な GPT を作成する必要があるかもしれません。例えば、次のようなプロンプトを作成することが考えられます：

```

### Greptime Docs:  
公式ドキュメントはこちらでご覧いただけます: [https://docs.greptime.com](https://docs.greptime.com)

* [クイックスタートガイド](https://docs.greptime.com/getting-started/quick-start)  
* [ユーザーガイド](https://docs.greptime.com/user-guide/overview)  
* [デモ](https://github.com/GreptimeTeam/demo-scene)  
* [FAQ](https://docs.greptime.com/faq-and-others/faq)

### リポジトリURL:
以下は、GreptimeDBリポジトリのルートからの主要なディレクトリとファイルです:

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)  
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)  
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)  
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)  
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)  
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)

追加の主要ファイル:

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)  
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)  
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)  
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)  
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)  
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)

ユーザーのクエリに応答する前に、これらのリソースを検索してください。

```markdown
```

これにより、ユーザーはドキュメントに基づいて質問に答えるGPTベースのチャットボットと対話できるようになり、より正確な応答が保証されます。

このGPTを作成しましょう: [https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

この質問に答えることができませんでした。

```
greptimedb/src/query/src/query_engine/context.rs は何についてのファイルですか？
```



## エージェント

私は、統合プロセスを簡素化するために`greptimedb-agent`というツールを構想しています。

以下のようなシンプルなコマンドを実行することを想像してみてください:

```bash
pip install greptimedb-agent
greptimedb-agent
```

上記のコマンドは、GreptimeDBエージェントをインストールし、起動するためのものです。`pip install greptimedb-agent`でエージェントをインストールし、`greptimedb-agent`でエージェントを実行します。

`greptimedb-agent`は、現在のシステムに関する情報（マシンの詳細や既存のコードなど）をインテリジェントに収集し、コンテキストを理解してGreptime DBを最適に統合する方法を決定します。

このコマンドは、あなたのコードを自動的に更新し、Greptime DBを統合します。わずか数ステップで、現在のデータベースをシームレスにGreptime DBに置き換えることができます。

