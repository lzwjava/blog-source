---
audio: false
generated: false
lang: ja
layout: post
title: ハミング符号の問題についてFPを論じる
translated: true
---

この記事は元々中国語で書かれ、CSDNに掲載されました。

---

[問題のリンク](https://www.luogu.com.cn/problem/P1461)

この問題では、ハミング距離が少なくとも `d` であるように、辞書順に最小の `n` 個の数を見つけることが求められています。

ハミング距離はXORを使って計算できます。`1^0=1`、`0^1=1`、`0^0=0`、`1^1=0` です。したがって、2つの数にXORをかけると、異なるビットを表すセットビットが含まれる数が得られます。その後、結果のセットビットの数をカウントします。

一度、出力が1行に10個の数を要すること、最後の行に10未満の数が含まれることができることを忘れてしまったため、エラーが発生しました。私の最初の出力では、最後の数の後に改行の前に余分なスペースがありました。

これは、私にとって非常に良い関数型プログラミングスタイルのコードだと思います。その利点は、構造化されていることで、`main`がLispや他の関数型言語のトップレベルのように動作します。

この方法では、未知の関数をテストしたり、個々の関数をデバッグするために新しいcppファイルを作成する必要がありません。`deal()`をコメントアウトし、`main`をトップレベルのREPL（リードプリント評価ループ）として使うだけです。

Lispも私にできる限り関数的にプログラムを作ることを教えてくれました。FP! この方法では、各関数を個別に抽出し、デバッグできます。意味論も明確です。例えば：

`hamming(0, 7, 2)`は、0と7のバイナリ表現が少なくとも2ビット異なるかどうかを確認することを意味します。7は`111`なので、3ビット異なり、関数はtrueを返します。

したがって、`deal()`をコメントアウトし、`hamming(0, 7, 2)`を追加して、この関数を独立してテストできます。

ACコード：

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