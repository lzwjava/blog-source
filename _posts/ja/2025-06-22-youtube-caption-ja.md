---
audio: false
generated: true
lang: ja
layout: post
title: YouTube動画キャプション抽出方法
translated: true
type: note
---

YouTube動画のすべての字幕を取得するには、以下の手順に従ってください。手動または自動のアプローチ、およびニーズに応じて方法が異なります。字幕は動画で利用可能である必要があります（自動生成または作成者によってアップロードされたもの）。

### 手動方法（YouTubeの組み込みトランスクリプト機能を使用）
1. **動画を開く**: WebブラウザでYouTubeにアクセスし、目的の動画に移動します。
2. **字幕を確認**: 動画をクリックして一時停止します。プレイヤーの右下近くにある「CC」（クローズドキャプション）アイコンを探します。表示されている場合、字幕が利用可能です。
3. **トランスクリプトにアクセス**:
   - 動画の説明文を下にスクロールし、「さらに表示」をクリックします。
   - 「トランスクリプトを表示」を探してクリックします（利用可能な場合）。これにより、動画の右側にタイムスタンプ付きのテキストを含むトランスクリプトパネルが開きます。
4. **タイムスタンプの切り替え**: トランスクリプトパネルの右上にある3つの縦ドットをクリックし、「タイムスタンプを切り替え」を選択して、タイムスタンプの表示/非表示を切り替えます。
5. **トランスクリプトをコピー**:
   - トランスクリプトの最下部までスクロールし、最後の単語の後でクリックして押したまま、上部までドラッグしてすべてのテキストをハイライトします。
   - `Ctrl + C`（Windows）または `Command + C`（Mac）を押してコピーします。
6. **貼り付けと保存**: テキストエディタ（例: Notepad、TextEdit、Word）を開き、`Ctrl + V` または `Command + V` でテキストを貼り付け、`.txt`ファイルまたは希望の形式で保存します。

