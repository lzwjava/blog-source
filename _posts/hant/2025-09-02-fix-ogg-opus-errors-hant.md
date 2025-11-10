---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 輕鬆修復 OGG Opus 解碼錯誤
translated: true
type: note
---

簡短回答：請勿在 `ExplicitDecodingConfig` 中設定 `audio_channel_count`（或 `sample_rate_hertz`）來處理 OGG/Opus 檔案。這正是導致 v2 出現以下錯誤的原因：

```
explicit_decoding_config.audio_channel_count: audio_channel_count 超出範圍
```

## 需要修改的內容（程式碼）

在你的 `.ogg` 分支中，建立配置時**不要**指定聲道數/取樣率，讓服務自行推斷：

```python
if file_extension == "ogg":
    # 僅保留編碼格式；讓 STT 自行推斷取樣率/聲道數。
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

> 如果你**確切知道**檔案是立體聲/48 kHz Opus 格式，可以設定 `sample_rate_hertz=48000` 和 `audio_channel_count=2`。否則，請省略這兩項參數——不要猜測。

---

## 是否需要使用 ffmpeg 進行預處理？

如果上述修改有效，則無需預處理。但如果仍然出現解碼問題（混合串流、異常容器格式、可變聲道數），轉碼成「標準」格式能讓批次 API 更穩定運行。以下兩種方式皆可安全使用：

### 選項 A：FLAC（無損格式，首選）

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a flac haifeng_and_zhiwei.flac
```

### 選項 B：Linear16 WAV（無損格式）

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a pcm_s16le haifeng_and_zhiwei.wav
```

然後將轉換後的檔案上傳至相同 GCS 儲存桶，並使用 **`auto_decoding_config`** 執行（FLAC/WAV 無需明確解碼設定）：

```python
# 適用於 .flac 或 .wav
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

## 快速檢查事項

* 請確保語言標籤符合有效的 BCP-47 標準。對於普通話可使用 `"cmn-CN"` 或 `"cmn-Hans-CN"`。
* 保持檔案名稱簡潔（使用 ASCII 字元），避免容器中繼資料異常。
* 若需在決策前確認聲道數/取樣率，可使用以下指令檢查：

  ```bash
  ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,channels,sample_rate -of default=nw=1 haifeng_and_zhiwei.ogg
  ```

**最終建議：** 先嘗試移除 `audio_channel_count`（及 `sample_rate_hertz`）。若仍失敗，請轉碼為 FLAC/WAV 格式並切換至 `auto_decoding_config`。