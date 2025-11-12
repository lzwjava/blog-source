---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: GPG秘密鍵の安全なエクスポート
translated: true
type: note
---

### GPGで秘密鍵をアーマー形式でエクスポートする

GPG（GNU Privacy Guard）では、秘密鍵をアーマー（ASCII）形式でエクスポートすることができ、人間が読みやすい `.asc` ファイル（バイナリ形式ではない）として保存されます。これはバックアップ、転送、または別のマシンへのインポートに便利です。

**重要な警告:** 秘密鍵は機密情報を含みます。必要な場合にのみエクスポートし、保存または送信する場合は出力ファイルを暗号化し、使用後はエクスポートしたファイルを削除して意図しない漏洩を防いでください。秘密鍵を公開してはいけません。

#### 基本的なコマンド構造
特定のユーザーID（鍵に関連付けられたメールアドレスまたは名前）の秘密鍵をエクスポートするには、以下を使用します:

```
gpg --export-secret-keys --armor [KEY_ID] > filename.asc
```

- `KEY_ID`: 鍵のフィンガープリント、短縮ID、メールアドレス、または名前。`gpg --list-secret-keys` で鍵の一覧を表示できます。
- `--armor`: バイナリ形式ではなく、アーマー（ASCII）形式で出力します。
- `> filename.asc`: 出力をファイル（例: `my_secret_key.asc`）にリダイレクトします。これを省略するとターミナルに出力されます。

#### ステップバイステップの使用例
1. **秘密鍵の一覧を表示**して KEY_ID を探します:
   ```
   gpg --list-secret-keys
   ```
   出力例:
   ```
   sec   rsa3072/ABC12345 2023-01-01 [SC] [expires: 2025-01-01]
         Key fingerprint = 1234 5678 ABCD EF01 2345 6789 ABCD EF01 2345 6789
   uid                 [ultimate] Your Name <your@email.com>
   ```

   ここで、`ABC12345` が短縮鍵IDです。正確を期す場合は完全なフィンガープリント `ABCDEF0123456789ABCDEF0123456789` を使用します。

2. **秘密鍵をエクスポート**します:
   ```
   gpg --export-secret-keys --armor ABC12345 > my_secret_key.asc
   ```

3. **エクスポートを検証**します（オプション）:
   ```
   cat my_secret_key.asc
   ```
   ファイルの先頭が `-----BEGIN PGP PRIVATE KEY BLOCK-----` で、末尾が `-----END PGP PRIVATE KEY BLOCK-----` で終わっていることを確認します。

#### 追加オプション
- **すべての秘密鍵をエクスポート**: KEY_ID を省略するとすべてをエクスポートします:
  ```
  gpg --export-secret-keys --armor > all_secret_keys.asc
  ```
- **パスフレーズ保護付き**: 鍵が暗号化されている場合（デフォルト）、GPGはパスフレーズの入力を求めます。
- **公開鍵のみが必要な場合**: `--export` を使用します（公開鍵のみ）。

完全なドキュメントについては、GPGのmanページを参照してください: `man gpg`。GPGを初めて使用する場合は、まず `gpg --gen-key` で鍵を生成してください。