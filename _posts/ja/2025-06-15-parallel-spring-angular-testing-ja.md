---
audio: false
generated: true
image: false
lang: ja
layout: post
title: パラレルスプリングアンギュラーブラウザテスト
translated: true
type: note
---

Spring（Java）＋ Angular サイトを **Edge と Chrome で並行して**、主に **手動で**（役立つ場合には軽い自動化も含めて）テストする実践的な方法が必要なのですね。以下は、広いテーブルを避けつつ、現場で実証されたワークフローです。

---

# 1) クリーンで比較可能なブラウザをセットアップする

* **最新の安定版** Chrome と Edge をインストールします。バージョンをメモしておきます。
* それぞれでテスト用の **独立したクリーンプロファイル** を作成します：

  * Chrome: `chrome --user-data-dir=/tmp/chrome-qa --no-first-run`
  * Edge: `msedge --user-data-dir=/tmp/edge-qa --no-first-run`
* **ズーム (100%)**、**DPR**、**言語**、**OS テーマ**、**フォントパック** を一致させ、拡張機能はオフにします。
* 両方のブラウザを並べて配置します（可能なら2台のモニターを使用）。同じ **ビューポート**（例: 1440×900）を使用します。

---

# 2) 安定したバックエンドと現実的なデータを準備する

* Spring バックエンドを **ステージングモード** で起動し、決定的なシードデータを使用します。
* **不変のテストアカウント** と **既知のデータセット**（例: データベーススナップショット用の Testcontainers や Flyway/Liquibase のシードスクリプト）を優先します。
* 不安定な依存関係には、**WireMock** スタブ（HTTP）を使用し、UI の動作を再現可能にします。

---

# 3) ブラウザ間で操作をミラーリングする（手動だが同期）

真に並行した手動テストのために、あるブラウザからのクリック、スクロール、タイピングをもう一方のブラウザにミラーリングします：

* **Browsersync** をローカルプロキシとして使用し、**操作を同期** します：

  ```bash
  npm i -g browser-sync
  browser-sync start --proxy "http://localhost:4200" --files "dist/**/*" --open "external"
  ```

  プロキシされた URL を **Chrome** と **Edge** で開きます。スクロール、クリック、フォーム入力がミラーリングされます。
  （レイアウトの差異、ホバー/フォーカスのチェック、クイックフローの確認に最適です。）

> プロキシが使用できない場合（認証の制約、社内ネットワーク）、2つのウィンドウを実行し、厳密な **ステップリスト**（下記）と分割画面の画面録画を保持します。

---

# 4) クロスブラウザチェックリスト（両方同時に実行）

このリストを **並行して** 進めます。次のステップに進む前に、両方のブラウザで同じステップを実行します。

* **ブートストラップ & フォント:** スタイル未適用コンテンツの瞬間的表示 (FOUC)、アイコンフォント、フォールバックフォント。
* **レイアウト:** Flex/Grid の間隔、固定ヘッダー/フッター、オーバーフロー/省略表示、RTL/ローカライズされたテキストの折り返し。
* **フォーム:** オートフィル、プレースホルダー、バリデーションメッセージ、数値/日付入力、IME/日本語入力、コピー/ペースト。
* **フォーカス/キーボード:** Tab 順序、フォーカスリングの可視性、`:focus-visible` と `:focus` の違い、Enter/Esc の動作、ショートカット。
* **ホバー/アクティブ:** メニュー、ツールチップ、リップル効果、Angular Material の状態クラス。
* **ファイル & ダウンロード:** ファイル入力の accept フィルタ、ドラッグ&ドロップ、ダウンロードプロンプト。
* **認証/セッション:** クッキー、SameSite、タブ間でのストレージ分離、セッションタイムアウトとリフレッシュトークンのフロー。
* **ルーティング:** ディープリンク、ネストされたルートでのハードリフレッシュ、404 フォールバック。
* **キャッシング:** Service Worker の更新サイクル、古いアセットのバスティング、オフラインページの動作。
* **メディア & API:** getUserMedia/クリップボード、通知のパーミッション。
* **アクセシビリティ簡易チェック:** ランドマーク/ロール、色コントラスト (DevTools)、キーボードのみでのナビゲーション。
* **パフォーマンス確認:** DevTools パフォーマンス、ロングタスクの確認、および **両方の** ブラウザでの Lighthouse。

ヒント: 両方のブラウザで **DevTools を開いたまま**（F12）にし、下部にドッキングして、**コンソール** の警告（フレームワーク、CSP、非推奨メッセージ）を比較します。

---

# 5) 差異が生じやすい Angular 固有の事項

* **変更検知 & 非同期:** マイクロタスクのタイミングにより、競合状態が異なるブラウザで表面化することがあります。スピナーや「保存」ボタンのダブルクリック問題に注意してください。
* **Zone.js エラー:** 一方のブラウザでは未処理の Promise 拒否が発生し、もう一方では発生しない場合があります。コンソールを確認してください。
* **Angular Material テーマ:** ダーク/ライトのトークン、ハイコントラストモード、フォーカスアウトラインを確認します（Edge はフォーカスのレンダリングがわずかに異なることが多いです）。
* **i18n パイプ & 日付フォーマット:** Chromium の亜種間での `DatePipe` と `Intl` のロケール差異。

