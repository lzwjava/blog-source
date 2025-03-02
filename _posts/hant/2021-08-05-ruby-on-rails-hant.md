---
audio: false
generated: false
lang: hant
layout: post
title: 使用 Ruby on Rails
translated: true
---

在 ShowMeBug 的工作期間，我參與了企業微信整合項目。這涉及將 ShowMeBug 與企業微信整合，為企業微信生態系統內的技術面試工具提供無縫訪問。我利用了 Ruby、Ruby on Rails、PostgreSQL 和微信 SDK 等技術，為面試官和候選人創建了流暢的用戶體驗。

這篇博客文章是由 AI 在 2025 年 2 月左右協助撰寫的。

---

Ruby on Rails（通常簡稱為「Rails」）是一個強大的網頁開發框架，基於 Ruby 程式語言。它旨在通過強調約定優於配置和 DRY（不要重複自己）原則，使構建網頁應用程式變得快速且愉快。讓我們來看看如何設置並創建一個簡單的應用程式。

#### 第 1 步：安裝 Ruby 和 Rails
首先，你需要安裝 Ruby，因為 Rails 是一個 Ruby 寶石（庫）。大多數系統都沒有預裝 Ruby，所以這是如何設置的：

- **在 macOS/Linux 上：**
  - 使用像 `rbenv` 或 `rvm` 這樣的版本管理器來獲得靈活性。通過 Homebrew 安裝它（`brew install rbenv`），然後運行：
    ```bash
    rbenv install 3.2.2  # 截至 2025 年的穩定 Ruby 版本
    rbenv global 3.2.2
    ```
  - 安裝 Rails：
    ```bash
    gem install rails
    ```

- **在 Windows 上：**
  - 使用 RubyInstaller（從 rubyinstaller.org 下載）。選擇一個像 3.2.2 這樣的版本，並附帶 DevKit。
  - 安裝 Ruby 後，打開命令提示符並運行：
    ```bash
    gem install rails
    ```

驗證安裝：
```bash
ruby -v  # 應該顯示類似於 ruby 3.2.2 的內容
rails -v # 應該顯示最新的 Rails 版本，例如 7.1.x
```

#### 第 2 步：創建新的 Rails 項目
安裝 Rails 後，生成一個新應用程式：
```bash
rails new myapp --database=sqlite3
cd myapp
```
這將創建一個名為 `myapp` 的文件夾，其中包含完整的 Rails 結構，使用 SQLite 作為默認數據庫（對於開發非常好）。

#### 第 3 步：啟動伺服器
運行內置的 Rails 伺服器：
```bash
rails server
```
在瀏覽器中打開 `http://localhost:3000`。你會看到一個歡迎頁面。恭喜，你的 Rails 應用程式正在運行！

#### 第 4 步：構建一些簡單的東西
讓我們創建一個基本的「文章」功能，以了解 Rails 的 MVC（模型-視圖-控制器）模式。

- **生成模型和控制器：**
  ```bash
  rails generate scaffold Post title:string body:text
  ```
  這將創建一個 `Post` 模型、數據庫遷移、控制器和視圖——所有這些都已連接在一起。

- **運行遷移：**
  ```bash
  rails db:migrate
  ```
  這將設置文章的數據庫表。

- **查看它：**
  重新啟動伺服器（`rails server`）並訪問 `http://localhost:3000/posts`。你會看到一個 CRUD 介面，用於創建、讀取、更新和刪除文章。

#### 第 5 步：探索關鍵概念
- **路由：**打開 `config/routes.rb`。你會看到 `resources :posts`，這將自動生成 RESTful 路由，例如 `/posts/new` 或 `/posts/1/edit`。
- **控制器：**查看 `app/controllers/posts_controller.rb`。它處理請求和響應。
- **視圖：**檢查 `app/views/posts/`。這些是 ERB 模板（嵌入 Ruby 的 HTML）。
- **模型：**查看 `app/models/post.rb`。它與數據庫相關聯，並可以包括驗證（例如 `validates :title, presence: true`）。

#### 第 6 步：自定義和部署
- 在 `app/assets/stylesheets/` 中添加一些樣式的 CSS。
- 針對生產環境，切換到像 PostgreSQL 這樣的數據庫（`rails new myapp --database=postgresql`），並部署到像 Render 或 Heroku 這樣的平台。在 `Gemfile` 中更新 `gem "pg"` 並運行 `bundle install`。

#### 專業技巧
- 使用 `rails console` 即時實驗你的模型。
- 運行 `rails generate --help` 以查看 Rails 提供的所有快捷方式。
- 利用像 `devise` 這樣的寶石進行身份驗證或 `pundit` 進行授權——將它們添加到你的 `Gemfile` 中並按需配置。

這就是了！你已經有一個基本的 Rails 應用程式在運行。從這裡，探索官方 Rails 指南（guides.rubyonrails.org）或構建一些實際的東西來鞏固你的技能。你在考慮什麼樣的項目？