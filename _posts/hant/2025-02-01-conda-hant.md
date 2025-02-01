---
audio: false
lang: hant
layout: post
title: Conda的問題
translated: true
---

## 問題

請參閱此連結: [https://www.reddit.com/r/MachineLearning/comments/myl8yn/d_is_anaconda_worth_the_trouble/](https://www.reddit.com/r/MachineLearning/comments/myl8yn/d_is_anaconda_worth_the_trouble/).

我遇到過 conda 的問題，其他人也討論過類似的問題。

隨著時間的推移，你會忘記不同環境的設定。所以，我不得不刪除其他環境。現在，我主要使用 `Python 3.10.9`，偶爾使用 `Python 3.11.11`。然而，我甚至很少使用 `Python 3.11.11`。我個人不需要太多的環境。我只需要一或兩個環境來執行我目前研究或學習的內容。

我更喜歡簡單的解決方案。如果我有兩個相互衝突的項目，我會選擇一個，放棄運行另一個。

例如，遇到以下問題會讓人非常困擾：

```bash
conda config --set proxy_servers.http $HTTP_PROXY
conda config --set proxy_servers.https $HTTP_PROXY
```

儘管最初設定 conda 的代理似乎加快了速度，但我最終決定移除它。

## 移除

```bash
rm -rf ~/anaconda3
rm -rf ~/.condarc
rm -rf ~/Library/Caches/pip
# 更新 ~/.zprofile
# 更新 ~/.bash_profile
```

`~/.bash_profile`:

```
# >>> conda initialize >>>
# !! 這個區塊的內容由 'conda init' 管理 !!
__conda_setup="$('/Users/lzwjava/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/lzwjava/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/lzwjava/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/lzwjava/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

但它仍然顯示：

```bash
% which conda
conda () {
	\local cmd="${1-__missing__}"
	case "$cmd" in
		(activate | deactivate) __conda_activate "$@" ;;
		(install | update | upgrade | remove | uninstall) __conda_exe "$@" || \return
			__conda_reactivate ;;
		(*) __conda_exe "$@" ;;
	esac
}
```

重新啟動 iTerm2 後，我決定轉換到 Homebrew 的 Python 設置。看起來我電腦上有多個 Python 設置，總共六個，如下所示。

- ~/Library/Python/3.9
- ~/Library/Python/3.11
- /opt/homebrew/lib/python3.11
- /opt/homebrew/lib/python3.12
- /opt/homebrew/lib/python3.13
- /opt/homebrew/lib/python3.9

使用命令刪除，`brew uninstall python@3.11`。

```bash
% brew uninstall python@3.13
Error: 因為它是 cairo, docutils, ffmpeg, ghostscript, glib, gradle, harfbuzz, imagemagick, libass, libheif, liblqr, maven, openjdk, openjdk@17, pango, poppler, tesseract, wireshark 和 yt-dlp 當前安裝的程式所需，所以拒絕卸載 /opt/homebrew/Cellar/python@3.13/3.13.1。
你可以覆蓋這一點並強制移除：
  brew uninstall --ignore-dependencies python@3.13
```

## 日誌

```bash
  - defaults/osx-arm64::markdown==3.4.1=py310hca03da5_0
  - defaults/osx-arm64::numpydoc==1.5.0=py310hca03da5_0
  - defaults/noarch::tldextract==3.2.0=pyhd3eb1b0_0
failed with initial frozen solve. Retrying with flexible solve.
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): / 警告 conda.models.version:get_matcher(546): 使用 .* 關聯運算符是冗余和已過時，並將在未來版本的 conda 中移除。你的規格是 1.8.0.*, 但 conda 正忽略 .* 並將其視為 1.8.0
警告 conda.models.version:get_matcher(546): 使用 .* 關聯運算符是冗余和已過時，並將在未來版本的 conda 中移除。你的規格是 1.9.0.*, 但 conda 正忽略 .* 並將其視為 1.9.0
done
Solving environment: /
環境不一致，請仔細檢查套件計劃
以下套件導致不一致：

  - defaults/osx-arm64::tabulate==0.8.10=py310hca03da5_0
  - defaults/osx-arm64::cymem==2.0.6=py310hc377ac9_0
  - defaults/noarch::conda-pack==0.6.0=pyhd3eb1b0_0
  # ...
  - defaults/noarch::pandocfilters==1.5.0=pyhd3eb1b0_0
  - defaults/osx-arm64::markdown==3.4.1=py310hca03da5_0
  - defaults/osx-arm64::numpydoc==1.5.0=py310hca03da5_0
  - defaults/noarch::tldextract==3.2.0=pyhd3eb1b0_0
-/ ^R
\
\
/
-
/
-
\
done

==> 警告：存在較新版本的 conda。 <==
  當前版本：23.3.1
  最新版本：25.1.1

請通過運行

    $ conda update -n base -c defaults conda

更新 conda，或最小化在 conda 更新期間更新的套件數量，請使用

     conda install conda=25.1.1
