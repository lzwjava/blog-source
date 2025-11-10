---
audio: false
generated: true
image: false
lang: ja
layout: post
title: OGG Opusデコードエラーの簡単な修正方法
translated: true
type: note
---

短い回答: OGG/Opus の場合、`ExplicitDecodingConfig` で `audio_channel_count`（または `sample_rate_hertz`）を設定**しないでください**。これが v2 で以下のエラーを引き起こす原因です:

```
explicit_decoding_config.audio_channel_count: audio_channel_count is out of range
```

## 変更点 (コード)

あなたの `.ogg` ブランチで、サービスがチャンネル数/サンプルレートを推論できるように、これらを**含めずに**設定を構築してください:

```python
if file_extension == "ogg":
    # エンコーディングのみ保持。レートとチャンネル数は STT に推論させる。
    decoding = cloud_speech.ExplicitDecodingConfig(
        encoding=cloud_speech.ExplicitDecodingConfig.AudioEncoding.OGG_OPUS
    )
    config = cloud_speech.RecognitionConfig(
        explicit_decoding_config=decoding,
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
    )
else:
    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
    )
```

> ファイルがステレオ/48 kHz Opus であることを**確実に知っている**場合のみ、`sample_rate_hertz=48000` と `audio_channel_count=2` を設定しても構いません。それ以外の場合は、両方とも省略してください―推測しないでください。

---

## ffmpeg で前処理すべきですか？

上記の変更で動作する場合は、必要ありません。しかし、依然としてデコードに関する不具合（混合ストリーム、奇妙なコンテナ、可変チャンネルなど）が見られる場合は、退屈なフォーマットにトランスコードすることで、バッチ API は非常に快適に動作します。以下のいずれかが安全です:

### オプション A: FLAC (ロスレス、推奨)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a flac haifeng_and_zhiwei.flac
```

### オプション B: Linear16 WAV (ロスレス)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a pcm_s16le haifeng_and_zhiwei.wav
```

その後、そのファイルを同じ GCS バケットにアップロードし、**`auto_decoding_config`** を使用して実行してください（FLAC/WAV では明示的なデコードは不要です）:

```python
# .flac または .wav の場合
config = cloud_speech.RecognitionConfig(
    auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
    features=cloud_speech.RecognitionFeatures(
        enable_word_confidence=True,
        enable_word_time_offsets=True,
    ),
    model="long",
    language_codes=[language_code],
)
```

---

## 簡単なサニティチェック

* 言語タグが有効な BCP-47 形式であることを確認してください。北京語の場合は `"cmn-CN"` または `"cmn-Hans-CN"` を使用できます。
* 奇妙なコンテナメタデータを避けるため、ファイル名はシンプルな（ASCII）ものに保ってください。
* 決定する前にチャンネル数/サンプルレートを確認したい場合は、以下で検査できます:

  ```bash
  ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,channels,sample_rate -of default=nw=1 haifeng_and_zhiwei.ogg
  ```

**結論:** まず `audio_channel_count`（および `sample_rate_hertz`）を削除してみてください。それでも失敗する場合は、FLAC/WAV にトランスコードし、`auto_decoding_config` に切り替えてください。