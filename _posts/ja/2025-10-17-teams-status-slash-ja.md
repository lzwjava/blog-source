---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: スラッシュコマンドでMicrosoft Teamsのステータスを設定
translated: true
type: note
---

### Microsoft Teams でスラッシュコマンドを使用してステータスを設定する

Microsoft Teams のスラッシュコマンドを使用すると、チャットインターフェースから直接、プレゼンスステータス（利用可能、退席中、オフラインなど）を素早く更新できます。これらはコマンドラインやターミナルからではなく、Teams アプリ（デスクトップ、Web、モバイル）内でのみ機能します。使用方法は以下のとおりです：

1.  **Microsoft Teams を開き**、任意のチャット、チャネル、またはダイレクトメッセージに移動します。
2.  通常メッセージを入力する下部の**作成ボックスをクリック**します。
3.  **スラッシュ (/) に続けてステータスコマンドを入力します**。例：
    - `/available` – ステータスを「利用可能」に設定します（緑のドット）。
    - `/away` – ステータスを「退席中」に設定します（黄色の時計）。
    - `/busy` – ステータスを「取り込み中」に設定します（赤い丸）。
    - `/brb` – ステータスを「すぐに戻ります」に設定します（青い時計）。
    - `/dnd` – ステータスを「通知をしない」に設定します（斜線の入った赤い丸）。
    - `/offline` – ステータスを「オフラインとして表示」に設定します（X の付いた灰色の丸）。
4.  **Enter キーを押して**コマンドを実行します。ステータスは即座に更新され、組織内の他のユーザーに表示されます。

これらの変更は一時的なものであり、アクティビティ（例えば、5分間の非アクティブ後）に基づいて自動的にリセットされる場合があります（自動的に「退席中」に切り替わるなど）。カスタムの期間（例：1時間「取り込み中」）を設定するには、代わりにプロファイルメニューを使用してください：
- 右上のプロフィール画像をクリックします。
- 現在のステータスにカーソルを合わせ、新しいステータスを選択し、**期間**を選択して時間枠を選びます。

スラッシュコマンドは会話中の素早い切り替えに便利ですが、より詳細に制御するにはプロファイルメニューの方が適しています。

[Use commands in Microsoft Teams](https://support.microsoft.com/en-us/office/use-commands-in-microsoft-teams-88f61508-284d-417f-a53d-9e082164050b)  
[Microsoft Teams - Setting Your Presence Status](https://www.dataprise.com/resources/blog/microsoft-teams-set-presence-status/)  
[Change your status in Microsoft Teams](https://support.microsoft.com/en-us/office/change-your-status-in-microsoft-teams-ce36ed14-6bc9-4775-a33e-6629ba4ff78e)