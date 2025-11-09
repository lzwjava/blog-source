---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Red Hat Enterprise Linux デフォルトテキストエディター
translated: true
type: note
---

### Red Hat Enterprise Linux のデフォルトテキストエディタ

Red Hat Enterprise Linux (RHEL) のデフォルトテキストエディタは **Vi** (多くの場合 **Vim** - "Vi IMproved" の略 - としてエイリアスされています) です。Vi はモーダルなコマンドラインテキストエディタで、1970年代から Unix ライクなシステムで標準となっています。軽量でどこにでも存在し、`vim-minimal` または `vim-enhanced` パッケージ経由でほとんどの RHEL システムにプリインストールされています。

#### Vi/Vim が選ばれる理由
- GUI エディタが実用的ではないサーバー環境で効率的です。
- コマンドはキーボードベース: 入力用の挿入モード (`i`) と、編集用のコマンドモード (例: 行を削除する `dd`、保存して終了する `:wq`) があります。
- 初めて使う場合、学習曲線はありますが、習得すれば強力です。

#### 確認と使用方法
- ファイルを開くには `vi filename.txt` (または `vim filename.txt`) を実行します。
- 現在のデフォルトエディタを確認するには: `echo $EDITOR` (通常は `/usr/bin/vi` を出力します)。
- 他のエディタ (前回の質問で出た Emacs など) を好む場合は、`~/.bashrc` で `export EDITOR=emacs` を設定します。

クイックスタートとして、`vimtutor` と入力すると対話型チュートリアルが起動します。

[Vi エディタの使い方 - Red Hat](https://www.redhat.com/en/blog/get-started-vi-editor)  
[Linux スキル: テキストエディタをさらに活用する 9 つのチュートリアル - Red Hat](https://www.redhat.com/en/blog/text-editor-roundup-2022)