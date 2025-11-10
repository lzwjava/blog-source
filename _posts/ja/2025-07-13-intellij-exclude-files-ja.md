---
audio: false
generated: true
image: false
lang: ja
layout: post
title: IntelliJ IDEAでのファイル除外
translated: true
type: note
---

IntelliJ IDEAでは、ファイルやディレクトリを検索、インデックス作成、コード補完、ビルドから除外することができます。目的に応じて、いくつかの方法があります：

---

### 1. ディレクトリを *除外* としてマークする

* **プロジェクトビュー**で、除外したいフォルダを右クリックします。
* **Mark Directory as → Excluded** を選択します。
* IDEAはそのディレクトリのインデックス作成を停止するため、検索、ナビゲーション、コード分析に表示されなくなります。

これは通常、ビルド出力フォルダ（`target/`、`out/`、`dist/` など）に使用されます。

---

### 2. バージョン管理から除外する (VCS Ignore)

IDEA（およびGit）に特定のファイルを追跡させたくない場合：

* プロジェクト内に `.gitignore` ファイルを作成または編集します。
* そこにディレクトリやファイル名のパターンを追加します。
* IDEAは `.gitignore` を認識し、それらをVCS操作から非表示にします。

---

### 3. コード分析 / インスペクションからファイルを除外する

* **Settings → Editor → Inspections** に移動します。
* そこで **Scopes** を設定し、特定のファイルセットのみにインスペクションを割り当て、他のファイルを除外することができます。

---

### 4. ビルドから除外する (Gradle/Maven)

GradleまたはMavenを使用している場合、`build.gradle` または `pom.xml` を設定して、特定のディレクトリ（生成されたコードやリソースなど）を除外できます。IDEAはこれらのビルドツールの設定を尊重します。

---

### 5. 特定のファイルタイプを除外する

* **Settings → Editor → File Types** に移動します。
* 「Ignore files and folders」リストにパターン（`*.log`、`*.tmp` など）を追加します。

---

👉 クイックヒント：IDEAが `node_modules/` のような大きなフォルダのインデックス作成にリソースを浪費するのを防ぐだけが目的であれば、**Mark Directory as Excluded** オプションが最速で最も効果的です。

IDEAでテストディレクトリ（`src/test/java` など）を **コードカバレッジ** の実行から除外する方法もご紹介しましょうか？