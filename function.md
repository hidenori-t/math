
一般に, 整関数, 分数関数, 無理関数, 三角関数, 指数関数, 対数関数などの関数 $f(x)$ については, $a$ が関数の定義域に属するとき

$$  \lim_{x \to a} f(x)=f(a)$$

が成り立つ.


# Floor function (床関数)  
https://ja.wikipedia.org/wiki/%E5%BA%8A%E9%96%A2%E6%95%B0%E3%81%A8%E5%A4%A9%E4%BA%95%E9%96%A2%E6%95%B0

実数 $x$ に対して $x$ 以下の最大の整数と定義

$$ \lfloor x \rfloor=\max\{n\in\mathbb{Z}\mid n\le x\}.$$

実数 $x$ に対し,$\lfloor x \rfloor$ を整数部分  
$x - \lfloor x \rfloor$ を小数部分と呼ぶ

小数部分は $x \mod 1$ や $\{x\}$ とも書かれる  
整数部分の値は床関数の値そのものであるから,例えば -2.3 の整数部分は -2 ではなく -3 であること  
また小数部分は -0.3 ではなく 0.7 であることに注意が必要  
（ただし, -2.3 の整数部分を -2 と定義する流儀（「切り捨て式」）もあるが一般的ではない.  
またプログラミング言語によっては「切り捨て式」を採用しているものがある）.  
小数部分は,任意の実数に対して 0 以上 1 未満である.

例えば,  
* $\lfloor\mathrm{4.68}\rfloor = 4$　　　　　　　　　                       小数部分 = 0.68
* $\lfloor\mathrm{e}\rfloor = \lfloor\mathrm{2.71828...}\rfloor = 2$　　　　小数部分 = 0.71828....
* $\lfloor\sqrt{53}\rfloor = \lfloor\mathrm{7.2801...}\rfloor = 7$　　　　　小数部分 = 0.2801....
* $\lfloor\mathrm{-4}\rfloor = -4$　　　　　　　　　                        小数部分 = 0
* $\lfloor\mathrm{-4.68}\rfloor = -5$　　　　　　                           小数部分 = 0.32
* $\lfloor-\pi\rfloor = \lfloor\mathrm{-3.14159...}\rfloor = -4$　　　　　　小数部分 = 0.8584....

といった具合である.
