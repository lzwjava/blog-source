---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Kusto クエリ言語入門
translated: true
type: note
---

### KQL (Kusto Query Language) を Azure で始める

KQL は、Azure Data Explorer、Azure Monitor (Log Analytics)、Microsoft Sentinel などの Azure サービスにおいて、大量の構造化データ、半構造化データ、非構造化データを分析するために設計された、強力な読み取り専用のクエリ言語です。直感的で、パイプベース (データフローに `|` を使用)、ログ分析、テレメトリ、脅威検出などのビッグデータシナリオに最適化されています。以下に、その使用方法をステップバイステップで説明します。

#### 前提条件
- 関連するサービス (例: Azure Data Explorer クラスター、Log Analytics ワークスペース、Sentinel インスタンス) にアクセスできるアクティブな Azure サブスクリプション。
- 適切な権限: 少なくとも、データベース、テーブル、ワークスペースへの読み取り権限。
- データの概念 (テーブルやフィルタリングなど) に関する基本的な知識があると役立ちますが、KQL は初心者にも扱いやすいです。
- オプション: Azure Data Explorer アプリをインストールするか、Web UI を使用してすぐに始められます。最初はコーディング環境は必要ありません。

#### ステップ 1: クエリを実行する場所を選択する
KQL はいくつかの Azure サービスで実行されます。データソースに合ったサービスから始めましょう:
- **Azure Data Explorer**: ビッグデータの探索に最適です。Web UI ([dataexplorer.azure.com](https://dataexplorer.azure.com/)) にアクセスし、クラスターとデータベースを選択して、クエリ エディターを開きます。
- **Azure Monitor / Log Analytics**: ログとメトリックの場合。Azure ポータル (portal.azure.com) で、**Monitor > ログ** に移動し、ワークスペースを選択して、クエリ エディターを使用します。
- **Microsoft Sentinel**: セキュリティ分析の場合。Azure ポータルで、**Microsoft Sentinel > ログ** (ワークスペース内) に移動します。
- **その他のオプション**: Microsoft Fabric (KQL クエリ エディター経由) や、Power BI などのツールと統合して視覚化します。

データは階層 (データベース > テーブル > 列) で整理されます。クエリは読み取り専用です。スキーマ変更には管理コマンド (`.` で始まる) を使用します。

#### ステップ 2: 基本的な構文を理解する
KQL クエリは、セミコロン (`;`) で区切られたプレーンテキストのステートメントです。データフローモデルを使用します:
- テーブル名 (例: `StormEvents`) で始めます。
- データをパイプ (`|`) で演算子に渡して、フィルタリング、集計などを行います。
- `count` や `summarize` などの出力で終わります。
- 名前や演算子は大文字と小文字を区別します。必要に応じてキーワードを `['keyword']` で囲みます。

簡単なクエリ構造:
```
テーブル名
| where 条件
| summarize カウント = count() by グループ化列
```

管理コマンド (クエリではありません) は `.` で始まります (例: テーブルを一覧表示する `.show tables`)。

#### ステップ 3: 最初のクエリを作成して実行する
1. 選択したサービス (例: Azure Data Explorer Web UI) でクエリ エディターを開きます。
2. 基本的なクエリを入力します。サンプルデータ (ほとんどの環境で利用可能な StormEvents テーブル) を使用した例:
   ```
   StormEvents
   | where StartTime between (datetime(2007-11-01) .. datetime(2007-12-01))
   | where State == "FLORIDA"
   | count
   ```
   - これは、2007年11月にフロリダ州で発生した嵐をフィルタリングし、その数を返します (例: 28)。
3. **実行** をクリックして実行します。結果はテーブルとして表示されます。UI を使用してグラフとして視覚化したり、エクスポートしたりできます。
4. 反復: `project` (列を選択)、`summarize` (集計)、`extend` (計算列を追加) などの演算子を追加します。

最初に学ぶべき一般的な演算子:
- `where`: 行をフィルタリング (例: `| where Level == "Error"`)。
- `summarize`: 集計 (例: `| summarize avg(Duration) by User`)。
- `join`: テーブルを結合。
- `search`: テーブル全体を全文検索。

#### ステップ 4: 高度な機能とベスト プラクティスを探る
- **時系列と分析**: 傾向に `make-series`、外れ値に `detect-anomalies` などの関数を使用します。
- **視覚化**: エディターで、グリッド/グラフ ビューに切り替えます。ダッシュボード用に Power BI にエクスポートします。
- **パフォーマンスのヒント**: 演算子を論理的に順序付け (早い段階でフィルタリング)、`take 100` で結果を制限し、小さなデータセットでテストします。
- **一般的な使用例**:
  - **ログ分析**: アプリのエラーをクエリ (`| where Level == "Error" | take 50`)。
  - **セキュリティ ハンティング**: Sentinel で脅威を検索 (`search "suspicious login"`)。
  - **データ探索**: メトリックを集計 (`| summarize count() by bin(TimeGenerated, 1h)`)。

#### トラブルシューティング
- エラーですか？ エディターで構文を確認してください (問題が強調表示されます)。テーブル/列名が正確に一致することを確認してください。
- データがありませんか？ ワークスペースにログが取り込まれていることを確認するか、サンプル データセットを使用してください。
- Azure ポータルまたはドキュメントのインタラクティブなチュートリアルで詳細を学べます。

実践的な演習として、Azure Data Explorer にサンプル データを読み込んで実験してください。

[参考文献]
[Kusto クエリ言語 (KQL) の概要](https://learn.microsoft.com/ja-jp/azure/data-explorer/kusto/query/)
[最初の KQL クエリを作成して実行する](https://learn.microsoft.com/ja-jp/azure/data-explorer/kusto/query/tutorial?pivots=azuredataexplorer-cluster)
[一般的な KQL 演算子](https://learn.microsoft.com/ja-jp/azure/data-explorer/kusto/query/tutorial?pivots=azuredataexplorer-cluster&tabs=beginner)