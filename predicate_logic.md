# predicate logic (述語論理)
### 参考文献
1) 戸川, 中嶋, 杉原, 野寺:『[インターネット時代の数学](http://amzn.to/1KpdK1i)』共立出版, 1997.
***
# 6.3.2 述語論理

## 述語論理の原子式
$\wedge, \vee, \rightarrow, \neg$ などのつかない, 述語とその引数だけの式
***
集合の前提として要素があったように, 述語論理の前提として, "もの" と, それらの間の"関係" がある.

たとえば特定の物体 "box1" の "color" が特定の色 "red1" であるという関係を
$$ color(box1, red1)$$
のように表す.

特別な場合として, $0$ 項関係や $1$ 項関係があり  
$0$ 項関係は"もの"に言及することなく成立するし,  
$1$ 項関係は一つの"もの"だけで成立する.

$1$ 項関係の例はdogやflyなどで, 分類(classification)とよばれることもある.

述語論理が有用なのは"もの"を表す対称変数が使えること.

たとえば
$x$ を変数, $a$ を定数だとすると
$$on(x, a)$$

という式は何か $x$ が $a$ の上(on)にあるという風に読める.

これだけでは式の真偽値を決めることができない.  
述語論理が面白いのはこれらの変数に限定子をつけて, 変数の範囲を明示できるからである.  
これを使うことにより,  
"すべてのカナリヤは鳥である"  

$$ \forall x.canary(x) \rightarrow bird(x)$$

というような記述が可能になる.  

$$ \forall x \exists y.loves(x, y) $$

という式は
$$ \forall x.( \exists y.loves(x, y)) $$
と同じ.  
すべての $x$ に対し, $loves(x, y)$ という述語を満たす, (別々の) $y$ が存在する  
という文.  

また
$$ \exists y \forall x.loves(x, y) $$
という式は  
ある一定の $y$ が存在し, すべての $x$ に対し $loves(x, y)$ という述語を満たすという文になる.

> 論理記号 $\forall, \exists$ は、基本的には  
論理記号 変項.述語(命題関数)  
というかたちのなかで、用いられる
http://www.ne.jp/asahi/search-center/internationalrelation/mathWeb/meidai/Exist.htm

# 6.3.3 推論

## 推論規則
演繹に使われる規則のこと. 通常は横棒の上側に最初の論理式 $p$, 下側にそれから導ける論理式 $q$ を書き,

$$ \frac{p}{q} $$
のように表す. 下辺は上辺の論理的帰結.

たとえば

$$ \frac{p, ~p \rightarrow q}{q} $$

は命題論理の (通常, 三段論法とよばれる)推論規則.  
$p$ という論理式と $p \rightarrow q$ という論理式から $q$ という論理式が導けることを示している.

また, よく使われる推論に以下のものがある.

$$ \frac{\forall x.p(x)}{p(a)} $$

すべての $x$ に関して $p$ が成立するなら, それは任意の定数 $a$ に対しても $p$ が成立する, というもの.  

実際にはこれが単独で使われることは少なく, 上記の三段論法と組み合わされる.  

$$ \frac{ canary(Tweety)\frac{\forall x. canary(x) \rightarrow fly(x)}{canary(Tweety) \rightarrow fly(Tweety)}} {fly(Tweety)} $$


$canary(Tweety)$ [Tweety という canary] という論理式と

$\forall x. canary(x) \rightarrow fly(x)$ [すべての canary は飛ぶ] という論理式から  
$canary(Tweety) \rightarrow fly(Tweety)$ [Tweety という canary ならば Tweety は飛ぶ] という論理式から

$fly(Tweety)$ [Tweety は飛ぶ] という論理式が導けることを示している.  

# 6.3.5 証明

定理を求める具体的な計算手続きが必要である.  

## 半決定性
述語論理の限定子を含む式に関しては, このような一般的な手続きが存在しないことが証明されている.詳しく言うと,  
定理を与えれば止まる手続きは存在するが, 定理でない式を与えた場合には止まらないかもしれない.このような性質のこと

# 6.3.6 統合 (resolution)

推論規則
$$ \frac{ \Delta \rightarrow \Gamma, p ~~ p,   \Lambda \rightarrow \Theta}{\Delta, \Lambda \rightarrow \Gamma, \Theta} $$

これ自体は $p$ を仲立ちとして推論していくもので, この $\Delta, \Lambda, \Gamma$ が空の場合が三段論法
$$ \frac{ \rightarrow p ~~ p \rightarrow \Theta}{\rightarrow \Theta} $$
に相当. $p$ と $\rightarrow p$ は等価であり, どちらの場合も, 下辺は上辺の論理的帰結になっている.
## 単一化 (unification)
$P$ と $P \prime$ の変数に適当な値を代入したり, 別の変数で置き換えることにより(どちらも置換)同じ形にする操作のこと
***
置換を $\theta$ のようなギリシャ小文字で表し, 式の後ろに書くことによりその置換を適用した値を示す.  
たとえば

$$\theta = [ x/a, y/b, z/x ]$$
のとき,  
$$ p(x, y, z)\theta = p(a, b, a) $$
$$ q(1, y, z)\theta = p(1, b, a) $$
$$ r(x, y, w)\theta = p(a, b, w) $$

$P\theta = Q\theta$ のとき, 以下の推論規則が成立. つまり以下の推論が論理的に正しいもの.

$$ \frac{ \Delta \rightarrow \Gamma, P ~~~ Q, \Lambda \rightarrow \Theta}{\Delta \theta, \Lambda \theta \rightarrow \Gamma \theta, \Theta \theta} $$
