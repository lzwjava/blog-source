---
audio: false
generated: true
image: false
lang: ja
layout: post
title: OpenAIに学ぶPythonライブラリ設計の教訓
translated: true
type: note
---

`openai/openai-python` の簡単な内部解析と、優れた Python ライブラリを構築するために活用できる教訓をご紹介します。

# リポジトリが示すもの（一目で）

* **明確な「src レイアウト」**: コードは `src/openai`、トップレベルに `tests/`, `examples/`, `scripts/`, `.github/`, `pyproject.toml`, `mypy.ini`, `noxfile.py` など。この分離により、インポートパスが整理され、テストの発見が予測可能になる。（[GitHub][1]）
* **型付けされた公開サーフェス**: リクエストは `TypedDict` を使用、レスポンスは **Pydantic** モデル。優れた DX と安全なリファクタリングを実現。（[GitHub][1]）
* **同期 + 非同期の同等性**: `OpenAI` と `AsyncOpenAI` は同じ API を共有。デフォルトのトランスポートは `httpx`、オプションで `aiohttp`。（[GitHub][1]）
* **ファーストクラスのストリーミング**: Server-Sent Events を同期・非同期の両方でシンプルなイテレーションとして扱える。（[GitHub][1]）
* **自動ページネーション**: ユーザーが自前でページループを書かなくてよいように、リストエンドポイントをイテラブルに。（[GitHub][1]）
* **リアルタイム/WebSocket クライアント**: オプトインのサブクライアントとして、例とエラーハンドリングのガイダンスを提供。（[GitHub][1]）
* **コード生成パイプライン**: SDK は OpenAPI 仕様から (Stainless 経由で) 生成され、一貫性と型カバレッジを強制。（[GitHub][1]）

# 再利用可能な設計上の要点

* **「一つの明白な方法」を保つ**: 単一の `Client` (と `AsyncClient`) を公開し、メソッド名を同じにする。ユーザーが「どのクラスを使うべき？」と迷わないように。OpenAI SDK は `OpenAI` と `AsyncOpenAI` でこれを示している。（[GitHub][1]）
* **移植可能なトランスポート**: デフォルトは `httpx` だが、交換可能な HTTP バックエンド (例: `aiohttp`) を許可し、高並行性ユーザーを閉じ込めない。（[GitHub][1]）
* **型付けされたリクエスト + モデル**: 型付けされたリクエストペイロードとリッチなレスポンスモデルを提供。これにより、エディタのオートコンプリート、リンターでチェック可能な例、安全な破壊的変更が可能になる。（[GitHub][1]）
* **摩擦のないストリーミング**: ストリーミングをプレーンなイテレータ / 非同期イテレータとして設計。カスタムイベントポンプは不要。（[GitHub][1]）
* **イテレータベースのページネーション**: `for item in client.resource.list(limit=...)` を公開し、ページを遅延読み込みする。ユーザーコードを小さく保ちながら効率的。（[GitHub][1]）
* **サブシステムはサブクライアントとして**: 特殊な機能 (例: リアルタイム) は、明確な名前空間 (`client.beta.realtime`) の背後に配置し、主要なサーフェスを整理された状態に保つ。（[GitHub][1]）
* **役立つ場合は生成する**: API が仕様駆動である場合、コード生成に退屈で厳密な型付けの層を作成させ、人間工学に基づいた部分は手作業で作成する。（[GitHub][1]）

# コピー可能なスケルトン

```bash
yourlib/
  pyproject.toml
  noxfile.py
  mypy.ini
  README.md
  CHANGELOG.md
  SECURITY.md
  src/yourlib/
    __init__.py
    _version.py
    _types.py            # TypedDicts, enums
    _errors.py           # 例外階層
    _http.py             # httpx クライアントラッパー、リトライ、タイムアウト
    _pagination.py       # 汎用 Pager[T]
    client.py            # Client + AsyncClient, 認証, ベース URL
    resources/
      __init__.py
      widgets.py         # リソースグループ (同期+非同期メソッド)
    streaming.py         # SSE ヘルパー (同期/非同期)
  tests/
    test_client.py
    test_widgets.py
  examples/
    quickstart.py
    async_quickstart.py
```

## 公開 API (`src/yourlib/__init__.py`)

* ユーザーが必要なものだけを再エクスポート:

```python
from .client import Client, AsyncClient
from ._errors import YourLibError, APIError, RateLimitError
__all__ = ["Client", "AsyncClient", "YourLibError", "APIError", "RateLimitError"]
```

## クライアントの形状 (同期 & 非同期)

* 同じメソッド名を維持。`await`/`async` の有無のみが異なる:

```python
# src/yourlib/client.py
import httpx
from .resources.widgets import Widgets
from ._http import HttpTransport

class Client:
    def __init__(self, api_key=None, base_url="https://api.example.com", http_client=None):
        self._transport = HttpTransport(api_key, base_url, http_client or httpx.Client(timeout=30))
        self.widgets = Widgets(self._transport)

class AsyncClient:
    def __init__(self, api_key=None, base_url="https://api.example.com", http_client=None):
        self._transport = HttpTransport(api_key, base_url, http_client or httpx.AsyncClient(timeout=30))
        self.widgets = Widgets(self._transport)
```

