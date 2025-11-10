---
audio: false
generated: true
lang: ja
layout: post
title: YouTube-dlボット認証エラーの修正
translated: true
type: note
---

youtube-dl で発生する「Sign in to confirm you’re not a bot」エラーは、通常、YouTubeがリクエストをブロックしていることが原因で発生します。これは、IP制限、VPNの使用、または認証がないためであることが多いです。この問題を解決するための手順を、最も単純な解決策から順に説明します。

1. **youtube-dl の更新**:
   - このエラーは、youtube-dl のバージョンが古いことが原因である可能性があります。YouTubeはシステムを頻繁に更新するため、最新バージョンに更新してください:
     ```bash
     sudo youtube-dl -U
     ```
     または、pip でインストールした場合は:
     ```bash
     pip install --upgrade youtube-dl
     ```
   - 更新後、再度コマンドを試してください:
     ```bash
     youtube-dl https://www.youtube.com/watch?v=st3mUEub99E
     ```

2. **yt-dlp への切り替え (推奨される代替案)**:
   - youtube-dl は積極的にメンテナンスされていません。youtube-dl のフォークである yt-dlp は、最近の YouTube の変更に対してより信頼性が高いです。yt-dlp をインストールします:
     ```bash
     sudo pip install yt-dlp
     ```
     その後、以下を使用します:
     ```bash
     yt-dlp https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - yt-dlp は認証と IP 制限をより適切に処理します。

3. **VPN の無効化またはサーバーの変更**:
   - VPN を使用している場合、YouTube があなたの IP を不審なものとしてフラグを立てている可能性があります。VPN を無効にするか、別のサーバーに切り替えてみてください:
     ```bash
     yt-dlp https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - ユーザーからの報告によると、VPN から切断するか、サーバーを切り替えた後に成功した例があります。

4. **認証に Cookie を使用する**:
   - YouTube はボットチェックを回避するために認証を要求する場合があります。YouTube にログインしているブラウザから Cookie をエクスポートします:
     - Firefox または Chrome 用の "Export Cookies" のようなブラウザ拡張機能をインストールします。
     - YouTube にサインインし、Cookie を `cookies.txt` ファイルにエクスポートし、それを以下のように使用します:
       ```bash
       youtube-dl --cookies ~/path/to/cookies.txt https://www.youtube.com/watch?v=st3mUEub99E
       ```
       または yt-dlp の場合:
       ```bash
       yt-dlp --cookies ~/path/to/cookies.txt https://www.youtube.com/watch?v=st3mUEub99E
       ```
     - あるいは、`--cookies-from-browser firefox` (または `firefox` を `chrome`, `edge` などに置き換えて) を使用して Cookie を自動的に抽出します:
       ```bash
       yt-dlp --cookies-from-browser firefox https://www.youtube.com/watch?v=st3mUEub99E
       ```
     - 注意: 潜在的なフラグ付けを防ぐために、主要な Google アカウントの使用は避けてください。可能であれば使い捨てのアカウントを使用してください。

5. **プロキシを使用する**:
   - 問題が解決しない場合、あなたの IP が (データセンター IP を使用している場合などに) ブロックされている可能性があります。あなたの IP を隠すために、レジデンシャルプロキシを試してみてください:
     ```bash
     youtube-dl --proxy "http://proxy_address:port" https://www.youtube.com/watch?v=st3mUEub99E
     ```
     または yt-dlp の場合:
     ```bash
     yt-dlp --proxy "http://proxy_address:port" https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - レジデンシャルプロキシは、データセンタープロキシよりもフラグが立てられる可能性が低いです。

6. **キャッシュのクリアまたは別のネットワークの試行**:
   - 最近ログや一時ファイルをクリアした場合は、youtube-dl/yt-dlp が破損したキャッシュに依存していないことを確認してください。キャッシュをクリアします:
     ```bash
     rm -rf ~/.cache/youtube-dl
     rm -rf ~/.cache/yt-dlp
     ```
   - 問題が IP 関連であるかテストするために、別のネットワーク (例: モバイルホットスポット) に切り替えてください。

7. **デバッグのための詳細出力**:
   - 上記の手順が失敗した場合、詳細な出力を伴うコマンドを実行して、さらに診断します:
     ```bash
     youtube-dl -v https://www.youtube.com/watch?v=st3mUEub99E
     ```
     または yt-dlp の場合:
     ```bash
     yt-dlp -v https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - 出力を関連するフォーラム (例: yt-dlp の GitHub issues) で共有し、コミュニティの支援を求めてください。

**注意点**:
- YouTube のボット検出は厳しくなっており、データセンター IP や未認証のリクエストを対象とすることが多いです。
- Cookie の使用にはアカウントがフラグ付けされる小さなリスクがあるため、セカンダリアカウントを使用してください。
- ビデオが非公開または制限されている場合は、Cookie を使用する前にあなたのアカウントがアクセス権を持っていることを確認してください。
- これらのいずれも機能しない場合は、Invidious や NewPipe のような代替フロントエンドの使用を検討してください。ただし、制限がある可能性があります。

これらの手順を、更新または yt-dlp への切り替えから順に試してください。これが最も可能性の高い修正方法です。問題が解決しない場合は、詳細な出力または特定の詳細 (例: VPN の使用状況、OS) をお知らせください。