---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: LibreChatウェブ検索のトラブルシューティング
translated: true
type: note
---

注意深くトラブルシューティングしましょう — **LibreChatでWeb検索が機能しない**場合、**Firecrawl**、**SerpApi**、**Jina API**キーを追加した後でも、問題はほぼ常に以下のいずれかです：設定ミス、バックエンドの有効化フラグの欠落、またはUIの誤解。

以下は明確な解説です（表はなく、説明のみ）：

---

### 1. **バックエンド設定で「Web検索」が有効になっているか確認**

LibreChatサーバー設定ファイル（通常は`.env`または`api/config.yaml`、設定によって異なります）を開き、以下のような記述があることを確認してください：

```
# .envの場合
SEARCH_ENABLED=true
```

または、YAMLを使用している場合：

```yaml
features:
  search: true
```

`SEARCH_ENABLED`または`search`が明示的に`true`に設定されていない場合、UIボタンは表示されても実際には検索を実行しません。

---

### 2. **APIキーが適切に命名されていることを確認**

各プロバイダーは特定の環境変数名を期待します。例：

* **SerpApi**の場合：

  ```
  SERPAPI_API_KEY=your_key_here
  ```
* **Firecrawl**の場合：

  ```
  FIRECRAWL_API_KEY=your_key_here
  ```
* **Jina**の場合：

  ```
  JINA_API_KEY=your_key_here
  ```

また、これらが実行中の`backend`プロセスと同じ環境でエクスポートまたはロードされていることを確認してください。

確認方法：

```bash
echo $SERPAPI_API_KEY
```

空白が返された場合、バックエンドはそれを認識していません。

---

### 3. **キーを編集した後、LibreChatを再起動**

LibreChatは環境変数をホットリロードしません。以下を実行してください：

```bash
docker compose down
docker compose up -d
```

（またはDockerを使用していない場合は`npm run start`を再度実行）。

---

### 4. **LibreChatが実際に使用している検索プロバイダーを確認**

LibreChatは設定順序に応じてデフォルトのWeb検索バックエンドを1つ選択します。

例えば、SerpApiを使用させたい場合は、以下を指定する必要があります：

```
SEARCH_PROVIDER=serpapi
```

または、Jinaを使用させたい場合：

```
SEARCH_PROVIDER=jina
```

キーを設定しただけで、使用するプロバイダーを定義しなかった場合、LibreChatはデフォルトでなしになる可能性があります。

---

### 5. **バックエンドログを確認**

実行：

```bash
docker logs librechat-backend
```

または

```bash
npm run start:debug
```

以下のようなメッセージを探してください：

```
[Search] SerpApi key missing or invalid
```

または

```
Search provider not configured
```

これらが最良の手がかりです。

---

### 6. **APIを直接テスト**

キーが実際に機能することを確認するため：

**SerpApiテスト：**

```bash
curl "https://serpapi.com/search.json?q=chatgpt&api_key=YOUR_KEY"
```

**Firecrawlテスト：**

```bash
curl "https://api.firecrawl.dev/v1/search?q=chatgpt" -H "Authorization: Bearer YOUR_KEY"
```

**Jinaテスト：**

```bash
curl "https://r.jina.ai/chatgpt" -H "Authorization: Bearer YOUR_KEY"
```

これらが失敗した場合、キー自体が無効またはレート制限されています。

---

### 7. **フロントエンドのバージョン不一致**

最近LibreChatを更新した場合（特にv0.7以前からv0.8+へ）、フロントエンドの`Web Search`トグルが存在しても、バックエンドバージョンが統合されたFirecrawl/Jina検索モジュールをまだサポートしていない可能性があります。
実行：

```bash
git pull
```

そしてリビルド：

```bash
docker compose build --no-cache
docker compose up -d
```

---

### 8. **最終確認 — Web UIから確認**

UIを開き、**Settings → Features**に移動して確認してください：

* 「Web Search」トグルがON
* 選択したプロバイダー（SerpApi、Firecrawl、またはJina）がリストされている

*「利用可能なプロバイダーがありません」*と表示される場合、バックエンドはキーを読み取っていません。

---

必要であれば、関連する`.env`（キーはマスクして）を貼り付けてください。どの行が欠落しているか、または誤って命名されているかを正確に指摘します。

そのスニペットを表示しますか？