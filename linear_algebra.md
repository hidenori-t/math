# linear algebra (線形代数)

### 参考文献

1. 泉屋 周一:『[初級 線形代数](http://amzn.to/2ekvaC5)』共立出版，2008．
1. 海野 裕也  (著)，岡野原 大輔  (著)，得居 誠也  (著)，徳永 拓之  (著):『[オンライン機械学習 (機械学習プロフェッショナルシリーズ)](http://amzn.to/2ekqQmB)』講談社，2015．  
1. 竹内 淳:『[高校数学でわかる線形代数](http://amzn.to/2eTX6sP)』講談社，2010．
1. 平岡 和幸:『[プログラミングのための線形代数](http://amzn.to/2ekqInc)』オーム社, 2004．  
1. [線形代数学とは by.大学の物理学](https://youtu.be/BGCgcTO4nbk)

## 線形代数学とは  
  線形性をもつ対象(ベクトル空間と線形写像)について研究する学問(代数学の一分野)   
  一言で言えば「行列」と「ベクトル」の学問



# 第1章 行列の代数的性質
## 1.2
## 行列の和
同じ型の行列 $\mathbf{A},\mathbf{B}$ について,それぞれの行列の対応する成分の和を成分とする行列を $\mathbf{A},\mathbf{B}$ の和と呼び $\mathbf{A}+\mathbf{B}$ で表す．  
すなわち，  
$\mathbf{A}=(a_{ij}),\mathbf{B}=(b_{ij})$ をともに $m \times n$行列とするとき，  
$\mathbf{A}+\mathbf{B}=(a_{ij}+b_{ij})$ である．  
ただし,違う型の行列どうしの和は定義しない．

## スカラー倍(scalar multiplication)

行列 $\mathbf{A}$ と数 (scalar) $k$について各成分の$k$倍を成分とする行列を行列 $\mathbf{A}$ の$k$倍と呼び $kA$ で表す．   
すなわち，  
$\mathbf{A} = (a_{ij})$ と数$k$に対して，$kA = (ka_{ij})$ である．

## 零行列またはゼロ行列
各成分が全て $0$ である行列を,零行列またはゼロ行列といい $\mathbf{O}$ で表す．

$$
\mathbf{O}_{2,3}=\left( \begin{matrix} 0& 0& 0\\ 0& 0& 0\end{matrix} \right),
\quad
\mathbf{O}_{3}=\left( \begin{matrix} 0& 0& 0\\ 0& 0& 0\\ 0& 0& 0\end{matrix} \right)
$$

任意のベクトル $\boldsymbol{ x }$ に対して $\boldsymbol{ Ox } = \boldsymbol{ o }$ なので，ゼロ行列が表している写像は，すべてを原点に移す写像

## 1.3.1
## 行列の積
$\mathbf{AB = BA}$ とはかぎらない．

一般に，$\mathbf{A}$ を $m \times n$ 行列，$\mathbf{B}$ を $n \times p$ 行列とする．   
このとき $\mathbf{A}$ の第 $i$ 行と $\mathbf{B}$ の第 $j$ 列はともに $n$ 個の成分からなっているので，
その対応する成分の積の和

$$ c_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}= a_{i1}b_{1j}+a_{i2}b_{2j}+ \cdot\cdot\cdot +a_{in}b_{nj} \ \ \ (1 \leq i \leq m; 1 \leq j \leq p)$$

$\mathbf{A}$ の列数 $n$ と $\mathbf{B}$ の行数 $n$ なので $\mathbf{A}\mathbf{B}$ の積を定義出来る．

**$\mathbf{B}$ の列数 $p$ と $\mathbf{A}$ の行数 $m$ は一致しないので $\mathbf{BA}$ の積は定義出来ない．**

## 単位行列
単位行列 $\mathbf{I}$ は，掛けても変わらない行列のことで，数の場合の $1$ と同じような役割をになうもの．
一般に $n$ 次正方行列で $\mathbf{A}_{11}=a_{22}=\cdots=a_{nn}=1$ で，それ以外の成分が $0$ である行列を $n$ 次の単位行列と呼ぶ．
$n$ 次正方行列[単位行列と同じ行数の正方行列] $\mathbf{A}$ に対して $\mathbf{A} \mathbf{I} = \mathbf{I} \mathbf{A}  = \mathbf{A}$ という性質をもつ．


$2$ 次の単位行列
$$
\mathbf{I}_{2} =
\left(
    \begin{array}{cc}
      1 & 0  \\
      0 & 1  \\
    \end{array}
  \right)
= diag \ (1, 1)
$$

$n$ 次の単位行列

\[
  \mathbf{I}_{n} = \left(
    \begin{array}{cccc}
      1 & 0 & \ldots & 0 \\
      0 & 1 & \ldots & 0 \\
      \vdots & \vdots & \ddots & \vdots \\
      0 & 0 & \ldots & 1
    \end{array}
  \right)
= diag \ (1,\ldots ,1)
\]

また,零行列 $\mathbf{O}$ に対しては，$\mathbf{AO = AO = O}$ が成り立つ．

## 1.4
##正則行列
$2$ 次行列 $\mathbf{A}$ が正則であるとは, $2$ 次行列 $\mathbf{X}$ が存在して $\mathbf{AX = XA = I}$ を満たすことをいう．  
正則行列 $\mathbf{A}$ に対して $\mathbf{AX = XA = I}$ を満たす $X$ はただ一つしかない．   
このことから，$X$ は $\mathbf{A}$ だけから定まることがわかり，  
この $X$ を今後 $\mathbf{A}^{-1}$($\mathbf{A}$ インバース)と書き，  
$\mathbf{A}$ の **逆行列(inverse matrix)** と呼ぶ．  
すなわち，  
$\mathbf{A}$ の逆行列とは $\mathbf{AA}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$ によって定まる正方行列 $\mathbf{A}^{-1}$ のことである．
***
Definition
* 行列 $\mathbf{P}$ が正則であるとは，
$\mathbf{P}^{-1}\mathbf{P} = \mathbf{PP}^{-1} = \mathbf{I}$
を満たす行列 $\mathbf{P}^{-1}$ が存在するときをいう．
*  $\mathbf{P}^{-1}$ を $\mathbf{P}$ の逆行列と呼ぶ．

## 1.5
## 転置行列 (transposed matrix)

$\mathbf{A}^{\top}, \mathbf{A}^\mathrm{T}, {}^t\!\mathbf{A}$

等さまざまな表現があり，$\mathbf{A}$ トランスポーズ，$\mathbf{A}$ 転置 と発音される．

## 2次対角行列
$$
\left(
    \begin{array}{cc}
      a & 0  \\
      0 & d  \\
    \end{array}
  \right)
$$

の形の行列を2次対角行列と呼ぶ．  

正方行列の $a_{11}, a_{22}, \cdots, a_{nn}$ の値を **対角成分** という．  
対角成分以外の値は，**非対角成分**  
非対角成分がすべて $0$ の行列を **対角行列(diagonal matrix)** と呼ぶ．

$$
\left( \begin{matrix} a_{1}& & \\ & \ddots & \\ & & a_{5}\end{matrix} \right)= diag \ (a_{1},a_{2},a_{3},a_{4},a_{5})
$$
のように略記できる．  
diag は diagonal（対角線 ダイアゴナル）の略

単位行列は $a_{11}=a_{22}=・・・=a_{nn}=1$ なので別

## 2次対称行列
より一般に $2$ 次行列 $\mathbf{A}$ が $\mathbf{A}^{\top}  = \mathbf{A}$ を満たすとき，  
$\mathbf{A}$ は $2$ 次対称行列と呼ぶ．

$$
\left(
    \begin{array}{cc}
      a & b  \\
      c & d  \\
    \end{array}
  \right)
$$
(ベクトル $abcd$ と読む)    
が $2$ 次対称行列であることは $b = c$ が成り立つことであり,

$$
\left(
    \begin{array}{cc}
      a & b  \\
      b & d  \\
    \end{array}
  \right)
$$
の形をした行列である．  
例えば,
$$
\left(
    \begin{array}{cc}
      1 & 2  \\
      2 & 0  \\
    \end{array}
  \right)
$$
は$2$ 次対称行列である．

## 2次交代行列
$2$ 次正方行列 $\mathbf{A}$ が $\mathbf{A}^{\top}  = \mathbf{-A}$ を満たすとき，  
$\mathbf{A}$ を $2$ 次交代行列と呼ぶ．  
$$
\left(
    \begin{array}{cc}
      a & b  \\
      c & d  \\
    \end{array}
  \right)
$$   
が $2$ 次交代行列であることは  
対角成分 $a,d$は $0$ かつ $b = -c$ が成り立つことであり,

$$
\left(
    \begin{array}{cc}
      0 & b  \\
      -b & 0  \\
    \end{array}
  \right)
$$

の形をした行列である．  
例えば,
$$
\left(
    \begin{array}{cc}
      0 & 2  \\
      -2 & 0  \\
    \end{array}
  \right)
$$
や
$$
\left(
    \begin{array}{cc}
      0 & -5  \\
      5 & 0  \\
    \end{array}
  \right)
$$

は $2$ 次交代行列である．
## 1.6
## 階段行列
## 行基本変形

一般の2次行列では  
$$
\left(
    \begin{array}{cc}
      0 & 0  \\
      0 & 0  \\
    \end{array}
  \right)
$$
(ゼロ行列 $\mathbf{O}$ ),

$$
\left(
    \begin{array}{cc}
      0 & 1  \\
      0 & 0  \\
    \end{array}
  \right)
$$
,

$$
\left(
    \begin{array}{cc}
      1 &  \alpha  \\
      0 & 0  \\
    \end{array}
  \right)
$$
( $\alpha$ は任意の実数),

$$
\left(
    \begin{array}{cc}
      1 & 0  \\
      0 & 1  \\
    \end{array}
  \right)
$$
(単位行列)  

の形の行列を $2$ 次の階段行列と呼ぶ．  
ゼロ行列 $\mathbf{O}$ も単位行列も,階段行列の一種．

# ブロック行列(block matrix)
## 定義と性質
行列の縦横に区切りを入れ，各区域を小さな行列と見なしたもの

$$A=\begin{eqnarray}
\left(
  \begin{array}{cc|cc}
    a & b & 0 & 0 \\
    c & d & 0 & 0 \\
    \hline
    x & y & 1 & 0 \\
    z & w & 0 & 1 \\
  \end{array}
\right)
=
\left( \begin{matrix} A_{11}& A_{12}\\ A_{21}& A_{22}\end{matrix} \right)
\end{eqnarray}$$

ブロック行列の足し算  
例:

$$\begin{eqnarray}
\left(
  \begin{array}{cc|cc}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    \hline
    3 & 1 & 1 & 0 \\
    4 & 1 & 0 & 1 \\
  \end{array}
\right)
+
\left(
  \begin{array}{cc|cc}
    5 & 9 & 5 & 3 \\
    2 & 6 & 5 & 8 \\
    \hline
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1 \\
  \end{array}
\right)
=
\left(
  \begin{array}{cc|cc}
    6 & 9 & 5 & 3 \\
    2 & 7 & 5 & 8 \\
    \hline
    3 & 1 & 2 & 0 \\
    4 & 1 & 0 & 2 \\
  \end{array}
\right)
\end{eqnarray}$$

ブロック行列の定数倍

$$
c\left( \begin{matrix} A_{11} & \ldots &  A_{1n}\\
  \vdots && \vdots \\
  A_{m1} & \ldots & A_{mn}
  \end{matrix} \right)
=
\left( \begin{matrix} cA_{11} & \ldots &  cA_{1n}\\
  \vdots && \vdots \\
  cA_{m1} & \ldots & cA_{mn}
  \end{matrix} \right)
$$

$A_{ij},\ B_{ij}$ が数であるかのように計算してよいということ

ブロック行列の積

$$
\left(
  \begin{matrix} B_{11} & \ldots &  B_{1m}\\
  \vdots && \vdots \\
  B_{k1} & \ldots & B_{km}
  \end{matrix}
\right)
\left(
  \begin{matrix} A_{11} & \ldots &  A_{1n}\\
  \vdots && \vdots \\
  A_{m1} & \ldots & A_{mn}
  \end{matrix}
\right)
=
\left(
  \begin{matrix}
  (B_{11}A_{11}+\ldots +B_{1m}A_{m1})& \ldots & (B_{11}A_{1n}+\ldots +B_{1m}A_{mn})\\
  \vdots && \vdots \\
  (B_{k1}A_{11}+\ldots +B_{km}A_{m1})& \ldots & (B_{k1}A_{11}+\ldots +B_{km}A_{mn})
\end{matrix}
\right)$$

例:

$$\begin{eqnarray}
\left(
  \begin{array}{cc|cc}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    \hline
    3 & 1 & 1 & 0 \\
    4 & 1 & 0 & 1 \\
  \end{array}
\right)
\left(
  \begin{array}{cc|cc}
    5 & 9 & 5 & 3 \\
    2 & 6 & 5 & 8 \\
    \hline
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1 \\
  \end{array}
\right)
&=&

\left(\begin{array}{c|c}
    \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right) \left( \begin{matrix} 5& 9\\ 2& 6\end{matrix} \right)
    +
    \left( \begin{matrix} 0& 0\\ 0& 0\end{matrix} \right) \left( \begin{matrix} 0& 0\\ 0& 0\end{matrix} \right)
    &
    \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right) \left( \begin{matrix} 5& 3\\ 5& 8\end{matrix} \right)
    +
    \left( \begin{matrix} 0& 0\\ 0& 0\end{matrix} \right) \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right)
    \\
    \hline
    \left( \begin{matrix} 3& 1\\ 4& 1\end{matrix} \right) \left( \begin{matrix} 5& 9\\ 2& 6\end{matrix} \right)
    +
    \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right) \left( \begin{matrix} 0& 0\\ 0& 0\end{matrix} \right)
    &
    \left( \begin{matrix} 3& 1\\ 4& 1\end{matrix} \right) \left( \begin{matrix} 5& 3\\ 5& 8\end{matrix} \right)
    +
    \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right) \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right)
    \end{array}\right)\\
