---
audio: false
lang: ja
layout: post
title: アルゴリズム問題の解決方法
translated: true
---

このは、GitHubプロジェクト[https://github.com/lzwjava/algorithm-solutions](https://github.com/lzwjava/algorithm-solutions)のREADME.mdです。

---

# アルゴリズム問題の解法

オンラインジャッジプラットフォームからのアルゴリズム問題の解法です。

| プラットフォーム | 解決した問題数 |
| ------------- | ------------- |
| [UVa](https://uhunt.onlinejudge.org/id/113519) | 568 |
| [Codeforces](https://codeforces.com/profile/lzwjava) | 419 |
| [LeetCode](https://leetcode.com/lzwjava/) | 20 |
| [Hacker Rank](https://www.hackerrank.com/profile/lzwjava) | 20(SQL) |

| 言語 | 行数 |
| --- | ---- |
| Java | 70851 |
| C++ | 3214 |
| Python | 1193 |
| SQL | 101 |

このリポジトリには、Codeforces、HackerRank、LeetCode、Lintcode、Nowcoder、UVaなどのプラットフォームからのさまざまなアルゴリズム問題の解法が含まれています。各解法は問題番号ごとに整理されており、ソースコード、入力ファイル、場合によっては追加ドキュメントが含まれています。

## リポジトリの構造

- `README.md`: このファイルです。
- `codeforces/`: Codeforcesの問題の解法が含まれています。
- `hacker_rank/`: HackerRank SQL問題の解法が含まれています。
- `leetcode/`: LeetCodeの問題の解法が含まれています。
- `lintcode/`: Lintcodeの問題の解法が含まれています。
- `nowcoder/`: Nowcoderの問題の解法が含まれています。
- `uva/`: UVaの問題の解法が含まれています。

### Codeforces

各サブディレクトリは問題番号で名前が付けられ、以下を含みます。

- `1.in`: 問題の入力ファイルです。
- `src/Main.java`: 問題の解法を含むJavaソースコードファイルです。

### HackerRank

`hacker_rank`ディレクトリには、各問題を解決するためのSQLファイルが含まれています。各ファイルは、解決する問題の名前が付けられています。

### LeetCode

`leetcode`ディレクトリには、各問題を解決するためのPythonスクリプトが含まれています。ファイル名はそれぞれの問題を解決するスクリプトに基づいて命名されています。

### Lintcode

各サブディレクトリは問題番号で名前が付けられ、以下を含みます。

- `src/com/lintcode/Main.java`: 解法のメインクラスファイルです。
- `src/com/lintcode/Solution.java`: 問題の解法クラスファイルです。
- `src/com/lintcode/`: 問題によって必要な追加クラスファイルです。

### Nowcoder

各サブディレクトリは問題の名前で名前が付けられ、以下を含みます。

- `Solution.java`: 問題の解法クラスファイルです。
- `Test.java`: 問題のテストクラスファイルです。
- `TreeNode.java`: (適用可能な場合) 木構造に関連する問題のためのTreeNodeクラスファイルです。

### UVa

解決: 568, 提出した回数: 1776

| Q1 | Q2 | Q3 |
| ------------- | ------------- |-------------|
| 100: 3n + 1 問題 | 101: ブロック問題 | 102: 生態学的なビン詰め |
| 103: 荷重を積む | 104: 為替相場 | 105: スカイライン問題 |
| 106: フェルマーの最終定理 | 107: 猫の帽子 | 108: 最大値 |
| 110: メタループレスソート | 111: 歴史の評価 | 112: 木の和 |
| 113: クリプトグラフィの力 | 116: 一方向TSP | 118: ミュータントフラットワールド探検家 |
| 119: 多くの贈り物をする | 120: フラップジャックの山 | 122: レベルの木 |
| 123: 迅速な検索 | 124: 従う順序 | 127: 「アコーディオン」ペータンス |
| 128: ソフトウェアCRC | 129: クリプトンファクター | 131: ドミノ効果 |
| 133: ドール・キュー | 136: 素数 | 138: ストリートナンバー |
| 140: バンド幅 | 146: IDコード | 147: ドル |
| 151: 危機 | 152: 木の群れ | 156: アナグラム |
| 160: 因数と階乗 | 167: スルタンの後継者 | 185: ローマ数字 |
| 190: 三点を通る円 | 193: グラフの色付け | 195: アナグラム |
| 196: 電子表 | 197: 衛星の軌道 | 200: 稀な順序 |
| 201: 正方形 | 202: 繰り返しの小数 | 208: 消防車 |
| 210: 周期の決定 | 211: ドミノ効果 | 213: メッセージのデコード |
| 216: 並ぶ | 221: ポリゴンの区切り | 225: ゴロムのルーラー |
| 227: パズル | 230: 借り手 | 231: テストCATCHER |
| 247: 電話のサークル | 253: キューブのペイント | 256: 奇妙な正方形 |
| 260: イル・ジョコ・デル'X | 264: カントール数 | 272: TEXクォート |
| 278: チェス | 280: 頂点 | 291: サンタクロースの家 |
| 294: 因数 | 297: クワッドツリー | 299: 列車の入れ替え |
| 301: 交通 | 305: ヨセフ | 307: 槊 |
| 315: ネットワーク | 317: 電力の送電 | 324: 阶乗の頻度 |
| 327: シンプルなC式の評価 | 331: 入れ替えのマッピング | 336: 遠すぎるノード |
| 340: マスターマインドのヒント | 343: これはいくつの基数ですか? | 344: ローマ数字診断 |
| 348: オプティマル配列乗算シーケンス | 350: 疑似乱数 | 352: 季節の戦争 |
| 353: 面倒なパリンドローム | 357: 数え方 | 369: コンビネーション |
| 371: アッカーマン関数 | 374: 大きなモジュラ | 375: 内接円と等辺三角形 |
| 378: 交わる線 | 382: 完全な数 | 386: 完全な立方体 |
| 387: 繰り返し置換を使ったsed | 389: 基本言語 | 392: 多項式ショーダウン |
| 400: Unix ls | 401: パリンドローム | 406: プライムカット |
| 408: 一様なジェネレーター | 409: 言い訳、言い訳! | 412: 円周率 |
| 414: 加工された表面 | 417: 単語のインデックス | 424: 整数の質問 |
| 429: 単語の変換 | 437: バビロニアの塔 | 438: 円の周囲 |
| 439: ナイトの動き | 440: イーニーメニーモー | 441: ロット |
| 442: 行列の連鎖乗算 | 443: ユーモラス数 | 444: エンコーダーとデコーダー |
| 445: 魅力的な迷路 | 446: キブルズ`n'ビッツ`n'ビッツ`n'ビッツ | 455: 定周期文字列 |
| 457: 線形セルオートマトン | 458: デコーダー | 459: グラフの接続性 |
| 465: オーバーフロー | 469: フロリダの湿地 | 476: 点の図: 長方形 |
| 477: 点の図: 長方形と円 | 478: 点の図: 長方形、円、三角形 | 481: どこまでも上がっていく |
| 482: 排列配列 | 483: 単語のスクラムブル | 484: 冗長性の部門 |
| 488: 三角波 | 489: ハングマン判定 | 490: 回転する句 |
| 492: ピグ・ラテン | 494: キンダーガーデンの数え方 | 495: フィボナッチフリーズ |
| 496: 単純な部分集合 | 497: 戦略的防衛イニシアチブ | 499: キンバリーの頻度、ケネスさん? |
| 507: ジルは再び乗馬 | 509: 事実だけ | 512: 台湾鉄道 |
| 514: 鉄道 | 524: プライムリング問題 | 530: 二進数のショーダウン |
| 531: コンプロミーズ | 532: ダンジョンマスター | 534: フログ |
| 536: 木の回復 | 537: 鉄道 | 539: カタンの定住者 |
| 540: チームのキュー | 541: エラー訂正 | 543: ゴールドバッハの予想 |
| 544: 重い貨物 | 548: 木 | 550: 回転による乗算 |
| 558: ウームホール | 562: コイントス | 567: リスク |
| 568: 事実だけ | 572: オイルデポジット | 573: 蝶 |
| 574: 合計 | 575: 偶数の2進数 | 576: ハイクレビュー |
| 579: 時計の針 | 583: プライム要素 | 591: ブロックの箱 |
| 594: 1つのリスト、2つのリスト、3つのリストのエンドイアン | 612: DNAソート | 621: 秘密の研究 |
| 623: 500! | 624: CD | 637: ふだんの印刷 |
| 639: ドントゲットルッキング | 640: 自分の数 | 644: 即時デコーダブル |
| 657: ジ・ダイス・キャスト | 661: ファスの吹き飛ばし | 673: カッコのバランス |
| 674: コインの変換 | 679: フロップするボール | 686: ゴールドバッハの予想(II) |
| 694: コラッツ数列 | 696: ナイトの数 | 699: 落ちる葉 |
| 705: スラッシュ迷路 | 706: LC表示 | 712: S木 |
| 713: 逆さまに足し算 | 714: 書籍のコピー | 725: 除法 |
| 727: 方程式 | 729: ハミング距離問題 | 748: 指数化 |
| 750: 8クイーンチェス問題 | 755: 487--3279 | 784: 迷路の探検 |
| 793: ネットワーク接続 | 796: 重要なリンク | 815: フラッディング! |
| 818: ジョブマッチング | 820: インターネットバンド幅 | 821: ページホッピング |
| 834: 続分数 | 836: 最大のサブマトリックス | 839: Not so Mobile |
| 846: ステップ | 847: マルチプレーカーゲーム | 900: 煉瓦の壁のパターン |
| 913: ジョアナと奇数 | 924: ニュースの広がり | 929: ナンバーの迷路 |
| 948: フィボナッチマル基数 | 993: 乗数 | 1124: セレブリティジェパディ |
| 1149: デンジャラスダイブ | 1152: 4つの値の合計は0 | 1203: アルグス |
| 1225: 1つの数のカウント | 1230: モディクス | 1237: エキスパート |
| 1260: 販促 | 1339: 古代の暗号 | 1368: DNAコンセンサス文字列 |
| 1374: 電力の送電 | 1451: ゴーストバスターズ2 | 1471: デンジャラスダイブ |
| 1583: デジタルルート | 1584: 数学 | 1585: スコア |
| 1586: 分子量 | 1587: 箱 | 1588: 戦争 |
| 1589: 分割 | 1590: エレベーター | 1592: トランスミッション |
| 1593: パイプ | 1594: ダイヤモンド | 1595: ワンライナー |
| 1604: ジャンプチャンピオン | 1605: フィボナッチの合計 | 1606: キャンディ |
| 1607: カプレカ数 | 1608: ランダムウォーク | 1609: 見る・言うシーケンス |
| 10000: 最長のパス | 10003: カットスティック | 10004: 二重塗装 |
| 10006: カルメル数 | 10008: これは何の解読ですか? | 10010: どこにワルドルフがいる? |
| 10012: これがどれだけ大きいのか? | 10013: 超ロングサム | 10014: 単純なベース変換 |
| 10018: 逆さまにして加算 | 10019: 面白い暗号化方法 | 10025: マスターマインドのゲーム |
| 10026: 靴直しの問題 | 10033: ビリヤード | 10034: フレック |
| 10035: 初等算術 | 10036: 除去のできる数 | 10038: ジョリージャンパー |
| 10041: ビートの家族 | 10042: スミス数 | 10047: モノサイクル |
| 10048: オーディオフォビア | 10050: ハルトラル | 10054: ネックレス |
| 10055: ハッシュマットの勇者戦士 | 10056: これは何の確率? | 10061: この暗号を解く方法は? |
| 10062: この頻度を教えて! | 10066: ツインタワー | 10067: 回るウィール |
| 10070: 閏年かどうか閏年かどうか... | 10071: 高校物理学への戻り | 10074: 土地を取る |
| 10077: スターン＝ブロコット数体系 | 10079: ピザの切断 | 10082: WERTYU |
| 10098: 生成しやすい | 10099: 観光案内 | 10101: バングラ言語 |
| 10102: 着色されたフィールドの道 | 10104: ユークリッド問題 | 10105: 多項式係数 |
| 10106: 積 | 10107: これはメディアンですか? | 10110: 光、さらに光 |
| 10112: マイアクロン生活時間達成賞 | 10114: 車を買ったい人 | 10115: 自動編集 |
| 10116: ロボットの動き | 10123: 雪だるま戦争! | 10125: サムセット |
| 10127: ダイエット中 | 10129: 言葉の遊び | 10130: スーパーセール |
| 10131: そうであれば頭もよいのか? | 10137: 旅 | 10139: ファクトビソー |
| 10140: プライム距離 | 10141: 要求書 | 10152: シェルソート |
| 10160: サービスステーション | 10161: チェスボードのアリ | 10167: 誕生日ケーキ |
| 10168: 四つの素数の合計 | 10170: 無限の部屋があるホテル | 10177: 魔法の正方形パリンドローム |
| 10179: 不可約の基本分数 | 10183: ハウマニーファイ? | 10189: マインスイーパー |
| 10190: 分割しかし完全には分割しない! | 10191: 長い残暑 | 10192: 休暇 |
| 10193: 愛のすべて | 10194: サッカー（サッカー） | 10195: ラウンドテーブルの騎士 |
| 10198: カウント | 10199: 観光ガイド | 10205: スタック'em Up |
| 10209: これは積分か? | 10219: 方法を探す! | 10220: 私はバカ大好き! |
| 10221: 2-3動き | 10222: メッセージのデコード | 10226: ハードウッド種 |
| 10229: モジュラフィボナッチ | 10235: 単純なエミラップ | 10242: 4つの点!! |
| 10245: 最も近いペアの問題 | 10250: その他の2つの木 | 10252: 共通の順序 |
| 10258: コンテストスコアボード | 10260: サウンドエックス | 10267: グラフィカルエディタ |
| 10276: ハノイの塔のトラブルアゲイン! | 10281: 平均速度 | 10282: バベルフィッシュ |
| 10285: 長いスノーボードの走行 | 10286: ペンタゴンのトラブル | 10295: 階層点 |
| 10298: パワースリング | 10299: 親族 | 10300: 生態学的プレミアム |
| 10302: 多項式の合計 | 10305: タスクの順序 | 10310: 犬とゴファー |
| 10323: ファクトリアル! 君は本気で言っているのか? | 10324: ゼロと一つ | 10327: フィップソート |
| 10334: 光を通す眼鏡 | 10336: ランクの言語 | 10338: まちがった子供 |
| 10340: 全部全部 | 10341: これを解決する | 10344: 23を5で |
| 10346: ピーターズの煙草 | 10347: メディアン | 10361: 自動詩 |
| 10369: アークティックネットワーク | 10370: 平均値 | 10387: ビリヤードのボール |
| 10391: 複合語 | 10392: 大きな数の因数分解 | 10394: 双子の素数 |
| 10397: キャンパスを接続 | 10405: 長い共通サブシーケンス | 10409: さいころゲーム |
| 10420: 征服のリスト | 10424: 愛の計算機 | 10432: 保管庫 |
| 10450: ワールドカップの騒音 | 10452: マーカス | 10452: ホーマー・シンプソン |
| 10465: ホーマー・シンプソン | 10469: 運ぶか運ばないか | 10473: 木の登り |
| 10474: キャンディマンカン | 10487: 近似の和 | 10494: もし子供が再びしていたら |
| 10496: ビーパーを集める | 10499: 実に大きな実数 | 10515: 累乗和 |
| 10523: 非常に簡単!! | 10523: 非常に簡単!! | 10530: 当てずっぽう |
| 10533: デジットの素数 | 10534: ワヴィオシーケンス | 10550: コンビネーションロック |
| 10557: XYZZY | 10562: 木の描画を消す | 10579: フィボナッチ数 |
| 10583: 普遍的な宗教 | 10591: ハッピー数 | 10596: 深い下で |
| 10600: ACMコンテストとブラックアウト | 10603: 実験的なライブラリ | 10608: フレンド |
| 10611: プレイボーイのサル | 10616: 可除性のグループ合計 | 10653: ボム! いいえ、それは地雷です!! |
| 10656: 最大値（II） | 10664: 手荷物 | 10673: フロアと天井の遊び |
| 10676: 私は文字が好き! | 10684: ジャックポット | 10696: f91 |
| 10699: 要素のカウント | 10703: 空き場所 | 10719: クィアキアンティファイア |
| 10723: 道路の数え方 | 10773: 中級数学への戻り | 10783: 奇数の合計 |
| 10784: 対角線 | 10785: スピードリミット | 10789: バブルソート |
| 10790: ポイントの交差の数を数える? | 10810: ウルトラクイックソート | 10812: ビートザースプレッド! |
| 10815: アンドリューの最初の辞書 | 10878: テープをデコード | 10879: 最大値（II） |
| 10905: 子供のゲーム | 10911: クイズチームの形成 | 10921: 電話を探す |
| 10922: 2520 | 10924: 単純なマインドのハッシュ | 10929: 11を言える |
| 10931: 奇偶性 | 10935: カードを捨てるI | 10940: カードを捨てるII |
| 10943: どうやって加える? | 10945: 母親熊 | 10948: プライマリ問題 |
| 10954: 加えると | 10970: 大きなチョコ | 10976: 分数Again?! |
| 10986: メールを送る | 11000: び | 11044: ネッシーを探す |
| 11054: ジルダのワイン貿易 | 11057: 正確な合計 | 11059: 最大値 |
| 11060: 飲み物 | 11085: 8クイーンへの帰還 | 11093: これを終わらせる |
| 11094: 大陸 | 11111: 一般的なマトリョーシカ | 11134: フェーブルドルーク |
| 11137: 3つの太ったレディ | 11150: コーラ | 11151: 最長のパリンドローム |
| 11152: カラフルな花 | 11172: 関係詞 | 11185: 三進法 |
| 11192: 何の問題もない! | 11205: 破れたペドメータ | 11212: 書籍の編集 |
| 11214: アラジンと飛行キャラット | 11219: あなたは何歳ですか? | 11231: 黒と白のペイント |
| 11234: 式 | 11235: 繰り返しの値 | 11244: 星の数 |
| 11286: 一致 | 11292: ドラゴン・オブ・ルワタ | 11332: 数の合計 |
| 11340: 新聞 | 11349: 対称行列 | 11362: 電話番号簿 |
| 11364: 駐車場 | 11369: ショッパホリック | 11388: GCD LCM |
| 11389: バスの運転手の問題 | 11417: GCD | 11428: 立方体 |
| 11450: ウェディングショッピング | 11455: 見よ、私の四角形 | 11461: 平方数 |
| 11462: 年齢順 | 11479: これは最も簡単な問題? | 11494: クイーン |
| 11498: ンロゴニアの分割 | 11503: バーチャルフレンド | 11504: ドミノ |
| 11530: SMS入力 | 11541: デコード | 11547: 自動応答 |
| 11559: イベント計画 | 11565: 単純な方程式 | 11572: ユニークな雪片 |
| 11577: 文字頻度 | 11586: 鉄道 | 11608: 何の問題もない! |
| 11614: エトルスクの戦士はチェスをしません | 11624: 火! | 11631: 暗いルート |
| 11636: ハロー、ワールド! | 11650: 鏡時計 | 11661: エアポート |
| 11677: アラーム時計 | 11679: サブプリム | 11689: ソーダサプライヤー |
| 11713: 抽象的な名前 | 11715: カー | 11716: デジタルフォートレス |
| 11723: 道路の番号付け | 11727: コスト削減 | 11729: コマンドウォー |
| 11734: 大規模なチームがこれを解決する | 11743: クレジットチェック | 11764: ジャンプするマリオ |
| 11777: 自動評価 | 11799: ホラーダッシュ | 11805: バファナバファナ |
| 11809: 浮動小数点数 | 11827: 最大GCD | 11831: スティッカーコレクターロボット |
| 11849: CD | 11854: エジプト | 11875: ブリックゲーム |
| 11877: ココアコーラストア | 11879: 17の倍数 | 11900: 卵を煮る |
| 11933: 数字を分割 | 11934: 魔法の公式 | 11936: 怠け者の木こり |
| 11942: 木こりの配列 | 11953: バトルシップ | 11984: 熱変換の変更 |
| 11988: 修理中のキーボード（別名ベジュテキスト） | 11991: 簡単な問題からルジア・リュー | 11995: 私はデータ構造を予測できます! |
| 12015: Google Is Feeling Lucky | 12032: モンキーと油のバンブー | 12096: セットスタックコンピュータ |
| 12100: プリンタークイュー | 12107: 1つ2つ3つ | 12108: 非常に疲れた学生 |
| 12113: 異なる素数の合計 | 12149: ファインマン | 12157: 料金プラン |
| 12174: アセンブル | 12219: 検索速く | 12250: 言語検出 |
| 12279: エモーグルバランス | 12289: 1つ2つ3つ | 12325: 正確な避け |
| 12333: どこのマーブル? | 12372: 休暇のためのパッケージング | 12403: セトゥを助ける |
| 12405: スケアクロウ | 12412: 伝達の問題 | 12455: バース |
| 12468: 通して | 12478: これは最も難しい問題（簡単） | 12502: 3つの家族 |
| 12503: ロボットの指示 | 12504: 辞書の更新 | 12545: ビットとピース |
| 12554: 子供の遊び | 12558: サイクルの見つけ方 | 12569: セール |
| 12577: ハッジ・アクバル | 12578: 10:6:2 | 12627: エラーコレクション |
| 12646: 大多数決 |
| 12657: 一列に並べたボックス |

### Codeforces

| Q1 | Q2 | Q3 |
|---------------|---------------|-------------|
| 1003A: Polycarp's Pockets | 1030A: In Search of an Easy Problem | 1077A: Frog Jumping |
| 1092B: Teams Forming | 1095A: Repeating Cipher | 1097A: Gennady and a Card Game |
| 110A: Nearly Lucky Number | 112A: Petya and Strings | 1154A: Restoring Three Numbers |
| 115A: Party | 116A: Tram | 1183A: Nearest Interesting Number |
| 1186A: Vus the Cossack and a Contest | 118A: String Task | 1196A: Three Piles of Candies |
| 119A: Epic Game | 1206B: Make Product Equal One | 1220A: Cards |
| 122A: Lucky Division | 1234A: Equalize Prices Again | 124A: The Number of Positions |
| 1256A: Payment Without Change | 1283A: Minutes Before the New Year | 1285A: Mezo Playing Zoma |
| 1294A: Collecting Coins | 1294C: Product of Three Numbers | 1296A: Array with Odd Sum |
| 1296B: Food Buying | 1303A: Erasing Zeroes | 1304A: Two Rabbits |
| 1311A: Add Odd or Subtract Even | 1312A: Two Regular Polygons | 131A: cAPS lOCK |
| 1324A: Yet Another Tetris Problem | 1324B: Yet Another Palindrome Problem | 1324C: Frog Jumps |
| 1325A: EhAb AnD gCd | 1325B: CopyCopyCopyCopyCopy | 1326A: Bad Ugly Numbers |
| 1326B: Maximums | 1327A: Sum of Odd Integers | 1328A: Divisibility Problem |
| 1328B: K-th Beautiful String | 1328C: Ternary XOR | 1333A: Little Artem |
| 1334B: Middle Class | 1335A: Candies and Two Sisters | 1335B: Fair Division |
| 1335C: Hidden Word | 1335D: Anti-Sudoku | 1337A: Ichihime and Triangle |
| 1337B: Kana and Dragon Quest game | 1339A: Filling Diamonds | 1339B: Sorted Adjacent Differences |
| 133A: HQ9+ | 1341A: Nastya and Rice | 1342A: Road To Zero |
| 1342B: Binary Period | 1343A: Candies | 1343B: Balanced Array |
| 1343C: Alternating Subsequence | 1345A: Hilbert's Hotel | 1345B: Card Constructions |
| 1348A: Phoenix and Balance | 1350A: Orac and Factors | 1352A: Sum of Round Numbers |
| 1352B: Same Parity Summands | 1352C: K-th Not Divisible by n | 1353A: Most Unstable Array |
| 1353B: Number of Apartments | 1353C: Board Moves | 1354A: Alarm Clock |
| 1354B: Ternary String | 1355A: Sequence with Digits | 1355B: Young Explorers |
| 1358A: Park Lighting | 1358B: Maria Breaks the Self-isolation | 1359A: Berland Poker |
| 1359B: New Theatre Square | 1360A: Minimal Square | 1360B: Honest Coach |
| 1360C: Similar Pairs | 1360D: Buying Shovels | 1363A: Odd Selection |
| 1365A: Matrix Game | 1365B: Trouble Sort | 1366A: Shovels and Swords |
| 1367A: Short Substrings | 1367B: Even Array | 1368A: C+= |
| 1369A: FashionabLee | 1369B: AccurateLee | 136A: Presents |
| 1370A: Maximum GCD | 1371A: Magical Sticks | 1372A: Omkar and Password |
| 1372B: Omkar and Last Class of Math | 1373A: Donut Shops | 1373B: Balanced Tunnel |
| 1374A: Required Remainder | 1374B: Multiply by 2, divide by 6 | 1374C: Move Brackets |
| 1382A: Common Subsequence | 1382B: Sequential Nim | 1385A: Three Pairwise Maximums |
| 1385B: Restore the Permutation by Merger | 1385C: Make It Good | 1388A: Captain Flint and Crew Recruitment |
| 1389A: LCM Problem | 1391A: Suborray | 1391B: Fix You |
| 1397A: Juggling Letters | 1398A: Bad Triangle | 1398B: Substrings Sort |
| 1399A: Remove Smallest | 1399B: Gifts Fixing | 1399C: Boats Competition |
| 1400A: String Similarity | 1401A: Distance and Axis | 1409A: Yet Another Two Integers Problem |
| 1409B: Minimum Product | 141A: Amusing Joke | 1426A: Floor Number |
| 1433A: Boring Apartments | 1433B: Yet Another Bookshelf | 1433C: Dominant Piranha |
| 1436A: Reorder | 144A: Arrival of the General | 1451A: Subtract or Divide |
| 1454A: Special Permutation | 1454B: Unique Bid Auction | 1455A: Strange Functions |
| 1462A: Favorite Sequence | 1462B: Last Year's Substring | 1462C: Unique Number |
| 1466A: Bovine Dilemma | 1467A: Wizard of Orz | 1469A: Regular Bracket Sequence |
| 1472A: Cards for Friends | 1472B: Fair Division | 1472C: Long Jumps |
| 1473A: Replacing Elements | 1473B: String LCM | 1474A: Puzzle From the Future |
| 1475A: Odd Divisor | 1475B: New Year's Number | 1476A: K-divisible Sum |
| 1478A: Nezzar and Colorful Balls | 1480A: Yet Another String Game | 1481A: Space Navigation |
| 1486A: Shifting Stacks | 1487A: Arena | 148A: Insomnia cure |
| 1490A: Dense Array | 1490B: Balanced Remainders | 1490C: Sum of Cubes |
| 1497A: Meximization | 149A: Business trip | 1506A: Strange Table |
| 1509A: Average Height | 1512A: Spy Detected! | 1512B: Almost Rectangle |
| 1514A: Perfectly Imperfect Array | 1516A: Tit for Tat | 1517A: Sum of 2050 |
| 1519A: Red and Blue Beans | 1519B: The Cake Is a Lie | 151A: Soft Drinking |
| 1520A: Do Not Be Distracted! | 1520B: Ordinary Numbers | 1520C: Not Adjacent Matrix |
| 1520D: Same Differences | 1521A: Spy Syndrome 2 | 1525A: Potion-making |
| 1526A: Mean Inequality | 1527A: And Then There Were K | 1529A: In Game Theory |
| 1535A: Fair Playoff | 1535B: Array Reodering | 1537A: Arithmetic Array |
| 1537B: Bad Boy | 1538A: Stone Game | 1538B: Friends and Gifts |
| 1541A: Pretty Permutations | 1542A: Odd Set | 1547A: Shortest Path with Obstacle |
| 1547B: Alphabetical Strings | 1549A: Gregor and the Pawn Game | 1550A: Find The Array |
| 1551A: Polycarp and Coins | 1551B1: Wonderful Coloring - 1 | 1552A: Subsequence Addition |
| 1553A: Digits Sum | 1554A: Cherry | 1555A: PizzaForces |
| 1557A: Ezzat and Two Subsequences | 155A: I_love_%username% | 1560A: Dislike of Threes |
| 1560B: Who's Opposite? | 1560C: Infinity Table | 1562A: The Great Hero |
| 1567A: Domino Disaster | 1569A: The Raising Sand | 1579A: Casimir's String Solitaire |
| 1582A: Luntik and Concerts | 1582B: Luntik and Subsequences | 1582C: Luntik and Subsequences |
| 1585A: Pretty Permutations | 1585B: Find The Array | 1585C: Wonderful Coloring - 1 |
| 158A: Next Round | 158B: Taxi | 1593A: Casimir's String Solitaire |
| 1607A: Dislike of Threes | 1608A: Luntik and Concerts | 1608B: Luntik and Subsequences |
| 1609A: Domino Disaster | 1609B: Infinity Table | 1609C: The Great Hero |
| 160A: Luntik and Subsequences | 1610A: Pretty Permutations | 1610B: Find The Array |
| 1610C: Wonderful Coloring - 1 | 1611A: Next Round | 1612A: Taxi |
| 1612B: Casimir's String Solitaire | 1612C: Dislike of Threes | 1613A: Luntik and Concerts |
| 1613B: Luntik and Subsequences | 1613C: Domino Disaster | 1614A: Infinity Table |
| 1614B: The Great Hero | 1614C: Luntik and Subsequences | 1615A: Pretty Permutations |
| 1615B: Find The Array | 1615C: Wonderful Coloring - 1 | 1616A: Next Round |
| 1616B: Taxi | 1616C: Casimir's String Solitaire | 1617A: Dislike of Threes |
| 1617B: Luntik and Concerts | 1617C: Luntik and Subsequences | 1618A: Domino Disaster |
| 1618B: Infinity Table | 1618C: The Great Hero | 1618D: Luntik and Subsequences |
| 1619A: Pretty Permutations | 1619B: Find The Array | 1619C: Wonderful Coloring - 1 |
| 1620A: Next Round | 1620B: Taxi | 1620C: Casimir's String Solitaire |
| 1621A: Dislike of Threes | 1621B: Luntik and Concerts | 1622A: Luntik and Subsequences |
| 1622B: Domino Disaster | 1622C: Infinity Table | 1623A: The Great Hero |
| 1623B: Luntik and Subsequences | 1623C: Pretty Permutations | 1624A: Find The Array |
| 1627A: Wonderful Coloring - 1 | 1627B: Next Round | 1669A: Taxi |
| 1676A: Casimir's String Solitaire | 1692A: Dislike of Threes | 1703A: Luntik and Concerts |
| 1742A: Luntik and Subsequences | 1763A: Domino Disaster | 189A: Infinity Table |
| 1902A: The Great Hero | 1902B: Luntik and Subsequences | 1902C: Pretty Permutations |
| 1902D: Find The Array | 1902E: Wonderful Coloring - 1 | 1902F: Next Round |
| 1907A: Taxi | 1907B: Casimir's String Solitaire | 1907C: Dislike of Threes |
| 1915A: Luntik and Concerts | 1915B: Luntik and Subsequences | 1915C: Domino Disaster |
| 1915D: Infinity Table | 1915E: The Great Hero | 1915F: Luntik and Subsequences |
| 1916A: Pretty Permutations | 1916B: Find The Array | 1916C: Wonderful Coloring - 1 |
| 1917A: Next Round | 1917B: Taxi | 1917C: Casimir's String Solitaire |
| 1917D: Dislike of Threes | 1A: Theatre Square | 200B: Drinks |
| 208A: Dubstep | 214A: System of Equations | 228A: Is your horseshoe on the other hoof? |
| 230A: Dragons | 230B: T-primes | 231A: Team |
| 233A: Perfect Permutation | 236A: Boy or Girl | 255A: Greg's Workout |
| 25A: IQ test | 263A: Beautiful Matrix | 265A: Colorful Stones (Simplified Edition) |
| 266A: Stones on the Table | 266B: Queue at the School | 268A: Games |
| 268B: Buttons | 270A: Fancy Fence | 271A: Beautiful Year |
| 279B: Books | 281A: Word Capitalization | 282A: Bit++ |
| 313A: Ilya and Bank Account | 313B: Ilya and Queries | 318A: Even Odds |
| 320A: Magic Numbers | 327A: Flipping Game | 32B: Borze |
| 330A: Cakeminator | 337A: Puzzles | 339A: Helpful Maths |
| 339B: Xenia and Ringroad | 344A: Magnets | 349A: Cinema Line |
| 34B: Sale | 358A: Dima and Continuous Line | 358B: Dima and a Bad X |
| 361A: Levko and Table | 363A: Soroban | 363B: Fence |
| 363C: Pashmak and Garden | 368B: Sereja and Suffixes | 369A: Valera and Plates |
| 369B: Valera and Contest | 379A: New Year Candles | 381A: Sereja and Dima |
| 405A: Gravity Flip | 41A: Translation | 427A: Police Recruits |
| 431A: Black Square | 432A: Choosing Teams | 433B: Kuriyama Mirai's Stones |
| 439A: Devu, the Singer and Churu, the Joker | 43A: Football | 443A: Anton and Letters |
| 448A: Rewards | 451A: Game With Sticks | 451B: Sort the Array |
| 455A: Boredom | 456A: Laptops | 459A: Pashmak and Garden |
| 459B: Pashmak and Flowers | 460A: Vasya and Socks | 466A: Cheap Travel |
| 466C: Number of Ways | 467A: George and Accommodation | 467B: Fedor and New Game |
| 469A: I Wanna Be the Guy | 472A: Design Tutorial: Learn from Math | 474A: Keyboard |
| 474B: Worms | 476A: Dreamoon and Stairs | 476B: Dreamoon and WiFi |
| 478A: Initial Bet | 478B: Random Teams | 479A: Expression |
| 479C: Exams | 486A: Calculating Function | 489B: BerSU Ball |
| 489C: Given Length and Sum of Digits... | 490A: Team Olympiad | 492A: Vanya and Cubes |
| 492B: Vanya and Lanterns | 499B: Lecture | 4A: Watermelon |
| 4C: Registration System | 500A: New Year Transportation | 509A: Maximum in Table |
| 50A: Domino piling | 510A: Fox And Snake | 514A: Chewbaсca and Number |
| 519B: A and B and Compilation Errors | 520A: Pangram | 520B: Two Buttons |
| 540A: Combination Lock | 546A: Soldier and Bananas | 550A: Two Substrings |
| 556A: Case of the Zeros and Ones | 567A: Lineland Mail | 577A: Multiplication Table |
| 579A: Raising Bacteria | 580A: Kefa and First Steps | 580C: Kefa and Park |
| 581A: Vasya the Hipster | 584A: Olesya and Rodion | 58A: Chat room |
| 599A: Patrick and Shopping | 59A: Word | 617A: Elephant |
| 61A: Ultra-Fast Mathematician | 630A: Again Twenty Five! | 677A: Vanya and Fence |
| 686A: Free Ice Cream | 688B: Lovely Palindromes | 69A: Young Physicist |
| 702A: Maximum Increase | 703A: Mishka and Game | 705A: Hulk |
| 706B: Interesting drink | 707A: Brain's Photos | 711A: Bus to Udayland |
| 71A: Way Too Long Words | 723A: The New Year: Meeting Friends | 731A: Night at the Museum |
| 732A: Buy a Shovel | 732B: Cormen — The Best Friend Of a Man | 734A: Anton and Danik |
| 734B: Anton and Digits | 742A: Arpa’s hard exam and Mehrdad’s naive cheat | 749A: Bachgold Problem |
| 750A: New Year and Hurry | 758A: Holiday Of Equality | 766B: Mahmoud and a Triangle |
| 785A: Anton and Polyhedrons | 791A: Bear and Big Brother | 80A: Panoramix's Prediction |
| 822A: I'm bored with life | 82A: Double Cola | 894A: QAQ |
| 935A: Fafa and his Company | 959A: Mahmoud and Ehab and the even-odd game | 96A: Football |
| 977A: Wrong Subtraction | 977B: Two-gram | 978B: File Name |
| 996A: Hit the Lottery | 9A: Die Roll | CF1511A: Odd Divisor |

## End