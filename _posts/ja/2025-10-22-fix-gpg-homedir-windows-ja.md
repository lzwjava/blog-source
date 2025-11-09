---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WindowsでのGPGホームディレクトリパスの修正
translated: true
type: note
---

はい、その通りです。WindowsのGit Bash（MSYS2/Cygwinに似た環境で動作）では、`gpg`の`--homedir`パスでバックスラッシュ（`\`）を使用すると、エスケープとパス変換の仕組みにより、シェルが引数を誤って解釈します。これによりパスが不正な形式に変換され（例: `C:\Users\me\.gnupg` が `C:Usersme.gnupg` のような無効なパスに解決される、またはWindows形式への自動変換中にさらに乱れる）、ディレクトリを解決できなくなります。その結果、GPGがキーファイルを見つけられず、「秘密鍵がありません」エラー（または `pubring.kbx` に対する「そのようなファイルやディレクトリはありません」のような類似エラー）が発生します。

### クイック修正
- MSYS2形式のドライブプレフィックスとスラッシュ（`/`）を使用する: `gpg --homedir /c/Users/me/.gnupg ...`
- これによりMSYS2がネイティブのGPGバイナリに渡す際に適切なWindowsパス（例: `C:\Users\me\.gnupg`）に自動変換されます。
- 先頭の `/` なしの `c:/` のようなドライブレターは避けてください。これらは相対パスとして扱われ、現在の作業ディレクトリが先頭に追加され、同じ検索失敗を引き起こします。

`GNUPGHOME`のような環境変数にも同じルールが適用されます：`/`を使用して設定します（例: `export GNUPGHOME=/c/Users/me/.gnupg`）。

[MSYS2ファイルシステムパス](https://www.msys2.org/docs/filesystem-paths/)  
[MSYS2でのGNUPGHOMEの議論](https://lists.gnupg.org/pipermail/gnupg-users/2025-February/067536.html)  
[Windows/MSYS2でのGPG --homedirバグ](https://www.reddit.com/r/GnuPG/comments/1cl4dw8/bug_windows_homedir_with_drive_letter_treated_as/)