&=&
\left(\begin{array}{c|c}
    \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right) \left( \begin{matrix} 5& 9\\ 2& 6\end{matrix} \right)
    +
    \left( \begin{matrix} 0& 0\\ 0& 0\end{matrix} \right)
    &
    \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right) \left( \begin{matrix} 5& 3\\ 5& 8\end{matrix} \right)
    +
    \left( \begin{matrix} 0& 0\\ 0& 0\end{matrix} \right)
    \\
    \hline
    \left( \begin{matrix} 3& 1\\ 4& 1\end{matrix} \right) \left( \begin{matrix} 5& 9\\ 2& 6\end{matrix} \right)
    +
    \left( \begin{matrix} 0& 0\\ 0& 0\end{matrix} \right)
    &
    \left( \begin{matrix} 3& 1\\ 4& 1\end{matrix} \right) \left( \begin{matrix} 5& 3\\ 5& 8\end{matrix} \right)
    +
    \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right) \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right)
    \end{array}\right)\\
&=&
\left(\begin{array}{c|c}
    \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right) \left( \begin{matrix} 5& 9\\ 2& 6\end{matrix} \right)

    &
    \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right) \left( \begin{matrix} 5& 3\\ 5& 8\end{matrix} \right)

    \\
    \hline
    \left( \begin{matrix} 3& 1\\ 4& 1\end{matrix} \right) \left( \begin{matrix} 5& 9\\ 2& 6\end{matrix} \right)

    &
    \left( \begin{matrix} 3& 1\\ 4& 1\end{matrix} \right) \left( \begin{matrix} 5& 3\\ 5& 8\end{matrix} \right)
    +
    \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right) \left( \begin{matrix} 1& 0\\ 0& 1\end{matrix} \right)
    \end{array}\right)\\
