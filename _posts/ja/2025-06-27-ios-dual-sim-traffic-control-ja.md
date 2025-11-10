---
audio: false
generated: true
lang: ja
layout: post
title: iOSでのデュアルSIMトラフィックルーティング管理とGFWの考慮事項
translated: true
type: note
---

iOSはデュアルSIM機能を使用する際に、異なる携帯データプランのネットワークトラフィックを管理・分離するためのAPIを提供していますが、制限があり、中国のグレートファイアウォール（GFW）の制限に基づいて特定のトラフィックを特定のSIMにルーティングする直接的な制御は、詳細なレベルではネイティブにサポートされていません。ただし、iOS API、手動設定、そして場合によってはサードパーティ製ツールを組み合わせることで、Macao SIMと中国電信SIMのトラフィックを異なる方法で処理するためのある程度の分離を実現できます。以下では、関連するAPI、設定、考慮事項、およびGFW関連の課題への対処方法について概説します。

### デュアルSIMとトラフィック管理のための主要なiOS APIと機能

1. **CoreTelephony Framework**:
   - **目的**: デュアルSIMデバイスのための携帯関連情報と設定へのアクセスを提供します。
   - **主要クラス**:
     - `CTCellularPlanProvisioning`: 携帯プランの追加や管理（例: eSIMや物理SIM）を可能にします。
     - `CTTelephonyNetworkInfo`: 利用可能な携帯プランとそのプロパティ（キャリア名、モバイル国コード（MCC）、モバイルネットワークコード（MNC）など）に関する情報を提供します。
     - `CTCellularData`: 携帯データの使用量とネットワーク状態（例: 携帯データが有効かどうか）を監視します。
   - **制限**: CoreTelephonyは携帯プランの照会と管理を可能にしますが、特定のアプリのトラフィックを特定のSIMにルーティングする直接的な制御は提供しません。データ用にアクティブなSIMを検出することはできますが、APIレベルで特定のトラフィック（例: 特定のアプリや宛先）をプログラムでSIMに割り当てることはできません。

2. **NetworkExtension Framework**:
   - **目的**: カスタムVPNの作成やネットワークトラフィックルールの管理など、高度なネットワーク設定を可能にします。
   - **主要機能**:
     - **NEVPNManager**: VPN接続の設定と管理を可能にし、GFWの制限を回避するために特定のサーバーを経由してトラフィックをルーティングするために使用できます。
     - **NEPacketTunnelProvider**: カスタムVPNトンネルの作成に使用され、GFWの制限を回避するためにMacao SIMを経由して特定のトラフィックをルーティングするように設定できます。
   - **GFWのユースケース**: Macao SIM（Macaoのネットワークは独立しているためGFWの検閲対象外）でVPNを設定することで、中国本土外のサーバーを経由してトラフィックをルーティングし、Google、WhatsApp、YouTubeなどのブロックされたサービスにアクセスできます。[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)
   - **制限**: VPN設定は通常、システムレベルで適用され、SIMごとには適用されません。アクティブなデータSIMを手動で切り替えるか、カスタムVPNソリューションを使用してトラフィックを選択的にルーティングする必要があります。

