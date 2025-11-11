---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Psutilを使用したポートのプロセス終了
translated: true
type: note
---

### 特定ポートで動作するプロセスの検出と終了（Windows向け psutil 使用）

Psutilは、実行中のプロセス情報とシステム使用率を取得するためのクロスプラットフォームなPythonライブラリです。特定のポートで待ち受けているプロセス（例：npm devサーバーなど）を検出し、そのプロセスを終了させるために使用できます。これはWindowsで動作しますが、以下の点に注意してください：

- **権限**: Windowsでは、プロセスを終了させるには多くの場合管理者権限が必要です（Pythonスクリプトを管理者として実行してください）。これを怠ると`AccessDenied`例外が発生する可能性があります。
- **ポート検出**: ここでは「inet」種別（IPv4とIPv6をカバー）のTCP接続に焦点を当てます。これは`npm run dev`などで起動されるWebサーバーで一般的です。
- **前提**: ここではリスニング（サーバー）ポート（例：ローカルにバインドされているもの）をチェックしたいと想定しています。ポートへのアウトバウンド接続を意味する場合は、アプローチが若干異なります。詳細が必要な場合はお知らせください。

#### ステップ 1: psutilのインストール
まだインストールしていない場合：
```bash
pip install psutil
```

#### ステップ 2: 検出と終了のサンプルコード
以下は完全なPythonスクリプトです。指定されたポートで待ち受けているプロセスのPIDを検出する関数を定義し（指定通り`kind='inet'`を使用）、その後終了させます。Windowsでは、`kill()`よりも`terminate()`が推奨されます（UnixのSIGTERMと同等で、グレースフルシャットダウンが可能です）。

```python
import psutil
import time  # オプションの遅延用

def get_pid_listening_on_port(port, kind='inet'):
    """
    指定されたポートで待ち受けているプロセスをネットワーク接続からスキャンします。
    PIDのリストを返します（通常は1つですが、稀に複数の場合もあります）。
    """
    pids = []
    for conn in psutil.net_connections(kind=kind):
        # リスニング接続（status='LISTEN'）で、ローカルアドレスのポートが一致するかチェック
        if conn.status == 'LISTEN' and conn.laddr and conn.laddr.port == port:
            if conn.pid:
                pids.append(conn.pid)
    return pids

def kill_process_on_port(port, kind='inet'):
    """
    指定されたポートで待ち受けているプロセスを検出して終了させます。
    複数のプロセスがある場合は、すべて終了させます（警告付き）。
    """
    pids = get_pid_listening_on_port(port, kind)
    if not pids:
        print(f"ポート {port} で待ち受けているプロセスは見つかりませんでした。")
        return
    
    for pid in pids:
        try:
            proc = psutil.Process(pid)
            print(f"ポート {port} のプロセス {proc.name()} (PID {pid}) を終了させています...")
            # グレースフルシャットダウンのため terminate() を使用。SIGTERM的なシグナルを送信します。
            proc.terminate()
            # オプション：少し待機し、終了しない場合は強制終了
            gone, still_alive = psutil.wait_procs([proc], timeout=3)
            if still_alive:
                print(f"PID {pid} を強制終了しています...")
                still_alive[0].kill()
        except psutil.AccessDenied:
            print(f"アクセスが拒否されました：PID {pid} を終了できません。管理者として実行していますか？")
        except psutil.NoSuchProcess:
            print(f"プロセス {pid} は既に存在しません。")

# 使用例：3000を対象のポートに置き換えてください（例：npm devサーバーはしばしば3000を使用）
if __name__ == "__main__":
    kill_process_on_port(3000)  # 必要に応じてkindを調整（例：IPv4のみの場合は 'inet4'）
```

#### 主な説明
- **`psutil.net_connections(kind='inet')`**: これは種別 'inet'（IPv4とIPv6を含む）のネットワーク接続を取得します。各接続は以下のようなフィールドを持つnamedtupleです：
  - `laddr`: ローカルアドレス（例：('0.0.0.0', 8080) – IPとポート）。
  - `status`: 接続を待ち受けているサーバーの場合は 'LISTEN'。
  - `pid`: 所有者のプロセスID。
  - サーバー（npmのdevポートなど）を見つけるため、クライアント接続ではなく`status == 'LISTEN'`でフィルタリングします。
- **PIDの取得**: スクリプトは接続タプルから直接PIDを取得します。終了させずに検出のみ行いたい場合は、PIDを返す`get_pid_listening_on_port(port)`を使用してください。
- **プロセスの終了**:
  - `psutil.Process(pid).terminate()`: 終了シグナルを送信します。WindowsではCTRL+Cのようなものです。
  - 終了しない場合は、オプションで`kill()`で強制終了します（SIGKILL相当）。
  - Psutilの`wait_procs()`はプロセスが終了するのを待機します。
- **inet種別の特異性**: 'inet'はIPv4とIPv6の両方を含みます。IPv4のみと分かっている場合は`kind='inet4'`に変更してください。THISNAMEは「inet kind」リクエストに直接対応します。
- **Windows固有の注意点**:
  - PsutilはWindowsの内部をうまく処理しますが、ネットワーク情報によっては管理者権限が必要な場合があります。
  - 1024未満のポート（特権ポート）にはシステムサービスのみがバインドできますが、検出は可能です。
- **エラーハンドリング**: プロセス不在やアクセス問題の基本的なチェックを追加しました。
- **テスト**: `npm run dev`などを実行してポート3000を占有させ、その後このスクリプトを実行してください。

もしこれが正確なニーズに合わない場合（例：「npm run port」が別の意味を持つ、または非リスニング接続を検出したい場合）、詳細を提供していただければ修正します！セキュリティ/安全性のため、意図したプロセスのみを終了させていることを確認してください。