&=&
\left(\begin{array}{c|c}
    \begin{matrix} 1\cdot 5 +0\cdot 2 & 1\cdot 9 +0\cdot 6\\ 0\cdot 5 + 1\cdot 2 & 0\cdot 9 +1\cdot 6\end{matrix}
    &
    \begin{matrix} 1\cdot 5 +0\cdot 5 & 1\cdot 3 +0\cdot 8\\ 0\cdot 5 + 1\cdot 5 & 0\cdot 3 +1\cdot 8\end{matrix}

    \\
    \hline
    \begin{matrix} 3\cdot 5 +1\cdot 2 & 3\cdot 9 +1\cdot 6\\ 4\cdot 5 + 1\cdot 2 & 4\cdot 9 +1\cdot 6\end{matrix}
    &
    \left(
      \begin{matrix} 3\cdot 5 +1\cdot 5 & 3\cdot 3 +1\cdot 8\\ 4\cdot 5 + 1\cdot 5 & 4\cdot 3 +1\cdot 8\end{matrix}
    \right)
    +
    \left(
      \begin{matrix} 1\cdot 1 +0\cdot 0 & 1\cdot 0 +0\cdot 1\\ 0\cdot 1 + 1\cdot 0 & 0\cdot 0 +1\cdot 1\end{matrix}
    \right)
    \end{array}\right)\\
