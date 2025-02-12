---
audio: false
lang: ja
layout: post
title: スプリングブートプロジェクトのAIツールを使った開発
translated: true
---

JDKのパスは、`/opt/homebrew/Cellar/openjdk@17/17.0.14/libexec/openjdk.jdk/Contents/Home`にあります。

```bash
mvn clean install
mvn spring-boot:run
mvn compile
mvn test
mvn package
mvn deploy
mvn verify
mvn site
mvn archetype:generate
```

コマンドラインを使用してアプリケーションをコンパイルし、実行します。