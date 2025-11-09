---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: BrowserStackテストプラットフォーム概要
translated: true
type: note
---

BrowserStackは、開発者、QAチーム、テスターが数千もの実際のブラウザ、オペレーティングシステム、デバイスでWebサイトとモバイルアプリケーションを検証できる、クラウドベースのソフトウェアテストプラットフォームのリーディングカンパニーです。2011年にローンチされ、Chrome、Firefox、Safari、Edgeの最新バージョンや、iOSおよびAndroid上のモバイル環境を含む3,500以上のブラウザとデバイスの組み合わせに即時アクセスを提供することで、物理的なハードウェアラボの維持管理の必要性を排除します。クロスブラウザ互換性テスト、自動化スクリプト、手動での対話型セッションをサポートし、Webアプリとネイティブ/ハイブリッドアプリの両方に対応している点で特に高く評価されています。

## BrowserStackを利用する理由

多様な環境でのテストは、アプリケーションが一貫して動作することを保証するために不可欠ですが、リソースを大量に消費します。BrowserStackは以下の方法でこの課題に対処します：
-  正確な結果を得るために、実機と実ブラウザ（エミュレータではない）を提供。
-  テストサイクルを高速化する並列テストを可能に。
-   Selenium、Appium、Cypress、CI/CDパイプライン（Jenkins、GitHub Actionsなど）などの人気ツールとの統合。
-  メンテナンスを削減するAI搭載機能（自己修復テスト、失敗分析など）を提供。
-   協調的なデバッグ、バグ報告、分析機能でチームをサポート。

Fortune 500企業を含む世界中の50,000以上のチームに利用され、設定の手間なく、より高速なリリースと高いテストカバレッジを実現しています。

## サインアップと開始方法

1.  **アカウント作成**: BrowserStackのWebサイトにアクセスし、メールアドレス、Googleアカウント、またはGitHubアカウントでサインアップします。ライブテストとAutomate機能への限定アクセスを含む無料トライアルが利用できます。
2.  **ダッシュボードへのアクセス**: ログインしてユーザー名とアクセスキー（Automate > アカウント設定で確認可能）を表示します。これらはスクリプト作成に不可欠です。
3.  **製品の探索**: 上部メニューから、Live（手動テスト）、Automate（スクリプトによるWeb/モバイルテスト）、App Live/Automate（アプリに特化）、Percy（ビジュアルテスト）などを選択します。
4.  **ローカルテストの設定**: プライベートなアプリの場合、BrowserStack Localツール（Windows/Mac/Linux用バイナリ）をインストールして、localhostトラフィックを安全にトンネリングします。
5.  **チーム設定**: メールでユーザーを招待し、共同アクセスのためのロールを設定します。

ローカルエージェント以外のインストールは不要で、テストはクラウド上で実行されます。

## ライブテスト（手動対話型テスト）

ライブテストでは、リモートデバイス上のアプリとリアルタイムで対話でき、探索的なQAに最適です。

### Webアプリケーションのテスト

1.  製品ドロップダウンから **Live** を選択します。
2.  OS（例: Windows 10, macOS, Android）を選択します。
3.  ブラウザ/バージョン（例: Chrome 120, Safari 17）を選択します。
4.  アプリのURLを入力します。セッションが新しいタブで起動します。
5.  組み込みツール（DevTools、コンソール、ネットワークインスペクタ、スクリーンショット、レスポンシブチェッカー）を使用します。
6.  ダッシュボードのサイドバー経由でセッション中にブラウザを切り替えます。
7.  バグを報告：問題点をハイライトし、注釈を付け、Jira、Slack、またはメールと連携します。

セッションは、地理位置情報（100か国以上）、ネットワークスロットリング、Proプランでは最大25分のアイドルタイムアウトをサポートします。

### モバイルWebのテスト（デバイス上のブラウザ）

