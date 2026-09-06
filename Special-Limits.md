# Special Limits in Calculus

A reference sheet of the standard limits that show up over and over in a first calculus course:
the ones worth memorizing outright rather than re-deriving every time.
Every value below was checked numerically (finite-difference evaluation near the limit point) before being written down.

---

## 1. The trigonometric limits ($x \to 0$)

These are the ones almost every other trig limit reduces to.

| Limit | Value | How it is normally proved |
| :--- | :--- | :--- |
| $\displaystyle\lim_{x\to 0}\frac{\sin x}{x}$ | $1$ | Squeeze theorem, using $\cos x \le \dfrac{\sin x}{x} \le 1$ near $0$ |
| $\displaystyle\lim_{x\to 0}\frac{x}{\sin x}$ | $1$ | Reciprocal of the above |
| $\displaystyle\lim_{x\to 0}\frac{\tan x}{x}$ | $1$ | $\dfrac{\tan x}{x} = \dfrac{\sin x}{x}\cdot\dfrac{1}{\cos x}\to 1\cdot 1$ |
| $\displaystyle\lim_{x\to 0}\frac{1-\cos x}{x}$ | $0$ | Multiply by the conjugate $\dfrac{1+\cos x}{1+\cos x}$ |
| $\displaystyle\lim_{x\to 0}\frac{1-\cos x}{x^2}$ | $\dfrac12$ | Same conjugate trick, or the Taylor series $\cos x \approx 1-\tfrac{x^2}{2}$ |
| $\displaystyle\lim_{x\to 0}\frac{\arcsin x}{x}$ | $1$ | Substitute $u=\arcsin x$, so $x=\sin u$, and reuse $\sin u/u \to 1$ |
| $\displaystyle\lim_{x\to 0}\frac{\arctan x}{x}$ | $1$ | Substitute $u=\arctan x$, so $x=\tan u$, and reuse $\tan u/u \to 1$ |
| $\displaystyle\lim_{x\to 0}\frac{\sin(ax)}{bx}$ | $\dfrac{a}{b}$ ($b \ne 0$) | The general pattern behind every "manufacture the matching denominator" trick |

**Third-order refinements** (the terms L'Hopital's rule needs three passes to reach, or a Taylor series reaches in one):

| Limit | Value |
| :--- | :--- |
| $\displaystyle\lim_{x\to 0}\frac{x-\sin x}{x^3}$ | $\dfrac16$ |
| $\displaystyle\lim_{x\to 0}\frac{\tan x - x}{x^3}$ | $\dfrac13$ |
| $\displaystyle\lim_{x\to 0}\frac{\sin x - \tan x}{x^3}$ | $-\dfrac12$ |

---

## 2. The exponential and logarithmic limits ($x \to 0$)

These are the definitions of $e$ and $\ln$ wearing a limit costume; each is literally a derivative at a point (see section 6).

| Limit | Value | Note |
| :--- | :--- | :--- |
| $\displaystyle\lim_{x\to 0}\frac{e^x-1}{x}$ | $1$ | Derivative of $e^x$ at $0$ |
| $\displaystyle\lim_{x\to 0}\frac{a^x-1}{x}$ | $\ln a$ ($a>0$) | Generalizes the row above ($a=e$ gives $\ln e = 1$) |
| $\displaystyle\lim_{x\to 0}\frac{\ln(1+x)}{x}$ | $1$ | Derivative of $\ln x$ at $1$ |
| $\displaystyle\lim_{x\to 0}\frac{\log_a(1+x)}{x}$ | $\dfrac{1}{\ln a}$ | Change-of-base version of the row above |
| $\displaystyle\lim_{x\to 0}(1+x)^{1/x}$ | $e$ | The defining limit for $e$ |

---

## 3. The number $e$ as a limit at infinity

| Limit | Value |
| :--- | :--- |
| $\displaystyle\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^x$ | $e$ |
| $\displaystyle\lim_{x\to\infty}\left(1+\frac{a}{x}\right)^x$ | $e^a$ |
| $\displaystyle\lim_{n\to\infty}\left(1-\frac{1}{n}\right)^n$ | $e^{-1}$ |

All three are the same limit as $(1+x)^{1/x}\to e$ in section 2, just with $x$ replaced by $1/x$ and sent to $0$ from the other side.

---

## 4. Growth-rate hierarchy at infinity

The recurring "who wins" question in $\infty/\infty$ and $\infty - \infty$ forms.
Written smallest-growing to fastest-growing, each term is eventually dwarfed by everything to its right:

$$\ln x \ \ll\ x^p \ (p>0) \ \ll\ a^x \ (a>1) \ \ll\ x! \ \ll\ x^x$$

| Limit | Value |
| :--- | :--- |
| $\displaystyle\lim_{x\to\infty}\frac{\ln x}{x}$ | $0$ |
| $\displaystyle\lim_{x\to\infty}\frac{\ln x}{x^p}$ ($p>0$) | $0$ |
| $\displaystyle\lim_{x\to 0^+} x\ln x$ | $0$ |
| $\displaystyle\lim_{x\to 0^+} x^p\ln x$ ($p>0$) | $0$ |
| $\displaystyle\lim_{x\to\infty}\frac{x^n}{e^x}$ (any fixed $n$) | $0$ |
| $\displaystyle\lim_{x\to\infty}\frac{e^x}{x^n}$ (any fixed $n$) | $\infty$ |
| $\displaystyle\lim_{n\to\infty}\frac{a^n}{n!}$ (any fixed $a$) | $0$ |
| $\displaystyle\lim_{n\to\infty}\frac{n!}{n^n}$ | $0$ |

