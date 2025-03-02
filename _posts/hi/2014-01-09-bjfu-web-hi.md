---
audio: false
generated: false
lang: hi
layout: post
title: बेजिंग फॉरेस्ट्री यूनिवर्सिटी लॉगिन प्रणाली का विश्लेषण
translated: true
---

इस पोस्ट को मूल रूप से चीनी भाषा में लिखा गया था और इसे [CSDN](https://blog.csdn.net/lzw_java/article/details/18049581) पर प्रकाशित किया गया था।

---

इस पोस्ट में बेजिंग फॉरेस्ट्री यूनिवर्सिटी द्वारा उपयोग की जाने वाली नेटवर्क लॉगिन सिस्टम के रिवर्स इंजीनियरिंग की प्रक्रिया का विवरण दिया गया है।

लक्ष्य है कि लॉगिन प्रक्रिया को प्रोग्रामेटिक रूप से सिमुलेट करने के लिए, एक वेब ब्राउजर के माध्यम से नेटवर्क से कनेक्ट होने वाले उपयोगकर्ता के कार्यों की नकल करने के लिए।

क्रोम के डेवलपर्स टूल्स का उपयोग करके, हम लॉगिन प्रक्रिया के दौरान किए गए नेटवर्क रिक्वेस्ट्स को देख सकते हैं।

पहला रिक्वेस्ट `CheckLogin.jsp` को होता है, उसके बाद `index.jsp` को एक रिक्वेस्ट होता है, जो `CheckLogin.jsp` द्वारा ट्रिगर किया जाता है।

चलिए `CheckLogin.jsp` को साफ़ देखते हैं।

हम देखते हैं कि यह एक पोस्ट रिक्वेस्ट का उपयोग करता है और इसमें कई की-वैल्यू पैरों शामिल हैं। लेकिन `एक्शन` क्या है?

"फॉर्म डेटा" को डेवलपर्स टूल में देखने से, हम स्रोत देख सकते हैं:

`एक्शन` की वास्तविक वल्यू को पाने के लिए, हम पेज स्रोत को इन्स्पेक्ट कर सकते हैं:

`एक्शन` का मूल्य दूसरा लाइन का स्ट्रिंग है।

अब, हम IP एड्रेस कैसे प्राप्त करते हैं? लॉगिन सिस्टम को कैंपस के किसी भी हिस्से से, चाहे वह वाई-फाई हो या कॉलेज की एक डॉर्म रूम में कनेक्शन हो, एक्सेस किया जा सकता है। IP एड्रेस डायनामिक है। हम इसे ऑटोमैटिक रूप से कैसे प्राप्त कर सकते हैं?

पहला चित्र याद रखें?

वेबपेज IP एड्रेस ऑटोमैटिक रूप से प्रदान करता है। लॉगिन सिस्टम जानता है कि कौन सा IP उसे एक्सेस कर रहा है। हम इसे पेज से निकाल सकते हैं।

क्रोम को उपयोग में लाते हैं, जो वेबपेज के कोड के विशिष्ट हिस्से को तेजी से ढूंढने के लिए सुविधाजनक उपकरण प्रदान करता है। फायरफॉक्स में एक समान प्लगइन के नाम से फायरबग है।

"इंस्पेक्ट एलिमेंट" टूल (मैग्निफाइंग ग्लास आइकन) का उपयोग करके, हम पेज पर IP एड्रेस पर क्लिक कर सकते हैं।

डेवलपर्स टूल हमें HTML संरचना दिखेंगे, जो बताएगा कि IP एड्रेस एक `<span>` टैग के अंदर है, जिसका क्लास `login_txt` है, विशेष रूप से इसका टेक्स्ट कॉन्टेंट।

`select` फंक्शन में Jsoup CSS क्वेरी के लिए मिलने वाले तत्वों को ढूंढ सकता है, और `first()` पहले मिलने वाले तत्व को वापिस कर सकता है।

सभी की-वैल्यू पैरों के साथ, हम अब लॉगिन प्रक्रिया को सिमुलेट कर सकते हैं।

पोस्ट रिक्वेस्ट की-वैल्यू पैरों को रिक्वेस्ट बॉडी में भेजता है। `post.abort()` कॉल रिक्वेस्ट को रोका देता है। यह इसलिए है कि हम बाद के रिक्वेस्ट्स के लिए `httpClient` को पुनः उपयोग करेंगे। `org.apache.http` वर्गों का प्रयास होता है कि HTTP कनेक्शन को जितना संभव हो सके उतना ही पुनरخدام किया जाए। यदि एक रिक्वेस्ट संपन्न नहीं हो जाता, तो उसी कनेक्शन का उपयोग करके दूसरे रिक्वेस्ट भेजने से एक एक्सेप्शन हो सकता है।

हम `httpClient` को फिर से क्यों उपयोग करते हैं? मैं बाद में इसका स्पष्टिकरण करूँगा।

`checkLogin.jsp` को सबमिट करने से भी नेटवर्क से कनेक्ट होने में असफल रहेंगे। यह JSP केवल उपयोगकर्ता नाम और पासवर्ड सही हैं यानि यह केवल यह जांचता है।

एक प्रिंट स्टेटमेंट जोड़कर, हम रिस्पॉन्स कोड देख सकते हैं।

200 रिस्पॉन्स एक सफल लॉगिन को दर्शाता है, 303 गलत क्रेडेंशियल्स को दर्शाता है, और 404 एक कनेक्शन त्रुटि को दर्शाता है।

दूसरा जेएसपी स्क्रिप्ट जो चलता है `index.jsp` है, जो एक GET रिक्वेस्ट है।

उसके बाद भी हम अभी भी नेटवर्क से कनेक्ट नहीं होंगे। हम एक रिक्वेस्ट को `connect_action.jsp` को सिमुलेट करने की आवश्यकता है, जिसके लिए एक `userid` पैरामीटर (अर्थात `userid=88888`) की आवश्यकता होती है, जो एक छात्र ID के संबंधित है। मैंने देखा कि मेरे पूर्व छात्र ID से छात्र के पास `userid` केवल एक ही कम है। हम इस वल्यू को कैसे प्राप्त कर सकते हैं?

खुशकिस्मती से, मैंने याद किया कि हमने वेबपेज से IP एड्रेस निकाल लिया था। क्या हम इसके लिए `userid` भी कर सकते हैं?

यह स्क्रीनशॉट एक डिसकनेक्टेड पेज से है, लेकिन उसी तर्क को `connect.jsp` भी लागू करता है। दूसरे जेएसपी द्वारा लौटे गए पेज के स्रोत कोड में, अगले जेएसपी के लिए हमको रिक्वेस्ट करने की आवश्यकता है।

यहां हम एक रेगुलर एक्सप्रेशन का उपयोग करते हैं। `group(0)` पूरे मैच (अर्थात `userid=88888`) है, और `group(1)` पैरेंथिस के अंदर का सामग्री (अर्थात `88888`) है। `\d` किसी भी अंक के लिए मैच करता है, और `+` एक या अधिक बार हो सकता है। `find()` का उपयोग उस परिस्थिति का पता करने के लिए किया जाता है कि कोई व्यक्तिगत एक्सप्रेशन कोई हिस्सा है या नहीं, जबकि `matches()` पूरी स्ट्रिंग के साथ एक्सप्रेशन मैच करता है। इसलिए, यदि `src` जैसे है `<frame userid=88888&ip="`, `matches()` `false` लौटाएगा क्योंकि रेगुलर एक्सप्रेशन पूरी स्ट्रिंग के साथ मैच नहीं करता है।

यहाँ जावा कोड है:

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

पूर्ण स्रोत कोड GitHub पर उपलब्ध है। ध्यान रखें कि आप इसे एक वैध यूनिवर्सिटी नेटवर्क खाते के बिना चलाने में असमर्थ हो सकते हैं।

हम `HttpClient` को फिर से उपयोग करने का कारण यह है कि यह कुकिस को ऑटोमैटिक रूप से स्टोर करता है। JSP स्क्रिप्ट्स कुकिस का उपयोग करते हैं कि रिक्वेस्ट उस सेसन से हैं या नहीं। यही वजह है कि Taobao से किसी और ब्राउजर में URL को कॉपी करने से टाइमआउट त्रुटि हो सकती है।

`jsoup` और रेगुलर एक्सप्रेशन बहुत उपयोगी उपकरण हैं। इनके साथ पैसे बनाने के लिए ऑनलाइन उपकरण उपलब्ध हैं। इनके साथ उपयोग करने में मजे लेते हैं!