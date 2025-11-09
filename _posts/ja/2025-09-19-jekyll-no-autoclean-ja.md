---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Jekyllビルドに自動クリーン機能が不足
translated: true
type: note
---

Jekyll自体には`--replace`や`--refresh`フラグはありません。各`jekyll build`実行時には、指定した`--destination`フォルダに生成されたファイルが書き込まれ（または上書きされ）ますが、**ソース内に存在しなくなった古いファイルは自動的には削除されません**。つまり、古くなったファイルが残り続ける可能性があります。

クリーンなビルド出力を得たい場合は、`jekyll build`を実行する前に出力先ディレクトリを自分でクリアする必要があります。一般的な2つの方法：

**1. スクリプト内での手動クリーンアップ**
`jekyll build`を呼び出す前に、出力先ディレクトリを削除：

```python
import shutil

def run_jekyll(destination: str, extra_args: list[str]) -> int:
    # 古いファイルを削除
    dest_path = Path(destination)
    if dest_path.exists():
        shutil.rmtree(dest_path)

    command = [
        "jekyll",
        "build",
        "--destination",
        destination,
        *extra_args,
    ]
    completed = subprocess.run(command, check=False)
    return completed.returncode
```

**2. Jekyllの`_site`を使用する**
カスタムの`--destination`ではなく、プロジェクトルート下のデフォルトの`_site`をJekyllに使用させる場合、`jekyll clean`を使用してビルド前に出力を削除できます：

```bash
jekyll clean && jekyll build
```

ただし`jekyll clean`はカスタムフォルダではなく`_site`のみを認識します。

---

まとめ：

* `--replace`機能は組み込まれていません
* スクリプト内でカスタム出力先を使用している場合、新しい出力が必要な場合はビルド前に明示的に削除する必要があります

スクリプトに`--clean`オプション（`jekyll clean`のように）を追加して、ビルド前に自動的に出力先をクリアするように調整しましょうか？