1.  Liveで、モバイルOS（Android/iOS）を選択します。
2.  デバイス（例: Samsung Galaxy S24, iPhone 15）とブラウザ（例: Android上のChrome）を選択します。
3.  URLを読み込み、対話します。ピンチズームなどのジェスチャーをサポート。
4.  モバイル専用ツール（タッチシミュレーション、画面方向変更、パフォーマンスメトリクス）でデバッグします。

### ネイティブ/ハイブリッドモバイルアプリのテスト

1.  **App Live** に移動します。
2.  アプリ（Androidは.apk、iOSは.ipa、最大500MB）をアップロードするか、App Center/HockeyAppから同期します。
3.  30,000以上の実機からデバイス（例: iOS 18のiPad Pro）を選択します。
4.  アプリを起動してテスト：スワイプ、タップ、シェイク、またはGPS/カメラなどのハードウェアを使用します。
5.  高度な機能：QRコードの注入、生体認証のシミュレーション、Apple Pay/Google Payのテスト、タイムゾーン/ダークモードの変更。
6.  セッションを終了し、ビデオ記録とログを確認します。

| 機能 | Web Live | App Live |
|---------|----------|----------|
| デバイス | 3,000以上のブラウザ | 30,000以上の実機 |
| アップロード | URLのみ | アプリバイナリ |
| ツール | DevTools, 解像度 | ジェスチャー, 生体認証, 音声入力 |
| 制限 | 無制限分（有料版） | 10-25分のアイドルタイムアウト |

## 自動テスト

実際の環境でスクリプトを使用して反復テストを自動化し、数千の並列実行にスケールします。

### セットアップ

1.  フレームワークを選択：Selenium (Java/Python/JS)、Cypress、Playwright、またはモバイル向けAppium。
2.  認証情報を取得：Automateダッシュボードからユーザー名とアクセスキー。
3.  Capabilitiesを設定：JSONを使用してブラウザ、OS、デバイスを指定（例: `{"browser": "Chrome", "os": "Windows", "os_version": "10", "real_mobile": true}`）。

### 実行

1.  スクリプトをBrowserStackのハブに向ける： `https://username:accesskey@hub-cloud.browserstack.com/wd/hub`。
2.  ローカルまたはCI/CD経由で実行。テストは並列実行されます。
3.  結果を表示：ダッシュボードにビデオ、スクリーンショット、コンソール/ネットワークログ、AI分析された失敗が表示されます。
4.  モバイルの場合：まずAPI経由でアプリをアップロードし、その後capabilitiesで指定します。

#### Seleniumスクリプトのサンプル (Java, iPhoneでのGoogleテスト)

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.By;
import java.net.URL;

public class BrowserStackSample {
    public static final String USERNAME = "your_username";
    public static final String AUTOMATE_KEY = "your_access_key";
    public static final String URL = "https://" + USERNAME + ":" + AUTOMATE_KEY + "@hub-cloud.browserstack.com/wd/hub";

