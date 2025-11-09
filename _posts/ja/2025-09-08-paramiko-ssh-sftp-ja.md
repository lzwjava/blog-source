---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Paramiko SSHとSFTPガイド
translated: true
type: note
---

### インストール
ParamikoはSSHとSFTPのためのPythonライブラリです。pip経由でインストールします：

```bash
pip install paramiko
```

### 基本的な使い方
Paramikoを使用すると、SSHサーバーに接続し、コマンドを実行し、ファイルを転送できます。秘密鍵は常に安全に扱い、強力なパスワードを使用してください。Paramikoは鍵ベース認証とパスワード認証の両方をサポートしています。

主な概念：
- **Client**: `paramiko.SSHClient()` を使用して接続を設定します。
- **Transport**: 低レベル制御には `paramiko.Transport()` を使用します。
- `client.connect()` でホスト名、ユーザー名、およびパスワードまたは鍵（例：`paramiko.RSAKey.from_private_key_file()`）を使用して認証します。

### 例：接続とコマンド実行
SSHサーバーに接続し、コマンドを実行し、出力を表示する完全なスクリプトです。プレースホルダーを実際の情報に置き換えてください。

```python
import paramiko

# SSHクライアントを作成
client = paramiko.SSHClient()

# ホスト鍵を自動追加（本番環境では注意。代わりにknown_hostsを読み込む）
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # 接続（パスワードまたは鍵ファイルを使用）
    client.connect(
        hostname='your.server.com',
        port=22,  # デフォルトSSHポート
        username='your_username',
        password='your_password',  # または key_filename='path/to/private_key.pem'
    )

    # コマンドを実行
    stdin, stdout, stderr = client.exec_command('echo "Hello from SSH!"')

    # 出力を読み取り
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    print("出力:", output)
    print("エラー:", error)

except paramiko.SSHException as e:
    print(f"SSHエラー: {e}")
finally:
    client.close()
```

### 高度な例：鍵ベース認証とファイル転送
鍵認証の場合、必要に応じて鍵ペアを生成し（例：`ssh-keygen`）、サーバーの `~/.ssh/authorized_keys` に公開鍵を追加してから、以下を使用します：

```python
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # 鍵ベース接続
    client.connect(
        hostname='your.server.com',
        username='your_username',
        key_filename='~/.ssh/id_rsa',  # 秘密鍵へのパス
    )

    # コマンド実行
    stdin, stdout, stderr = client.exec_command('ls -la')
    print(stdout.read().decode('utf-8'))

    # SFTP例：ファイル転送
    sftp = client.open_sftp()
    sftp.put('local_file.txt', 'remote_file.txt')  # アップロード
    sftp.get('remote_file.txt', 'local_copy.txt')  # ダウンロード
    sftp.close()

except Exception as e:
    print(f"エラー: {e}")
finally:
    client.close()
```

### ヒントとベストプラクティス
- **セキュリティ**: パスワードより鍵ベース認証を優先します。本番環境では `AutoAddPolicy` を無効にし、`client.load_host_keys()` でホスト鍵を検証してください。
- **エラーハンドリング**: 常に `paramiko.SSHException` をキャッチし、`exit_status = stdout.channel.recv_exit_status()` で終了コードを確認します。
- **スレッド**: Paramikoはデフォルトではスレッドセーフではありません。必要に応じてロックを使用してください。
- **ドキュメント**: 詳細は [公式Paramikoドキュメント](https://docs.paramiko.org/) を参照してください。OpenSSHの `sshd` やローカルVMなどのツールでテストします。

これで開始できます。必要に応じて適応させてください！