&=&
    \left(\begin{array}{c|c}
        \begin{matrix} 1\cdot 5 +0\cdot 2 & 1\cdot 9 +0\cdot 6\\ 0\cdot 5 + 1\cdot 2 & 0\cdot 9 +1\cdot 6\end{matrix}
        &
        \begin{matrix} 1\cdot 5 +0\cdot 5 & 1\cdot 3 +0\cdot 8\\ 0\cdot 5 + 1\cdot 5 & 0\cdot 3 +1\cdot 8\end{matrix}

        \\
        \hline
        \begin{matrix} 3\cdot 5 +1\cdot 2 & 3\cdot 9 +1\cdot 6\\ 4\cdot 5 + 1\cdot 2 & 4\cdot 9 +1\cdot 6\end{matrix}
        &
        \left(
          \begin{matrix} 20 & 17\\ 25 & 20\end{matrix}
        \right)
        +
        \left(
          \begin{matrix} 1 & 0\\ 0 & 1\end{matrix}
        \right)
        \end{array}\right)\\
&=&
  \left(
    \begin{array}{cc|cc}
      5 & 9 & 5 & 3 \\
      2 & 6 & 5 & 8 \\
    \hline
      17 & 33 & 21 & 17 \\
      22 & 42 & 25 & 21 \\
    \end{array}
  \right)\\
