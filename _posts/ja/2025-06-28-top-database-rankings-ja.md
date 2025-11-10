---
audio: false
generated: true
lang: ja
layout: post
title: 主要データベースランキングソース
translated: true
type: note
---

データベースのランキング指標については、検索ボリューム、コミュニティ参加度、求人需要などの様々な指標に基づいてデータベース管理システム（DBMS）の人気を追跡する、最も信頼できる情報源を以下に示します：

1.  **DB-Engines Ranking**
    - **ウェブサイト**: [db-engines.com](https://www.db-engines.com/en/ranking)
    - **説明**: DB-Engines Rankingは、リレーショナル、NoSQL、グラフデータベースを含む400以上のDBMSをランク付けする主要な月次指標です。検索エンジンの結果（GoogleとBing）、Google Trends、Stack OverflowとDBA Stack Exchangeでの議論、求人情報（IndeedとSimply Hired）、ソーシャルメディアでの言及などのパラメータを使用して人気を測定します。2024年6月現在、Oracle、MySQL、Microsoft SQL Serverが上位3位でした。また、歴史的傾向やカテゴリ別のランキング（例：グラフDBMS）も提供しています。[](https://en.wikipedia.org/wiki/DB-Engines_ranking)[](https://www.statista.com/statistics/809750/worldwide-popularity-ranking-database-management-systems/)[](https://www.red-gate.com/blog/db-engines-shares-q1-2025-database-industry-rankings-and-top-climbers-snowflake-and-postgresql-trending)

2.  **TOPDB Top Database Index**
    - **ウェブサイト**: [pypl.github.io/TOPDB](https://pypl.github.io/TOPDB.html)
    - **説明**: プログラミング言語のPYPL Indexと同様に、TOPDB Indexはデータベース関連用語のGoogle検索頻度に基づいてデータベースをランク付けし、検索ボリュームが高いほど人気が高いと仮定しています。これはシンプルな先行指標であり、月次更新で、特定の国別のデータも利用できます。[](https://pypl.github.io/DB.html)

3.  **Red9 Database Rankings**
    - **ウェブサイト**: [red9.com](https://red9.com/db-engines-rankings-2025/)
    - **説明**: Red9は、Amazonの書籍検索、オンラインでの言及、その他の指標からのデータを分析する加重アルゴリズムを使用して、DBMSの月次ランキングを提供します。現在のトレンドを重視し、簡単な比較のためのチャートや表が含まれています。[](https://red9.com/database-popularity-ranking/)

4.  **Stack Overflow Developer Survey**
    - **ウェブサイト**: [survey.stackoverflow.co](https://survey.stackoverflow.co)
    - **説明**: この年次調査は、開発者の使用状況と選好に基づいてデータベースをランク付けします。2024年には、PostgreSQL (48.7%)、MySQL (40.3%)、SQLite (33.1%) が開発者間で上位3つのデータベースとなり、実世界での採用状況を反映しています。

5.  **benchANT Database Ranking**
    - **ウェブサイト**: [benchant.com](https://benchant.com/database-ranking)
    - **説明**: パフォーマンスとコストに焦点を当てたbenchANTは、YCSBやTSBSなどのベンチマークを使用して、SQL、NoSQL、NewSQLデータベースをランク付けします。汎用（50%読み取り/書き込み）、OLTP、時系列データなどのワークロードに対するスループットとレイテンシを評価します。これは人気よりもパフォーマンス主導の比較に最適です。[](https://benchant.com/ranking/database-ranking)

これらの情報源は焦点が異なります：DB-EnginesとTOPDBは人気を重視し、Stack Overflowは開発者の使用状況を反映し、benchANTはパフォーマンスを優先します。最も包括的な視点を得るには、幅広い指標と頻繁な更新により、DB-Enginesが代表的です。特定の種類のデータベース（例：NoSQLやリレーショナル）や指標（例：パフォーマンス対人気）に興味がある場合は、お知らせください。最適な情報源を提案します！