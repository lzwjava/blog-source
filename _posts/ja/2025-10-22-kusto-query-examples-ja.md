---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 高度なKustoクエリ言語の例
translated: true
type: note
---

Kusto Query Language (KQL) は、Azure Data Explorer や Azure Monitor などの Azure サービスで大規模なデータセットをクエリするための強力なツールです。以下に、時系列分析、異常検出、ピボット、ユーザー定義関数などの高度な機能と、複数の演算子や関数を組み合わせた、いくつかの複雑な例を示します。これらは、暴風雨イベントや販売データの分析などの実際のシナリオから引用しています。各例には、クエリと簡単な説明が含まれています。

### 1. 時系列データにおける異常検出
このクエリは、メトリックテーブルから日次平均を集計し、系列分解を使用して異常を特定します。ログやテレメトリにおける異常なパターンの監視に最適です。

```
TableName
| make-series Metric = avg(Value) on Timestamp step 1d
| extend Anomalies = series_decompose_anomalies(Metric)
```

### 2. パラメータ化されたフィルタリングと集計のためのユーザー定義関数
ここでは、再利用可能な関数が地域と閾値で販売データをフィルタリングし、合計を計算します。Azure Data Explorer ダッシュボードでの動的なレポート作成に有用です。

```
let CalculateSales = (region: string, minSales: int) {
    SalesData
    | where Region == region and Sales > minSales
    | summarize TotalSales = sum(Sales)
};
CalculateSales("North America", 1000)
```

### 3. クロス集計分析のための集計データのピボット
これはカテゴリと地域別に値を集計し、地域を列にピボットして比較を容易にします。ビジネスインテリジェンスクエリで一般的です。

```
TableName
| summarize Total = sum(Value) by Category, Region
| evaluate pivot(Region, sum(Total))
```

### 4. 時系列メトリック間の相関分析
暴風雨イベントデータを使用して、2つのメトリックの日次系列を作成し、それらの相関を計算して、損害と死亡者数などの関係を明らかにします。

```
StormEvents
| make-series PropertyDamage = avg(DamageProperty), Fatalities = avg(Fatalities) on BeginTime step 1d
| extend Correlation = series_correlation(PropertyDamage, Fatalities)
```

### 5. イベント分析のためのフィルタリング、トップ選択、および期間計算
これはテキサス州の洪水イベントをフィルタリングし、損害額で上位5件を選択し、計算された期間列を追加します。Azure Sentinel でのインシデント対応に最適です。

```
StormEvents
| where State == 'TEXAS' and EventType == 'Flood'
| top 5 by DamageProperty
| project StartTime, EndTime, Duration = EndTime - StartTime, DamageProperty
```

### 6. データ変換のための Let ステートメントを使用した静的な値のマッピング
ソースタイプをマッピングする辞書を定義し、イベントをフィルタリングし、わかりやすい名前を投影します。ログのカテゴリデータを正規化するのに役立ちます。

```
let sourceMapping = dynamic(
  {
    "Emergency Manager" : "Public",
    "Utility Company" : "Private"
  });
StormEvents
| where Source == "Emergency Manager" or Source == "Utility Company"
| project EventId, Source, FriendlyName = sourceMapping[Source]
```

これらの例は、Azure Data Explorer Web UI または Log Analytics で直接実行できます。詳細については、公式のサンプルギャラリーを参照してください。

[Comprehensive Guide to Kusto Query Language (KQL)](https://medium.com/@danushidk507/comprehensive-guide-to-kusto-query-language-kql-from-beginner-to-advanced-8dff3bd7568e)  
[Tutorial: Learn common Kusto Query Language operators](https://learn.microsoft.com/en-us/kusto/query/tutorials/learn-common-operators?view=microsoft-fabric)