\end{eqnarray}$$

## クラメールの公式 (Cramer's rule)
これを使えば方程式を解ける．  
$2$ 行 $2$ 列の次のような方程式の場合  

$$
\left(
    \begin{array}{cc}
      a & b  \\
      c & d  \\
    \end{array}
  \right)

\begin{pmatrix} x \\ y \end{pmatrix}
=
\begin{pmatrix} e \\ f \end{pmatrix}
$$

$$
x = \frac{de-bf}{ad-bc}
=
\frac{
\begin{vmatrix}
e & b \\
f & d
\end{vmatrix}
}
{|\mathbf{A}|}
$$

$$
y = \frac{af-ce}{ad-bc}
=
\frac{
\begin{vmatrix}
a & e \\
c & f
\end{vmatrix}
}
{|\mathbf{A}|}
$$
3行3列の次のような方程式の場合

$$
\mathbf{A}
=
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
$$

$$
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}

\begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \end{pmatrix}
=
\begin{pmatrix} b_{1} \\ b_{2} \\ b_{3} \end{pmatrix}
$$

分母は行列 $\mathbf{A}$ の行列式で，  
分子は行列 $\mathbf{A}$ の行列式の列を1列ずつ列ベクトル $\mathbf{B}$ の成分に置き換えると解が求まる．  
以下の3つがそれぞれ $x_{1}, x_{2}, x_{3}$ の解になる．

