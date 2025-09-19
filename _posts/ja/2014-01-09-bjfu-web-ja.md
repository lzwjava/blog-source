---
audio: false
generated: false
image: false
lang: ja
layout: post
title: 北京林業大学ログインシステムの分析
translated: true
---

この記事は、元々中国語で書かれ、[CSDN](https://blog.csdn.net/lzw_java/article/details/18049581)に公開されました。

---

この記事では、北京林業大学のネットワークログインシステムを逆手に取るプロセスについて詳述しています。

目標は、プログラムでログインプロセスをシミュレートし、ユーザーがウェブブラウザを通じてネットワークに接続する動作を効果的に模倣することです。

Chromeの開発者ツールを使用して、ログインプロセス中に行われるネットワークリクエストを観察できます。

最初のリクエストは`CheckLogin.jsp`に対して行われ、次に`CheckLogin.jsp`によってトリガーされる`index.jsp`に対してリクエストが行われます。

それでは、`CheckLogin.jsp`をより詳細に調べます。

POSTリクエストを使用し、いくつかのキーと値のペアを含むことがわかります。しかし、`action`とは何でしょうか？

開発者ツールの「フォームデータ」を確認することで、ソースを表示できます。

実際の`action`の値を見つけるには、ページソースを確認します。

`action`の値は、2行目の文字列です。

では、IPアドレスはどうやって取得しますか？ログインシステムは、キャンパスのどこからでもアクセスでき、Wi-Fiまたは寮のケーブル接続でもアクセスできます。IPアドレスは動的です。これを自動的に取得する方法は何でしょうか？

最初の画像を覚えていますか？

ウェブページは自動的にIPアドレスを提供します。ログインシステムは、どのIPがアクセスしているかを知っています。ウェブページから簡単に抽出できます。

Chromeは、ウェブページのコードの特定の部分を迅速に特定するための便利なツールを提供します。Firefoxには、Firebugという同様のプラグインがあります。

「要素を検証する」ツール（拡大鏡アイコン）を使用して、ページ上のIPアドレスをクリックします。

開発者ツールは、HTML構造を表示し、IPアドレスが`<span>`タグで`login_txt`クラス、特にそのテキストコンテンツにあることを示します。

Jsoupの`select`関数は、CSSクエリにマッチする要素を見つけ、`first()`は最初のマッチング要素を返します。

すべてのキーと値のペアを持つことで、現在ログインプロセスをシミュレートできます。

POSTリクエストは、リクエスト本文にキーと値のペアを送信します。`post.abort()`呼び出しはリクエストを中断します。これは、後のリクエストで`httpClient`を再利用するためです。`org.apache.http`クラスは、可能な限りHTTP接続を再利用しようとします。リクエストが終了しない場合、同じ接続を使用して別のリクエストを送信することで例外が発生する可能性があります。

なぜ`httpClient`を再利用する必要があるのか、後で説明します。

`checkLogin.jsp`に送信するだけでは、ネットワークに接続できません。このJSPは、ユーザー名とパスワードが正しいかどうかを確認するだけです。

印刷ステートメントを追加することで、応答コードを確認できます。

200の応答は正常なログインを示し、303は認証情報が誤っていることを示し、404は接続エラーを示します。

2番目のJSPスクリプトが実行されるのは`index.jsp`で、これはGETリクエストです。

その後もまだネットワークに接続できません。`connect_action.jsp`に対するリクエストをシミュレートする必要があります。これは、`userid`パラメータ（例：`userid=88888`）が必要で、これは学生のIDに対応します。前の学生IDの学生の`userid`が私のIDと1つ違っていたことに気づきました。この値はどうやって取得できますか？

幸いにも、IPアドレスをウェブページから抽出することを思い出しました。`userid`も同じことができますか？

このスクリーンショットは、切断されたページからのものですが、`connect.jsp`にも同じ論理が適用されます。2番目のJSPが返すページのソースコードには、次にリクエストする必要があるJSPのためのキーと値のペアが含まれています。

ここでは、正規表現を使用します。`group(0)`は、完全な一致（例：`userid=88888`）であり、`group(1)`はカッコ内のコンテンツ（例：`88888`）です。`\d`は任意の数字にマッチし、`+`は1回以上の発生を意味します。`find()`は、正規表現が文字列の任意の部分に一致するかどうかを確認し、`matches()`は正規表現が完全に一致するかどうかを確認します。したがって、`src`が`<frame userid=88888&ip="`のような場合、`matches()`は`false`を返します。これは、正規表現が完全に一致するためです。

以下は、Javaコードです：

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.utils.URLEncodedUtils;
import org.apache.http.cookie.Cookie;
import org.apache.http.impl.client.AbstractHttpClient;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.protocol.HTTP;
import org.apache.http.util.EntityUtils;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Login{

	static void print(String format, Object... args) {
		System.out.println(String.format(format, args));
	}

	public static void main(String[] args) {
		HttpClient httpClient = new DefaultHttpClient();
		String ip;
		String userId;
		String username="130888888";
		String password = "88888888";

		ip=cssQueryFirstText("http://login.bjfu.edu.cn/index.jsp","span.login_txt");

		doPost(httpClient,"http://login.bjfu.edu.cn/checkLogin.jsp",
				"username",username,"password",password,
				"ip",ip,"action","checkLogin.jsp");
		String content=doGet(httpClient,"http://login.bjfu.edu.cn/user/index.jsp",
		  "ip",ip,"action","connect");
		userId=userId(content);
		doGet(httpClient,"http://login.bjfu.edu.cn/user/network/connect_action.jsp",
			"userid",userId,"ip",ip,"type","2");
	}

	static String userId(String html){
		Document doc=Jsoup.parse(html);
		Element elem=doc.select("frame#main").first();
		String src=elem.attr("src");
		Pattern pattern=Pattern.compile("userid=(\\d+)");
		Matcher matcher=pattern.matcher(src);
		String ans="";
		if(matcher.find()){
		  ans=matcher.group(1);
		}
		return ans;
	}

	static String cssQueryFirstText(String url,String cssQuery) {
		String ip=null;
		try{
			Document doc=Jsoup.connect(url).get();
			Elements elems=doc.select(cssQuery);
			Element elem=elems.first();
			ip=elem.text();
		}catch(Exception e){
			e.printStackTrace();
		}
		return ip;
	}

	static String doGet(HttpClient httpClient, String url, String... pairs) {
		String entityContent=null;
		try {
			url = makeGetSrl(url, pairs);
			HttpGet get = new HttpGet(url);
			HttpResponse response = httpClient.execute(get);
			//print("%d", response.getStatusLine().getStatusCode());
			entityContent = entity(response);
			EntityUtils.consume(response.getEntity());
		} catch (IOException e) {
			e.printStackTrace();
		}
		return entityContent;
	}

	static void printEntity(HttpResponse rp){
		print("%s",entity(rp));
	}

	static String entity(HttpResponse response) {
		StringBuilder sb = new StringBuilder("");
		try {
			HttpEntity entity = response.getEntity();
			if (entity != null) {
				BufferedReader br = new BufferedReader(new InputStreamReader(
						entity.getContent()));
				String line = null;
				while ((line = br.readLine()) != null) {
					sb.append(line + "\n");
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return sb.toString();
	}

	static String makeGetSrl(String url,String... pairs) {
		if(!url.endsWith("?")){
			url+="?";
		}
		List<NameValuePair>params=new LinkedList<NameValuePair>();
		int len=pairs.length;
		for(int i=0;i<len/2;i++){
			params.add(new BasicNameValuePair(pairs[2*i],pairs[2*i+1]));
		}
		String paramsStr=URLEncodedUtils.format(params,"utf-8");
		url+=paramsStr;
		return url;
	}

	static String doPost(HttpClient httpClient, String url, String... pairs) {
		String entityContent = null;
		try {
			HttpPost post = new HttpPost(url);
			List<NameValuePair> params = new ArrayList<NameValuePair>();
			for (int i = 0; i < pairs.length / 2; i++) {
				params.add(new BasicNameValuePair(pairs[2 * i], pairs[2 * i + 1]));
			}
			post.setEntity(new UrlEncodedFormEntity(params, HTTP.UTF_8));
			HttpResponse response = httpClient.execute(post);
			entityContent = entity(response);
			//print("%d", response.getStatusLine().getStatusCode());
			post.abort();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return entityContent;
	}

	private static String getCookies(HttpClient client) {
        StringBuilder sb = new StringBuilder();
        List<Cookie> cookies = ((AbstractHttpClient)
        		client).getCookieStore().getCookies();
        for(Cookie cookie: cookies)
            sb.append(cookie.getName() + "=" + cookie.getValue() + ";");
        return sb.toString();
   }
}
```

完全なソースコードはGitHubで入手できます。ただし、有効な大学ネットワークアカウントがなければ実行できないかもしれません。

同じ`HttpClient`を再利用する理由は、クッキーを自動的に保存するからです。JSPスクリプトは、クッキーを使用してリクエストが同じセッションからのものかどうかを確認します。これは、淘宝のURLを他のブラウザにコピーするとタイムアウトエラーが発生する理由です。

`jsoup`と正規表現は非常に便利なツールです。正規表現を練習するためのオンラインツールがあります。これを楽しんで使ってください！