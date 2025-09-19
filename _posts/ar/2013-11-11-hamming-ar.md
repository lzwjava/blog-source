---
audio: false
generated: false
image: false
lang: ar
layout: post
title: نُقاش الترميز الإرشادي مع المشكلات الحمية
translated: true
---

هذا المنشور كان مكتوبًا بالصينية وأُنشر على CSDN.

---

[روابط المشكلة](https://www.luogu.com.cn/problem/P1461)

المسألة تطلب إيجاد أصغر `n` أرقام من حيث الترتيب اللفظي بحيث تكون المسافة الهامينغ بين أي زوج من الأرقام على الأقل `d`.

يمكن حساب المسافة الهامينغ باستخدام XOR. `1^0=1`, `0^1=1`, `0^0=0`, `1^1=0`. لذلك، XOR بين زوج من الأرقام سينتج رقمًا حيث تمثل الأعداد المفعلة الأرقام المختلفة. ثم يمكننا حساب عدد الأعداد المتفاعلة في النتيجة.

أرتكب خطأ مرة واحدة لأنه يجب أن يكون الإخراج 10 أرقام في كل سطر، بينما يمكن أن يكون السطر الأخير يحتوي على أقل من 10. كان الإخراج الأولي لدي يحتوي على فراغ بعد آخر رقم في الأخير، متبوعًا بصفحة جديدة.

أعتقد أن هذا هو كود ممتاز بالبرمجة الوظيفي. الفائدة هي أن له بنية أفضل، مما يجعل `main` يعمل مثل المستوى الأعلى في Lisp أو لغات برمجة وظيفية أخرى.

بهذه الطريقة، لا needing أن أعمل على ملف cpp جديد للاختبار الوظائف الغير مألوفة أو تصحيح الوظائف الفردية. يمكنني ببساطة تعليق `deal()` واستخدام `main` ك REPL مستوى أعلى (read-print-eval-loop).

Lisp أيضًا علمتني البرمجة بقدر ما يمكن، FP! بهذه الطريقة، يمكن استخراج كل وظيفة وتصححها بشكل منفصل. أيضًا، الأعراف أكثر وضوحًا. على سبيل المثال:

`hamming(0, 7, 2)` يعني فحص ما إذا كانت التعبيرات الثنائية لـ 0 و 7 تختلف ب 2 بتات على الأقل. 7 هو `111`، لذلك تختلف ب 3 بت، وتعود الوظيفة إلى `true`.

إذن، يمكنني تعليق `deal()` وإضافة `hamming(0, 7, 2)` لاختبار هذه الوظيفة بشكل منفصل.

AC Code:

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
```

```