    public static void main(String[] args) throws Exception {
        DesiredCapabilities caps = new DesiredCapabilities();
        caps.setCapability("browserName", "iPhone");
        caps.setCapability("device", "iPhone 15");
        caps.setCapability("realMobile", "true");
        caps.setCapability("os_version", "17");
        caps.setCapability("name", "Sample Test");

        WebDriver driver = new RemoteWebDriver(new URL(URL), caps);
        driver.get("https://www.google.com");
        WebElement searchBox = driver.findElement(By.name("q"));
        searchBox.sendKeys("BrowserStack");
        searchBox.submit();
        System.out.println("Page title: " + driver.getTitle());
        driver.quit();
    }
}
```
Python/JSでも同様に適応できます。安定性のために待機（例: WebDriverWait）を追加してください。

## テスト自動化ワークフロー

以下のステップで効率的なパイプラインを構築します：
1.  **計画**: 高価値テスト（例: コアフロー）を特定。アジャイルと連携。
2.  **ツール選択**: クラウド実行にBrowserStack Automateを利用。スクリプト不要のLow Codeを追加。
3.  **設計**: 再利用可能なコンポーネントでモジュール式スクリプトを作成。AIを活用した自然言語での作成を活用。
4.  **実行**: CI/CD経由でトリガー。カスタムネットワーク/地理位置情報を設定した実機で並列実行。
5.  **分析**: AIによるインサイト、ログ、傾向を確認。Jiraに欠陥を記録。
6.  **保守**: UI変更に対して自己修復を適用。不安定なテストを最適化。

これにより、メンテナンスを40%削減し、リリースを加速できます。

## 主な機能と統合

-   **AIエージェント**: 自己修復、失敗の分類、テスト生成。
-   **ビジュアル/アクセシビリティ**: UI差分にPercy。WCAG準拠のスキャン。
-   **レポート**: カスタムダッシュボード、アラート、1年間の保持。
-   **統合**: CI/CD (Jenkins, Travis)、バグトラッカー (Jira, Trello)、バージョン管理 (GitHub)、ローコードツール。
-   **セキュリティ**: SOC2準拠、データ暗号化、RBAC。

低遅延のため、21のデータセンターをサポート。

## 価格プラン (2025年10月現在)

プランは年間契約（25%節約）で、ユーザー数/並列数でスケールします。無料枠/限定トライアルあり。オープンソースは無制限。

| 製品 | スタータープラン | Pro/Team | 主な機能 |
|---------|--------------|----------|--------------|
| **Live (デスクトップ/モバイル)** | $29/ユーザー/月 (デスクトップ) | $39/ユーザー/月 (モバイル) | 無制限分、3,000以上のブラウザ、地理位置情報。Team: $30+/ユーザー。 |
| **Automate (Web/モバイル)** | $99/月 (1並列) | $225/月 (Pro, 1並列) | Selenium/Appium、AI自己修復、ビデオ/ログ。25以上の並列にスケール。 |
| **App Live/Automate** | $39/月 (個人) | $199/月 (1並列) | 30,000以上のデバイス、ジェスチャー、生体認証。Pro: $249/月。 |
| **Percy (ビジュアル)** | 無料 (5Kスクリーンショット) | $199/月 (10K) | AIレビュー、Figma連携。モバイル: $599/月。 |
| **アクセシビリティ** | 無料 (5ページ/スキャン) | $199/月 (Monitor) | スクリーンリーダー、デイリースキャン。Automate: $459/月。 |
| **テスト管理** | 無料 (5ユーザー) | $99/月 (Team) | リポジトリ、CI統合。Pro: $199/月。 |

エンタープライズ：カスタム、SSOとプライベートデバイス付き。最大90%のボリュームディスカウント。

## 長所と短所

**長所**:
-   ハードウェアコストなしでの広範な実機カバレッジ。
-   高速なセットアップと並列スケーリング。
-   堅牢なデバッグとAIによる効率化。
-   DevOpsのための強力な統合。

**短所**:
-   インターネット依存。ローカルと比べて時折遅延が発生。
-   フルアクセスは有料のみ（完全無料枠なし）。
-   チュートリアルなしでは完全な初心者には複雑。

## ベストプラクティス

-   影響の大きいテストから開始。回帰テストの70%を自動化。
-   ステージングアプリにはローカルトンネリングを使用。
-   AIレポートで不安定性を監視。最新のOS/ブラウザで最初に実行。
-   包括的なカバレッジのために手動と自動を組み合わせる。
-   迅速なトリアージにビデオ/スクリーンショットを活用。
-   モバイルの場合：多様なネットワークと画面方向で早期にテスト。

このガイドは、BrowserStackを効果的に活用するための知識を提供します。実践するには、無料トライアルを探索してください。

## 参考文献

-   [BrowserStack 公式サイト](https://www.browserstack.com/)
-   [BrowserStack 価格](https://www.browserstack.com/pricing)
-   [BrowserStack チュートリアル: アプリとブラウザのテスト](https://www.softwaretestinghelp.com/browserstack-tutorial/)
-   [テスト自動化ワークフローガイド](https://www.browserstack.com/guide/test-automation-workflow)
-   [BrowserStack 機能概要](https://www.browserstack.com/guide)