---
audio: false
generated: true
lang: ja
layout: post
title: qBittorrentファイル検証：SHA-1ハッシュ
translated: true
type: note
---

qBittorrentでファイルの場所を移動し、シーディング前に再度ファイルをチェックするとき、新しい場所にあるファイルが元々扱っていたものと同じであることを確認しています。この検証は、誤ったデータや破損したデータを共有しないようにするため、トレントにおいて重要です。以下に、そのプロセスと使用されるアルゴリズムについて説明します。

### qBittorrentによるファイルの検証方法
qBittorrentは、移動されたファイルが正しいと単純に信じるのではなく、トレントファイルに保存されている情報と比較して完全性をチェックします。トレントでは、データは**ピース**と呼ばれる小さなチャンクに分割され、各ピースには一意のハッシュ値があります。これらのハッシュはトレントファイルに含まれており、データの各ピースの指紋として機能します。ファイルを新しい場所に移動すると、qBittorrentはこれらのピースハッシュを使用して、ファイルが変更されていないことを確認します。

このプロセスは以下の手順に分解できます：

1. **新しい場所の指定**：新しいファイルパスを設定することで、ファイルが現在どこにあるかをqBittorrentに伝えます。
2. **ファイルのトレントへのマッピング**：qBittorrentは、新しい場所にあるファイルをトレントにリストされているファイルと（通常はファイル名とサイズを使用して）照合します（この情報はトレントファイルに含まれています）。
3. **ピースハッシュの検証**：qBittorrentは新しいファイルからデータをピースごとに読み取り、各ピースのハッシュを計算し、それをトレントファイルに保存されている対応するハッシュと比較します。
4. **完全性の確認**：計算されたすべてのハッシュがトレントのハッシュと一致する場合、ファイルは同一であると確認され、qBittorrentはシーディングを再開できます。いずれかのピースのハッシュが一致しない場合、そのピースは不完全または欠落しているとフラグが立てられ、qBittorrentはそのピースを再ダウンロードする必要があるかもしれません。

### 使用されるアルゴリズム
qBittorrentは、ファイル全体のチェックサム（例えばファイル全体に対するMD5やSHA-256など）を使用しません。それは、特に大きなファイルの場合、遅く非効率になるためです。代わりに、**BitTorrentプロトコルで定義されたピースハッシュ**に依存しています。これらのピースハッシュに使用されるアルゴリズムは、広く使用されている暗号化ハッシュ関数である**SHA-1**です。データの各ピース（トレントに応じて数キロバイトから数メガバイト）はSHA-1でハッシュ化され、それらのハッシュがqBittorrentが照合する対象となります。

ファイル全体のチェックサムの代わりにピースハッシュを使用することには、2つの大きな利点があります：
- **効率性**：小さなピースをチェックする方がファイル全体をハッシュ化するよりも高速です。
- **粒度**：何か問題があった場合、qBittorrentはファイル全体を拒否するのではなく、修正が必要な正確なピースを特定できます。

### これが重要な理由
このハッシュベースの検証は、新しい場所からシーディングしているデータが他のピアが期待するものと一致することを保証し、トレントのスウォームの完全性を維持します。このチェックがなければ、ファイルを移動すると、破損したデータや不一致のデータを共有することにつながり、トレントのプロセスを混乱させる可能性があります。

要するに、qBittorrentでファイルの場所を移動すると、各ピースの**SHA-1ハッシュ**を計算し、それをトレントファイルのハッシュと比較することでファイルを再チェックします。これが、シーディングを再開する前にすべてが正しいことを確認する方法です。

---

qBittorrentがファイルの場所を移動する際にピースハッシュ（具体的にはSHA-1ハッシュ）を使用してファイルの完全性を検証する方法を実証するために、ここに簡単なPythonスクリプトを示します。qBittorrentはBitTorrentプロトコルに従い、ファイルをピースに分割し、各ピースのSHA-1ハッシュを計算し、これらのハッシュを使用して、ファイルの場所に関係なくその内容が変更されていないことを保証します。このスクリプトは、サンプルファイルを作成し、そのピースハッシュを計算し、同一のコピーを検証し、その後変更が検証を失敗させることを示すことで、そのプロセスをシミュレートします。

