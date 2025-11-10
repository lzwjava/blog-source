---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Pythonシークレットによる安全な乱数生成
translated: true
type: note
---

### `secrets`モジュールの紹介
`secrets`モジュール（Python 3.6で導入）は標準ライブラリの一部であり、暗号論的に強力な乱数生成へのアクセスを提供します。シミュレーションやゲームに適した`random`モジュールとは異なり、`secrets`はパスワード、トークン、シークレットの生成などのセキュリティ関連タスク向けに設計されており、オペレーティングシステムの暗号論的に安全な乱数生成器（例：Unix系システムでの`/dev/urandom`）を使用します。

使用するには、単純にインポートします：
```python
import secrets
```

### 主な関数と使用法
以下は`secrets`の主な関数と、簡単な説明と例です。これらは予測が困難なランダムな値を生成します。

| 関数 | 目的 | 使用例 |
|----------|---------|---------------|
| `secrets.token_bytes(n)` | `n`個のランダムなバイトを生成します。バイナリキーの作成に有用です。 | `key = secrets.token_bytes(16)`  # 16個のランダムなバイト |
| `secrets.token_hex(n)` | `n`個のランダムなバイトを生成し、16進数文字列として返します（16進数エンコーディングにより`n`の2倍の長さになります）。16進数トークンに最適です。 | `hex_key = secrets.token_hex(16)`  # 32文字の16進数文字列 |
| `secrets.token_urlsafe(n)` | `n`個のランダムなバイトを生成し、URL-safeなbase64エンコードを行います（例：ウェブトークンで使用）。 | `url_token = secrets.token_urlsafe(32)`  # 約43文字の文字列 |
| `secrets.randbelow(n)` | 0から`n-1`までのランダムな整数を返します（両端を含む）。`random.randint`の安全な代替です。 | `num = secrets.randbelow(100)`  # 0から99のランダムな整数 |
| `secrets.choice(seq)` | 空でないシーケンス`seq`からランダムな要素を返します。`random.choice`の安全な代替です。 | `item = secrets.choice(['a', 'b', 'c'])`  # リストからランダム選択 |

### 実用的な例
1. **安全なパスワードの生成**:
   `secrets.choice`と文字列定数を組み合わせてランダムなパスワードを生成します。
   ```python
   import string
   import secrets

   alphabet = string.ascii_letters + string.digits + string.punctuation
   password = ''.join(secrets.choice(alphabet) for _ in range(12))
   print(password)  # 例: "X8f#9L&pW2c%"
   ```

2. **APIトークンの作成**:
   ウェブセーフなランダム文字列に`token_urlsafe`を使用します。
   ```python
   token = secrets.token_urlsafe(32)
   print(token)  # 例: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
   ```

3. **ゲームやシミュレーションでのランダム選択（セキュリティ考慮）**:
   ```python
   winners = secrets.choice(['Alice', 'Bob', 'Charlie'])
   print(f"Winner: {winners}")
   ```

### ベストプラクティスと注意点
- **セキュリティ上の理由**: `secrets`は予測可能性を回避し、攻撃に対する耐性があります。パスワードやトークンに`random`を使用しないでください。シード設定や予測が可能です。
- **パフォーマンス**: `random`よりも呼び出しが遅くなる場合がありますが、セキュリティが重要なコードでは問題ありません。重要でないタスクでのループ内での過度な使用は避けてください。
- **エッジケース**: `secrets.choice`は空のシーケンスに対して`ValueError`を発生させます。`randbelow(0)`は`ValueError`を発生させます。
- **依存関係**: 外部ライブラリは必要ありません。組み込みです。
- 詳細については、[公式Pythonドキュメント](https://docs.python.org/3/library/secrets.html)を確認してください。特定のユースケースがある場合は、より適切なアドバイスのために詳細なコンテキストを提供してください！