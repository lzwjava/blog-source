---
audio: false
generated: true
lang: ja
layout: post
title: バターカーフを用いたビューバインディング
translated: true
type: note
---

Butter Knifeは、UI要素をコード内のフィールドにバインドするプロセスを簡素化する人気のAndroid向けビューバインディングライブラリです。ただし、Butter Knifeは現在非推奨となっており、現代のAndroid開発では代わりにView Binding（Android Jetpackで導入）の使用が推奨されています。それでも、2015年頃にリリースされた古いバージョンであるButter Knife 6.1.0を、Androidプロジェクトで`.jar`ファイルを使用する必要がある場合、2025年3月3日時点でのAndroid Studioでの実施方法を以下に示します。

### 前提条件
- Android Studioがインストールされていること（最新バージョンであれば動作しますが、バージョンによってプロセスが若干異なる場合があります）
- 基本的なAndroidプロジェクトが設定されていること
- `butterknife-6.1.0.jar`ファイルがダウンロードされていること。通常、古いバージョンはMaven Centralなどのリポジトリや、`.jar`ファイルをローカルで持っている場合はアーカイブソースから入手できます

### `butterknife-6.1.0.jar`をAndroid開発で使用する手順

#### ステップ1: `.jar`ファイルをプロジェクトに追加する
1. **`libs`フォルダを探す**:
   - Android Studioプロジェクトで、`app`モジュールに移動します
   - `app`フォルダ内で、`libs`という名前のフォルダを探すか作成します。存在しない場合は、`app`フォルダを右クリックし、`New > Directory`を選択して`libs`という名前を付けます

2. **`.jar`ファイルをコピーする**:
   - `butterknife-6.1.0.jar`ファイルを`libs`フォルダにコピーします。Android Studioでファイルを`libs`フォルダにドラッグ＆ドロップするか、ファイルエクスプローラー経由で手動で配置することで行えます

3. **Gradleで`.jar`ファイルを同期する**:
   - `app`モジュールの`build.gradle`ファイル（`app/build.gradle`にあります）を開きます
   - `dependencies`ブロックの下に以下の行を追加して、`libs`フォルダ内のすべての`.jar`ファイルを含めます：
     ```gradle
     dependencies {
         compile fileTree(dir: 'libs', include: ['*.jar'])
     }
     ```
   - Android Studioで「Sync Project with Gradle Files」ボタンをクリックしてプロジェクトを同期します

#### ステップ2: プロジェクトを設定する
Butter Knife 6.1.0はアノテーションプロセッシングを使用しますが、この特定のバージョン（8.x以降などの後続バージョンとは異なり）ではアノテーションプロセッサの依存関係は必要ありません。`.jar`ファイルにはランタイムライブラリが含まれており、Butter Knife 6.1.0はその機能の大部分にコンパイル時コード生成ではなくランタイムリフレクションに依存しています。

ただし、プロジェクトがJavaアノテーションをサポートするように設定されていることを確認してください：
- `app/build.gradle`で、Javaバージョンが互換性があることを確認します（Butter Knife 6.1.0はJava 6以上で動作します）：
  ```gradle
  android {
      compileOptions {
          sourceCompatibility JavaVersion.VERSION_1_6
          targetCompatibility JavaVersion.VERSION_1_6
      }
  }
  ```

#### ステップ3: コードでButter Knifeを使用する
1. **Butter Knifeアノテーションを追加する**:
   - ActivityやFragmentで、Butter Knifeをインポートし、ビューに`@InjectView`（バージョン6.1.0で使用されるアノテーション）を付けます。例：
     ```java
     import android.os.Bundle;
     import android.widget.Button;
     import android.widget.TextView;
     import butterknife.InjectView;
     import butterknife.ButterKnife;
     import androidx.appcompat.app.AppCompatActivity;

     public class MainActivity extends AppCompatActivity {

         @InjectView(R.id.my_button)
         Button myButton;

         @InjectView(R.id.my_text)
         TextView myText;

         @Override
         protected void onCreate(Bundle savedInstanceState) {
             super.onCreate(savedInstanceState);
             setContentView(R.layout.activity_main);
             ButterKnife.inject(this); // ビューのバインド

             // 使用例
             myButton.setOnClickListener(v -> myText.setText("Button clicked!"));
         }
     }
     ```

2. **XMLレイアウト**:
   - レイアウトファイル（例：`res/layout/activity_main.xml`）に対応するIDを持つビューが含まれていることを確認します：
     ```xml
     <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
         android:layout_width="match_parent"
         android:layout_height="match_parent"
         android:orientation="vertical">

         <TextView
             android:id="@+id/my_text"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:text="Hello World" />

         <Button
             android:id="@+id/my_button"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:text="Click Me" />
     </LinearLayout>
     ```

3. **ビューのバインド**:
   - `onCreate`内の`ButterKnife.inject(this)`呼び出しが、アノテーションが付けられたフィールドをレイアウトからのビューにバインドします。バージョン6.1.0では、`bind`（7.xや8.xなどの後続バージョンで導入）ではなく`inject`が使用されることに注意してください

#### ステップ4: プロジェクトを実行する
- プロジェクトをビルドして実行します。すべてが正しく設定されていれば、Butter Knifeがビューをバインドし、UIが期待通りに機能するはずです

### 重要な注意点
- **バージョンの制限**: Butter Knife 6.1.0は非常に古く（2015年リリース）、コンパイル時コード生成（アノテーションプロセッサ経由）や`@InjectView`の代わりとなる`@BindView`のサポートなど、後続バージョンで導入された機能が欠けています。ランタイム時のリフレクションを使用するため、現代の代替手段と比較してパフォーマンスに若干の影響が出る可能性があります
- **非推奨ステータス**: Butter Knifeはもはやメンテナンスされていません（開発は2020年頃に停止）、新しいプロジェクトではView BindingまたはJetpack Composeを使用することが公式に推奨されています
- **代替設定**: 新しいバージョン（例：10.2.3）を使用していた場合は、アノテーションプロセッサの依存関係（例：`annotationProcessor 'com.jakewharton:butterknife-compiler:10.2.3'`）を追加する必要がありますが、6.1.0の`.jar`ファイルではこれは必要ありません
- **トラブルシューティング**:
  - Butter Knifeクラスに対して「cannot resolve symbol」エラーが発生する場合は、`.jar`ファイルが正しく`libs`フォルダに追加され、Gradleの依存関係に含まれていることを確認してください
  - アプリが`NoClassDefFoundError`でクラッシュする場合は、`.jar`ファイルが`libs`フォルダにあり、プロジェクトが同期されていることを再確認してください

### 推奨事項
このガイドでは`butterknife-6.1.0.jar`の使用方法を示していますが、より現代的でサポートされたアプローチのためにView Bindingへの移行を検討してください。簡単な比較を以下に示します：
- **Butter Knife 6.1.0**: `@InjectView`を使用、ランタイムリフレクション、手動での`.jar`統合
- **View Binding**: Androidに組み込まれ、外部依存関係なし、コンパイル時にバインディングクラスを生成、null安全

View Bindingへの移行に関するガイダンスが必要ですか？