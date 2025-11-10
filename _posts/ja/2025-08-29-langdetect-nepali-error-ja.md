---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 言語検出がテキストをネパール語と誤判定
translated: true
type: note
---

ああ、なるほど — ご説明ありがとうございます。

貼り付けていただいたログでは：

```
Debug: raw langdetect output: [('ne', 0.9999953270916105)]
Debug: normalized langdetect output: [('ne', 0.9999953270916105)]
Debug: Detected languages: [('ne', 0.9999953270916105)]
```

ここでの **`ne` はフランス語の単語ではありません** — これは実際には `langdetect` によって出力された**言語コード**です。

`langdetect` ライブラリは、**ネパール語** の ISO 639-1 コードとして、時々 `"ne"` を返します。

* `"en"` = 英語
* `"fr"` = フランス語
* `"hi"` = ヒンディー語
* `"ne"` = ネパール語

したがってこのケースでは、`langdetect` はあなたのテキストを確率 `~0.99999` でネパール語であると判断しました。

これが、あなたのバリデーションが以下のエラーで失敗した理由です：

```
Translated text does not contain the target language 'hi' (detected: [('ne', 0.9999953270916105)])
```

👉 まとめ：

* ここでの `ne` = **ネパール語** の ISO 言語コードであり、フランス語の否定語 `"ne"` ではありません。
* これは `langdetect` があなたの入力テキストをネパール語のように見えると判断した場合に表示されます。

予期しない言語が検出された場合にあなたのバリデータが問題を起こさないように、`ne` (ネパール語) を `_map_target_code` で**正規化または再マップ**する方法をお見せしましょうか？