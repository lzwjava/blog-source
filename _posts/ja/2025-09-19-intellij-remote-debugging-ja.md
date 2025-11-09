---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: IntelliJリモートデバッグ設定ガイド
translated: true
type: note
---

短い答え: はい — ビルドと実行中のJVMを同期させておけば、IntelliJのリモートデバッグは問題なくアタッチできます。以下に、Libertyのローカル環境とCloud Foundryで動作する確実で手間のかからない方法を紹介します。

## 1) アタッチ前に「クラスの不一致」を防ぐ

* 常にJDKを揃える: Mavenコンパイル、LibertyのJVM、（CF上の場合）JavaビルドパックのJDKがメジャーバージョンで一致している必要があります。Mavenでは、`maven-compiler-plugin`（`release`または`source/target`）で固定し、Liberty/CFが同じバージョンを使用するようにします。
* ブランチの切り替えやモジュールのオンオフ時に古いバイトコードをクリーンする: `mvn clean package -DskipTests`が最も簡単な予防策です。
* IntelliJでは、以前にIDEビルドとMavenビルドを混在させていた場合は、一度「Rebuild Project」を実行してください。

## 2) 必要な時だけ自動リビルド（30分ルール）

コンパイルされたクラスが30分以上古い場合にのみリビルドしたい場合は、Mavenを小さなチェックでラップします。

### Bash (macOS/Linux)

```bash
#!/usr/bin/env bash
set -euo pipefail

CLASSES_DIR="target/classes"
THRESHOLD_MIN=30

needs_build() {
  # クラスがまだない？
  [[ ! -d "$CLASSES_DIR" ]] && return 0
  # 最新のクラスの修正時刻が閾値より古い？
  last_mod_epoch=$(find "$CLASSES_DIR" -type f -name '*.class' -printf '%T@\n' 2>/dev/null | sort -n | tail -1)
  [[ -z "${last_mod_epoch:-}" ]] && return 0
  now_epoch=$(date +%s)
  diff_min=$(( ( now_epoch - ${last_mod_epoch%.*} ) / 60 ))
  (( diff_min >= THRESHOLD_MIN ))
}

if needs_build; then
  echo "Classes are old (>= ${THRESHOLD_MIN}m) or missing — building…"
  mvn clean package -DskipTests
else
  echo "Classes are fresh (< ${THRESHOLD_MIN}m) — skipping build."
fi
```

### PowerShell (Windows)

```powershell
$classes = "target\classes"
$thresholdMin = 30

function Needs-Build {
  if (-not (Test-Path $classes)) { return $true }
  $last = Get-ChildItem $classes -Recurse -Filter *.class |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1
  if (-not $last) { return $true }
  $age = (New-TimeSpan -Start $last.LastWriteTime -End (Get-Date)).TotalMinutes
  return ($age -ge $thresholdMin)
}

if (Needs-Build) {
  Write-Host "Classes are old (>= $thresholdMin m) or missing — building…"
  mvn clean package -DskipTests
} else {
  Write-Host "Classes are fresh (< $thresholdMin m) — skipping build."
}
```

## 3) Liberty (ローカル) — デバッグモードで起動し、IntelliJからアタッチ

2つの簡単なオプションがあります:

**A. ワンショットのデバッグ起動**

```bash
server debug myServer   # デフォルトのJDWPポートは7777
```

**B. 永続的な設定**

* `wlp/usr/servers/myServer/jvm.options`内:

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:7777
```

* または環境変数経由:

```
WLP_DEBUG_ADDRESS=7777
WLP_DEBUG_SUSPEND=false
```

**IntelliJでのアタッチ**

* Run → 「Edit Configurations…」 → 「Remote JVM Debug」。
* Host: `localhost`, Port: `7777`。
* Debugを実行; 「Connected to the target VM…」が表示され、ブレークポイントがバインドされるはずです。

> ヒント: リビルド後、Libertyはホットスワップを通じてほとんどの機能の更新されたクラスを読み込みます。メソッドシグネチャやクラスの形状が変更された場合は、それらの変更を読み込むためにサーバーの再起動が必要です。

## 4) Cloud Foundry (PCF) — 現実的な選択肢

CFはアプリをそのルーティング層の背後で実行します；通常、JDWPポートを直接公開することはできません。実行可能なパターンは2つあります:

**オプション 1: ビルドパックデバッグ + SSHトンネル (開発/ステージング環境のみ)**

1. JavaビルドパックでJVMデバッグを有効化:

   * プッシュ前に環境変数を設定（ビルドパックのバージョンにより名前が若干異なる）:

   ```
   cf set-env <APP> JBP_CONFIG_DEBUG '{enabled: true, port: 7777}'
   ```
2. リステージ:

   ```
   cf restage <APP>
   ```
3. SSHトンネルを開く:

   ```
   cf ssh -N -L 7777:localhost:7777 <APP>
   ```
4. IntelliJで、`localhost:7777`にアタッチ。

**オプション 2: JDWPの代わりにCF SSH JMX/診断機能を使用**

* 直接JDWPが許可されていない場合、以下に頼ります:

  * アプリログ + 対象を絞ったロガー、
  * `cf ssh` + `jcmd`/`jmap`（存在する場合）によるスレッド/ヒープダンプ、
  * Libertyのトレースやヘルスエンドポイントなどの機能フラグ。

> 現実的な確認: 多くのCF組織では、本番環境でデバッグポートを無効にしています。CF上のリモートJDWPは、非本番スペースのためのデバッグ専用パスとして扱ってください。プラットフォームチームがブロックしている場合は、ログ + SSH診断にフォールバックします。

## 5) よくある「ブレークポイントをバインドできません」の原因（と修正方法）

* **クラスファイルの不一致**: クリーンリビルドを実行；ランタイムのクラスパス上にクラスのコピーが1つだけであることを確認（fat JARや重複モジュールに注意）。
* **間違ったJDWPポート**: Libertyが実際にリッスンしていることを確認（ローカルでは`server debug`ログや`netstat`；CFでは、SSHトンネルの行が一致する必要あり）。
* **異なるJDKメジャーバージョン**: Maven/Liberty/CFのJDKが同じであることを確認（例: すべてJava 17）。
* **コンパイラのデバッグ情報が剥ぎ取られている**: `maven-compiler-plugin`が`-g:none`を使用していないことを確認。デフォルトは問題なし；カスタマイズしている場合は、`-g`を含める。
* **リロードが必要**: シグネチャ変更後は、Libertyを再起動（またはCF上でリステージ）。

---

上記のように設定すれば — 常に`mvn clean package`を実行するか、「30分フレッシュネス」ラッパーのどちらか — IntelliJのリモートデバッグはLibertyに確実にアタッチし、非本番環境のCFではSSHトンネル経由で動作します。