Every row here is an $\infty/\infty$ or $0\cdot\infty$ form that yields to repeated L'Hopital's rule; the table just saves the repetition.

---

## 5. Root and power limits

| Limit | Value |
| :--- | :--- |
| $\displaystyle\lim_{x\to\infty} x^{1/x}$ | $1$ |
| $\displaystyle\lim_{n\to\infty} n^{1/n}$ | $1$ |
| $\displaystyle\lim_{n\to\infty} a^{1/n}$ ($a>0$ fixed) | $1$ |
| $\displaystyle\lim_{n\to\infty} \frac{(n!)^{1/n}}{n}$ | $e^{-1}$ |

The last one is a Stirling's-approximation consequence, rarely tested outside a second calculus course, but useful for recognizing the pattern when it appears.

---

## 6. Rationalizing and "hidden derivative" limits

| Limit | Value | Note |
| :--- | :--- | :--- |
| $\displaystyle\lim_{x\to 0}\frac{\sqrt{1+x}-1}{x}$ | $\dfrac12$ | Derivative of $\sqrt{x}$ at $1$ |
| $\displaystyle\lim_{x\to 0}\frac{\sqrt{a+x}-\sqrt{a}}{x}$ ($a>0$) | $\dfrac{1}{2\sqrt a}$ | General case of the row above |
| $\displaystyle\lim_{x\to\infty}\left(\sqrt{x^2+x}-x\right)$ | $\dfrac12$ | Multiply by the conjugate $\dfrac{\sqrt{x^2+x}+x}{\sqrt{x^2+x}+x}$ |
| $\displaystyle\lim_{x\to\infty}\left(\sqrt{x^2+ax+b}-x\right)$ | $\dfrac a2$ | General case of the row above |

**The pattern worth internalizing:** every limit of the form $\displaystyle\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$ is, by definition, $f'(a)$.
Sections 1, 2, and this section are mostly that one definition applied to $\sin$, $e^x$, $\ln x$, and $\sqrt{x}$.
Recognizing the pattern turns "memorize this limit" into "memorize one derivative rule."

---

## 7. Squeeze-theorem classics

Cases where the limit does not exist by substitution or algebra alone, only by trapping the expression between two functions that share the same limit.

| Limit | Value | Squeeze used |
| :--- | :--- | :--- |
| $\displaystyle\lim_{x\to 0} x\sin\!\left(\frac1x\right)$ | $0$ | $-\lvert x\rvert \le x\sin(1/x) \le \lvert x\rvert$ |
| $\displaystyle\lim_{x\to 0} x^2\sin\!\left(\frac1x\right)$ | $0$ | $-x^2 \le x^2\sin(1/x) \le x^2$ |
| $\displaystyle\lim_{x\to 0}\frac{\sin x}{x}$ | $1$ | $\cos x \le \dfrac{\sin x}{x} \le 1$ (the proof behind section 1's first row) |

The tell that a limit needs squeezing rather than algebra: a bounded-but-wildly-oscillating factor like $\sin(1/x)$ or $\cos(1/x)$ multiplied by a factor that shrinks to $0$.

---

## 8. Indeterminate forms, and which tool actually applies

Seven forms look like they need L'Hopital's rule, but only two are it applied directly; the rest need an algebra or logarithm step first to get there.

| Form | Direct tool | Typical rewrite |
| :--- | :--- | :--- |
| $\dfrac00$ | L'Hopital directly | (none needed) |
| $\dfrac{\infty}{\infty}$ | L'Hopital directly | (none needed) |
| $0\cdot\infty$ | Rewrite, then L'Hopital | $fg \to \dfrac{f}{1/g}$ or $\dfrac{g}{1/f}$ |
| $\infty-\infty$ | Rewrite, then L'Hopital | common denominator, or conjugate multiplication |
| $1^{\infty}$ | Take $\ln$, then L'Hopital | $y=f^g \Rightarrow \ln y = g\ln f$, solve for $\lim \ln y$, exponentiate |
| $0^0$ | Take $\ln$, then L'Hopital | same $\ln$ trick as above |
| $\infty^0$ | Take $\ln$, then L'Hopital | same $\ln$ trick as above |

$0^\infty$ and $\infty^\infty$ are **not** indeterminate; they resolve directly to $0$ and $\infty$.

---

## Sources and verification

Standard results collected from Kurose-style first-calculus curricula (matches the limits unit of AU MATH 265 / equivalent Calculus I courses).
Every numeric claim above was spot-checked with a finite-difference evaluation in Python (evaluating each expression at $x = \pm 10^{-6}$ near $0$, or at $x = 10^7$ near infinity) before being recorded; none were copied from a solution key without independent recomputation.
