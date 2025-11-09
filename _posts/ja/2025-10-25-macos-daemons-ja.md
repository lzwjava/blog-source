---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: macOSデフォルトデーモンプロセス
translated: true
type: note
---

### macOSのデフォルトデーモンプロセス

macOSでは、デーモンプロセスはユーザーインターフェースなしで実行されるバックグラウンドサービスであり、通常は起動時またはオンデマンドで開始されます。これらはシステムのinitおよびサービス管理フレームワークである **launchd**（PID 1）によって管理されます。デーモンはエージェントとは異なります：デーモンはroot/システム全体として（ログイン前に）実行され、エージェントはユーザーごとに（ログイン後に）実行されます。

デフォルトのシステムデーモンは、`/System/Library/LaunchDaemons/` にあるプロパティリスト（.plist）ファイルで定義されています。標準インストールでは通常約300～350個存在します（例：macOS 10.14 Mojaveでは339個）。これらはネットワークやセキュリティからハードウェア管理まで、あらゆる範囲をカバーしています。ユーザーがインストールした、またはサードパーティのデーモンは `/Library/LaunchDaemons/` に配置されます。

#### デフォルトデーモンの表示方法
ターミナルでロードされているすべてのデーモン（およびエージェント）をリスト表示するには：
- `sudo launchctl list`（システム全体のデーモンとエージェントを表示）
- `launchctl list`（ユーザー固有のエージェントのみを表示）

完全なディレクトリリストについては：`ls /System/Library/LaunchDaemons/`（sudoは不要ですが、ファイルは読み取り専用です）

これらのコマンドは、PID、ステータス、ラベル（例：`com.apple.timed`）などの列を出力します。

#### 「timed」デーモン
特に「timed」について言及されていますが、これは **com.apple.timed**（タイムシンクデーモン）を指します。これはmacOS High Sierra（10.13）で導入された、古い `ntpd` プロセスを置き換えるためのコアシステムデーモンです。

- **目的**：MacのシステムクロックをNTP（Network Time Protocol）サーバーと15分ごとに照会し、自動的に同期させて正確性を保ちます。これにより、ログ、証明書、ネットワーク操作のための正確な時間管理が確保されます。
- **動作方法**：launchdによって `/System/Library/LaunchDaemons/com.apple.timed.plist` から起動され、`_timed` ユーザー（`_timed` および `_sntpd` グループ内）として実行されます。サーバー応答に基づいてクロックを調整するために `settimeofday` システムコールを使用します。設定は `/etc/ntpd.conf`（NTPサーバー）にあり、状態は `/var/db/timed/com.apple.timed.plist` にキャッシュされます。
- **関連事項**：システム設定 > 一般 > 日付と時間 > 「日付と時刻を自動的に設定」に関連しています。これが無効になっている場合、timedは同期しません。高精度の設定など、高度なセットアップの場合、Chronyなどのツールで置き換えることができますが、その場合はtimedを無効にする必要があります。

クロックがずれる場合は、ネットワークの問題やNTP（UDPポート123）に対するファイアウォールのブロックを確認してください。

#### その他の一般的なデフォルトデーモン（「など」）
以下は、頻繁に実行されるデフォルトのシステムデーモンの一部を機能別にまとめた表です。網羅的ではありません（数百あります）が、基本をカバーしています。ラベルは.plistファイル名から取られています。

| カテゴリ       | デーモンラベル                  | 説明 |
|----------------|-------------------------------|-------------|
| **コアシステム** | `com.apple.launchd`          | launchdプロセス自体。他のすべてを起動します。 |
| **時間と同期** | `com.apple.timed`             | NTP時間同期（上記参照）。 |
| **ユーザー管理** | `com.apple.opendirectoryd`   | ユーザー/グループアカウントとディレクトリサービスを処理します。 |
| **ユーザー管理** | `com.apple.accounts`         | ユーザーアカウントと認証を管理します。 |
| **ネットワーキング** | `com.apple.mDNSResponder`    | Bonjour/mDNSによるローカルネットワーク検出（例：AirDrop）。 |
| **ネットワーキング** | `com.apple.nesessionmanager` | ネットワーク拡張とVPN管理。 |
| **Bluetooth/無線** | `com.apple.bluetoothd`      | Bluetoothデバイスの処理。 |
| **iCloud/同期** | `com.apple.cloudd`            | iCloudデータ同期とサービス。 |
| **セキュリティ**   | `com.apple.securityd`        | キーチェーンと資格情報の管理（多くの場合、エージェントとしても機能）。 |
| **アップデート**    | `com.apple.softwareupdated`  | ソフトウェアアップデートとカタログのダウンロードを処理します。 |
| **ハードウェア**   | `com.apple.kextd`             | カーネル拡張のロードと管理。 |
| **ロギング**    | `com.apple.systemnotificationd` | システム通知とロギング。 |
| **MDM（有効な場合）** | `com.apple.mdmclient`     | エンタープライズ設定のためのモバイルデバイス管理クライアント。 |

これらは、macOSを安定させるために、継続的またはトリガーで実行されます。もし動作がおかしい場合（例：CPU使用率が高い）、`sudo launchctl unload /System/Library/LaunchDaemons/com.apple.example.plist` で一時的にアンロードできますが、システムファイルの変更は避けてください。

お使いのMacでの完全で最新のリスト（2025年10月現在、おそらくmacOS 15 Sequoia以降）については、上記のコマンドを実行してください。バージョンによって少しずつ進化します。

#### 参考文献
- [The macOS Process Journey — “timed” (Time Sync Daemon)](https://medium.com/@boutnaru/the-macos-process-journey-timed-time-sync-daemon-4898c8185b4b)
- [Daemons and Agents could be slowing down your Mac](https://appleinsider.com/inside/macos/tips/daemons-and-agents-could-be-slowing-down-your-mac)
- [What files are included in the /System/Library/LaunchAgents and /System/Library/LaunchDaemons](https://apple.stackexchange.com/questions/361029/what-files-are-included-in-the-system-library-launchagents-and-system-library)
- [Script management with launchd in Terminal on Mac](https://support.apple.com/guide/terminal/script-management-with-launchd-apdc6c1077b-5d5d-4d35-9c19-60f2397b2369/mac)
- [How to show all running launchctl daemons/agents?](https://apple.stackexchange.com/questions/134817/how-to-show-all-running-launchctl-daemons-agents)