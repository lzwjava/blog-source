---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: macOSとLinuxのUNIX継承
translated: true
type: note
---

### macOSとLinuxの共通の起源

macOS（旧OS X）とLinuxは、1970年代にベル研究所で開発された先駆的なマルチタスクオペレーティングシステムであるUnixにその概念的ルーツを共有しています。1991年にリーナス・トーバルズによって作成されたLinuxは、Unixをモデルにしたオープンソースのカーネルですが、独立して開発されており、Unixのソースコードから派生したものではありません。一方、macOSはDarwin（AppleのUnix系OS、FreeBSDベース）上に構築されており、Unixコンポーネントを含み、The Open GroupからUnix準拠として認定されています。この共通の系譜が、両者がUnix的な機能を提供することを目指しているため、ツールやコマンドにおける多くの類似点を説明しています。

補足説明: Unixの標準（例: POSIX）は、互換性を確保するために両システムに影響を与えました。UbuntuのようなLinuxディストリビューションは明示的にUnix系であり、macOSはBSD（Berkeley Software Distribution）を通じてUnixツールを継承しています。BSDはもう一つの初期のUnixの分派です。

### 両方に'ps'コマンドが存在する理由

'ps'（プロセスステータス）コマンドは、実行中のプロセスに関する情報を表示し、1970年代に最初に実装されたUnixに直接由来します。macOSとLinuxの両方に'ps'が含まれている理由は以下の通りです：
- Unixの系譜の一部であるため：macOSはDarwin/FreeBSD経由で、LinuxはPROCファイルシステムおよびGNUやPOSIX仕様からの標準ユーティリティ経由で継承。
- システム診断、スクリプト作成、管理に不可欠なため、コアツールセット（例: macOSのターミナルやLinuxのシェル）にデフォルトでバンドルされている。

`ps -p pid -o pid,ppid,lstart,etime,command`のようなコマンド構文は、共有のPOSIX標準により両方でサポートされていますが、オプションが若干異なる場合があります（例: macOSはBSD風のフラグ、LinuxはGNUバリアントを使用することが多い）。これは偶然ではなく、Unixからの直接の系譜です。

### macOSとLinuxは両方ともUnixと言えるか？

厳密には違います：「Unix」はOSのファミリーであり、登録商標です。macOSは、Darwinが（The Open Groupによって）認定されており、Single Unix Specification (SUS) に準拠しているため、Unixとして認定されています。一方、Linuxは（Debianなどのディストロとして）完全なOSの基礎を形成するカーネルですが、カーネル自体およびそのディストリビューションは公式には「Unix」ではありません。これらは、完全な認定や共有コードベースなしでPOSIXに準拠しているため、「Unix系」または「Unix互換」です。

これらを「Unix的」または「Unixの伝統の継承者」と言うことはできますが、Linuxを「すべてUnixである」と呼ぶのは不正確です。実際には、'ps'のようなコマンドでは同様に動作するため、ほとんどのユーザーにとってこれは大きな問題ではありません。厳密さが重要であれば、認定状況を確認するか、公式の定義を参照してください。