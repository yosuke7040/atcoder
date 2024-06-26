Python で割り算を行う際に演算子 / を使うと、計算結果が小数型(float 型)になってしまいます。
整数値を出力したい場合は、演算子 // を使いましょう。

max(a, b, c, d)みたいに何個でも max 探してくれる

[2-10]
Python の場合文字列の一部の文字を単純に変更することはできません。
そのため、文字列を配列型に変換してから要素を入れ替え、文字列型に戻す必要があります。
S = "algo"
S[0] = "b" # エラーが発生する

python の再起関数はデフォで 1000 回しか回せないので増やす
import sys
sys.setrecursionlimit(10\*\*6)

python でインクリメント使えないじゃん

### 029 C

- 順列・組み合わせ(<https://cocoinit23.com/python-itertools/>)

### 141 D

- 優先度付きキュー

heappopは最小値の取り出し。最大値の取り出しは、ひと手間必要(<https://qiita.com/ell/items/fe52a9eb9499b7060ed6>)

```python
import heapq
a = [1, 6, 8, 0, -1]
a = list(map(lambda x: x*(-1), a))  # 各要素を-1倍
print(a)

heapq.heapify(a)
print(heapq.heappop(a)*(-1))  # 最大値の取り出し
print(a)
```

### 149 C

- 素数の計算
  素数判定のアルゴリズム（<https://algo-method.com/descriptions/93>）
  Nの平方根までの計算で良い
  ```python
  # 素数を判定する関数
  def isprime(N):
      if N < 2:
          return False
      i = 2
      while i * i <= N:
          if N % i == 0:
              return False
          i += 1
      return True
  ```

### 154 D

- 和の公式
  1/2 * n * (n+1)

### 158 D

- 「文字を先頭に加える」という操作は文字列やリストでやると文字列の長さをNとして計算量がO(N)かかってしまう
- dequeで対応する
- 要素の追加
  - 末尾：append(要素)
  - 先頭：appendleft(要素)
- 要素の取り出し
  - 末尾から：pop()
  - 先頭から：popleft()

### ✅167 C

- bit全探索
  N=22がギリギリ限界

以下は一緒な考え方になる
```python
for i in range(2**N):

for i in range(1<<N):
```

だいたいこんな感じの実装になるはず
```python
for bit in range(1 << N):
    for i in range(N):
        if bit & (1 << i):
            cost += C[i]
```

### 180 C

- 約数列挙

1. N が 1 で割り切れるか確認する。(絶対に割り切れる)→1 と、N//1 を約数として記録。

2. N が 2 で割り切れるか確認する。割り切れるなら →2 と、N//2 を約数として記録。
3. N が 3 で割り切れるか確認する。割り切れるなら →3 と、N//3 を約数として記録。
   …
4. √N<(割る数)になったら終わり。記録した約数を出力する。

```python
平方根
math.sqrt(N)

切り上げ
math.ceil(N)
```

### 181 C

- 二次元平面上で 3 点が同一直線上にあるか判定する方法

### ✅182 C

- 余りの足し算、引き算、掛け算

- 全桁の足し算が X の倍数ならばもとの数も X の倍数
  - 例）3
  - 123 は 1+2+3=6 で全桁の足し算が 3 の倍数 →123 も 3 の倍数
- 余りの計算は足し算と引き算ができる

### 189 B

- 少数の計算は注意
- 少数が出てくる計算を避けられる実装をできるように
  - パーセントの計算がある場合は最初から 100 倍にして計算するとか

### 195 B

- 最小値、最大値を求める問題。
- 計算量が問題にならなければ、最小値の初期値はバカでかい数(=10^15)で、最大値の初期値はとてつもなく小さい数(=10^15)にして計算するのが良い。

### 199 C

- 文字列の並び替えは一見O(1)でできそうだが実際には文字列の長さをNとしてO(N)かかる

### 201 C

- 文字列・数値をゼロ埋め（ゼロパディング）
- 右寄せゼロ埋め: zfill()
- 右寄せ、中央寄せ、左寄せ: rjust(), center(), ljust()

```python
s = '1234'
print(s.zfill(8))
# 00001234
```

### 237 D

- 双方向連結リスト
- 両端queue

### 337 B

- char の文字は大小で比較可能
  - `A < B`は True
  - `A > B`は False

### 338 C

- 線形計画法

  ```python
  import pulp

  # 線形計画の定義 (整数計画問題)
  problem_min = pulp.LpProblem("minimize problem", pulp.LpMinimize)
  problem_max = pulp.LpProblem("Maximize problem", pulp.LpMaximize)

  # 変数の定義
  # 変数名→最小値→最大値→変数の種類
  x = pulp.LpVariable("x", 0, None, pulp.LpInteger)
  y = pulp.LpVariable("y", 0, None, pulp.LpInteger)

  # 目的関数の定義
  problem += x + y

  # 制約条件の定義
  for i in range(N):
      problem += A[i] * x + B[i] * y <= Q[i]

  # 問題を解く
  problem.solve(pulp.PULP_CBC_CMD(msg=False))

  print(int(pulp.value(problem.objective)))
  ```

### 340 A

- 数値の配列をスペースごとに出力
  ans = [1,2,3]
  print(" ".join(map(str, ans)))
  出力 -> 1 2 3

### 340 C

- 繰り上げの割り算
  math.ceil(N / 2)とかしてたが、(N + 1) // 2でいける

- メモ化再帰

  デコレータを使ってメモ化再帰は簡単に解ける

  ```python
  from functools import cache

  @cache
  def f(N):
    return 0 if N == 1 else f(N // 2) + f((N + 1) // 2) + N
  ```

### 346 C

- sortはHackされるとO(N)になる
  - <https://atcoder.jp/contests/abc346/editorial/9635>
- Hackを防ぐために乱数を使うか、赤黒木で実装されたSortedSetを使うか
  - <https://www.youtube.com/watch?v=NireH9qqt3Y>

### 357 D

- 合同式、逆元、フェルマーの小定理、mod
- <https://www.creativ.xyz/modulo-basic/>こっちのほうがわかりやすいかも
- <https://drken1215.hatenablog.com/entry/2023/12/06/020241>

```text
最低限必要な知識を超特急でおさらいすると......

a+b を 998244353 で割った余りを求めたいときは、先に a,b を 998244353 で割った余りに置き換えて、それらを足して、改めて 998244353 で割った余りを求めてもよい

a×b を 998244353 で割った余りを求めたいときは、先に a,b を 998244353 で割った余りに置き換えて、それらをかけて、改めて 998244353 で割った余りを求めてもよい

ということを確認しておきましょう。このように、「計算したい各値について、先に 98244353 で割った余りを求めてから、計算しても結果は変わらない」という事実はとても重要です。


mod の世界でも同様です。mod の世界でも、普通の数の世界における「逆数」に対応する概念として、「逆元」という概念
mod 998244353  における a の逆元とは、「a にかけてあまりが1になる数」のこと
```
### 358 E

- 文字列の組み合わせDP


## 文字扱い

- 数値を2進数、8進数、16進数表記の文字列に変換
  - bin(x)
  - oct(x)
  - hex(x)

### 文字列

- 反転出力
  - string[::-1]

### 文字チェック

- 文字列が十進数字か判定: str.isdecimal()
- 文字列が数字か判定: str.isdigit()
- 文字列が数を表す文字か判定: str.isnumeric()
- 文字列が英字か判定: str.isalpha()
- 文字列が英数字か判定: str.isalnum()
- 文字列がASCII文字か判定: str.isascii()

### 組み合わせ（initertools）

- 順列
(1,2,3),(1,3,2),(2,1,3),(2,3,1),...,(3,2,1)
for seq in itertools.permutations(range(1,4)):

- 重複なしの組み合わせ
(1,2,3),(1,2,4),...,(7,8,9)
for seq in itertools.combinations(range(1,10),3):

- 重複ありの組み合わせ
(1,1,1),(1,1,2),...,(9,9,9)
for seq in itertools.combinations_with_replacement(range(1,10),3):

- 直積
(1,1),(1,2),(1,3),(2,1),(2,2),...,(3,3)
for seq in itertools.product(range(1,4),range(1,4)):
