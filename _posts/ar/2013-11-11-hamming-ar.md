---
audio: false
lang: ar
layout: post
title: تحدث عن FP باستخدام بوليات هاملينغ
translated: true
---

هذا المقال كان مكتوبًا أصلاً باللغة الصينية ونشر على CSDN.

---

[رابط المشكلة](https://www.luogu.com.cn/problem/P1461)

يتطلب السؤال العثور على `n` أصغر عدد من حيث الترتيب الكتبي بحيث تكون المسافة الهامينغ بين أي رقمين على الأقل `d`.

يمكن حساب المسافة الهامينغ باستخدام XOR. `1^0=1`, `0^1=1`, `0^0=0`, `1^1=0`. فإجراء XOR بين رقمين سيؤدي إلى عدد حيث تتوضع الأرقام المعبأة على الحروف المختلفة. ثم يمكن حصر عدد الأرقام المعبأة في النتيجة.

ارتكبت خطأً مرة واحدة لأن الأخرجات يتطلب 10 أرقام في كل سطر، مع أن الأخير قد يكون أقل من 10. كان لدىzad كود أولي يحتوي على فراغ بعد آخر عدد في السطر الأخير، يليه newline.

أعتقد أن هذا هو حاسب جيد. فائدة ذلك هي أن تكون أكثر تنظيمًا، مما يجعل `main` يعمل مثل المستوى الأعلى في Lisp أو لغات أخرى وظيفية.

بهذا الطريق، لا تحتاج إلى إنشاء ملف cpp جديد لتجربة وظائف غريبة أو تصحيح وظائف منفردة. يمكنني فقط كتابة تعليق على `deal()` واستخدام `main` كأعلى مستوى REPL (read-print-eval-loop).

أعلمني Lisp أيضًا أن أكتب ككاتب وظيفي قدر الإمكان، FP! بهذه الطريقة، يمكن أن يتم استخراج كل وظيفة وتصحح منفصلة. أما الأسلوبية، فهي أكثر وضوحًا. على سبيل المثال:

`hamming(0, 7, 2)` يعني فحص ما إذا كانت الترميز الثنائي لـ 0 و 7 تختلف على الأقل 2 بت. 7 هو `111`، لذا فهي تختلف عن 3 بت، وتسترجع الوظيفة قيمة صحيحة.

ف могу أن أنشئ تعليق على `deal()` وأضيف `hamming(0, 7, 2)` لتجربة هذه الوظيفة بشكل مستقل.

الرمز AC:

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