3. **デュアルSIM設定（設定ベース）**:
   - iOSは互換性のあるiPhone（例: iPhone XS、XR以降で、Macaoや香港などの地域で購入された、2枚のnano-SIMまたはeSIMでデュアルSIMをサポートするモデル）でデュアルSIMデュアルスタンバイ（DSDS）をサポートしています。これにより以下が可能です:[](https://support.apple.com/en-us/109317)[](https://support.apple.com/en-us/108898)
     - 携帯データのデフォルトSIMを割り当てる（設定 > 携帯 > 携帯データ）。
     - 「携帯データの切り替えを許可」を有効にして、カバレッジや利用状況に基づいてSIM間で自動的に切り替える（設定 > 携帯 > 携帯データ > 携帯データの切り替えを許可）。[](https://support.apple.com/en-us/108898)
     - SIMにラベルを付ける（例: 制限のないアクセスのための「Macao SIM」、ローカルサービスのための「中国電信」）し、特定のタスクのデータをどのSIMが処理するかを手動で選択する。
   - **手動トラフィック分離**: 設定でアクティブなデータSIMを手動で切り替えて、すべての携帯トラフィックをMacao SIM（GFWを回避するため）または中国電信SIM（GFWの対象となるローカルサービスのため）のいずれかを経由させるようにすることができます。ただし、iOSはユーザーの介入なしにアプリや宛先に基づいて動的にトラフィックを特定のSIMにルーティングするAPIを提供していません。

4. **アプリごとのVPN（NetworkExtension）**:
   - iOSは、`NetworkExtension`フレームワークの`NEAppProxyProvider`または`NEAppRule`クラスを介して、通常はエンタープライズ設定（例: 管理対象アプリ設定）で使用されるアプリごとのVPN設定をサポートしています。
   - **ユースケース**: 特定のアプリ（例: YouTube、Google）からのトラフィックを、GFWの制限を回避するためにMacao SIMのデータ接続を経由するVPNトンネルを通じてルーティングするようにアプリごとのVPNを設定でき、他のアプリはローカルサービスに中国電信SIMを使用するようにすることができます。
   - **要件**: これにはカスタムVPNアプリまたはエンタープライズのモバイルデバイス管理（MDM）ソリューションが必要であり、個人の開発者にとって実装は複雑です。さらに、VPN使用時にMacao SIMがアクティブなデータSIMに設定されていることを確認する必要があります。

5. **URLSessionとカスタムネットワーキング**:
   - `URLSession` APIでは、`allowsCellularAccess`を使用するか、特定のネットワークインターフェースにバインドすることにより、特定の携帯インターフェースでネットワークリクエストを設定できます。
   - **ユースケース**: 特定のリクエストに対して携帯アクセスを無効にしたり（Wi-Fiや他のインターフェースを強制）、トラフィックをルーティングするためにVPNを使用したりすることができます。ただし、特定のリクエストを特定のSIMの携帯インターフェースにバインドすることは直接サポートされていません。システムのアクティブなデータSIM設定に依存する必要があります。
   - **回避策**: Macao SIMのデータを使用するように設定されたVPNと組み合わせて`URLSession`を使用し、中国国外のサーバーにトラフィックをルーティングします。

### デュアルSIMによるGFW制限の処理

中国のグレートファイアウォール（GFW）は、中国電信のような本土のキャリアを使用する場合、多くの外国のウェブサイトやサービス（例: Google、YouTube、WhatsApp）へのアクセスをブロックします。それらのトラフィックは中国の検閲済みインフラを経由するためです。対照的に、Macao SIM（例: CTMまたは3 Macaoからのもの）は、Macaoの独立したネットワークを経由してトラフィックをルーティングし、これらはGFWの検閲対象外です（ただし、中国電信MacaoはGFW制限を実施します）。以下に、Macao SIMと中国電信SIMを活用する方法を示します:[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://prepaid-data-sim-card.fandom.com/wiki/China)[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)

1. **制限のないアクセスのためのMacao SIM**:
   - GFWによってブロックされたアプリやサービス（例: Google、YouTube）のために、Macao SIMをデフォルトの携帯データプランとして使用します。
   - **設定**:
     - 設定 > 携帯 > 携帯データに移動し、Macao SIMを選択します。
     - 中国本土内で使用する場合、Macao SIMのデータローミングが有効になっていることを確認します。これにより、トラフィックはMacaoのネットワークを経由し、GFWを回避します。[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)
     - 必要に応じて、（`NEVPNManager`を使用するなどして）VPNを設定してトラフィックをさらに保護することもできますが、Macao SIMは通常、ブロックされたサービスにアクセスするためにVPNを必要としません。
   - **APIサポート**: `CTTelephonyNetworkInfo`を使用して、Macao SIMがデータ用にアクティブであること（`dataServiceIdentifier`プロパティ）を確認し、その状態を監視します。

2. **ローカルサービスのための中国電信SIM**:
   - 中国の電話番号を必要とする、または本土のネットワークに最適化されたローカルアプリやサービス（例: WeChat、Alipay）のために中国電信SIMを使用します。
   - **設定**:
     - ローカルサービスにアクセスするときは、設定 > 携帯 > 携帯データで手動で中国電信SIMに切り替えます。
     - このSIM上のトラフィックはGFWの制限対象となるため、VPNを使用しない限り多くの外国のサイトへのアクセスがブロックされることに注意してください。
   - **APIサポート**: `CTCellularData`を使用して携帯データの使用量を監視し、正しいSIMがアクティブであることを確認します。`NEVPNManager`を使用して、中国電信SIM上でGFWを回避するための特定のアプリ用にVPNを設定することもできますが、中国でのVPNの信頼性は積極的なブロックにより一貫していません。[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

3. **トラフィック分離のための実用的なワークフロー**:
   - **手動切り替え**: シンプルにするために、タスクに基づいて設定でアクティブなデータSIMを切り替えます（例: 国際アプリにはMacao SIM、ローカルアプリには中国電信SIM）。これは最も straightforward なアプローチですが、ユーザーの介入が必要です。
   - **中国電信SIM用のVPN**: 中国電信SIMを使用している間にブロックされたサービスにアクセスする必要がある場合は、`NEVPNManager`を使用してVPNを設定します。多くのVPN（例: ExpressVPN、NordVPN）は、GFWによるブロックのため中国では信頼性が低い可能性があるため、Astrillやカスタムソリューションなどのプロバイダーを事前にテストしてください。一部のeSIMプロバイダー（例: Holafly、ByteSIM）は、制限を回避するためにアクティ化できる組み込みVPNを提供しています。[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://www.reddit.com/r/chinalife/comments/1ebjcxi/can_you_use_esims_to_get_around_the_firewall/)[](https://esim.holafly.com/internet/mobile-internet-china/)
   - **アプリごとのVPN**: 高度な使用法では、中国電信SIMがアクティブなときに特定のアプリのトラフィックをVPN経由でルーティングし、他のアプリがMacao SIMを直接使用できるようにするために、`NEAppProxyProvider`を使用したカスタムアプリを開発します。
   - **自動化の制限**: iOSは、アプリや宛先URLに基づいてプログラムでアクティブなデータSIMを切り替えるAPIを提供していません。トラフィックのルーティングを管理するには、ユーザー開始によるSIM切り替えまたはVPNに依存する必要があります。

### トラフィック分離を実装する手順

1. **デュアルSIMをセットアップ**:
   - お使いのiPhoneがデュアルSIMをサポートしていることを確認します（例: iPhone XS以降、iOS 12.1以降）。[](https://support.apple.com/en-us/109317)
   - Macao SIMと中国電信SIMを挿入する（またはいずれか一方をeSIMで設定する）。
   - 設定 > 携帯に移動し、プランにラベルを付け（例: 「Macao」と「中国電信」）、デフォルトのデータSIMを設定します（例: 制限のないアクセスのためのMacao）。[](https://support.apple.com/en-us/108898)

2. **携帯データ設定を構成**:
   - 自動的なSIM切り替えを防ぎ、データにどのSIMを使用するかを手動で制御するために、「携帯データの切り替えを許可」を無効にします（設定 > 携帯 > 携帯データ > 携帯データの切り替えを許可）。[](https://support.apple.com/en-us/108898)
   - アプリ内で`CTTelephonyNetworkInfo`を使用して、プログラムでどのSIMがデータ用にアクティブであるかを確認します。

3. **GFW回避のためのVPNを実装**:
   - 中国電信SIMについては、`NEVPNManager`またはサードパーティ製VPNアプリ（例: Astrill、Holaflyの組み込みVPN）を使用してVPNを設定し、GFW制限を回避します。
   - Macao SIMについては、そのトラフィックが中国の検閲済みインフラ外をルーティングするため、VPNは必要ないかもしれません。[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)

4. **トラフィックを監視および管理**:
   - `CTCellularData`を使用して携帯データの使用量を監視し、正しいSIMが使用されていることを確認します。
   - 高度なルーティングについては、`NEPacketTunnelProvider`を探索して、アプリや宛先に基づいてトラフィックを選択的にルーティングするカスタムVPNを作成しますが、これには相当の開発努力が必要です。

5. **テストと最適化**:
   - 両方のSIMで中国本土内の接続性をテストし、Macao SIMが期待通りにGFWを回避することを確認し、中国電信SIMがローカルサービスで機能することを確認します。
   - GFWが多くのVPNプロトコルを積極的にブロックするため、中国電信SIMでのVPNのパフォーマンスを確認します。[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

### 制限と課題

- **動的SIMルーティングのネイティブAPIなし**: iOSは、アプリ、URL、宛先に基づいて動的にトラフィックを特定のSIMにルーティングするAPIを提供していません。アクティブなデータSIMを手動で切り替えるか、VPNを使用してトラフィックを管理する必要があります。
- **GFWによるVPNブロック**: GFWは多くのVPNプロトコル（例: IPsec、PPTP）を積極的にブロックし、SSLベースのVPNでさえ検出された場合にはレート制限される可能性があります。多くの場合、VPNなしでGFWを回避するにはMacao SIMの方が信頼性が高いです。[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)
- **中国電信SIMの制限**: 中国電信のCDMAベースのネットワークは、一部の外国製電話と互換性の問題がある可能性がありますが、そのLTE/5Gネットワークはより広く互換性があります。さらに、そのトラフィックはGFWの検閲対象となるため、ブロックされたサービスにはVPNが必要です。[](https://esim.holafly.com/sim-card/china-sim-card/)[](https://yesim.app/blog/mobile-internet-and-sim-card-in-china/)
- **実名登録**: Macao SIMと中国電信SIMの両方に実名登録（例: パスポートの詳細）が必要な場合があり、セットアップが複雑になる可能性があります。[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://prepaid-data-sim-card.fandom.com/wiki/China)
- **パフォーマンス**: 中国本土内でのMacao SIMのローミングは、特に地方地域では、ローカルの中国電信SIMと比較して速度が遅くなる可能性があります。[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

### 推奨事項

- **主な戦略**: ブロックされたサービスにアクセスするためのデフォルトの携帯データプランとしてMacao SIMを使用します。これは、トラフィックをMacaoの検閲されていないネットワーク経由でルーティングするため、自然にGFWを回避します。中国の番号を必要とする、または本土のネットワークに最適化されたWeChatやAlipayなどのローカルアプリには中国電信SIMに切り替えます。[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)
- **バックアップとしてのVPN**: 中国電信SIMについては、信頼性の高いVPNプロバイダー（例: Astrill、またはHolaflyやByteSIMなどの組み込みVPN付きeSIM）を使用してブロックされたサービスにアクセスします。中国国内ではVPNアプリのダウンロードが制限されている可能性があるため、中国に入国する前にVPNを事前にインストールしてテストしてください。[](https://esim.holafly.com/internet/mobile-internet-china/)[](https://bytesim.com/blogs/esim/mobile-internet-china)[](https://prepaid-data-sim-card.fandom.com/wiki/China)
- **開発努力**: アプリを構築している場合は、`NetworkExtension`を使用して選択的なトラフィックルーティングのためのカスタムVPNを実装しますが、これは複雑であり、エンタープライズレベルの権限が必要になる可能性があることに注意してください。ほとんどのユーザーにとっては、手動のSIM切り替えとVPNの組み合わせで十分です。
- **旅行前のセットアップ**: 本土のポリシーにより中国国内でのeSIMの購入が制限されている可能性があるため、中国到着前に両方のSIM（またはeSIM）を購入してアクティベートしてください。例えば、NomadやHolaflyなどのプロバイダーは、組み込みのGFW回避機能付きeSIMの事前購入とアクティベーションを可能にしています。[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://esim.holafly.com/internet/mobile-internet-china/)

### コードスニペットの例

以下は、`CTTelephonyNetworkInfo`を使用してアクティブな携帯プランを確認し、`NEVPNManager`を使用して中国電信SIM用にVPNを設定する基本的な例です:

```swift
import CoreTelephony
import NetworkExtension

// アクティブな携帯プランを確認
func checkActiveCellularPlan() {
    let networkInfo = CTTelephonyNetworkInfo()
    if let dataService = networkInfo.serviceCurrentRadioAccessTechnology {
        for (serviceIdentifier, rat) in dataService {
            print("Service: \(serviceIdentifier), Radio Access Technology: \(rat)")
            // どのSIMがアクティブか識別（例: Macaoまたは中国電信）
        }
    }
}

// 中国電信SIM用にVPNを設定
func setupVPN() {
    let vpnManager = NEVPNManager.shared()
    vpnManager.loadFromPreferences { error in
        if let error = error {
            print("Failed to load VPN preferences: \(error)")
            return
        }
        
        let vpnProtocol = NEVPNProtocolIKEv2()
        vpnProtocol.serverAddress = "vpn.example.com" // VPNサーバーに置き換え
        vpnProtocol.remoteIdentifier = "vpn.example.com"
        vpnProtocol.authenticationMethod = .certificate // 必要に応じて設定
        
        vpnManager.protocolConfiguration = vpnProtocol
        vpnManager.isEnabled = true
        
        vpnManager.saveToPreferences { error in
            if let error = error {
                print("Failed to save VPN preferences: \(error)")
            } else {
                print("VPN configured successfully")
            }
        }
    }
}
```

### 結論

iOSは、アプリや宛先に基づいて動的にトラフィックを特定のSIMにルーティングするネイティブAPIを提供していませんが、以下によってトラフィック分離を実現できます:
1. VPNなしでGFWを回避するために、制限のないアクセスにMacao SIMを使用する。
2. ブロックされたサービスにアクセスするために、VPN（`NEVPNManager`またはサードパーティ製アプリで設定）とペアにした中国電信SIMをローカルサービスに使用する。
3. 異なるタスクに対して設定でアクティブなデータSIMを手動で切り替える。
4. オプションで、アプリごとのトラフィックルーティングのためのカスタムVPNソリューションを`NetworkExtension`で開発する（ただし、これは複雑）。

最も簡単なアプローチとしては、GFWでブロックされたサービスにはMacao SIMを、ローカルのニーズには中国電信SIMに切り替えることに依存し、後者には信頼性の高いVPNを事前にインストールしてください。GFWのポリシーとVPNの信頼性は急速に変化する可能性があるため、常に中国に旅行する前に設定をテストしてください。[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://prepaid-data-sim-card.fandom.com/wiki/China)

特定のAPI実装についてさらに明確化または支援が必要な場合は、お知らせください！