**注意**: この方法はYouTubeのウェブサイトでのみ機能し、モバイルアプリでは機能しません。[](https://www.wikihow.com/Download-YouTube-Video-Subtitles)

### コンテンツクリエイター向け（自身の動画から字幕をダウンロード）
動画を所有している場合、YouTube Studioから直接字幕をダウンロードできます:
1. **YouTube Studioにログイン**: [studio.youtube.com](https://studio.youtube.com) にアクセスします。
2. **動画を選択**: 左メニューの「コンテンツ」をクリックし、動画を選択します。
3. **字幕にアクセス**: 左メニューの「字幕」をクリックし、言語を選択します。
4. **字幕をダウンロード**: 字幕トラック横の3点メニューをクリックし、「ダウンロード」を選択します。`.srt`、`.vtt`、`.sbv`などの形式を選択します。
5. **編集または使用**: ダウンロードしたファイルをテキストエディタまたは字幕エディタ（例: Aegisub）で開き、さらに使用します。

**注意**: 管理しているチャンネルの動画についてのみ字幕ファイルをダウンロードできます。[](https://ito-engineering.screenstepslive.com/s/ito_fase/a/1639680-how-do-i-download-a-caption-file-from-youtube)

### 自動化方法（サードパーティ製ツールを使用）
特定の形式（例: `.srt`）での字幕や、所有していない動画の字幕が必要な場合は、信頼できるサードパーティ製ツールを使用します:
1. **ツールを選択**: 人気のあるオプションは以下の通りです:
   - **DownSub**: 字幕をダウンロードするための無料オンラインツール。
   - **Notta**: 高精度な文字起こしと字幕ダウンロードを提供します。[](https://www.notta.ai/en/blog/download-subtitles-from-youtube)
   - **4K Download**: 字幕抽出用のデスクトップアプリ。[](https://verbit.ai/captioning/a-guide-to-downloading-subtitles-and-captions-from-youtube-enhancing-accessibility-and-user-experience/)
2. **動画URLをコピー**: YouTube動画を開き、動画の下の「共有」をクリックしてURLをコピーします。
3. **ツールを使用**:
   - ツールの入力フィールドにURLを貼り付けます。
   - 希望の言語と形式（例: `.srt`、`.txt`）を選択します。
   - 「ダウンロード」または「抽出」をクリックし、ファイルを保存します。
4. **確認**: ファイルを開いて正確さを確認します。自動生成された字幕にはエラーが含まれる可能性があります。

**注意**: セキュリティリスクを避けるため、信頼できるツールを使用してください。一部のツールには広告が表示されたり、高度な機能に支払いが必要な場合があります。[](https://gotranscript.com/blog/how-to-download-subtitles-from-youtube)

### YouTube APIの使用（開発者向け）
字幕の一括抽出やアプリ統合には、YouTube Data APIを使用します:
1. **APIアクセスを設定**: [Google Cloud Console](https://console.cloud.google.com) でプロジェクトを作成し、YouTube Data API v3を有効にして、APIキーを取得します。
2. **字幕トラックをリスト**: `captions.list` エンドポイントを使用して、動画の利用可能な字幕トラックを取得します。例:
   ```
   GET https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId=VIDEO_ID&key=API_KEY
   ```
3. **字幕をダウンロード**: `captions.download` エンドポイントを使用して、特定の字幕トラックを取得します。例:
   ```
   GET https://www.googleapis.com/youtube/v3/captions/CAPTION_ID?tfmt=srt&key=API_KEY
   ```
4. **制限事項**:
   - 自身の動画の字幕のみダウンロード可能です。ただし、動画所有者が字幕を公開している場合は除きます。
   - APIの使用にはクォータ制限があります（字幕ダウンロード1回あたり約200ユニット）。[](https://developers.google.com/youtube/v3/docs/captions)[](https://stackoverflow.com/questions/73863672/how-can-i-get-captions-of-a-youtube-video-and-display-it-separately)
5. **代替方法**: 一部の開発者は動画ページのソースからタイムテキストURL（例: `https://www.youtube.com/api/timedtext?...`）をスクレイピングしますが、これは信頼性が低く、YouTubeの利用規約に違反する可能性があり、IPブロックのリスクがあります。[](https://stackoverflow.com/questions/73863672/how-can-i-get-captions-of-a-youtube-video-and-display-it-separately)

### 追加のヒント
- **言語選択**: 字幕が複数の言語で利用可能な場合、「字幕/CC」設定またはトランスクリプトのドロップダウンメニューから希望の言語を選択します。[](https://riverside.fm/blog/youtube-transcription)
- **自動生成された字幕**: アクセント、背景ノイズ、または複雑なオーディオにより、エラーが含まれる可能性があります。正確さが重要な場合は、確認と編集を行います。[](https://support.google.com/youtube/answer/6373554?hl=en)
- **アクセシビリティ**: 字幕は、聴覚障害者や難聴の視聴者のためのアクセシビリティを向上させ、コンテンツを検索可能にすることでSEOを改善します。[](https://www.descript.com/blog/article/transcript-of-youtube-videos)
- **字幕が利用できない場合**: 動画に字幕がない場合は、RevやNottaなどの文字起こしサービスを使用して、オーディオからトランスクリプトを生成することを検討してください。[](https://www.rev.com/resources/how-to-download-youtube-subtitles-as-text-files)[](https://www.notta.ai/en/blog/download-subtitles-from-youtube)

### 制限事項
- すべての動画に字幕があるわけではありません。特に、作成者が無効にした場合、またはYouTubeの自動字幕生成がその言語またはオーディオ品質でサポートされていない場合です。[](https://support.google.com/youtube/answer/6373554?hl=en)
- YouTubeモバイルアプリはトランスクリプト表示をサポートしていませんが、「CC」ボタンから字幕を有効にすることはできます。[](https://riverside.fm/blog/youtube-transcription)
- 一部のサードパーティ製ツールまたはAPIメソッドは、自動生成された字幕または制限付き動画では機能しない場合があります。[](https://stackoverflow.com/questions/9611397/how-to-extract-closed-caption-transcript-from-youtube-video)

特定の動画の字幕や特定の形式での字幕が必要な場合は、お知らせください。さらに詳しく案内します！