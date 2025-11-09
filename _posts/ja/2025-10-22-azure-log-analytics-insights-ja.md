---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Azure Log Analytics と Azure Insights
translated: true
type: note
---

良い質問です。これらは**密接に関連していますが**、**同じものではありません**。明確に整理してみましょう。

---

### **1. Azure Log Analytics**

**Azure Log Analytics** は、**Azure Monitor** 内の**ツール/サービス**であり、クラウドおよびオンプレミスリソースからのログを**収集、クエリ、分析**することができます。

* ログは **Log Analytics ワークスペース**に保存されます。
* **Kusto クエリ言語 (KQL)** を使用してクエリを実行し、データを分析できます。
* 以下の用途に使用されます：

  * 問題のトラブルシューティング
  * パフォーマンスの調査
  * セキュリティの監視
  * カスタムダッシュボードとアラートの作成

Log Analytics は、Azure 内のすべてのログデータに対する**データレイクおよびクエリエンジン**と考えることができます。

---

### **2. Azure Insights**

**Azure Insights** (**Application Insights** または **Azure Monitor Insights** として表示されることが多い) は同じ監視エコシステムの一部ですが、生ログよりも**アプリケーションレベルの監視**に重点を置いています。

「Insights」にはさまざまな種類があります：

* **Application Insights** — アプリケーションを監視 (APM)：パフォーマンス、例外、依存関係、ユーザー行動など。
* **VM Insights**、**Container Insights**、**Network Insights** — 特定のリソースタイプ向けの事前構築済み監視ビューを提供。

これらすべての Insights は、**そのテレメトリとメトリックを Log Analytics ワークスペースに保存**するため、**内部では Log Analytics に依存しています**。

---

### **3. 関係性**

* **Azure Insights = 可視化 & インテリジェントな監視レイヤー**
* **Log Analytics = 基盤となるログストレージ & クエリエンジン**

要するに：

> Log Analytics は、データが*存在し*分析される*場所*です。
> Insights は、特定のリソースタイプに対してそのデータを*表示し解釈する方法*です。

---

### **例**

Web アプリで **Application Insights** を有効にすると：

* テレメトリ (リクエスト、依存関係、トレース、例外) を収集します。
* そのデータは **Log Analytics ワークスペース**に保存されます。
* 同じデータに対して **Log Analytics** を使用して KQL クエリを実行し、より深いカスタム分析を行うことができます。

---

Log Analytics が Application Insights のデータをどのようにクエリするか、簡単な **KQL の例**をお見せしましょうか？