### 説明
- **ピースハッシュ**: スクリプトはファイルを固定サイズのピース（例：10バイト）に分割し、各ピースのSHA-1ハッシュを計算します。これはトレントファイルがこれらのハッシュを保存する方法を模倣しています。
- **検証**: ファイルの計算されたハッシュが期待されるハッシュと一致するかどうかをチェックし、完全性を保証します。
- **シミュレーション**: ファイルを作成し、それをコピー（移動をシミュレート）し、検証し、その後コピーを変更して再度検証し、変更がどのように検出されるかを示します。

以下に、明確にするためのコメント付きのスクリプトを示します：

```python
import hashlib
import shutil
import os

def compute_piece_hashes(file_path, piece_size):
    """ファイルの各ピースのSHA-1ハッシュを計算します。"""
    hashes = []
    with open(file_path, 'rb') as f:
        while True:
            piece = f.read(piece_size)
            if not piece:
                break
            hash_obj = hashlib.sha1(piece)
            hashes.append(hash_obj.hexdigest())
    return hashes

def verify_file_integrity(file_path, piece_size, expected_hashes):
    """ピースハッシュを比較してファイルの完全性を検証します。"""
    current_hashes = compute_piece_hashes(file_path, piece_size)
    if len(current_hashes) != len(expected_hashes):
        return False
    for current, expected in zip(current_hashes, expected_hashes):
        if current != expected:
            return False
    return True

# 既知の内容でサンプルファイルを作成
with open('file1.txt', 'w') as f:
    f.write("Hello, this is a test file.")

piece_size = 10  # バイト、デモ用に小さく設定

# file1.txtから期待されるハッシュを計算（トレントハッシュをシミュレート）
expected_hashes = compute_piece_hashes('file1.txt', piece_size)
print("Expected hashes:", [h[:8] for h in expected_hashes])  # 可読性のために最初の8文字を表示

# file1.txtをfile2.txtにコピーしてファイルの移動をシミュレート
shutil.copyfile('file1.txt', 'file2.txt')

# file2.txtを期待されるハッシュに対して検証（合格するはず）
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Verification of file2.txt (unchanged):", "Valid" if is_valid else "Invalid")

# file2.txtを変更して破損または変更をシミュレート
with open('file2.txt', 'a') as f:
    f.write(" Modified")

# 再度検証（内容が変更されたため失敗するはず）
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Verification of file2.txt (modified):", "Valid" if is_valid else "Invalid")

# 作成されたファイルをクリーンアップ
os.remove('file1.txt')
os.remove('file2.txt')
```

### 動作の仕組み
1. **ファイル作成**: "Hello, this is a test file." (25バイト) を `file1.txt` に書き込みます。
2. **ハッシュ計算**: `file1.txt` を10バイトごとのピース（例: "Hello, thi", "s is a tes", "t file."）に分割し、SHA-1ハッシュを計算し、`expected_hashes` として保存します。
3. **移動のシミュレート**: `file1.txt` を `file2.txt` にコピーし、新しい場所へのファイル移動を表現します。
4. **初期検証**: `file2.txt` を `expected_hashes` に対してチェックします。内容が同一であるため、"Valid" と表示されます。
5. **変更**: `file2.txt` に " Modified" を追加し、その内容とサイズを変更します（現在34バイト、4つのピースに分割）。
6. **第二回検証**: 変更された `file2.txt` をチェックします。ピースの数またはそれらのハッシュが異なるため、"Invalid" と表示されます。
7. **クリーンアップ**: 一時ファイルを削除します。

### 出力例
```
Expected hashes: ['dffd6021', 'a2b3c4d5', 'e6f789ab']  # ハッシュプレフィックスの例
Verification of file2.txt (unchanged): Valid
Verification of file2.txt (modified): Invalid
```
（実際のハッシュ値は異なりますが、このパターンに従います。）

このスクリプトは、qBittorrentがピースハッシュを比較することでファイルの完全性を保証し、ファイルが移動された後でもあらゆる変更を検出する方法を説明しており、このプロセスのシンプルでありながら効果的な実演となっています。