---

# 6) Spring バックエンドの落とし穴

* **CORS & リダイレクト:** 同じルールですが、**Edge は開発中に CORS プリフライトの問題を早期に表面化させることがあります**。`OPTIONS` レスポンスとヘッダーを確認してください。
* **Content-Type & 圧縮:** `application/json;charset=UTF-8` と `application/json` の違いを確認します。gzip/br の不一致は、一方のブラウザで先に「読み込みに失敗しました」として表示される可能性があります。
* **セキュリティヘッダー:** CSP、HSTS、X-Frame-Options — より厳格なポリシーは、インラインスクリプト/スタイルを異なる方法でブロックする可能性があります。

---

# 7) 「手動」を薄い自動化レイヤーで繰り返し可能にする

完全な E2E テストが不要でも、**短く高速な** ブラウザハーネスを設定し、CI で全ての PR に対して Chrome と Edge の両方を実行できるようにします。これにより、回帰を早期に発見し、手動での確認作業を軽減できます。

### オプション A: Playwright (Angular アプリでの筆者の一押し)

* 単一のテストランナーが、**Chrome Stable** と **Microsoft Edge** チャネルを起動し、**並行して** 実行します。
* `npm i -D @playwright/test`
* `npx playwright install chromium`
* `playwright.config.ts` の例：

  ```ts
  import { defineConfig, devices } from '@playwright/test';

  export default defineConfig({
    testDir: './e2e',
    workers: 4, // 並列処理
    use: {
      baseURL: 'http://localhost:4200',
      trace: 'retain-on-failure',
    },
    projects: [
      {
        name: 'Chrome Stable',
        use: { ...devices['Desktop Chrome'], channel: 'chrome' },
      },
      {
        name: 'Microsoft Edge',
        use: { ...devices['Desktop Edge'], channel: 'msedge' },
      },
    ],
  });
  ```

  最小限のスモークテスト仕様 (`e2e/smoke.spec.ts`)：

  ```ts
  import { test, expect } from '@playwright/test';

  test('home loads and login works', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByRole('heading', { name: 'Welcome' })).toBeVisible();
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('Password123!');
    await page.getByRole('button', { name: 'Sign in' }).click();
    await expect(page.getByText('Dashboard')).toBeVisible();
  });
  ```

  実行: `npx playwright test`

### オプション B: Cypress (Chromium ファミリー、Chrome & Edge を実行)

* CI マトリックス（または Cypress Dashboard）による並列化。
* CI で以下を実行：

  * `cypress run --browser chrome`
  * `cypress run --browser edge`
* 仕様は小さく（スモークテストのみ）保ち、「手動優先」を維持します。

### オプション C: Selenium Grid (既に Selenium を使用している場合)

* Docker 化された Grid が **chromium/edge ノード** を同時に実行します。

  ```yaml
  # docker-compose.yml
  services:
    selenium-hub:
      image: selenium/hub:4
      ports: ["4444:4444"]
    chrome:
      image: selenium/node-chrome:4
      shm_size: 2gb
      depends_on: [selenium-hub]
      environment: [SE_EVENT_BUS_HOST=selenium-hub]
    edge:
      image: selenium/node-edge:4
      shm_size: 2gb
      depends_on: [selenium-hub]
      environment: [SE_EVENT_BUS_HOST=selenium-hub]
  ```

  WebDriver テストを `http://localhost:4444/wd/hub` に向け、テストスイートを並行して実行します。

---

# 8) CI で「デフォルトで並列実行」

* **マトリックス** ジョブ（Chrome/Edge）を使用し、Playwright/Cypress のスモークテストを並行して実行します。
* 時間を節約するために Fail-fast とし、失敗したブラウザの **トレース/動画** を添付します。
* 毎晩、やや広範囲のセットと **Lighthouse** の実行を両方のブラウザで行います。

---

# 9) 差異が生じた場合の迅速なトリアージ

* 各ブラウザから **HAR** を取得し、レスポンス（ステータス、ヘッダー、キャッシング）を比較します。
* 問題のある要素の **計算済みスタイル** を比較します（DevTools → スタイル → 計算済み）。
* **動きの削減** と **強制カラーモード** を切り替え、アクセシビリティに関する CSS の問題を明らかにします。
* **サイトデータ**（Application パネル）をクリアして再テストし、古い Service Worker/キャッシュが原因でないことを確認します。

---

# 10) 保持する最小限の成果物

* クロスブラウザチェックの **共有チェックリスト** (markdown) を 1 つ。
* **バージョン台帳**: アプリのコミット、Chrome/Edge のバージョン、OS、重要なフラグ。
* 「修正しない」として受け入れた視覚的差異について、同じビューポートでの **スクリーンショット** を添付します。

---

必要であれば、あなたの Angular アプリ用に、すぐに実行可能な **Playwright スケルトン**（`npm scripts`、CI マトリックス、2 つのスモークテスト仕様を含む）、またはあなたの開発サーバー設定に合わせた **Browsersync スクリプト** を生成できます。