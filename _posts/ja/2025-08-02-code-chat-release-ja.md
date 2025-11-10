---
audio: false
generated: true
image: false
lang: ja
layout: post
title: VS CodeのCopilotチャットコマンド
translated: true
type: note
---

Visual Studio Code（VS Code）で `code chat "hi"` コマンドを使用して GitHub Copilot チャットウィンドウを開く機能は、GitHub Copilot Chat とその関連機能（チャットビューや関連コマンドなど）のより広範な統合に関連しています。入手可能な情報に基づく分析は以下の通りです。

### `code chat` コマンドのリリース
`code chat` コマンドは、提供されている VS Code のリリースノートで明示的に言及されていませんが、GitHub Copilot Chat の機能と密接に関連しており、この機能は複数の VS Code リリースにわたって段階的に強化されてきました。このコマンドは、Copilot Chat ビューまたはインラインチャットを起動するためのエイリアスまたは短縮形である可能性が高いです。Copilot Chat 機能の導入により、これらの機能は特に注目されるようになりました。

- **GitHub Copilot Chat 統合**: チャットビューを含む Copilot Chat 機能は、2023年8月頃（VS Code バージョン 1.82）からのリリースで本格的に開発、強調され始め、バージョン 1.99（2025年3月）を含むその後のバージョンを通じて進化を続けました。`Chat: Open Chat` やインラインチャットコマンドなどのチャットビューおよび関連コマンドは、この期間中に導入され、改良されました。[](https://code.visualstudio.com/updates/v1_93)[](https://code.visualstudio.com/updates/v1_86)
- **コマンドパレットとチャットコマンド**: 2024年11月リリース（バージョン 1.96）までに、VS Code はチャットビューから Copilot Edits への移動や、チャットビューでのコンテキスト処理の改善などの機能を導入しており、チャット関連コマンドに対する堅牢なサポートを示していました。コマンドパレットからのコマンドで Copilot Chat をトリガーする機能はすでに整っており、`code chat` コマンドはこれらの機能強化の一環として登場した可能性が高いです。[](https://code.visualstudio.com/updates/v1_96)
- **バージョン 1.99.2 に関して**: 2025年3月リリース（バージョン 1.99）およびその更新（1.99.2 および 1.99.3）では、`code chat "hi"` コマンドについては明示的に言及されていません。しかし、カスタムチャットモード、エージェントモード、改善されたコンテキスト処理など、Copilot Chat エクスペリエンスの進歩について議論しており、この時期までにチャット関連コマンドが十分にサポートされていたことを示唆しています。明示的に文書化されていない `code chat` コマンドは、Copilot Chat とのコマンドパレットの統合の一部として、おそらく利用可能であったでしょう。[](https://code.visualstudio.com/updates/v1_99)

### `code chat "hi"` 機能はいつリリースされたか？
`code chat "hi"` コマンドの正確なリリース時期は提供されたノートでは特定されていませんが、Copilot Chat 機能が成熟した状態にあった2025年3月リリース（バージョン 1.99）頃、またはそれ以前には利用可能であったと推論するのが妥当です。このコマンドは、バージョン 1.96（2024年11月）までに `Chat: Open Chat` や `Open Quick Chat` などのコマンドで確立されていた、チャットビューを開くための既存のインフラストラクチャを活用している可能性が高いです。[](https://code.visualstudio.com/updates/v1_96)[](https://code.visualstudio.com/updates/v1_93)

- **最も早い可能性のあるリリース**: Quick Chat やコンテキストの改善などの機能を備えた Copilot Chat 機能は、2024年8月（バージョン 1.93）までに本格的に開発されました。`code chat` コマンドは、この時期前後、または Copilot とのコマンドパレット統合の一環としてその後まもなく導入された可能性があります。[](https://code.visualstudio.com/updates/v1_93)
- **1.99.2 での確認**: バージョン 1.99.2（2025年3月）までに、Copilot Chat システムは、カスタムモード、エージェントモード、`#codebase` のようなコンテキスト変数のサポートを備えて成熟していました。"hi" のようなプロンプトでチャットビューを開く `code chat "hi"` コマンドは、チャット機能が高度な状態にあったことを考慮すると、コマンドパレットの標準コマンドとしてサポートされていた可能性が高いです。[](https://code.visualstudio.com/updates/v1_99)

### 結論
Copilot Chat ウィンドウを開く `code chat "hi"` コマンドは、2025年3月リリース（バージョン 1.99）頃、またはおそらく Copilot Chat 機能が大幅に強化された2024年8月（バージョン 1.93）という早い時期から利用可能であった可能性が高いです。バージョン 1.99.2 に関しては、この時点でチャットビューと関連コマンドが十分に統合されていたため、このコマンドはほぼ確実に機能するでしょう。正確な確認が必要な場合は、VS Code 1.99.2 のコマンドパレットで `code chat` と入力し、有効なコマンドとして表示されるかどうかを確認できます。

**参考文献**:
- 2025年3月 (バージョン 1.99) - code.visualstudio.com[](https://code.visualstudio.com/updates/v1_99)
- 2024年11月 (バージョン 1.96) - code.visualstudio.com[](https://code.visualstudio.com/updates/v1_96)
- 2024年8月 (バージョン 1.93) - code.visualstudio.com[](https://code.visualstudio.com/updates/v1_93)