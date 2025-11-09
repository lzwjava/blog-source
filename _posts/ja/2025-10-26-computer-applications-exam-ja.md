---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: コンピュータ応用技術実技試験概要
translated: true
type: note
---

### 試験の理解
11325: コンピュータ及び応用コース実験（I）は、広東外語外貿大学（GDUFS）の専攻610201: コンピュータ応用技術（専門科レベル）における実践的（実機）評価です。これは10単位に値する総合的な実技試験であり、関連する理論科目の概念を実世界のコンピュータベースのタスクを通じて応用する能力をテストすることを目的としています。登録する前に、以下の5つの前提理論試験に合格する必要があります：

- 電子技術基礎(三) (Electronics Fundamentals III)
- 高級言語プログラミング(一) (Advanced Language Programming I – 一般的にC言語)
- コンピュータ応用技術 (Computer Application Technology)
- マイクロコンピュータ及びインターフェース技術 (Microcomputer and Interface Technology)
- データベース及びその応用 (Database and Its Application)

試験の配点は以下の通りです（10単位満点中）：
- Electronics Fundamentals III: 2単位
- Advanced Language Programming I: 2単位
- Microcomputer and Interface Technology: 2単位
- Computer Application Technology: 3単位
- Database and Its Application (実験部分): 1単位

この試験はコンピュータ上で実施され、実践的操作（例：コーディング、シミュレーション、データベースクエリ）と一部の筆記要素を組み合わせた形式です。焦点は3つのレベルにあります：記憶（基本概念）、理解（原理）、応用（独立した実装）。単純なプログラムの作成、基本的な回路の設計、データベースのクエリ、ハードウェア/ソフトウェアのインターフェースなどのタスクを想定してください。

### 主な対象トピック
評価概要に基づくと、この試験は前提科目の実験内容から出題されます。内訳は以下の通りです：

1. **Electronics Fundamentals III (2単位)**:
   - 基本回路の概念、法則（例：オームの法則、キルヒホッフの法則）、および解析方法。
   - 増幅回路、オペアンプ、およびその応用。
   - デジタル回路：論理ゲート、フリップフロップ、単純な組み合わせ/順序論理。
   - **テストされるスキル**: Multisimなどのソフトウェアを使用して基本回路をシミュレートまたは描画する。ツールを使用して値を計算する。

2. **Advanced Language Programming I (2単位)**:
   - C言語の基礎：変数、制御構造（ループ、条件分岐）、関数、配列、ポインタ。
   - ファイル入出力、文字列処理、モジュールプログラミング。
   - **テストされるスキル**: 単純なCプログラムの作成とデバッグ（例：1000年から2020年までの閏年の出力、または基本的なデータ処理）。Turbo CやDev-C++などのIDEを使用する。

3. **Microcomputer and Interface Technology (2単位)**:
   - マイクロプロセッサの基礎（例：8086/8088アーキテクチャ）、アセンブリ言語命令。
   - I/Oインターフェース：ポート、割り込み、DMA。
   - **テストされるスキル**: データ転送や制御のための単純なアセンブリコード。Proteusなどのツールを使用してハードウェアインターフェースをシミュレートする。

4. **Computer Application Technology (3単位)**:
   - オフィスソフトウェア：ワードプロセッシング、スプレッドシート（Excel）、プレゼンテーション（PowerPoint）。
   - 基本的なマルチメディアおよびインターネットアプリケーション。
   - **テストされるスキル**: 数式やグラフを含む文書の作成、マクロによるタスクの自動化、または単純なWebフォームの構築。

5. **Database and Its Application (1単位)**:
   - リレーショナルデータベースの概念（テーブル、クエリ、リレーションシップ）。
   - SQLの基礎またはAccess操作：データベースの作成、クエリの実行、レポートの生成。
   - **テストされるスキル**: 単純なデータベース（例：学生記録）の設計、データの挿入/更新、クエリ結果の取得。

### 準備方法
準備は実践的な練習を重視してください。これは実技試験です。前提科目から始める場合、2〜3ヶ月の集中学習を目指してください。