## ページネーションパターン

```python
# src/yourlib/_pagination.py
from typing import AsyncIterator, Iterator, Generic, TypeVar, Callable, Optional
T = TypeVar("T")
class Pager(Generic[T]):
    def __init__(self, fetch: Callable[..., dict], limit: int = 100):
        self._fetch = fetch
        self._limit = limit
        self._cursor = None
    def __iter__(self) -> Iterator[T]:
        while True:
            page = self._fetch(limit=self._limit, cursor=self._cursor)
            for item in page["data"]:
                yield item
            self._cursor = page.get("next_cursor")
            if not self._cursor:
                break
```

ユーザーが `for item in client.widgets.list(limit=50): ...` と書けるように公開する。(OpenAI の SDK も同じアプローチを取っている。（[GitHub][1]))

## ストリーミングパターン (SSE)

* `httpx` のストリーミングを、イベントを yield する小さなイテレータでラップ。非同期バリアントも同様に作成する。これにより、OpenAI SDK に見られる `for event in client.responses.create(..., stream=True)` という人間工学に基づいた UX が実現される。（[GitHub][1]）

# スケールするツーリング & リリースフロー

* **`pyproject.toml` (PEP 621)** でメタデータを管理。開発依存関係は別途固定。
* **型チェック**: 型を同梱し、CI で `mypy` を実行 (彼らのリポジトリには `mypy.ini` がある)。（[GitHub][1]）
* **タスクランナー**: テスト、lint、型チェック、ビルドのための `nox` セッション (彼らは `noxfile.py` を使用)。（[GitHub][1]）
* **CI**: `.github/` 内の GitHub Actions で、Python バージョンとプラットフォームを跨いだテストを実行。（[GitHub][2]）
* **CHANGELOG** と **バージョニング**: 人間が読めるログを維持。リリースを自動化 (彼らは release-please を使用)。（[GitHub][1]）
* **セキュリティ & コントリビューション文書**: 報告者と貢献者のための期待値を設定。（[GitHub][1]）

# ドキュメント & 例

* **README の例** は実行可能で、コピー＆ペーストに適しているべき — 同期、非同期、ストリーミング、ページネーション、そして (`aiohttp` のような) あらゆる「特殊なトランスポート」について。OpenAI の README はそれぞれを簡潔に示している。（[GitHub][1]）
* **API リファレンス**: コード生成されている場合、`api.md`/リファレンスサイトを公開し、リリースと連携させて維持する。（[GitHub][1]）
* **Examples フォルダ**: 最小限で焦点を絞ったスクリプトと、1つの「完全な」サンプルを含める。

# エラー、リトライ、タイムアウト (実装すべきこと)

* **エラー階層**: `YourLibError` → `APIError`, `AuthError`, `RateLimitError`, `TimeoutError`。HTTP ステータスコードを例外にマッピング。リクエスト ID を含める。
* **リトライ**: べき等な操作は、429/5xx に対して指数バックオフ + ジッター付きで自動リトライする。
* **タイムアウト**: 賢明なデフォルトを設定し、クライアントレベルと呼び出し毎のレベルで設定可能にする。
* **ロギングフック**: シークレットを漏らさない構造化されたデバッグログ。

# パッケージング & 互換性

* **3–4 つのアクティブな Python マイナーバージョン** (例: 3.9–3.13) をサポートし、CI でテストする。
* **インポート時の副作用なし**。ネットワーク/クライアントの作成は初回使用時まで遅延させる。
* **環境設定**: `API_KEY` 環境変数を受け入れるが、ユーザーが明示的に資格情報を渡すことも許可する (OpenAI は `OPENAI_API_KEY` と `.env` のヒントを示している)。（[GitHub][1]）
* **安定した公開 API**: 内部は非公開 (`_module.py`) に保ち、`__init__.py` で整理されたサーフェスだけを再エクスポートする。

# 避けるべき落とし穴

* すべてを単一モジュールに詰め込むこと。リソースごとに分割し、公開インポートを安定させる。
* トランスポートタイプを漏らすこと。リソースは `httpx` に直接依存するのではなく、小さな「トランスポート」プロトコルに依存すべき。
* 非同期を二流に感じさせること。テストと例で両方を同等にカバーすることを保証する (OpenAI の同等性は良いモデル)。（[GitHub][1]）
* ストリーミングにおいて、ユーザーにスレッドやコールバックの操作を強制しないこと — イテレータの方がシンプル。（[GitHub][1]）

必要であれば、具体的なドメイン (例えば、内部 REST サービス向けの型付けされたクライアントで、同期/非同期、ページネーション、ストリーミングを備えたもの) に対してこの構造を足場として用意し、すぐに実行可能な `nox`、CI、およびサンプルスクリプトを組み込むことができます。

[1]: https://github.com/openai/openai-python "GitHub - openai/openai-python: The official Python library for the OpenAI API"
[2]: https://github.com/openai/openai-python/tree/main/.github "openai-python/.github at main · openai/openai-python · GitHub"