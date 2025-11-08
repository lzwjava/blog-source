---
audio: false
generated: false
image: false
lang: ar
layout: post
title: تحليل نظام تسجيل الدخول بجامعة بكين للغابات
translated: true
type: post
---

هذا المقال كان مكتوبًا بالأصل بالعربية ونُشرت على [CSDN](https://blog.csdn.net/lzw_java/article/details/18049581).

---

يتناول هذا المقال عملية الهندسة العكسية للنظام الذي يستخدمه جامعة بكين للزراعة في تسجيل الدخول عبر الإنترنت.

الهدف هو تقليد عملية تسجيل الدخول بنظام برنامجي، مما يتيح لك تقليد أفعال المستخدم الذي يتصل بالشبكة من خلال متصفح ويب.

باستخدام أدوات تطوير Google Chrome، يمكننا مراقبة الطلبات الشبكية التي يتم إرسالها خلال عملية تسجيل الدخول.

الطلب الأول هو إلى `CheckLogin.jsp`، يليه طلب إلى `index.jsp` الذي يتم إبداله بناءً على `CheckLogin.jsp`.

دعونا ننظر إلى `CheckLogin.jsp` بشكل أقرب.

نرى أنه يستخدم طلب POST ويحتوي على عدة أزواج من المفتاح والقيمة. ولكن ما هو `action`؟ من خلال فحص "Form Data" في أدوات التطوير، يمكننا مشاهدتها المصدر:

لإيجاد القيمة الفعلية لـ `action` ، يمكننا فحص مصدر الصفحة:

قيمة `action` هي السطر الثاني.

ولكن كيف نحصل على عنوان IP؟ يمكن الوصول إلى نظام تسجيل الدخول من أي مكان في الحرم الجامعي، سواء كانت عبر Wi-Fi أو اتصال باسلكي في غرفة نوم. عنوان IP هو ديناميكي. كيف يمكننا الحصول عليه بشكل تلقائي؟

تذكر الصورة الأولى؟

توفر الصفحة الويب عنوان IP تلقائيًا. يعرف النظام تسجيل الدخول أي IP لا يمكن الوصول إليه. يمكننا استخراجها من الصفحة الويب.

يوفر Chrome أدواتًا مفيدة لإنشاء أجزاء محددة من كود الصفحة الويب بسرعة. وفيرفوكس يوجد ملحق مماثل يسمى Firebug.

على الرغم من أننا استخدمنا "أداة فحص العنصر" (أيقونة الميكروسكوب)، يمكننا النقر على عنوان IP على الصفحة.

سيعرض أدوات التطوير بنية HTML وتكشف أن عنوان IP هو داخل علامة `<span>` مع الفئة `login_txt`، تحديدًا داخل محتوا النص.

يمكن أن يجد وظيفة `select` في Jsoup العناصر التي تتطابق مع استعلام CSS، ويمثل `first()` العنصر الأول المطابق.

مع جميع أزواج المفتاح والقيمة، يمكننا الآن تقليد عملية تسجيل الدخول.

 envie من POST يرسل أزواج المفتاح والقيمة في جسم الطلب. يوقف `post.abort()` الطلب. ذلك لأننا سنستخدم `httpClient` مرة أخرى في طلبات لاحقة. تفضل فئات `org.apache.http` إعادة استخدام اتصال HTTP قدر الإمكان. إذا لم يتم إنهاء الطلب، يمكن أن يسبب إرسال طلب آخر باستخدام نفس الاتصال استثناء.

لماذا نريد إعادة استخدام `httpClient`؟ سأشرح ذلك لاحقًا.

إرسال إلى `checkLogin.jsp` غير كافٍ للرابطة بالشبكة. هذه الصفحة JSP فقط تحقق من صحة اسم المستخدم وكلمة المرور.

من خلال إضافة بيان طباعة، يمكننا رؤية الرمز الرد.

يرمز 200 إلى تسجيل دخول ناجح، يرمز 303 إلى بيانات اعتماد خاطئة، و404 إلى خطأ في التوصيل.

الصفحة JSP الثانية التي يتم تنفيذها هي `index.jsp`، وهي طلب GET.

بعد ذلك، لا يمكننا بلوغ الشبكة. علينا تقليد طلب إلى `connect_action.jsp`، الذي يتطلب مبرر `userid` (مثل `userid=88888`) الذي يتوافق مع رقم طالب. لاحظت أن `userid` للطالب الذي لديه الرقم السابق هو أقل من 1 من الرقم. كيف يمكننا الحصول على هذه القيمة؟

لحسن الحظ، تذكرت أننا استخرجنا عنوان IP من الصفحة الويب. هل يمكننا القيام بنفس الشيء مع `userid`؟

هذه الصورة من الصفحة المنقطعة، ولكن نفس اللوجيك 적용 على `connect.jsp`. يحتوي مصدر الصفحة الذي يُرجعه JSP الثاني على زوج المفتاح والقيمة المطلوبين لصفحة JSP التالية التي يجب علينا إرسالها.

في هذه الحالة، نعتمد على تعبيرًا معياريًا. `group(0)` هو التطابق الكامل (مثل `userid=88888`)، `group(1)` هو المحتوى داخل الأقواس (مثل `88888`). `\d` تطابق أي رقم، و `+` يعني حدوث مرة واحدة أو أكثر. `find()` يحدد ما إذا كان التعبير يتطابق مع أي جزء من السلسلة بينما `matches()` يحدد ما إذا كان التعبير يتطابق مع السلسلة بأكملها. إذا كان `src` مثل `<frame userid=88888&ip="`، فإن `matches()` سيرجع `false` لأن التعبير المعتاد لا يتطابق مع السلسلة بأكملها.

هذا هو الكود Java:

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

يوجد الكود الكامل على GitHub. لاحظ أنه قد لا يمكنك تشغيله دون حساب صالح لشبكة الجامعة.

سبب إعادة استخدام نفس `HttpClient` هو أنه يوفر تخزين الطعنات تلقائيًا. تستخدم صفحات JSP الطعنات لتحديد ما إذا كان الطلبات من نفس الجلسة. هذا هو السبب في أن نسخ رابط من Taobao إلى متصفح آخر قد يؤدي إلى خطأ في الوقت.

`jsoup` وعبارات معيارية هي أدوات مفيدة جدًا. توجد أدوات على الإنترنت لتمارين عبارات معيارية. استمتع باستخدامها!