1. **前提科目の復習**:
   - 5科目の理論ノートを再確認する。教科書の「実験」章に焦点を当てる（例：Cプログラミング演習、回路シミュレーション）。
   - GDUFSまたは広東省の自考指定教科書を使用する：
     - C Programming: 《C语言程序设计》 (C Language Programming)
     - Database: 《数据库及其应用》 (Database and Its Application)
     - Electronics: 《电子技术基础》 (Electronics Fundamentals)

2. **実践的スキルの構築**:
   - **コーディング**: Code::Blocksなどの無料ツールをC言語用にインストールする。50〜100のサンプルプログラムを練習する（例：ソートアルゴリズム、ファイル操作）。LeetCodeやGeeksforGeeksなどのサイトには初心者向けのC言語チャレンジがある。
   - **Electronics/Microcomputer**: シミュレーションソフトウェアを使用する（デジタル回路にはTinkercad、Logisim。アセンブリにはEmu8086）。仮想ブレッドボードの配線と単純なI/Oプログラムの実行を練習する。
   - **Database**: Microsoft AccessをダウンロードするかSQLiteを使用する。サンプルデータベース（例：在庫管理システム）を構築し、クエリを練習する。
   - **Applications**: MS Officeスイートを習得する。ピボットテーブルやVBAマクロを含む複雑なExcelシートを作成する。

3. **試験形式に合わせた練習**:
   - 時間を計る：コンピュータ上で2〜3時間の模擬試験を実施する。
   - サンプルタスク（概要と過去の例から）：
     - 特定の範囲の閏年を計算して出力するCプログラムを作成する。
     - 学生用のデータベーステーブルを設計し、レコードを追加し、平均値をクエリする。
     - 基本的なオペアンプ回路をシミュレートし、出力電圧を計算する。
   - 正確さと効率性を目指す—コードのコンパイルエラーやクエリ結果の誤りは減点の対象となる。

4. **学習リソース**:
   - **公式概要**: GDUFSまたは広東金融学院のサイトからダウンロードする（同様の基準を共有している）。
   - **模擬試験**: ZhihuやBilibiliなどの中国プラットフォームで「11325 自考 模拟题」を検索し、ビデオ解説を探す。
   - **オンラインコース**: CプログラミングとSQLの無料MOOCs（Coursera/edX）。電子工学シミュレーションのYouTubeチュートリアル。
   - **書籍**: 《计算机及应用课程实验指导》 (Computer and Application Experiment Guide) で段階的な実験を学ぶ。

5. **登録と手続き**:
   - GDUFSポータル (jxjy.gdufs.edu.cn) を通じて、所定の期間中（例：2025年度下半期の場合は6月）に登録する。
   - 受験料：約120〜150元。身分証明書と前提科目合格証明書を持参する。
   - 試験日：下半期の場合は通常9月下旬。他の試験（全国コンピュータテストなど）との重複を通知で確認する。

6. **成功のためのヒント**:
   - 毎日練習する：コーディング1時間 + シミュレーション1時間。
   - 体系的にデバッグする：コードを小さな部分に分けてテストする。
   - 行き詰まったら、自考フォーラム（例：WeChat/QQの広東自考グループ）に参加する。
   - 60点以上で合格。高得点を目指すには応用レベルに焦点を当てる。

一貫した練習により、実機形式に対する自信を築くことができます。幸運を祈ります！

### 参考文献
- [Zhihu Discussion on 11325 Exam Content](https://www.zhihu.com/question/430869242)
- [Bilibili Sample Questions for Computer Experiments](https://www.bilibili.com/read/cv15294426/)
- [GDUFS 2023 Practical Assessment Notification](https://jxjy.gdufs.edu.cn/info/1178/17276.htm)
- [Scribd Exam Outline Excerpt](https://www.scribd.com/document/904739849/11325计算机及应用课程实验-一-实践-考核大纲)
- [Zikao365 PDF Outline Download](https://www.zikao365.com/zcms/contentcore/resource/download?ID=42711)
- [Guangdong Self-Exam Professional Plan](http://m.gdszkw.com/zkzy/42682.html)