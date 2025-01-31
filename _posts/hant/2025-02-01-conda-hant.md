---
audio: false
lang: hant
layout: post
title: Conda 的問題
translated: true
---

查看此連結，[https://www.reddit.com/r/MachineLearning/comments/myl8yn/d_is_anaconda_worth_the_trouble/](https://www.reddit.com/r/MachineLearning/comments/myl8yn/d_is_anaconda_worth_the_trouble/)。

我有問題使用 conda，其他人也討論過相似的問題。

隨著時間的推移，你會對不同的環境設置變得不再敏感。所以，我必須刪除其他環境。現在，我主要使用 `Python 3.10.9`，偶爾使用 `Python 3.11.11`。然而，我甚至很少使用 `Python 3.11.11`。個人來說，我不需要太多的環境。我只需要一到兩個環境來運行我目前正在研究或學習的內容。

我更喜歡更簡單的解決方案。如果我有兩個相互衝突的項目，我會選擇一個並放棄運行另一個。

例如，遇到以下問題確實很麻煩：

```bash
conda config --set proxy_servers.http $HTTP_PROXY
conda config --set proxy_servers.https $HTTP_PROXY
```

儘管最初設定代理以加快速度，但我最終決定移除它。

```bash
  - defaults/osx-arm64::markdown==3.4.1=py310hca03da5_0
  - defaults/osx-arm64::numpydoc==1.5.0=py310hca03da5_0
  - defaults/noarch::tldextract==3.2.0=pyhd3eb1b0_0
failed with initial frozen solve. Retrying with flexible solve.
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): / WARNING conda.models.version:get_matcher(546): Using .* with relational operator is superfluous and deprecated and will be removed in a future version of conda. Your spec was 1.8.0.*, but conda is ignoring the .* and treating it as 1.8.0
WARNING conda.models.version:get_matcher(546): Using .* with relational operator is superfluous and deprecated and will be removed in a future version of conda. Your spec was 1.9.0.*, but conda is ignoring the .* and treating it as 1.9.0
done
Solving environment: /
The environment is inconsistent, please check the package plan carefully
The following packages are causing the inconsistency:

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

==> WARNING: A newer version of conda exists. <==
  current version: 23.3.1
  latest version: 25.1.1

請更新 conda 以執行

    $ conda update -n base -c defaults conda

或者最小化更新過程中的套件數量時使用

     conda install conda=25.1.1

## Package Plan ##

  environment location: /Users/lzwjava/anaconda3

  added / updated specs:
    - ipykernel

The following packages will be downloaded:

    package                    |            build
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
                                           Total:        16.6 MB

The following NEW packages will be INSTALLED:

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

The following packages will be UPDATED:

  ca-certificates                      2023.7.22-hf0a4a13_0 --> 2025.1.31-hf0a4a13_0
  openssl                                 1.1.1u-h53f4e23_0 --> 1.1.1w-h53f4e23_0

是否繼續 ([y]/n)?

Downloading and Extracting Packages

Preparing transaction: done
Verifying transaction: failed

RemoveError: 'jsonpatch' is a dependency of conda and cannot be removed from
conda's operating environment.
RemoveError: 'tqdm' is a dependency of conda and cannot be removed from
conda's operating environment.