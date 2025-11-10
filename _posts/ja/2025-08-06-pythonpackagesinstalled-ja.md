---
audio: false
generated: true
image: false
lang: ja
layout: post
title: インストール済みPythonパッケージ
translated: true
type: note
---

これらはすべてインストールされるPythonパッケージ（wheel）です。以下に各パッケージの簡単な概要を示します：

* **safetensors**: pickleのセキュリティ問題なしにテンソルデータを保存/読み込みするための高速で安全なファイル形式
* **typer**: Pythonの型ヒントを使ってCLIアプリケーションを構築するためのモダンなライブラリ
* **shellingham**: 使用中のシェル（bash、zshなど）を検出するユーティリティ
* **uvicorn**: Pythonウェブアプリ（FastAPIなど）をホストするための高速なASGIサーバー
* **httptools**: 低レベルHTTPパースライブラリ。Uvicornなどのサーバーで速度向上のために使用
* **uvloop**: Cythonで実装された超高速asyncioイベントループ。asyncioの代替品として使用可能
* **watchfiles**: ファイルシステムの変更時にアクション（自動リロードなど）をトリガーできるファイル監視ライブラリ
* **airportsdata**: 空港コード、名称、所在地のシンプルな参照テーブル
* **astor**: Python ASTをソースコードに変換するツール（およびその逆）
* **blake3**: BLAKE3暗号ハッシュアルゴリズムのPythonバインディング
* **cloudpickle**: Pythonオブジェクトの拡張ピックラー。標準ライブラリのpickleより多くの型を処理
* **cupy_cuda12x**: CUDA 12.x用のNumPy互換GPU配列ライブラリ
* **fastrlock**: Python用の非常に高速な再入可能ロック実装
* **diskcache**: Pythonオブジェクトを効率的に永続化するディスクバックアップキャッシュライブラリ
* **einops**: 表現力豊かで読みやすいテンソルの形状変更と並べ替え操作
* **importlib_metadata**: 実行時のパッケージメタデータ（バージョン、エントリーポイント）へのアクセス（旧Python用バックポート）
* **zipp**: ZIPアーカイブ用のpathlibスタイルインターフェース。importlib_metadataで使用
* **msgspec**: 高性能メッセージシリアライゼーション/デシリアライゼーション（JSON、Msgpackなど）
* **nest_asyncio**: asyncioイベントループのネストを可能にする（ノートブック実行用など）
* **ninja**: NinjaビルドシステムのPythonバインディング（高速、インクリメンタルビルド）
* **partial_json_parser**: 大規模または不正なJSON用のストリーミング/部分JSONパーサー
* **py_cpuinfo**: CPUの詳細情報（モデル、コア数、周波数）を収集
* **python_json_logger**: Pythonのロギングモジュール用JSONフォーマッタ
* **pyzmq**: ZeroMQ高性能メッセージングライブラリのPythonバインディング
* **scipy**: コア科学計算ライブラリ（最適化、積分、統計など）
* **outlines_core**: 「outlines」ライブラリ用コアユーティリティ（文書のアウトライン/構造を処理）
* **xformers**: Metaによる効率的でモジュラーなトランスフォーマー（アテンション）実装
* **sentencepiece**: 教師なしテキストトークナイザー/デトークナイザー（NLPで一般的に使用）