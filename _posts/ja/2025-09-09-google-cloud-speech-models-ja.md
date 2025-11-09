---
audio: false
date: 2025-09-09
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Google Cloud音声テキスト変換モデルの比較
translated: true
type: note
---

Google CloudのSpeech-to-Text API V2における各種モデルの違いを、モデルファミリーとユースケース別に分かりやすく整理しました（表を使用せず読みやすくしています）：

---

## Chirpファミリー（Universal Speech Models - USM）

### **`chirp`**

* **概要**: GoogleのオリジナルUniversal Speech Model (USM)。非ストリーミングコンテキストで多様な多言語書き起こしをサポート。([Google Cloud][1])
* **使用方法**: 同期（`Recognize`）およびバッチ（`BatchRecognize`）メソッドで動作。ストリーミングは**サポートされていません**。([Google Cloud][1])
* **制限事項**:

  * ストリーミング非サポート
  * 信頼度スコア、話者分離、適応、強制正規化、単語レベルの信頼度が未対応([Google Cloud][1])

### **`chirp_2`**

* **概要**: 次世代Universal Speech Model。オリジナルより高精度かつ効率的。ストリーミング、同期、バッチ処理をサポート。多言語書き起こしと翻訳、モデル適応を提供。([Google Cloud][2], [Medium][3])

### **`chirp_3`**

* **概要**: 最新世代。精度と速度がさらに向上。ストリーミング、同期、バッチ認識に加え、話者分離、自動言語検出をサポート。([Google Cloud][4])
* **機能サポート**:

  * ストリーミング（`StreamingRecognize`）、同期（`Recognize`）、バッチ（`BatchRecognize`）すべてサポート([Google Cloud][4])
  * 話者分離と言語検出をサポート([Google Cloud][4])
  * 単語レベルのタイムスタンプと適応は非サポート([Google Cloud][4])

---

## レガシー／汎用モデル

これらは主に下位互換性のために維持されている旧式アーキテクチャのモデルです：

* **`long`**: メディアコンテンツや自然な会話などの長いコンテンツ向け。([Google Cloud][2])
* **`short`**: 数秒程度の非常に短い発話に最適化（コマンド入力に理想的）。([Google Cloud][2])
* **`telephony` / `telephony_short`**: 電話通話オーディオ（通常8kHz）向けに調整。「short」バリアントは短い発話や単語単位の発話を処理。([Google Cloud][2])
* **医療モデル**:

  * `medical_conversation`: 医療提供者と患者間の対話向け（話者分離対応）。
  * `medical_dictation`: 単一話者による口述筆記向け。([Google Cloud][2])

---

## ユースケース別モデル差異まとめ

* **非ストリーミング・多言語で最高精度が必要？** → **`chirp`**
* **ストリーミングサポート＋多言語＋適応が必要？** → **`chirp_2`**
* **ストリーミング、話者分離、自動言語検出、最高精度が欲しい？** → **`chirp_3`**
* **単純な長いコンテンツの書き起こしのみ？** → **`long`**
* **短い音声コマンドを処理？** → **`short`**
* **電話通話録音？** → **`telephony`** または **`telephony_short`**
* **医療ユースケース？** → **`medical_conversation`** または **`medical_dictation`**

---

## Googleドキュメンテーションからの補足

Googleの「文字起こしモデルの選択」ページ（2025年9月4日更新）には、上記のすべてのモデル識別子と説明が含まれています。また、レガシーモデルは積極的にはメンテナンスされていないが、下位互換性のために保持されていることも記載されています。([Google Cloud][2])

「latest\_long」/「latest\_short」に関する以前の記述は、別のConformerベースのモデルセットを指していますが、これらはChirp系統外のものであり、Chirpまたはレガシーモデルに焦点を当てている場合は関連しません。([Google Cloud][5])

---

## 要約 - 選択方法：

* **最高品質 + 新機能（話者分離、ストリーミングなど）が必要** → **`chirp_3`**
* **ストリーミング & モデル適応サポートが必要** → **`chirp_2`**
* **非ストリーミング多言語ベースライン** → **`chirp`**
* **短い発話、長いオーディオ、電話、医療向け** → 適切なレガシーモデルを使用（`short`、`long`、`telephony`、`medical_*`）

---

ご利用のオーディオタイプ、言語、ストリーミング vs バッチ処理の必要性に基づいて適切なモデルを選択するお手伝いが必要でしたら、お知らせください！

[1]: https://cloud.google.com/speech-to-text/v2/docs/chirp-model?utm_source=chatgpt.com "Chirp: Universal speech model"
[2]: https://cloud.google.com/speech-to-text/v2/docs/transcription-model?utm_source=chatgpt.com "Select a transcription model - Cloud Speech-to-Text"
[3]: https://medium.com/google-cloud/transcribe-everything-everywhere-all-at-once-with-chirp-2-615ac362947d?utm_source=chatgpt.com "Transcribe everything everywhere all at once with Chirp 2"
[4]: https://cloud.google.com/speech-to-text/v2/docs/chirp_3-model?utm_source=chatgpt.com "Chirp 3 Transcription: Enhanced multilingual accuracy"
[5]: https://cloud.google.com/speech-to-text/docs/latest-models?utm_source=chatgpt.com "Introduction to Latest Models | Cloud Speech-to-Text ..."