```

## 套件計劃 ##

  環境位置：/Users/lzwjava/anaconda3

  添加/更新規格：
    - ipykernel

將下載以下套件：

    套件                    |            build
    ---------------------------|-----------------
    attrs-25.1.0               |     pyh71513ae_0          55 KB  conda-forge
    bcrypt-3.2.0               |  py310h80987f9_2          37 KB
    ca-certificates-2025.1.31  |       hf0a4a13_0         155 KB  conda-forge
    certifi-2024.12.14         |     pyhd8ed1ab_0         158 KB  conda-forge
    charset-normalizer-2.1.1   |     pyhd8ed1ab_0          36 KB  conda-forge
    click-8.1.8                |     pyh707e725_0          83 KB  conda-forge
    fsspec-2024.12.0           |     pyhd8ed1ab_0         135 KB  conda-forge
    huggingface_hub-0.27.1     |     pyhd8ed1ab_0         272 KB  conda-forge
    jinja2-3.1.5               |     pyhd8ed1ab_0         110 KB  conda-forge
    jsonpatch-1.33             |     pyhd8ed1ab_1          17 KB  conda-forge
    pandas-2.1.4               |  py310h46d7db6_0        11.8 MB
    pyjwt-2.10.1               |     pyhd8ed1ab_0          25 KB  conda-forge
    pyrsistent-0.20.0          |  py310h80987f9_1         100 KB
    python-tzdata-2025.1       |     pyhd8ed1ab_0         140 KB  conda-forge
    pytz-2025.1                |     pyhd8ed1ab_0         182 KB  conda-forge
    pyyaml-6.0.2               |  py310h80987f9_0         176 KB
    sniffio-1.3.1              |     pyhd8ed1ab_1          15 KB  conda-forge
    tenacity-9.0.0             |     pyhd8ed1ab_1          24 KB  conda-forge
    tokenizers-0.13.2          |  py310h3dd52b7_1         2.9 MB
    tqdm-4.67.1                |     pyhd8ed1ab_1          87 KB  conda-forge
    websocket-client-1.8.0     |     pyhd8ed1ab_1          46 KB  conda-forge
    ------------------------------------------------------------
                                           總計：        16.6 MB

以下新套件將被安裝：

  attrs              conda-forge/noarch::attrs-25.1.0-pyh71513ae_0
  bcrypt             pkgs/main/osx-arm64::bcrypt-3.2.0-py310h80987f9_2
  certifi            conda-forge/noarch::certifi-2024.12.14-pyhd8ed1ab_0
  charset-normalizer conda-forge/noarch::charset-normalizer-2.1.1-pyhd8ed1ab_0
  click              conda-forge/noarch::click-8.1.8-pyh707e725_0
  fsspec             conda-forge/noarch::fsspec-2024.12.0-pyhd8ed1ab_0
  huggingface_hub    conda-forge/noarch::huggingface_hub-0.27.1-pyhd8ed1ab_0
  importlib-metadata pkgs/main/osx-arm64::importlib-metadata-4.11.3-py310hca03da5_0
  jinja2             conda-forge/noarch::jinja2-3.1.5-pyhd8ed1ab_0
  jsonpatch          conda-forge/noarch::jsonpatch-1.33-pyhd8ed1ab_1
  pandas             pkgs/main/osx-arm64::pandas-2.1.4-py310h46d7db6_0
  pyjwt              conda-forge/noarch::pyjwt-2.10.1-pyhd8ed1ab_0
  pyrsistent         pkgs/main/osx-arm64::pyrsistent-0.20.0-py310h80987f9_1
  python-tzdata      conda-forge/noarch::python-tzdata-2025.1-pyhd8ed1ab_0
  pytz               conda-forge/noarch::pytz-2025.1-pyhd8ed1ab_0
  pyyaml             pkgs/main/osx-arm64::pyyaml-6.0.2-py310h80987f9_0
  sniffio            conda-forge/noarch::sniffio-1.3.1-pyhd8ed1ab_1
  tenacity           conda-forge/noarch::tenacity-9.0.0-pyhd8ed1ab_1
  tokenizers         pkgs/main/osx-arm64::tokenizers-0.13.2-py310h3dd52b7_1
  tqdm               conda-forge/noarch::tqdm-4.67.1-pyhd8ed1ab_1
  typer              conda-forge/noarch::typer-0.7.0-pyhd8ed1ab_0
  typing_extensions  conda-forge/noarch::typing_extensions-4.7.1-pyha770c72_0
  urllib3            conda-forge/noarch::urllib3-1.26.15-pyhd8ed1ab_0
  websocket-client   conda-forge/noarch::websocket-client-1.8.0-pyhd8ed1ab_1

將更新以下套件：

  ca-certificates                      2023.7.22-hf0a4a13_0 --> 2025.1.31-hf0a4a13_0
  openssl                                 1.1.1u-h53f4e23_0 --> 1.1.1w-h53f4e23_0

繼續 ([y]/n)?

下載和解壓縮套件

準備交易：完成
驗證交易：失敗

RemoveError: 'jsonpatch' 是 conda 的依賴項，不能從 conda 的操作環境中刪除。
RemoveError: 'tqdm' 是 conda 的依賴項，不能從 conda 的操作環境中刪除。