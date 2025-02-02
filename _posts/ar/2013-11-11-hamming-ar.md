---
audio: false
lang: ar
layout: post
title: حول FP مع مشكلة شيفرة هاملينغ
translated: true
---

هذا النشر كان مكتوبًا أصلا بالعربية ونُشرت على CSDN.

---

[الرابط للمشكلة](https://www.luogu.com.cn/problem/P1461)

تطلب المشكلة العثور على أصغر `n` من الأعداد من حيث الترتيب الأبجدي بحيث تكون المسافة الهمينغ بين أي عددين على الأقل `d`.

يمكن حساب مسافة الهمينغ باستخدام XOR. `1^0=1`، `0^1=1`، `0^0=0`، `1^1=0`. لذلك، XORing رقمين ستنتج في رقم حيث تمثل العناوين المحددات البتات المختلفة. ثم يمكننا حساب عدد العناوين المحددات في النتيجة.

قتيعت مرة بسبب الخطأ لأن الخرج يتطلب 10 أرقام في كل سطر، حيث يمكن أن يكون السطر الأخير أقل من 10. كان خروجي الأول يحتوي على فاصل بعد آخر رقم في السطر الأخير متبوعًا بخط جديد.

أعتقد أن هذا هو كود في أسلوب البرمجة الوظيفية. الفائدة هي أنه أكثر تنظيمًا، مما يجعل `main` يعمل مثل المستوى الأعلى في Lisp أو لغات البرمجة الوظيفية الأخرى.

بذلك، لا تحتاج إلى إنشاء ملف cpp جديد للتجربة على وظائف غير مألوفة أو تصحيح الأخطاء في وظائف منفصلة. يمكنني فقط تعليق `deal()` واستخدام `main` كواجهة خطية (read-print-eval-loop).

تعلمني Lisp أيضًا البرمجة بأقصى قدر ممكن من الوظائف، FP! بهذه الطريقة، يمكن استخراج كل وظيفة واستكشاف الأخطاء منفردًا. أيضًا، تكون المعاني أكثر وضوحًا. على سبيل المثال:

`hamming(0, 7, 2)` يعني التحقق من أن التمثيلات الثنائية لـ 0 و 7 تختلف بأقل من 2 بت. 7 هو `111`، فلا يختلفان بأكثر من 3 بتات، وتعود الوظيفة إلى `صحيح`.

وبالتالي، يمكنني تعليق `deal()` وإضافة `hamming(0, 7, 2)` لاختبار هذه الوظيفة بشكل مستقل.

كود من أجل قبول:

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