$$
x_{1}
=
\frac{
  \begin{vmatrix}
  b_{1} & a_{12} & a_{13} \\
  b_{2} & a_{22} & a_{23} \\
  b_{3} & a_{32} & a_{33}
  \end{vmatrix}
}
{|\mathbf{A}|}
=
\frac{
  \begin{vmatrix}
  b_{1} & a_{12} & a_{13} \\
  b_{2} & a_{22} & a_{23} \\
  b_{3} & a_{32} & a_{33}
  \end{vmatrix}
}
{
  \begin{vmatrix}
  a_{11} & a_{12} & a_{13} \\
  a_{21} & a_{22} & a_{23} \\
  a_{31} & a_{32} & a_{33}
  \end{vmatrix}
}
$$


$$
x_{2}
=
\frac{
  \begin{vmatrix}
  a_{11} & b_{1} & a_{13} \\
  a_{21} & b_{2} & a_{23} \\
  a_{31} & b_{3} & a_{33}
  \end{vmatrix}
}
{|\mathbf{A}|}
=
\frac{
  \begin{vmatrix}
  a_{11} & b_{1} & a_{13} \\
  a_{21} & b_{2} & a_{23} \\
  a_{31} & b_{3} & a_{33}
  \end{vmatrix}
}
{
  \begin{vmatrix}
  a_{11} & a_{12} & a_{13} \\
  a_{21} & a_{22} & a_{23} \\
  a_{31} & a_{32} & a_{33}
  \end{vmatrix}
}
$$

$$
x_{3}
=
\frac{
  \begin{vmatrix}
  a_{11} & a_{12} & b_{1} \\
  a_{21} & a_{22} & b_{2} \\
  a_{31} & a_{32} & b_{3}
  \end{vmatrix}
}
{|\mathbf{A}|}
=
\frac{
  \begin{vmatrix}
  a_{11} & a_{12} & b_{1} \\
  a_{21} & a_{22} & b_{2} \\
  a_{31} & a_{32} & b_{3}
  \end{vmatrix}
}
{
  \begin{vmatrix}
  a_{11} & a_{12} & a_{13} \\
  a_{21} & a_{22} & a_{23} \\
  a_{31} & a_{32} & a_{33}
  \end{vmatrix}
}
$$

### 行列式 (determinant)

行列の成分を囲む記号が，$()$ なのか $| |$ なのかの違いで，行列と行列式を区別する．  
行列と行列式の表すものは違っていて，行列式は本当に，"式"．  
各行の各例から1つずつ成分を選んで，そのかけ算をとり，さらにその和（や差）をとったもの．  
行列式は，正方行列だけに適用できる．


行列
$\mathbf{A} =
\left(
    \begin{array}{cc}
      a & b  \\
      c & d  \\
    \end{array}
\right)$
に対して

$$
\mathrm{det}A = |\mathbf{A}| = \mathrm{det}
\left(
    \begin{array}{cc}
      a & b  \\
      c & d  \\
    \end{array}
\right)
= ad - bc =
\left|
    \begin{array}{cc}
      a & b  \\
      c & d  \\
    \end{array}
\right|
$$

#### 和か，差はどう決まっているのか?
かけ算の成分を1行目から拾うことにして，  
左上から右下の順番に拾ってかけた項は和  
右上から左下の順番に拾ってかけた項は差  
にとる．[**サラスの方法，またはたすきがけの方法** という]  
ただし，  
サラスの方法が使えるのは，3次の正方行列まで．  
4次以上の正方行列の場合は互換という操作の回数で決める．

#### 行列式の性質
* 行（または列）を入れ替えると符合が変わる
* 2つの行（または列）が同じであればゼロになる
* ある行（または列）に，他の行（または列）の定数倍を加えても，行列式の値は同じ


