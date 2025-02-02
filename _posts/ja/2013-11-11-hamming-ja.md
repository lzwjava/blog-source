---
audio: false
lang: ja
layout: post
title: Hammingコードについて話す問題
translated: true
---

この投稿は元々中国語で書かれ、CSDNに掲載されました。

---

[問題リンク](https://www.luogu.com.cn/problem/P1461)

この問題では、任意の2つの数の間のハミング距離が少なくとも `d` となるように、辞書式に最小の `n` 個の数を探す必要があります。

ハミング距離は XOR を使って計算できます。`1^0=1`、`0^1=1`、`0^0=0`、`1^1=0` です。したがって、2つの数の XOR は、異なるビットをセットビットとして表現する数になります。その結果、セットビットの数をカウントすることができます。

私は一度、出力に10個の数を1行にし、最後の行が10未満の数を含む場合があることを忘れていました。最初の出力には、最後の数の後ろにトレーリングスペースがあり、その後に改行が含まれていました。

私は、コードがかなり良い関数型プログラミングスタイルだと思います。その利点は、構造化されているため、`main` が Lisp や他の関数型言語のトップレベルのように働くことです。

この方法で、新しい cpp ファイルを作成して未知の関数をテストしたり、個々の関数をデバッグしたりする必要はありません。`deal()` をコメントアウトし、`main` をトップレベルの REPL（読み取り-印刷-評価-ループ）として使用するだけです。

Lisp は、できるだけ関数型プログラミングを実行するように教えてくれました。この方法で、各関数は分離してデバッグでき、意味論も明確になります。例えば：

`hamming(0, 7, 2)` は、0 と 7 のバイナリ表現が少なくとも2ビット異なるかどうかを確認する意味です。7 は `111` ですので、3ビット異なりますし、関数は `true` を返します。

したがって、`deal()` をコメントアウトし、`hamming(0, 7, 2)` を追加してこの関数を独立してテストできます。

AC コード：

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