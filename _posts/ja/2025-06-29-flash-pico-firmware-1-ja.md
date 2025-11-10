---
audio: false
generated: true
lang: ja
layout: post
title: UF2ファイルでFlash Picoを書き込む
translated: true
type: note
---

`RPI_PICO-20250415-v1.25.0.uf2`ファイルをRaspberry Pi Pico（`/media/lzw/RPI-RP2`にマウントされている）に書き込むには、次のコマンドを使用します：

```bash
cp ~/Downloads/RPI_PICO-20250415-v1.25.0.uf2 /media/lzw/RPI-RP2/
```

### 説明
- `cp`: ファイルをコピーします
- `~/Downloads/RPI_PICO-20250415-v1.25.0.uf2`: Downloadsディレクトリ内の`.uf2`ファイルへのパス
- `/media/lzw/RPI-RP2/`: Picoの`RPI-RP2`ドライブのマウントポイント（出力に表示されている通り）

### コマンド実行後
- `.uf2`ファイルがPicoにコピーされ、デバイスは自動的にファームウェアの書き込みを開始します
- 書き込みが完了すると、`RPI-RP2`ドライブはアンマウント（消える）され、成功を示します
- ドライブが再表示される場合は、書き込みが失敗した可能性があります。`.uf2`ファイルが有効か確認するか、別のUSBケーブル/ポートをお試しください

問題が発生した場合やさらにサポートが必要な場合は、お知らせください！