## 同次形の連立1次方程式
連立1次方程式
$$
\begin{cases}ax + by = 0 \\ cx + dy = 0 \end{cases}
$$
は，同次形の連立1次方程式と呼ばれ，いつでも $x = y = 0$ を解としてもつ．  
この解，$x = 0$ を **同次連立1次方程式の自明な解** と呼ぶ．

# 第2章 2次行列と平面図形
## 2.1
## 平面上のベクトル
## 幾何ベクトル
矢線と同一視した数ベクトルを幾何ベクトルと呼ぶ.

***
2点間の距離の定義から,ベクトル $\mathbf{a} = ( a_1，a_2 )$ の大きさ(ノルム)を

$$
 \|\mathbf{a}\| =  \sqrt{ a_1^2 + a_2^2 }
$$
と定める.

ノルムとは距離を一般化した概念で,ベクトルに対して定義される.いろいろな種類があり,    
上記は L2ノルム, ユークリッドノルム とも呼ばれる.

さらに，$\mathbf{a，b}$ のなす角を $\theta$ (ただし，$0  \leq \theta  \leq 180 ^\circ )$ とすると，  
$\mathbf{a，b}$ の内積が

$$ \mathbf{a \cdot b} = \|\mathbf{a}\| \|\mathbf{b}\| \cos \theta $$

と定義される．

抽象的な線形代数では内積の基本的性質を内積の満たすべき公理として,内積を定義しその後にベクトルのなす角などを定義する．  
このように抽象化すると汎用性を獲得し,平面や空間以外の対象(関数や微分方程式)にも内積を定めることが可能となる．

### シュワルツの不等式
$$ |\mathbf{a \cdot b}|  \leq \|\mathbf{a}\| \|\mathbf{b}\|  $$

## 2.2
## 直線と連立1次方程式
## パラメータ型の直線のベクトル方程式 または略して 直線のパラメータ表示

$$ \mathbf{p} = \mathbf{a} + t ( \mathbf{b-a} )  $$

<!-- 実数 $ t $ を任意の実数とすると，$ p $ は直線 $g$ 上のすべての点を示す．-->
## (内積型の) ベクトル方程式

$$  \displaystyle\boldsymbol{E} $$

$$ \mathbf{p \cdot h} = p $$
<!-- あとで直す -->
を直線 $g$ の (内積型の) ベクトル方程式と呼ぶ．

## ヘッセの標準系

(内積型の) ベクトル方程式の  
$\mathbf{p} = (x,y)$，$x$ 軸の正の方向と $\mathbf{h}$ のなす角を $α$ とすると，  
$\mathbf{h} = ( \cos α，\sin α )$ となり，

$$ (b_{2}-a_{2})x+(a_{1}-b_{1})y+(a_{2}b_{1}-a_{1}b_{2})=0 $$
は

$$ x\cos α + y\sin α = p (p \leq 0)$$
となる.  
この式を，ヘッセの標準系と呼ぶ．(上記のベクトル方程式も，ヘッセの標準系と呼ぶ．)

