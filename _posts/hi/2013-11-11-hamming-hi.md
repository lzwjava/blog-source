---
audio: false
lang: hi
layout: post
title: Floating Point ke Saath Hamming Codes Samasya Charcha
translated: true
---

यह पोस्ट मूल रूप से चीनी में लिखी गई थी और CSDN पर प्रकाशित हुई थी।

---

[प्रश्न लिंक](https://www.luogu.com.cn/problem/P1461)

इस प्रश्न में `n` अंकों में से लेक्सिकोग्राफी (अक्षराणुक्रम में) सबसे छोटे `n` अंक खोजने हैं, ताकि किसी भी दो अंकों के बीच हैमिंग दूरी कम से कम `d` हो।

हैमिंग दूरी XOR का उपयोग करके की जा सकती है। `1^0=1`, `0^1=1`, `0^0=0`, `1^1=0`. इसलिए दो संख्यों को XOR करने से एक ऐसी संख्या मिलेगी, जिसमें सेट बिट्स अलग-अलग बिट्स को दर्शाते हैं। फिर हम परिणाम में सेट बिट्स की संख्या गिन सकते हैं।

मुझे एक बार एक गलती हुई थी क्योंकि आउटपुट में 10 अंक प्रति पंक्ति चाहिए, और आखरी पंक्ति में कम से कम 10 से कम अंक हो सकते हैं। मेरे आरंभिक आउटपुट में आखरी पंक्ति के आखरी अंक के बाद एक ट्रेलिंग स्पेस था, जिसके बाद न्यूलाइन था।

मैं सोचता हूँ कि यह एक बहुत अच्छा फंक्शनल प्रोग्रामिंग शैली का कोड है। इसका लाभ यह है कि यह अधिक संरचित है, जिससे `main` Lisp या अन्य फंक्शनल भाषाओं में टॉप-लेवल जैसा काम करता है।

इस तरह, मुझे किसी नए cpp फ़ाइल के लिए अनजान फ़ंक्शन को टेस्ट करने या किसी व्यक्तिगत फ़ंक्शन को डिबग करने की आवश्यकता नहीं होती है। मैं बस `deal()` को टिप्पणी कर सकता हूँ और `main` को टॉप-लेवल REPL (रेड-प्रिंट-इवल्यू-लूप) के रूप में उपयोग कर सकता हूँ।

Lisp ने मुझे संभव रूप से सबसे अधिक फंक्शनल रूप से प्रोग्रामिंग करने के बारे में सिखाया। इस तरह, हर फ़ंक्शन को अलग से निकाल और डिबग किया जा सकता है। सिमांटिक्स भी स्पष्ट होते हैं, उदाहरण के लिए:

`hamming(0, 7, 2)` का अर्थ है कि 0 और 7 के बाइनरी प्रतीकों में कम से कम 2 बिट्स अलग हों। 7 `111` है, तो वे 3 बिट्स अलग हैं, और फ़ंक्शन सत्य लौटाता है।

तो, मैं `deal()` को टिप्पणी कर सकता हूँ और `hamming(0, 7, 2)` को जोड़ सकता हूँ इस फ़ंक्शन को स्वतंत्र रूप से टेस्ट करने के लिए।

AC कोड:

```java
/*
{
ID: lzwjava1
PROG: hamming
LANG: C++
}
*/
#include<cstdio>
#include<cstring>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<ctime>
using namespace std;
const int maxn=1000;

bool hamming(int a,int b,int d)
{
	int c=a^b;
	int cnt=0;
	for(int i=0;i<=30;i++)
	{
		if((1<<i) & c)
		{
			cnt++;
			if(cnt>=d) return true;
		}
	}
	return false;
}

void printArr(int *A,int n)
{
	for(int i=0;i<n;i++)
	{
		printf("%d",A[i]);
		if((i+1)%10==0 || (i==n-1)) printf("\n");
		else printf(" ");
	}
}

bool atLesat(int *A,int cur,int i,int d)
{
	for(int j=0;j<cur;j++)
		if(!hamming(A[j],i,d))
			return false;
	return true;
}

void dfs(int *A,int cur,int n,int d)
{
	if(cur==n)
	{
		printArr(A,n);
		return;
	}
	int st=(cur==0? 0: A[cur-1]+1);
	for(int i=st;;i++)
	{
		if(atLesat(A,cur,i,d))
		{
			A[cur]=i;
			dfs(A,cur+1,n,d);
			return;
		}
	}
}

void deal()
{
	int n,b,d;
	scanf("%d%d%d",&n,&b,&d);
	int A[n];
	dfs(A,0,n,d);
}

int main()
{
  freopen("hamming.in","r",stdin);
  freopen("hamming.out","w",stdout);
	deal();
	//printf("%.2lf\n",(double)clock()/CLOCKS_PER_SEC);
  return 0;
}

/*
*/
```