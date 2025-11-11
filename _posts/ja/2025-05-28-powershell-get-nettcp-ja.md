---
audio: false
generated: true
lang: ja
layout: post
title: 'PowerShell: Get NetTCPConnection の使用方法'
translated: true
type: note
---

PowerShellの`Get-NetTCPConnection`コマンドレットは、Windowsシステム上のTCP接続情報を取得します。これは`NetTCPIP`モジュールの一部で、Windows 8/Windows Server 2012以降で利用可能です。以下に使用方法を簡潔に示します：

### 基本的な使用方法
`Get-NetTCPConnection`を実行してすべてのアクティブなTCP接続をリスト表示：

```powershell
Get-NetTCPConnection
```

これにより、LocalAddress、LocalPort、RemoteAddress、RemotePort、State、OwningProcessなどの詳細が返されます。

### 一般的なパラメータ
- **-State**: 接続状態でフィルタ（例：Established、Listening、TimeWait）
  ```powershell
  Get-NetTCPConnection -State Established
  ```
- **-LocalPort**: ローカルポート番号でフィルタ
  ```powershell
  Get-NetTCPConnection -LocalPort 80
  ```
- **-RemoteAddress**: リモートIPアドレスでフィルタ
  ```powershell
  Get-NetTCPConnection -RemoteAddress 192.168.1.1
  ```
- **-RemotePort**: リモートポートでフィルタ
  ```powershell
  Get-NetTCPConnection -RemotePort 443
  ```
- **-OwningProcess**: 接続を所有するプロセスID（PID）でフィルタ
  ```powershell
  Get-NetTCPConnection -OwningProcess 1234
  ```

### フィルタの組み合わせ
パラメータを組み合わせてより具体的な結果を取得：
```powershell
Get-NetTCPConnection -State Established -LocalPort 80
```

### 特定のプロパティの表示
`Select-Object`を使用して必要なプロパティのみ表示：
```powershell
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### プロセス詳細の特定
接続に関連するプロセスを特定するには、`Get-Process`と組み合わせ：
```powershell
Get-NetTCPConnection -LocalPort 80 | ForEach-Object { Get-Process -Id $_.OwningProcess }
```

### 出力のソートとフォーマット
結果をソート（例：LocalPortで）し、テーブル形式で表示：
```powershell
Get-NetTCPConnection | Sort-Object LocalPort | Format-Table LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### 実用的な例
1. **すべてのリスニング接続をリスト表示：**
   ```powershell
   Get-NetTCPConnection -State Listening
   ```
2. **特定のリモートサーバーへの接続を検索：**
   ```powershell
   Get-NetTCPConnection -RemoteAddress "8.8.8.8"
   ```
3. **特定のポートを使用しているプロセスを確認：**
   ```powershell
   $connection = Get-NetTCPConnection -LocalPort 8080
   Get-Process -Id $connection.OwningProcess
   ```

### 注意点
- **管理者権限**: 一部の詳細（システムプロセスのOwningProcessなど）には、管理者としてPowerShellを実行する必要がある場合があります
- **IPv4/IPv6**: このコマンドレットはIPv4とIPv6の両方の接続を処理します
- **結果のエクスポート**: `Export-Csv`で出力をファイルに保存：
  ```powershell
  Get-NetTCPConnection | Export-Csv -Path "tcp_connections.csv" -NoTypeInformation
  ```

詳細については、以下を実行：
```powershell
Get-Help Get-NetTCPConnection -Full
```

特定の例が必要な場合や特定のユースケースがある場合は、お知らせください！