## 命題 2.2.1
$e$ の単位ベクトル
***
### 以下，参考文献
1. 竹内 薫:『[量子コンピューターが本当にすごい](http://amzn.to/2ff0OQO)』PHP研究所，2015．

# 行列 (matrix) とは(163)
連立方程式の成分を並べ替えたもの  
連立方程式を簡単に解くために考え出された表記法だった．  

行列の計算は必ず左から右に行われる  
行列 $m$ の成分の数だけ計算する  
そして,計算結果の行列も成分の数と同じになる  
だから,基本的に行と列の数が違う場合,計算できない

# 逆行列
正方行列 $A$ に対して，その逆写像に対応する行列を「 $A$ の **逆行列**」と呼び，
$A^{-1}$ で書く

$2$ に対する $1/2$ , $5$ に対する $1/5$ のように，  
掛けたら $1$ になる逆数みたいなもの．  
行列に掛けると,単位行列 $I$ になる．  
逆行列の作り方には公式がある．  
逆行列は存在したりしなかったりする．  

以下  
http://qiita.com/nognog/items/f6b6e64792ae1f8ac20c
# 基底
$e_1=(1,0)^t,e_2=(0,1)^t$ という２つのベクトルの組は2次元の基底

$$
{\begin{align}
\left(
\begin{matrix}
3\\\
5
\end{matrix}
\right)
&=3
\left(
\begin{matrix}
1\\\
0
\end{matrix}
\right)
+5
\left(
\begin{matrix}
0\\\
1
\end{matrix}
\right)\\\
&=
3 \mathbf{e}_1 + 5 \mathbf{e}_2
\end{align}
}
$$

同様に、平面上の任意の点 $(x,y)$ は以下のように表すことができます。

$$
{\begin{align}
\left(
\begin{matrix}
x\\\
y
\end{matrix}
\right)
&=x
\left(
\begin{matrix}
1\\\
0
\end{matrix}
\right)
+y
\left(
\begin{matrix}
0\\\
1
\end{matrix}
\right)\\\
&=
x \mathbf{e}_1 + y \mathbf{e}_2
\end{align}
}
$$

# ベクトル同士の積=ベクトルの内積  
ベクトルは掛け算が定義されず、掛け算に相当するものとして内積が定義  
$n$ 次元ベクトル

$$
{\mathbf{a}=
\left(
\begin{matrix}
a_1 \\\
a_2 \\\
\vdots \\\
a_n
\end{matrix}
\right)
}
$$
$$
{\mathbf{b}=
\left(
\begin{matrix}
b_1 \\\
b_2 \\\
\vdots \\\
b_n
\end{matrix}
\right)
}
$$

の内積は，以下の通り定義されます．

$$
{\begin{align}
\mathbf{a}^t \cdot \mathbf{b} & =
\left(
\begin{matrix}
a_1 & a_2 & \cdots & a_n
\end{matrix}
\right) \cdot
\left(
\begin{matrix}
b_1 \\\
b_2 \\\
\vdots \\\
b_n
\end{matrix}
\right) \\\
& = a_1 b_1 + a_2 b_2 + \cdots + a_n b_n
\end{align}
}
$$

* 大学以降の数学では、内積はサイズの等しい横ベクトルと縦ベクトルの間で、「横ベクトル ⋅⋅ 縦ベクトル」として定義されるということ  
（順番も重要 必ず横ベクトルが左）  
計算としては中の成分同士の掛け算の総和なので、順番なんかどっちでも同じではないかと思うかもしれませんが、  
以下のような計算は定義されないので注意  
（このような定義をしてしまうと、この後に出てくる行列の計算が定義できなくなってしまうため、内積は横ベクトルと縦ベクトルについて定義されています。**ベクトルや行列の計算では、縦・横のサイズを気にすることは非常に重要**）
* 内積は次元のない普通の数(scalar）であることにも注意．  
**ベクトルや行列の計算では、結果の縦・横のサイズを気にすることも非常に重要**

$$
{\left(
\begin{matrix}
a_1 \\\
a_2 \\\
\vdots \\\
a_n
\end{matrix}
\right)
\cdot

\left(
\begin{matrix}
b_1 \\\
b_2 \\\
\vdots \\\
b_n
\end{matrix}
\right)
 →　定義できない
}
$$

* 内積の例：  
$\mathbf{a}^t=(1,2,3,4)$  
$\mathbf{b}^t=(5, 6, 7, 8)$

$$
{\begin{align}
\mathbf{a}^t \cdot \mathbf{b} & =
\left(
\begin{matrix}
1 & 2 & 3 & 4
\end{matrix}
\right) \cdot
\left(
\begin{matrix}
5 \\\
6 \\\
7 \\\
8
\end{matrix}
\right) \\\
&= 1 \times 5 + 2 \times 6 + 3 \times 7 + 4 \times 8 \\
&= 80
\end{align}
}
$$
# 随時更新していきます:octocat:
