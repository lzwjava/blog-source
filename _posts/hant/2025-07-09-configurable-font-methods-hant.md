---
audio: false
generated: true
lang: hant
layout: post
title: LaTeX 中的可配置字型
translated: true
type: note
---

你可以透過在 LaTeX 文件頂部創建變數來設定字型配置。以下提供幾種方法：

## 方法 1：簡單變數（推薦）

## 方法 2：使用條件判斷適用不同系統

讓我創建一個具備自動作業系統偵測功能的進階版本：

## 方法 3：使用獨立設定檔

你也可以為字型設定創建獨立檔案：

然後在主文件中：

## 常用 Linux 字型替代方案

以下是一些適合 Linux 系統的優質字型替代方案：

**中文字型／CJK 字型：**
- `Noto Sans CJK SC`（推薦）
- `Source Han Sans SC`
- `WenQuanYi Micro Hei`
- `Droid Sans Fallback`

**英文字型：**
- `Liberation Serif`（Times New Roman 替代方案）
- `DejaVu Serif`
- `Linux Libertine`
- `TeX Gyre Termes`

## 使用方式

1. **方法 1** 最為簡單 - 需要時只需取消 Linux 字型行的註解即可
2. **方法 2** 允許你僅需更改單一變數（`\fontsystem`）即可切換不同系統
3. **方法 3** 將字型設定獨立存放，便於維護不同版本

請選擇最符合你工作流程的方法！