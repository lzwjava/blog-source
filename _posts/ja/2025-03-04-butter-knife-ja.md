---
audio: false
generated: true
lang: ja
layout: post
title: バターナイフを使用したビューバインド
translated: true
---

Butter Knifeは、AndroidのUI要素をコード内のフィールドにバインドするプロセスを簡素化するための人気のあるビューバインドライブラリです。ただし、Butter Knifeは現在非推奨となっており、最新のAndroid開発ではAndroid Jetpackで導入されたView Bindingを使用することを推奨しています。それでも、2015年にリリースされた古いバージョンであるButter Knife 6.1.0（`.jar`ファイル）をAndroidプロジェクトで使用する必要がある場合、以下のようにAndroid Studioで行うことができます（2025年3月3日現在）。

### 前提条件
- Android Studioがインストールされている（最新バージョンが推奨されますが、バージョンによっては若干異なる場合があります）。
- 基本的なAndroidプロジェクトがセットアップされている。
- `butterknife-6.1.0.jar`ファイルがダウンロードされている。通常、古いバージョンはMaven Centralやアーカイブソースから見つけることができます。

### `butterknife-6.1.0.jar`をAndroid開発で使用する手順

#### ステップ1: `.jar`ファイルをプロジェクトに追加する
1. **`libs`フォルダを探す**:
   - Android Studioプロジェクトの`app`モジュールに移動します。
   - `app`フォルダ内に`libs`という名前のフォルダが存在するか確認し、存在しない場合は右クリックして`New > Directory`を選択し、`libs`と名前を付けます。

2. **`.jar`ファイルをコピー**:
   - `butterknife-6.1.0.jar`ファイルを`libs`フォルダにコピーします。Android Studio内で`libs`フォルダにドラッグ＆ドロップするか、ファイルエクスプローラーを使用して手動で配置します。

3. **`.jar`ファイルをGradleと同期**:
   - `app`モジュールの`build.gradle`ファイルを開きます（`app/build.gradle`）。
   - `dependencies`ブロックの下に以下の行を追加して、`libs`フォルダ内のすべての`.jar`ファイルを含めます：
     ```gradle
     dependencies {
         compile fileTree(dir: 'libs', include: ['*.jar'])
     }
     ```
   - プロジェクトを同期するには、Android Studioの「プロジェクトをGradleファイルと同期」ボタンをクリックします。

#### ステップ2: プロジェクトの設定
Butter Knife 6.1.0はアノテーション処理を使用するため、この特定のバージョンにはアノテーションプロセッサ依存関係が必要ありません（8.x以降のバージョンとは異なります）。`.jar`ファイルにはランタイムライブラリが含まれており、Butter Knife 6.1.0はランタイムリフレクションに依存してほとんどの機能を提供します。

ただし、プロジェクトがJavaアノテーションをサポートしていることを確認してください：
- `app/build.gradle`でJavaバージョンが互換性があることを確認します（Butter Knife 6.1.0はJava 6+と互換性があります）：
  ```gradle
  android {
      compileOptions {
          sourceCompatibility JavaVersion.VERSION_1_6
          targetCompatibility JavaVersion.VERSION_1_6
      }
  }
  ```

#### ステップ3: コードでButter Knifeを使用する
1. **Butter Knifeアノテーションを追加**:
   - ActivityまたはFragmentでButter Knifeをインポートし、バージョン6.1.0で使用される`@InjectView`アノテーションをビューに付けます。例えば：
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
             ButterKnife.inject(this); // ビューをバインド

             // 例の使用
             myButton.setOnClickListener(v -> myText.setText("ボタンがクリックされました！"));
         }
     }
     ```

2. **XMLレイアウト**:
   - レイアウトファイル（例：`res/layout/activity_main.xml`）に、対応するIDを持つビューを含めます：
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
             android:text="クリックしてください" />
     </LinearLayout>
     ```

3. **ビューをバインド**:
   - `onCreate`内の`ButterKnife.inject(this)`呼び出しが、アノテーション付きのフィールドをレイアウトからのビューにバインドします。バージョン6.1.0では、`inject`が使用され、`bind`（バージョン7.xおよび8.xで導入された）とは異なります。

#### ステップ4: プロジェクトを実行する
- プロジェクトをビルドして実行します。設定が正しい場合、Butter Knifeはビューをバインドし、UIが期待通りに機能するはずです。

### 注意点
- **バージョンの制限**: Butter Knife 6.1.0は古い（2015年にリリース）ため、後続のバージョンで導入された機能（例：アノテーションプロセッサを使用したコンパイル時のコード生成や`@BindView`のサポート）が欠けている。ランタイムリフレクションを使用するため、現代の代替手段に比べてパフォーマンスに若干影響を与える可能性があります。
- **非推奨状態**: Butter Knifeはもはやメンテナンスされておらず（開発は2020年頃に停止）、新しいプロジェクトではView BindingまたはJetpack Composeを使用することを推奨しています。
- **代替設定**: 新しいバージョン（例：10.2.3）を使用している場合、アノテーションプロセッサ依存関係（例：`annotationProcessor 'com.jakewharton:butterknife-compiler:10.2.3'`）を追加する必要がありますが、6.1.0で`.jar`ファイルを使用する場合は必要ありません。
- **トラブルシューティング**:
  - Butter Knifeクラスの「シンボルが解決できない」エラーが発生した場合、`.jar`ファイルが正しく`libs`フォルダに追加され、Gradle依存関係に含まれていることを確認してください。
  - アプリが`NoClassDefFoundError`でクラッシュした場合、`.jar`ファイルが`libs`フォルダにあることを確認し、プロジェクトが同期されていることを確認してください。

### 推奨事項
このガイドでは、`butterknife-6.1.0.jar`の使用方法を示していますが、View Bindingに移行することを検討してください。以下は、簡単な比較です：
- **Butter Knife 6.1.0**: `@InjectView`を使用し、ランタイムリフレクション、手動の`.jar`統合。
- **View Binding**: Androidに組み込まれており、外部依存関係が不要で、コンパイル時にバインドクラスを生成し、null安全です。