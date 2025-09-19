---
audio: false
generated: false
image: false
lang: hi
layout: post
title: Hamming Code problem पर बात करना
translated: true
---

यह पोस्ट मूल रूप से चीनी में लिखा गया था और CSDN पर प्रकाशित किया गया था.

---

[समस्या लिंक](https://www.luogu.com.cn/problem/P1461)

समस्या से पूछता है कि एक्सी के लिए अल्फ़ाबेटिक रूप से सबसे छोटे `n` संख्या खोजें, ताकि किसी दो संख्याओं के बीच हैमिंग दूरी कम से कम `d` हो।

हैमिंग दूरी को XOR का उपयोग करके गणना की जा सकती है। `1^0=1`, `0^1=1`, `0^0=0`, `1^1=0`। तो, दो संख्याओं का XOR करने से एक संख्या मिलेगी जहां सेट बिट्स में भिन्न बिट्स का प्रतिनिधित्व किया जाता है। फिर हम परिणाम में सेट बिट्स की संख्या गिन सकते हैं।

मैं एक बार ऐसा गलती कर गया जब कि आउटपुट के लिए प्रत्येक लाइन पर 10 संख्या की आवश्यकता होती है, और अंतिम लाइन में 10 से कम भी हो सकती है। मेरा पहला आउटपुट अंतिम लाइन पर अंतिम संख्या के बाद एक ट्रेलिंग स्पेस और एक नया लाइन था।

मैं सोचता हूँ कि यह एक अच्छा यूजर्स रीड-प्रिंट-इवैलुएट-लूप (REPL) बनेगा। फंक्शनल प्रोग्रामिंग शैली में लिखा गया है।

इस तरह, मुझे अनजान फंक्शनों को टेस्ट करने या अलग-अलग फंक्शन को डिबग करने के लिए एक नया cpp फ़ाइल बनाना नहीं होगा। मैं बस `deal()` को टिप्पणी कर सकता हूं और `main` को एक टॉप-लेवल REPL (रेड-प्रिंट-इवैलुएट-लूप) के रूप में उपयोग कर सकता हूँ।

लिस्प ने मुझे भी एक्सी-फंक्शनल रूप से प्रोग्राम करने के लिए सिखाया। इस तरह, हर फंक्शन को अलग-अलग से जांचा और डिबग किया जा सकता है। सांकेतिक भी स्पष्ट हैं। उदाहरण के लिए:

`hamming(0, 7, 2)` का मतलब है कि 0 और 7 के बाइनरी प्रतिनिधित्व में कम से कम 2 बिट्स अंतर हो। 7 `111` है, इसलिए वे 3 बिट्स से अलग हैं और फंक्शन फेर्ष返回 करता है।

तो, मैं `deal()` को टिप्पणी कर सकता हूँ और `hamming(0, 7, 2)` जोड़ सकता हूँ, इस फंक्शन को स्वतंत्र रूप से टेस्ट करने के लिए।

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