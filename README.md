# Special Limits in Calculus

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

| Limit | Value |
| :--- | :--- |
| $\displaystyle\lim_{x\to 0}\frac{x-\sin x}{x^3}$ | $\dfrac16$ |
| $\displaystyle\lim_{x\to 0}\frac{\tan x - x}{x^3}$ | $\dfrac13$ |
| $\displaystyle\lim_{x\to 0}\frac{\sin x - \tan x}{x^3}$ | $-\dfrac12$ |

---

## 2. The exponential and logarithmic limits ($x \to 0$)

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

## 1. Formal (epsilon-delta) definition of a limit

$$\lim_{x\to a} f(x) = L$$

means: for every $\varepsilon > 0$, there exists a $\delta > 0$ such that whenever $0 < |x-a| < \delta$, it follows that $|f(x)-L| < \varepsilon$.

This is the definition every other rule on this page is ultimately built from.

---

## 2. One-sided limits

| Notation | Meaning |
| :--- | :--- |
| $\displaystyle\lim_{x\to a^-} f(x) = L$ | For every $\varepsilon>0$ there is a $\delta>0$ such that $a-\delta < x < a \Rightarrow \lvert f(x)-L\rvert < \varepsilon$ |
| $\displaystyle\lim_{x\to a^+} f(x) = L$ | For every $\varepsilon>0$ there is a $\delta>0$ such that $a < x < a+\delta \Rightarrow \lvert f(x)-L\rvert < \varepsilon$ |

**Existence rule:**

$$\lim_{x\to a} f(x) = L \quad\Longleftrightarrow\quad \lim_{x\to a^-} f(x) = \lim_{x\to a^+} f(x) = L$$

If the two one-sided limits disagree, or either fails to exist, the two-sided limit does not exist.

---

## 3. Algebra of limits (limit laws)

Assume $\displaystyle\lim_{x\to a} f(x) = L$ and $\displaystyle\lim_{x\to a} g(x) = M$, both finite, and $c$ is a constant.

| Law | Formula |
| :--- | :--- |
| Sum | $\displaystyle\lim_{x\to a}\big[f(x)+g(x)\big] = L+M$ |
| Difference | $\displaystyle\lim_{x\to a}\big[f(x)-g(x)\big] = L-M$ |
| Constant multiple | $\displaystyle\lim_{x\to a}\big[c\,f(x)\big] = cL$ |
| Product | $\displaystyle\lim_{x\to a}\big[f(x)g(x)\big] = LM$ |
| Quotient | $\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)} = \frac{L}{M}$, provided $M \neq 0$ |
| Power | $\displaystyle\lim_{x\to a}\big[f(x)\big]^n = L^n$ for any positive integer $n$ |
| Root | $\displaystyle\lim_{x\to a}\sqrt[n]{f(x)} = \sqrt[n]{L}$, provided $L \ge 0$ when $n$ is even |
| Constant function | $\displaystyle\lim_{x\to a} c = c$ |
| Identity function | $\displaystyle\lim_{x\to a} x = a$ |
| Polynomial / direct substitution | $\displaystyle\lim_{x\to a} f(x) = f(a)$ whenever $f$ is a polynomial (or any function continuous at $a$) |
| Composition | If $g$ is continuous at $L$ and $\displaystyle\lim_{x\to a} f(x) = L$, then $\displaystyle\lim_{x\to a} g(f(x)) = g(L)$ |

Every one of these fails if the hypothesis (both individual limits existing, or $M \neq 0$ for the quotient rule) is not met; that is exactly the situation that produces an indeterminate form.

---

## 4. Limits involving infinity

**Infinite limit (vertical asymptote), formal definition:**

$$\lim_{x\to a} f(x) = \infty$$

means: for every $N > 0$, there is a $\delta > 0$ such that $0 < |x-a| < \delta \Rightarrow f(x) > N$.
($\lim_{x\to a} f(x) = -\infty$ is the mirror statement with $f(x) < -N$.)

**Limit at infinity (horizontal asymptote), formal definition:**

$$\lim_{x\to\infty} f(x) = L$$

means: for every $\varepsilon > 0$, there is an $M > 0$ such that $x > M \Rightarrow |f(x)-L| < \varepsilon$.
($x \to -\infty$ is the mirror statement with $x < -M$.)

**Basic power-function limits:**

| Limit | Value |
| :--- | :--- |
| $\displaystyle\lim_{x\to\infty} x^p$ ($p>0$) | $\infty$ |
| $\displaystyle\lim_{x\to\infty} \frac{1}{x^p}$ ($p>0$) | $0$ |
| $\displaystyle\lim_{x\to-\infty} \frac{1}{x^p}$ ($p>0$, defined) | $0$ |
| $\displaystyle\lim_{x\to\infty} \frac{c}{x^p}$ (any constant $c$, $p>0$) | $0$ |

**Rational function at infinity (degree comparison), given**
$$f(x) = \frac{a_n x^n + \cdots + a_0}{b_m x^m + \cdots + b_0}:$$

| Degree comparison | $\displaystyle\lim_{x\to\pm\infty} f(x)$ |
| :--- | :--- |
| $n < m$ (numerator degree smaller) | $0$ |
| $n = m$ (equal degree) | $\dfrac{a_n}{b_m}$ (ratio of leading coefficients) |
| $n > m$ (numerator degree bigger) | $\pm\infty$, sign from the leading coefficients and the direction of approach |

The standard technique is to divide numerator and denominator by $x^m$ (the highest power in the denominator) before taking the limit; that mechanical step is what these three rows summarize.

---

## 5. Squeeze (sandwich) theorem

If $g(x) \le f(x) \le h(x)$ for all $x$ near $a$ (except possibly at $a$ itself), and

$$\lim_{x\to a} g(x) = \lim_{x\to a} h(x) = L,$$

then

$$\lim_{x\to a} f(x) = L.$$

This is the only tool on this page that proves a limit exists without ever evaluating $f$ directly; it works by trapping $f$ between two functions whose limits are already known.

---

## 6. L'Hopital's rule

If $\displaystyle\lim_{x\to a} \frac{f(x)}{g(x)}$ is of the form $\dfrac{0}{0}$ or $\dfrac{\infty}{\infty}$, and $f$ and $g$ are differentiable near $a$ with $g'(x) \neq 0$ near $a$ (except possibly at $a$), then

$$\lim_{x\to a} \frac{f(x)}{g(x)} = \lim_{x\to a} \frac{f'(x)}{g'(x)}$$

provided the limit on the right exists (as a finite number or as $\pm\infty$).
The rule applies at $a = \pm\infty$ as well as at a finite point, and it may be applied repeatedly if the new ratio is still $0/0$ or $\infty/\infty$.
It does **not** apply directly to the other five indeterminate forms ($0\cdot\infty$, $\infty-\infty$, $1^\infty$, $0^0$, $\infty^0$); those must first be rewritten as a single fraction or run through a logarithm before L'Hopital's rule can fire (see `Calculus-Techniques-Limits-Derivatives-Integrals.md`, techniques L14-L15, for the rewrite steps).

---

## 7. Continuity, stated as a limit equation

$f$ is continuous at $x=a$ if and only if all three conditions hold:

1. $f(a)$ is defined.
2. $\displaystyle\lim_{x\to a} f(x)$ exists.
3. $\displaystyle\lim_{x\to a} f(x) = f(a)$.

Equivalently, continuity is the single equation $\displaystyle\lim_{x\to a} f(x) = f(a)$, since the equation cannot hold unless both sides are defined.
This is also why "direct substitution" (row 10 of section 3) works: it is valid exactly when $f$ is continuous at the point being substituted.

---

## 8. The derivative, defined as a limit

$$f'(a) = \lim_{h\to 0} \frac{f(a+h)-f(a)}{h} = \lim_{x\to a} \frac{f(x)-f(a)}{x-a}$$

Both forms are the same limit; the first uses a step size $h = x-a$, the second uses $x$ directly.
Every "hidden derivative" special limit (section 6 of `Special-Limits.md`) is this formula applied to a specific $f$ and $a$.

---

## 9. The definite integral, defined as a limit of Riemann sums

$$\int_a^b f(x)\,dx = \lim_{n\to\infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x, \qquad \Delta x = \frac{b-a}{n}$$

where $x_i^*$ is any sample point in the $i$-th subinterval.
This is the limit that technique L19 (recognizing a Riemann sum) reverses: given a sum with $i/n$ in it, you rebuild the $f$, $a$, $b$ that would have produced it.

---

## 10. Limits of sequences

**Formal definition:**

$$\lim_{n\to\infty} a_n = L$$

means: for every $\varepsilon > 0$, there is an integer $N$ such that $n > N \Rightarrow |a_n - L| < \varepsilon$.

**Sequence limit laws** mirror the function limit laws in section 3 exactly (sum, difference, constant multiple, product, quotient with nonzero denominator limit, power) since a sequence is just a function with domain restricted to the positive integers.

**Squeeze theorem for sequences:** if $b_n \le a_n \le c_n$ for all $n$ past some point, and $\lim b_n = \lim c_n = L$, then $\lim a_n = L$; same statement as section 5 with $n\to\infty$ in place of $x\to a$.

**Monotone convergence theorem:** a sequence that is monotonic (always increasing, or always decreasing) and bounded must converge; this proves a limit exists without computing its value.

---

## Sources and cross-references

Standard definitions and theorem statements collected from a first-calculus curriculum (matches the limits unit of AU MATH 265 / equivalent Calculus I courses).
Where a formula here produces a specific numeric value worth memorizing, see `Special-Limits.md`.
Where a formula here needs an algebraic rewrite before it applies, see the matching L-numbered technique in `Calculus-Techniques-Limits-Derivatives-Integrals.md`.

# Algebra / Calculus / Trig Quick Reference

## 1. Quadratic formula

For `ax² + bx + c = 0` (a ≠ 0):

```
x = (-b ± √(b² - 4ac)) / (2a)
```

- Discriminant `D = b² - 4ac`
- `D > 0` → two distinct real roots
- `D = 0` → one repeated real root, `x = -b/(2a)`
- `D < 0` → two complex conjugate roots, `x = (-b ± i√(-D)) / (2a)`

Related forms:
- Sum of roots: `x₁ + x₂ = -b/a`
- Product of roots: `x₁x₂ = c/a`
- Vertex form via completing the square: `a(x + b/(2a))² + (c - b²/(4a))`

---

## 2. Transformation steps for `y = a·f(b·(x - h)) + k`

| Parameter | Meaning | Effect on graph |
|---|---|---|
| `a` | vertical scale factor | stretch if `|a| > 1`, compress if `0 < |a| < 1`; reflects over the x-axis if `a < 0` |
| `b` | horizontal scale factor (inside the function) | stretch if `0 < |b| < 1`, compress if `|b| > 1` (i.e. actual horizontal factor is `1/b`); reflects over the y-axis if `b < 0` |
| `h` | horizontal shift | shifts right if `h > 0`, left if `h < 0` |
| `k` | vertical shift | shifts up if `k > 0`, down if `k < 0` |

### Order of transformations (apply to the base graph `y = f(x)`)

Because the argument is written as `b·(x - h)` (b is factored out first), horizontal operations must be applied in this order:

1. Horizontal stretch/compression by factor `1/b` (and reflect over y-axis if `b < 0`)
2. Horizontal shift by `h` (left/right)
3. Vertical stretch/compression by factor `a` (and reflect over x-axis if `a < 0`)
4. Vertical shift by `k` (up/down)

Steps 1-2 (horizontal group) and steps 3-4 (vertical group) act on independent variables, so the two groups can be done in either order relative to each other. Within each group, scale/reflect must come before shift, because the formula subtracts `h` from `x` only after `b` is factored out (and similarly `a` scales `f(...)` before `k` is added).

If instead the equation were written as `y = a·f(bx - h) + k` (h not factored with b), the horizontal shift amount changes to `h/b` and the same "scale then shift" order still applies to the rewritten `b·(x - h/b)`.

---

## 3. Techniques for evaluating limits

General order of attack: try direct substitution first; if it produces an indeterminate form, pick a technique below based on the shape of the expression.

### Indeterminate forms
`0/0`, `∞/∞`, `∞ - ∞`, `0·∞`, `1^∞`, `0⁰`, `∞⁰`

### Core techniques

1. **Direct substitution** - plug in the value; works whenever the function is continuous there.
2. **Factoring** - factor numerator/denominator and cancel the common factor causing `0/0`.
   - e.g. `lim(x→2) (x² - 4)/(x - 2) = lim (x - 2)(x + 2)/(x - 2) = 4`
3. **Rationalizing (multiply by the conjugate)** - for expressions with a single square root causing `0/0`; multiply top and bottom by the conjugate of the radical expression.
4. **Multiply by conjugate of both numerator and denominator** - when both numerator and denominator contain radicals; multiply by each conjugate in turn (or their product) to clear both radicals.
5. **Divide by the highest power of x in the denominator** - for limits as `x → ±∞` of rational functions.
   - degree(num) < degree(denom) → limit is 0
   - degree(num) = degree(denom) → limit is ratio of leading coefficients
   - degree(num) > degree(denom) → limit is ±∞ (no horizontal asymptote)
6. **L'Hopital's Rule** - for `0/0` or `∞/∞`: `lim f(x)/g(x) = lim f'(x)/g'(x)`, provided the new limit exists (can reapply repeatedly).
7. **Squeeze (Sandwich) Theorem** - if `g(x) ≤ f(x) ≤ h(x)` near a point and `lim g = lim h = L`, then `lim f = L`.
8. **Special trig limits**
   - `lim(x→0) sin(x)/x = 1`
   - `lim(x→0) (1 - cos(x))/x = 0`
   - `lim(x→0) tan(x)/x = 1`
9. **One-sided limits** - evaluate left-hand and right-hand limits separately; the two-sided limit exists only if they agree. Required for piecewise functions and functions with absolute values or vertical asymptotes.
10. **Absolute value expressions** - split into cases based on the sign of the inner expression, then take the matching one-sided limit.
11. **Substitution / change of variable** - let `u = g(x)` to turn an unfamiliar limit into a standard one (e.g. as `x → a`, `u → g(a)`).
12. **The `e` limit** - `lim(n→∞) (1 + 1/n)ⁿ = e`, and more generally `lim(x→0) (1 + x)^(1/x) = e`. Useful for `1^∞` forms.

### Workarounds for the harder indeterminate forms

- **`∞ - ∞`**: combine into a single fraction (common denominator), or rationalize if radicals are involved, then reduce to `0/0` or `∞/∞`.
- **`0·∞`**: rewrite one factor as a reciprocal to convert to `0/0` or `∞/∞`, then apply L'Hopital or algebraic simplification.
- **`1^∞`, `0⁰`, `∞⁰`**: take the natural log of the expression, evaluate `lim ln(y)` (usually now `0·∞` or `0/0`), then exponentiate: `lim y = e^(lim ln(y))`.
- **Limits at infinity with nested radicals**: factor the highest power of `x` out from under each radical before simplifying.

---

## 4. Factoring formulas (powers 2 through 5)

### Difference and sum of squares
```
a² - b² = (a - b)(a + b)
a² + b² = does not factor over the reals
        = (a + bi)(a - bi)   [over the complex numbers]
```

### Difference and sum of cubes
```
a³ - b³ = (a - b)(a² + ab + b²)
a³ + b³ = (a + b)(a² - ab + b²)
```
Mnemonic: "SOAP" - Same sign, Opposite sign, Always Positive (for the sign of the middle term).

### Difference and sum of 4th powers
```
a⁴ - b⁴ = (a - b)(a + b)(a² + b²)              [difference of squares, applied twice]
a⁴ + b⁴ = (a² + √2·ab + b²)(a² - √2·ab + b²)   [not a rational factorization]
```

### Difference and sum of 5th powers
```
a⁵ - b⁵ = (a - b)(a⁴ + a³b + a²b² + ab³ + b⁴)
a⁵ + b⁵ = (a + b)(a⁴ - a³b + a²b² - ab³ + b⁴)
```

### General pattern (any positive integer n)
```
aⁿ - bⁿ = (a - b)(aⁿ⁻¹ + aⁿ⁻²b + aⁿ⁻³b² + ... + bⁿ⁻¹)
```
always factors this way.

```
aⁿ + bⁿ = (a + b)(aⁿ⁻¹ - aⁿ⁻²b + aⁿ⁻³b² - ... + bⁿ⁻¹)
```
only factors this way when `n` is **odd**. When `n` is even, `aⁿ + bⁿ` has no such rational factorization (for n=2, it doesn't factor over the reals at all; for n=4, only the irrational factorization above exists).

---

## 5. Trigonometric identities

### Pythagorean identities
```
sin²(x) + cos²(x) = 1
1 + tan²(x) = sec²(x)
1 + cot²(x) = csc²(x)
```

### Reciprocal identities
```
csc(x) = 1/sin(x)
sec(x) = 1/cos(x)
cot(x) = 1/tan(x)
```

### Quotient identities
```
tan(x) = sin(x)/cos(x)
cot(x) = cos(x)/sin(x)
```

### Even/odd (negative angle) identities
```
sin(-x) = -sin(x)        [odd]
cos(-x) = cos(x)         [even]
tan(-x) = -tan(x)        [odd]
```

### Co-function identities
```
sin(π/2 - x) = cos(x)
cos(π/2 - x) = sin(x)
tan(π/2 - x) = cot(x)
```

### Sum and difference identities
```
sin(a ± b) = sin(a)cos(b) ± cos(a)sin(b)
cos(a ± b) = cos(a)cos(b) ∓ sin(a)sin(b)
tan(a ± b) = (tan(a) ± tan(b)) / (1 ∓ tan(a)tan(b))
```

### Double angle identities
```
sin(2x) = 2sin(x)cos(x)
cos(2x) = cos²(x) - sin²(x)
        = 1 - 2sin²(x)
        = 2cos²(x) - 1
tan(2x) = 2tan(x) / (1 - tan²(x))
```

### Power-reduction identities (rearranged double angle)
```
sin²(x) = (1 - cos(2x)) / 2      ⇔   1 - cos(2x) = 2sin²(x)
cos²(x) = (1 + cos(2x)) / 2      ⇔   1 + cos(2x) = 2cos²(x)
tan²(x) = (1 - cos(2x)) / (1 + cos(2x))
```

### Half-angle identities
```
sin(x/2) = ± √((1 - cos(x)) / 2)
cos(x/2) = ± √((1 + cos(x)) / 2)
tan(x/2) = (1 - cos(x)) / sin(x)
         = sin(x) / (1 + cos(x))
```
(sign in the √ is chosen based on which quadrant `x/2` falls in)

### Product-to-sum identities
```
sin(a)cos(b) = 1/2 [sin(a+b) + sin(a-b)]
cos(a)sin(b) = 1/2 [sin(a+b) - sin(a-b)]
cos(a)cos(b) = 1/2 [cos(a-b) + cos(a+b)]
sin(a)sin(b) = 1/2 [cos(a-b) - cos(a+b)]
```

### Sum-to-product identities
```
sin(a) + sin(b) = 2sin((a+b)/2)cos((a-b)/2)
sin(a) - sin(b) = 2cos((a+b)/2)sin((a-b)/2)
cos(a) + cos(b) = 2cos((a+b)/2)cos((a-b)/2)
cos(a) - cos(b) = -2sin((a+b)/2)sin((a-b)/2)
```

# Techniques for Evaluating Limits, Derivatives, and Integrals

A complete catalog of the standard techniques, each with a worked example and the steps used to solve it.
The organizing idea is that evaluation is a *routing* problem: the hard part is rarely the algebra, it is recognizing which of the thirty-odd techniques the expression is asking for.
So each technique below leads with its **trigger** (what the problem looks like when this is the right tool) before the example.

Every numeric answer in this file was independently recomputed with SymPy and checked against a direct numerical evaluation before being written down.
The verification script and its output are recorded at the end of the file.

Companion sheets in this folder: `Special-Limits.md` (the memorize-outright limit table) and `Algebra-Calc-Trig-Reference.md` (the identities these techniques assume).

---

## How to use this file

1. Identify the **form** you are facing (a $0/0$, an $\infty-\infty$, a product of unlike functions, a radical, a rational function).
2. Jump to the matching technique using the index below.
3. Work the example, then the trigger line tells you when the technique will fail and what to escalate to.

### Index

**Part 1 - Limits (L1 to L20)**

| # | Technique | Trigger |
| :--- | :--- | :--- |
| L1 | Direct substitution | Function is continuous at the point |
| L2 | Factor and cancel | $0/0$ with polynomials |
| L3 | Conjugate multiplication | $0/0$ with a square root |
| L4 | Combine into a single fraction | $\infty-\infty$ or a compound fraction |
| L5 | Standard trig limits | $\sin$, $\tan$, $1-\cos$ over an argument going to $0$ |
| L6 | Squeeze theorem | A bounded factor times something going to $0$ |
| L7 | Divide by the dominant power | Rational function as $x\to\pm\infty$ |
| L8 | Degree comparison shortcut | Ratio of polynomials at infinity |
| L9 | Radicals at infinity and the $\lvert x\rvert$ trap | $\sqrt{\text{quadratic}}$ as $x\to-\infty$ |
| L10 | L'Hopital's rule | $0/0$ or $\infty/\infty$ after substitution |
| L11 | Taylor / Maclaurin expansion | $0/0$ needing several L'Hopital passes |
| L12 | Change of variable | Awkward root or nested argument |
| L13 | One-sided limits | Absolute value, piecewise, or a pole |
| L14 | Logarithm trick for indeterminate powers | $1^\infty$, $0^0$, $\infty^0$ |
| L15 | Rewriting $0\cdot\infty$ | A product where one factor blows up |
| L16 | Bounded over unbounded | $\sin x / x$ as $x\to\infty$ |
| L17 | Epsilon-delta proof | The question says "prove" |
| L18 | Showing a limit does not exist | Two paths give different values |
| L19 | Recognizing a Riemann sum | $\lim_{n\to\infty}$ of a sum with $i/n$ in it |
| L20 | Sequence-specific tools | Recursions, monotone convergence, Stolz-Cesaro |

**Part 2 - Derivatives (D1 to D18)**

| # | Technique | Trigger |
| :--- | :--- | :--- |
| D1 | Definition / first principles | The question says "by definition" |
| D2 | Power, constant multiple, sum rules | Polynomials and roots |
| D3 | Product rule | A product of two non-trivial factors |
| D4 | Quotient rule | A genuine fraction that will not simplify |
| D5 | Chain rule | A function inside a function |
| D6 | Trig, exponential, log tables | Named functions |
| D7 | Inverse trig and hyperbolic | $\arcsin$, $\arctan$, $\sinh$ |
| D8 | Implicit differentiation | $y$ cannot be isolated |
| D9 | Logarithmic differentiation | Variable exponent, or a big product/quotient |
| D10 | Inverse function derivative | You need $(f^{-1})'$ without inverting $f$ |
| D11 | Parametric and polar | $x(t), y(t)$ or $r(\theta)$ |
| D12 | Higher-order and Leibniz rule | An $n$th derivative pattern |
| D13 | Related rates | Two quantities changing in time |
| D14 | Differentials / linearization | Approximate a nearby value |
| D15 | Partial derivatives | More than one input variable |
| D16 | Multivariable chain rule and gradients | Composition of multivariable maps |
| D17 | Differentiating an integral (FTC 1 and Leibniz) | The variable is in a limit of integration |
| D18 | Numerical differentiation | No formula, only data or a black box |

**Part 3 - Integrals (I1 to I22)**

| # | Technique | Trigger |
| :--- | :--- | :--- |
| I1 | Reverse the derivative table | The integrand is already a known derivative |
| I2 | $u$-substitution | An inner function and (a multiple of) its derivative |
| I3 | Integration by parts | A product of unlike types (LIATE) |
| I4 | Tabular integration | Polynomial times $e^{ax}$, $\sin$, $\cos$ |
| I5 | Trigonometric integrals | Powers of $\sin/\cos$ or $\sec/\tan$ |
| I6 | Trigonometric substitution | $\sqrt{a^2-x^2}$, $\sqrt{a^2+x^2}$, $\sqrt{x^2-a^2}$ |
| I7 | Completing the square | An irreducible quadratic with a linear term |
| I8 | Partial fractions | A proper rational function |
| I9 | Long division first | An improper rational function |
| I10 | Weierstrass substitution $t=\tan(x/2)$ | A rational function of $\sin$ and $\cos$ |
| I11 | Rationalizing substitutions | Roots of a linear expression |
| I12 | Reduction formulas | A power $n$ left symbolic |
| I13 | Symmetry and periodicity | A symmetric interval |
| I14 | The reflection (king) property | $\int_a^b f(a+b-x)\,dx$ closes the loop |
| I15 | Fundamental Theorem part 2 | A definite integral of a function you can antidifferentiate |
| I16 | Riemann sums from the definition | The question says "by definition" |
| I17 | Improper integrals and convergence tests | An infinite limit or an interior blow-up |
| I18 | Numerical quadrature | No elementary antiderivative |
| I19 | Term-by-term series integration | The integrand has a known power series |
| I20 | Differentiation under the integral sign | A parameter you can introduce and differentiate |
| I21 | Multiple integrals and Jacobians | Area, volume, or a change of coordinates |
| I22 | Vector-calculus shortcuts | A line or surface integral with a boundary |

---

# Part 1 - Techniques for Evaluating Limits

The single most useful habit: **always substitute first**.
Substitution either gives the answer (L1) or tells you exactly which indeterminate form you have, and the form dictates the technique.

The seven indeterminate forms and where each routes:

| Form | Route to |
| :--- | :--- |
| $\dfrac{0}{0}$ | L2, L3, L4, L5, L10, L11, L12 |
| $\dfrac{\infty}{\infty}$ | L7, L8, L10 |
| $\infty-\infty$ | L4, L9 (then re-check the form) |
| $0\cdot\infty$ | L15 (rewrite as a quotient, then L10) |
| $1^{\infty}$, $0^{0}$, $\infty^{0}$ | L14 (take logs, then L10 or L11) |

Anything that is *not* on that list is not indeterminate.
In particular $\frac{5}{0}$ is not indeterminate: it is an infinite limit or a one-sided pair, and it routes to L13.

---

## L1. Direct substitution (continuity)

**Trigger.** The function is built from polynomials, roots, exponentials, logs, and trig, and the point is inside the domain.

**Why it works.** Every elementary function is continuous on its domain, and continuity is exactly the statement 
## $\lim_{x\to a} f(x) = f(a)$.

**Example.** 
## Evaluate $\displaystyle\lim_{x\to 2}\frac{x^3-4x+1}{x+3}$.

*Steps.*

1. Check the denominator at the point: $2+3 = 5 \ne 0$, so the point is in the domain.
2. Substitute: numerator $= 8 - 8 + 1 = 1$.
3. Divide: the limit is $\dfrac{1}{5}$.

**Failure mode.** If substitution gives $\frac00$, $\frac{\infty}{\infty}$, or an undefined expression, this technique is done and the form tells you where to go next.
Do not skip this step even when you expect it to fail, because the *kind* of failure is the routing information.

**MATH265 exam question (Q3.2c).** 
## Evaluate $\displaystyle\lim_{x\to 0}\frac{6x-9}{x^3-12x+3}$.

1. This one is included specifically because it looks like it should need a technique and does not.
2. Substitute directly: $\dfrac{6(0)-9}{0-0+3} = \dfrac{-9}{3} = -3$.
3. The limit is $-3$, and the whole exercise is checking that you try substitution before reaching for machinery.

**MATH265 exam question (Q3.1a).** Evaluate $\displaystyle\lim_{x\to 2}\left(3x^2-2x+1\right)$.

1. A polynomial is continuous everywhere, so direct substitution is legal with no diagnosis step needed.
2. Substitute: $3(2)^2-2(2)+1 = 12-4+1$.
3. The limit is $9$.

---

## L2. Factor and cancel

**Trigger.** Substitution gives $\frac00$ and both numerator and denominator are polynomials (or factorable).

**Why it works.** A $\frac00$ from polynomials means $(x-a)$ divides both.
The limit ignores the single point $x=a$, so cancelling that common factor changes nothing about the limit.

**Example.** 
## Evaluate $\displaystyle\lim_{x\to 3}\frac{x^2-9}{x^2-x-6}$.

*Steps.*

## 1. Substitute: $\frac{9-9}{9-3-6} = \frac00$, so it is indeterminate and $(x-3)$ is a factor of both.
2. Factor the numerator: $x^2-9 = (x-3)(x+3)$.
3. Factor the denominator: $x^2-x-6 = (x-3)(x+2)$.
4. Cancel the common $(x-3)$, valid because $x \ne 3$ while the limit is being taken.
5. The expression is now $\dfrac{x+3}{x+2}$, which is continuous at $3$.
6. Substitute: $\dfrac{6}{5}$.

**Second example (higher degree).** $\displaystyle\lim_{x\to 1}\frac{x^3-1}{x^4-1}$.

1. Both vanish at $x=1$.
2. Use the difference-of-powers factorization: $x^3-1 = (x-1)(x^2+x+1)$ and $x^4-1 = (x-1)(x^3+x^2+x+1)$.
3. Cancel and substitute: $\dfrac{1+1+1}{1+1+1+1} = \dfrac{3}{4}$.

**Pattern worth memorizing.** $\displaystyle\lim_{x\to 1}\frac{x^m-1}{x^n-1} = \frac{m}{n}$, which is the general form of the example above.

**MATH265 exam question (Q3.2a).** Evaluate $\displaystyle\lim_{x\to 1}\frac{x^2-1}{x^3-1}$.

1. This is exactly the memorized pattern above with $m=2$, $n=3$, so the answer is $\dfrac23$ by inspection.
2. Worked from scratch: factor both sides, $x^2-1=(x-1)(x+1)$ and $x^3-1=(x-1)(x^2+x+1)$.
3. Cancel the shared $(x-1)$ and substitute $x=1$: $\dfrac{1+1}{1+1+1} = \dfrac23$.

**MATH265 exam question (Q4.1) — factor/cancel feeding an asymptote analysis.** Find the vertical and horizontal asymptotes of $\displaystyle f(x)=\frac{x^2-3x-4}{x^2-16}$.

1. Factor first, always: $x^2-3x-4=(x-4)(x+1)$ and $x^2-16=(x-4)(x+4)$.
2. The $(x-4)$ factor cancels, leaving $f(x)=\dfrac{x+1}{x+4}$ for $x\ne4$: a **cancelled factor is a hole**, not an asymptote, sitting at $\left(4,\frac58\right)$.
3. The surviving denominator zero $x=-4$ is a genuine vertical asymptote, confirmed because the numerator there is $-3\ne0$.
4. The horizontal asymptote comes from L8 (degree comparison): both original degrees are $2$, so $y=\dfrac{1}{1}=1$.
5. Result: vertical asymptote $x=-4$, horizontal asymptote $y=1$, hole at $\left(4,\frac58\right)$.

**The trap this question is built around.** Reporting $x=4$ as a vertical asymptote before checking whether the offending factor cancels.

---

## L3. Conjugate multiplication (rationalizing)

**Trigger.** Substitution gives $\frac00$ and a square root appears in the numerator or denominator.

**Why it works.** Multiplying by $\frac{\text{conjugate}}{\text{conjugate}}$ turns $(\sqrt{A}-\sqrt{B})(\sqrt{A}+\sqrt{B})$ into $A-B$, which removes the root and exposes the cancelling factor.

**Example.** 
### Evaluate $\displaystyle\lim_{x\to 0}\frac{\sqrt{x+4}-2}{x}$.

*Steps.*

### 1. Substitute: $\frac{2-2}{0} = \frac00$.
### 2. Multiply top and bottom by the conjugate $\sqrt{x+4}+2$.
### 3. Numerator becomes $(x+4)-4 = x$.
### 4. The expression is $\dfrac{x}{x\left(\sqrt{x+4}+2\right)} = \dfrac{1}{\sqrt{x+4}+2}$ for $x\ne 0$.
### 5. Substitute: $\dfrac{1}{2+2} = \dfrac{1}{4}$.

**Variant with the root on the bottom.** $\displaystyle\lim_{x\to 9}\frac{x-9}{\sqrt{x}-3}$: multiply by $\frac{\sqrt{x}+3}{\sqrt{x}+3}$ to get $\sqrt{x}+3 \to 6$.

**Variant with two roots.** $\displaystyle\lim_{x\to 0}\frac{\sqrt{1+x}-\sqrt{1-x}}{x}$: the conjugate gives numerator $(1+x)-(1-x) = 2x$, so the value is $\dfrac{2}{1+1} = 1$.

**Cube roots.** Use the identity $a^3-b^3 = (a-b)(a^2+ab+b^2)$ instead, so the multiplier for $\sqrt[3]{A}-\sqrt[3]{B}$ is $\sqrt[3]{A^2}+\sqrt[3]{AB}+\sqrt[3]{B^2}$.

**MATH265 exam question (Q3.1d) — a root on both top and bottom.** 
### Evaluate $\displaystyle\lim_{x\to 2}\frac{\sqrt{6-x}-2}{\sqrt{3-x}-1}$.

1. Substitute: $\dfrac{\sqrt4-2}{\sqrt1-1} = \dfrac00$, and there are two separate roots to clear.
2. Multiply by both conjugates at once: $\left(\sqrt{6-x}+2\right)$ on top and $\left(\sqrt{3-x}+1\right)$ on the bottom (cross-multiplied so both differences of squares appear).
3. The numerator conjugate product is $(6-x)-4 = 2-x$; the denominator conjugate product is $(3-x)-1 = 2-x$: the **same** factor appears on both sides.
4. Cancel the shared $(2-x)$, leaving $\dfrac{\sqrt{3-x}+1}{\sqrt{6-x}+2}$, which is now continuous at $x=2$.
5. Substitute: $\dfrac{\sqrt1+1}{\sqrt4+2} = \dfrac{2}{4} = \dfrac12$.

---

## L4. Combine into a single fraction

**Trigger.** The form is $\infty-\infty$, or the expression is a fraction built out of fractions.

**Why it works.** $\infty-\infty$ is indeterminate only because the two pieces are written apart.
A common denominator turns the difference into a single quotient whose form ($\frac00$ or $\frac{\infty}{\infty}$) is then attackable.

**Example (compound fraction).** Evaluate $\displaystyle\lim_{x\to 2}\frac{\frac{1}{x}-\frac{1}{2}}{x-2}$.

*Steps.*

1. Substitute: $\frac{0}{0}$.
2. Combine the numerator over $2x$: $\dfrac{2-x}{2x}$.
3. The whole expression becomes $\dfrac{2-x}{2x(x-2)}$.
4. Note $2-x = -(x-2)$ and cancel: $\dfrac{-1}{2x}$.
5. Substitute: $-\dfrac{1}{4}$.

**Example ($\infty-\infty$).** Evaluate $\displaystyle\lim_{x\to 0}\left(\frac{1}{\sin x}-\frac{1}{x}\right)$.

1. Each term blows up, with opposite signs from each side, so the form is $\infty-\infty$.
2. Common denominator: $\dfrac{x-\sin x}{x\sin x}$, which is now $\frac00$.
3. Either apply L11 (series): $x-\sin x \approx \frac{x^3}{6}$ and $x\sin x \approx x^2$, so the ratio behaves like $\frac{x}{6}$.
4. The limit is $0$.

---

## L5. The standard trigonometric limits

**Trigger.** A trig function whose argument goes to $0$, divided by something also going to $0$.

**The two facts everything reduces to.**

$$\lim_{\theta\to 0}\frac{\sin\theta}{\theta} = 1, \qquad \lim_{\theta\to 0}\frac{1-\cos\theta}{\theta^2} = \frac{1}{2}.$$

**Why it works.** The first is the squeeze theorem applied to $\cos\theta \le \frac{\sin\theta}{\theta}\le 1$; the second follows by multiplying by the conjugate $1+\cos\theta$.

**Example.** Evaluate $\displaystyle\lim_{x\to 0}\frac{\sin 5x}{\sin 3x}$.

*Steps.*

1. Substitute: $\frac00$.
2. Manufacture the matching arguments by multiplying and dividing: write the expression as
$$\frac{\sin 5x}{5x}\cdot\frac{3x}{\sin 3x}\cdot\frac{5x}{3x}.$$
3. The first factor $\to 1$ and the second $\to 1$ by the standard limit.
4. The third factor is the constant $\frac53$.
5. The limit is $\dfrac{5}{3}$.

**The general pattern.** $\displaystyle\lim_{x\to 0}\frac{\sin(ax)}{bx} = \frac{a}{b}$.
Every problem in this family is the work of arranging the expression until each trig piece has its own matching denominator.

**Second example.** $\displaystyle\lim_{x\to 0}\frac{1-\cos x}{x\sin x}$.

1. Divide numerator and denominator by $x^2$: $\dfrac{(1-\cos x)/x^2}{(\sin x)/x}$.
2. Numerator $\to \frac12$, denominator $\to 1$.
3. The limit is $\dfrac{1}{2}$.

**MATH265 exam question (Q3.1e).** Evaluate $\displaystyle\lim_{x\to 0}\frac{\sin(3x)}{x^2-x}$.

1. Substitute: $\dfrac{\sin 0}{0-0} = \dfrac00$, and the sine says build the special limit.
2. Factor the denominator: $x^2-x = x(x-1)$.
3. Force a matching $3x$ underneath the sine: $\dfrac{\sin(3x)}{x(x-1)} = \dfrac{\sin(3x)}{3x}\cdot\dfrac{3x}{x(x-1)} = \dfrac{\sin(3x)}{3x}\cdot\dfrac{3}{x-1}$.
4. The first factor $\to1$ by the standard limit; the second $\to\dfrac{3}{0-1}=-3$.
5. The limit is $-3$.

**MATH265 exam question (Q3.2b) — a $1-\cos$ form with a doubled argument.** Evaluate $\displaystyle\lim_{x\to 0}\frac{x^2}{1-\cos(2x)}$.

1. Substitute: $\dfrac{0}{1-1} = \dfrac00$.
2. Use the identity $1-\cos(2\theta) = 2\sin^2\theta$ with $\theta=x$, which removes the cosine entirely rather than reaching for the memorized $1-\cos$ limit directly: $\dfrac{x^2}{1-\cos(2x)} = \dfrac{x^2}{2\sin^2 x}$.
3. Rewrite as a squared standard limit: $\dfrac12\left(\dfrac{x}{\sin x}\right)^2$.
4. The bracket $\to 1$, so the limit is $\dfrac12$.

---

## L6. The squeeze (sandwich) theorem

**Trigger.** A factor that oscillates but stays bounded ($\sin\frac1x$, $\cos\frac1x$, a fractional part) multiplied by something that goes to $0$.

**Why it works.** If $g(x)\le f(x)\le h(x)$ near $a$ and $g,h$ share the limit $L$, then $f$ has no room to do anything else.

**Example.** Evaluate $\displaystyle\lim_{x\to 0} x^2\sin\frac{1}{x}$.

*Steps.*

1. L'Hopital and substitution both fail, because $\sin\frac1x$ has no limit at $0$.
2. Bound the oscillating factor: $-1 \le \sin\frac1x \le 1$ for every $x\ne 0$.
3. Multiply through by $x^2$, which is non-negative so the inequalities keep their direction: $-x^2 \le x^2\sin\frac1x \le x^2$.
4. Both outer bounds go to $0$ as $x\to 0$.
5. Therefore the limit is $0$.

**The step people get wrong.** Multiplying an inequality by a factor that can be negative flips it.
State that $x^2 \ge 0$ explicitly, or use the absolute-value form $\left\lvert x^2\sin\frac1x\right\rvert \le x^2$ and conclude with $\lvert f\rvert \to 0 \implies f\to 0$.

**MATH265 exam question (Q3.3a) — squeeze chained onto a degree comparison.** Evaluate $\displaystyle\lim_{x\to\infty}\left(\frac{3x^2-4}{2x^4+2x+4}\right)\sin x$.

1. $\sin x$ has no limit, so do not try to evaluate the product directly; handle the rational factor $R(x)$ on its own first.
2. By L8, the denominator's degree ($4$) beats the numerator's ($2$), so $\displaystyle\lim_{x\to\infty}R(x) = 0$.
3. Bound the oscillating factor: $-1\le\sin x\le1$, so $-\lvert R(x)\rvert \le R(x)\sin x \le \lvert R(x)\rvert$.
4. Both outer bounds $\to 0$ because $R(x)\to0$, so the middle is squeezed to $0$.

This is the general pattern behind L16 as well: a bounded oscillating factor is harmless once it is multiplying something that already dies.

---

## L7. Divide by the dominant power (limits at infinity)

**Trigger.** $x\to\pm\infty$ with a ratio of polynomials or polynomial-like expressions.

**Why it works.** $\frac{1}{x^k}\to 0$ for every $k>0$, so dividing by the highest power turns every subordinate term into a term you can substitute $0$ into.

**Example.** Evaluate $\displaystyle\lim_{x\to\infty}\frac{3x^2-2x+7}{5x^2+x-1}$.

*Steps.*

1. Identify the highest power present anywhere: $x^2$.
2. Divide every term, top and bottom, by $x^2$:
$$\frac{3-\frac{2}{x}+\frac{7}{x^2}}{5+\frac{1}{x}-\frac{1}{x^2}}.$$
3. Send each $\frac{1}{x^k}$ to $0$.
4. The limit is $\dfrac{3}{5}$.

---

## L8. Degree comparison (the shortcut for L7)

For $\displaystyle\lim_{x\to\pm\infty}\frac{P(x)}{Q(x)}$ with $\deg P = m$ and $\deg Q = n$:

| Case | Limit |
| :--- | :--- |
| $m < n$ | $0$ |
| $m = n$ | ratio of the leading coefficients |
| $m > n$ | $\pm\infty$, sign from the leading coefficients and the parity of $m-n$ |

**Example (equal degrees).** Evaluate $\displaystyle\lim_{x\to\infty}\frac{4x^3+x}{2x^3-9}$.

*Steps.*

1. Read the degrees: $\deg P = 3$ and $\deg Q = 3$.
2. They are equal, so the middle row of the table applies.
3. Take the ratio of the leading coefficients: $\dfrac{4}{2}$.
4. The limit is $2$.

**Example (bottom heavier).** Evaluate $\displaystyle\lim_{x\to-\infty}\frac{x^2+1}{x^3}$.

*Steps.*

1. Read the degrees: $\deg P = 2$ and $\deg Q = 3$.
2. Since $m < n$, the first row applies and the denominator wins.
3. The limit is $0$, from either direction.

**Example (top heavier, where the sign matters).** Evaluate $\displaystyle\lim_{x\to-\infty}\frac{x^3}{x^2+1}$.

1. Here $m=3 > n=2$, so the magnitude goes to infinity and only the sign is in question.
2. The ratio behaves like $x$ for large $\lvert x\rvert$, and $m-n = 1$ is odd.
3. As $x\to-\infty$ that is negative, so the limit is $-\infty$.

**Use it as a check, not as the work.** On an exam that asks you to show your work, present L7 and use L8 to confirm you did not slip.

**MATH265 exam question (Q3.2d).** Evaluate $\displaystyle\lim_{x\to\infty}\frac{5-2x^3}{x^2+2}$.

1. Read the degrees: numerator degree $3$, denominator degree $2$, so $m>n$ and the top wins.
2. By L7, dividing by $x^2$ leaves $\dfrac{\frac{5}{x^2}-2x}{1+\frac{2}{x^2}}$, whose numerator behaves like $-2x\to-\infty$ while the denominator $\to1$.
3. The negative leading coefficient and $m-n=1$ (odd) send the ratio to $-\infty$.
4. There is no horizontal asymptote here, only the answer $-\infty$.

---

## L9. Radicals at infinity, and the $\lvert x \rvert$ trap

**Trigger.** A square root of a polynomial as $x\to\pm\infty$, or a $\sqrt{\ } - \sqrt{\ }$ difference at infinity.

**The rule that gets missed.** $\sqrt{x^2} = \lvert x\rvert$, which is $x$ when $x\to+\infty$ but $-x$ when $x\to-\infty$.
Pulling $x$ out of a root as $x\to-\infty$ without the sign flip is the single most common error in this family.

**Example (the trap).** Evaluate $\displaystyle\lim_{x\to-\infty}\frac{\sqrt{4x^2+x}}{x}$.

*Steps.*

1. Factor $x^2$ out of the root: $\sqrt{4x^2+x} = \sqrt{x^2}\sqrt{4+\frac1x} = \lvert x\rvert\sqrt{4+\frac1x}$.
2. Because $x\to-\infty$, $\lvert x\rvert = -x$.
3. The expression is $\dfrac{-x\sqrt{4+\frac1x}}{x} = -\sqrt{4+\tfrac1x}$.
4. Send $\frac1x\to 0$: the limit is $-2$.

The same limit as $x\to+\infty$ is $+2$, and the only difference in the whole calculation is step 2.

**Example ($\infty-\infty$ with roots).** Evaluate $\displaystyle\lim_{x\to\infty}\left(\sqrt{x^2+3x}-x\right)$.

1. The form is $\infty-\infty$, so combine using the conjugate $\sqrt{x^2+3x}+x$.
2. Numerator becomes $(x^2+3x)-x^2 = 3x$.
3. The expression is $\dfrac{3x}{\sqrt{x^2+3x}+x}$, now $\frac{\infty}{\infty}$.
4. Divide top and bottom by $x$ (positive, so $\sqrt{x^2+3x}/x = \sqrt{1+\frac3x}$): $\dfrac{3}{\sqrt{1+\frac3x}+1}$.
5. The limit is $\dfrac{3}{2}$.

**Generalization worth carrying.** $\displaystyle\lim_{x\to\infty}\left(\sqrt{x^2+bx+c}-x\right) = \frac{b}{2}$, independent of $c$.

---

## L10. L'Hopital's rule

**Trigger.** Substitution gives exactly $\frac00$ or $\frac{\infty}{\infty}$.

**Statement.** If $f,g$ are differentiable near $a$, $g'\ne 0$ near $a$, and $\frac{f}{g}$ has form $\frac00$ or $\frac{\infty}{\infty}$ at $a$, then
$$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$$
provided the right-hand limit exists.

**Example.** Evaluate $\displaystyle\lim_{x\to 0}\frac{e^x-1-x}{x^2}$.

*Steps.*

1. Substitute: $\frac{1-1-0}{0} = \frac00$. Rule applies.
2. Differentiate top and bottom **separately** (this is not the quotient rule): $\dfrac{e^x-1}{2x}$.
3. Substitute again: still $\frac00$, so apply the rule a second time.
4. Differentiate again: $\dfrac{e^x}{2}$.
5. Substitute: $\dfrac{1}{2}$.

**The three ways this rule is misused.**

1. Applying it when the form is not indeterminate.
   $\lim_{x\to 0}\frac{\cos x}{x^2}$ is $\frac10$, not $\frac00$, and the rule gives a wrong answer if you use it.
2. Using the quotient rule instead of differentiating the parts separately.
3. Looping forever.
   $\lim_{x\to\infty}\frac{\sqrt{x^2+1}}{x}$ cycles back to itself under the rule; L7 solves it in one line ($=1$).

**When it applies but is the wrong tool.** For $\frac{x-\sin x}{x^3}$ the rule needs three passes; the series in L11 needs none.

---

## L11. Taylor / Maclaurin expansion

**Trigger.** A $\frac00$ where L'Hopital would need two or more passes, or where the derivatives get messy.

**The expansions to know.** Each is valid near $0$.

| Function | Expansion |
| :--- | :--- |
| $e^x$ | $1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots$ |
| $\sin x$ | $x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$ |
| $\cos x$ | $1 - \frac{x^2}{2} + \frac{x^4}{24} - \cdots$ |
| $\ln(1+x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ |
| $\tan x$ | $x + \frac{x^3}{3} + \frac{2x^5}{15}+\cdots$ |
| $(1+x)^{\alpha}$ | $1 + \alpha x + \frac{\alpha(\alpha-1)}{2}x^2 + \cdots$ |

**Example.** Evaluate $\displaystyle\lim_{x\to 0}\frac{x-\sin x}{x^3}$.

*Steps.*

1. Expand the numerator far enough to survive the cancellation: $\sin x = x - \frac{x^3}{6} + O(x^5)$.
2. Subtract: $x - \sin x = \frac{x^3}{6} + O(x^5)$.
3. Divide by $x^3$: $\frac{1}{6} + O(x^2)$.
4. The limit is $\dfrac{1}{6}$.

**How far to expand.** Expand to the order of the denominator.
Here the denominator is $x^3$, so keep the numerator through $x^3$; stopping at $x$ would leave $0/x^3$ and lose the answer.

**Second example.** $\displaystyle\lim_{x\to 0}\frac{\cos x - 1 + \frac{x^2}{2}}{x^4} = \frac{1}{24}$, read straight off the $x^4$ term of $\cos x$.

---

## L12. Change of variable (substitution)

**Trigger.** A root of the variable, a nested argument, or a limit at infinity you would rather see at $0$.

**Why it works.** A limit is preserved under any substitution that is continuous and sends the old target to the new one.

**Example.** Evaluate $\displaystyle\lim_{x\to 1}\frac{\sqrt[3]{x}-1}{x-1}$.

*Steps.*

1. Let $u = \sqrt[3]{x}$, so $x = u^3$.
2. As $x\to 1$, $u\to 1$.
3. Rewrite: $\dfrac{u-1}{u^3-1} = \dfrac{u-1}{(u-1)(u^2+u+1)}$.
4. Cancel and substitute $u=1$: $\dfrac{1}{3}$.

**Example (infinity to zero).** $\displaystyle\lim_{x\to\infty} x\sin\frac{1}{x}$.

1. Let $t = \frac1x$, so $x = \frac1t$ and $t\to 0^+$.
2. The expression becomes $\dfrac{\sin t}{t}$.
3. By L5 the limit is $1$.

---

## L13. One-sided limits and piecewise functions

**Trigger.** An absolute value, a piecewise definition, an even root, or a denominator that hits zero without a matching zero on top.

**The rule.** $\lim_{x\to a} f(x)$ exists exactly when both one-sided limits exist and agree.

**Example.** Evaluate $\displaystyle\lim_{x\to 0}\frac{\lvert x\rvert}{x}$.

*Steps.*

1. Split the absolute value by sign: $\lvert x\rvert = x$ for $x>0$ and $-x$ for $x<0$.
2. From the right: $\frac{x}{x} = 1$, so the right-hand limit is $1$.
3. From the left: $\frac{-x}{x} = -1$, so the left-hand limit is $-1$.
4. The one-sided limits disagree, so the two-sided limit **does not exist**.

**Example (pole).** $\displaystyle\lim_{x\to 2}\frac{1}{x-2}$: from the right the denominator is a small positive, giving $+\infty$; from the left a small negative, giving $-\infty$.
The two-sided limit does not exist, and this is not an indeterminate form, so L'Hopital never enters the picture.

**Example (matching a piecewise function).** Find $a$ making
$$f(x) = \begin{cases} x^2+a & x\le 1\\ 3x-1 & x>1\end{cases}$$
continuous at $1$.

1. Left limit: $1+a$.
2. Right limit: $2$.
3. Set them equal: $1+a = 2$, so $a=1$.

**The two-step diagnosis this family always needs.** Substitute first; if the result is $\frac{k}{0}$ with $k\ne0$ (nothing to cancel, unlike L2's $\frac00$), go straight to the one-sided limits rather than hunting for an algebra step that does not exist.

**MATH265 exam question (Q3.1c) — direct $k/0$, no cancelling.** Evaluate $\displaystyle\lim_{x\to 3}\frac{2x^2-x+1}{x-3}$.

1. Numerator at $x=3$: $18-3+1=16\ne0$; denominator: $0$. This is $\frac{16}{0}$, so there is nothing to factor.
2. From the left, $x-3\to0^-$, giving $\dfrac{16}{0^-}\to-\infty$.
3. From the right, $x-3\to0^+$, giving $\dfrac{16}{0^+}\to+\infty$.
4. The limit **does not exist**: $x=3$ is a vertical asymptote with opposite behavior on the two sides.

**MATH265 exam question (Q3.1b) — a $\frac00$ that turns into $k/0$ after cancelling.** Evaluate $\displaystyle\lim_{x\to -2}\frac{3x^2-2x-16}{(x+2)^2}$.

1. Substitute: $\dfrac{0}{0}$, so factor (L2). The numerator factors as $(x+2)(3x-8)$.
2. Cancel one $(x+2)$: $\dfrac{3x-8}{x+2}$.
3. Re-diagnose: at $x=-2$ this is now $\dfrac{-14}{0}$, a genuine $k/0$, so the remaining $(x+2)$ cannot be cancelled and the one-sided check takes over.
4. Left: $x+2\to0^-$, so $\dfrac{-14}{0^-}\to+\infty$. Right: $x+2\to0^+$, so $\dfrac{-14}{0^+}\to-\infty$.
5. The limit **does not exist**, because the two sides disagree.

**MATH265 exam question (Q3.2e) — the $k/0$ disguised as a trig special limit.** Evaluate $\displaystyle\lim_{x\to-\pi/3}\frac{\tan(2x)}{3x+\pi}$.

1. It is tempting to reach for $\frac{\tan u}{u}\to1$, but check the numerator first: at $x=-\frac\pi3$, $2x=-\frac{2\pi}{3}$ and $\tan\left(-\frac{2\pi}{3}\right)=\sqrt3\ne0$.
2. So this is $\dfrac{\sqrt3}{0}$, not $\dfrac00$, and the special limit does not apply at all.
3. Left: $3x+\pi\to0^-$, giving $\dfrac{\sqrt3}{0^-}\to-\infty$. Right: $3x+\pi\to0^+$, giving $\dfrac{\sqrt3}{0^+}\to+\infty$.
4. The limit **does not exist**.

**MATH265 exam question (Q3.2f) — an even-power denominator forces the same sign from both sides.** Evaluate $\displaystyle\lim_{x\to 2}\frac{\cos(\pi x)}{(x-2)^2}$.

1. Numerator: $\cos(2\pi)=1$. Denominator: $(x-2)^2\to0^+$ from **both** sides, because a square is never negative.
2. So both one-sided limits are $\dfrac{1}{0^+}\to+\infty$, and they agree.
3. Unlike the previous three examples, this one is written $\displaystyle\lim_{x\to2}\frac{\cos(\pi x)}{(x-2)^2} = +\infty$: it does not exist as a finite number, but the sides agree well enough to name the shared infinite behavior.

**MATH265 exam question (Q3.3b) — a coterminal angle at a tangent asymptote.** Evaluate $\displaystyle\lim_{x\to 5\pi/2}\tan x$.

1. Reduce the angle: $\dfrac{5\pi}{2} = 2\pi+\dfrac{\pi}{2}$, coterminal with $\dfrac\pi2$, where $\cos x=0$.
2. Write $\tan x = \dfrac{\sin x}{\cos x}$, with $\sin\left(\dfrac{5\pi}{2}\right)=1$.
3. From the left, $\cos x\to0^+$, so $\tan x\to+\infty$. From the right, $\cos x\to0^-$, so $\tan x\to-\infty$.
4. The limit **does not exist**; $x=\dfrac{5\pi}{2}$ is a vertical asymptote of the tangent.

---

## L14. The logarithm trick for indeterminate powers

**Trigger.** The form is $1^{\infty}$, $0^0$, or $\infty^0$.

**Why it works.** $\ln$ turns an exponent into a product, converting the power form into $0\cdot\infty$, which L15 then turns into a quotient that L10 can finish.

**Method.** Set $L = \lim f(x)^{g(x)}$, compute $\ln L = \lim g(x)\ln f(x)$, then exponentiate: $L = e^{\ln L}$.
The final exponentiation is the step most often forgotten.

**Example ($0^0$).** Evaluate $\displaystyle\lim_{x\to 0^+} x^{x}$.

*Steps.*

1. Let $L$ be the limit and take logs: $\ln L = \lim_{x\to 0^+} x\ln x$.
2. That is $0\cdot(-\infty)$, so rewrite as a quotient: $\dfrac{\ln x}{1/x}$, now $\frac{-\infty}{\infty}$.
3. L'Hopital: $\dfrac{1/x}{-1/x^2} = -x$.
4. So $\ln L = 0$.
5. Exponentiate: $L = e^0 = 1$.

**Example ($1^{\infty}$).** Evaluate $\displaystyle\lim_{x\to\infty}\left(1+\frac{3}{x}\right)^{2x}$.

1. $\ln L = \lim 2x\ln\left(1+\frac3x\right)$.
2. Substitute $t=\frac1x\to0^+$: $\ln L = \lim_{t\to0^+}\dfrac{2\ln(1+3t)}{t}$.
3. This is $\frac00$; L'Hopital gives $\dfrac{6/(1+3t)}{1} \to 6$.
4. $L = e^{6}$.

**Shortcut for the $1^\infty$ family.** $\displaystyle\lim\left(1+\frac{a}{x}\right)^{bx} = e^{ab}$.

---

## L15. Rewriting a $0\cdot\infty$ product

**Trigger.** A product where one factor goes to $0$ and the other to $\pm\infty$.

**Method.** Move one factor into the denominator as its reciprocal, producing $\frac00$ or $\frac{\infty}{\infty}$.
Choose the direction that gives derivatives you actually want to compute.

**Example.** Evaluate $\displaystyle\lim_{x\to 0^+} x\ln x$.

*Steps.*

1. Form is $0\cdot(-\infty)$.
2. Two rewrites are available: $\frac{\ln x}{1/x}$ or $\frac{x}{1/\ln x}$.
3. Choose the first, because differentiating $1/\ln x$ is worse than differentiating $1/x$.
4. L'Hopital: $\dfrac{1/x}{-1/x^2} = -x \to 0$.
5. The limit is $0$.

**The general fact behind it.** Powers beat logarithms: $x^a \ln x \to 0$ as $x\to0^+$ for every $a>0$.

---

## L16. Bounded over unbounded

**Trigger.** A bounded numerator (a sine, a cosine, anything you can cap) over something going to infinity.

**Example.** Evaluate $\displaystyle\lim_{x\to\infty}\frac{\sin x}{x}$.

*Steps.*

1. L'Hopital is not available: $\sin x$ has no limit, so the form is not $\frac{\infty}{\infty}$.
2. Bound: $\left\lvert \frac{\sin x}{x}\right\rvert \le \frac{1}{x}$ for $x>0$.
3. $\frac1x \to 0$, so by squeeze the limit is $0$.

**Contrast.** $\displaystyle\lim_{x\to 0}\frac{\sin x}{x} = 1$ but $\displaystyle\lim_{x\to\infty}\frac{\sin x}{x} = 0$.
Same expression, different technique, because the *form* at the two points is different.

---

## L17. Epsilon-delta proof

**Trigger.** The question says "prove", "using the definition", or "show that".

**Definition.** $\lim_{x\to a} f(x) = L$ means: for every $\varepsilon>0$ there is a $\delta>0$ such that $0<\lvert x-a\rvert<\delta \implies \lvert f(x)-L\rvert<\varepsilon$.

**Example.** Prove $\displaystyle\lim_{x\to 3}(2x+1) = 7$.

*Steps.*

1. **Scratch work** (find $\delta$): $\lvert (2x+1)-7\rvert = \lvert 2x-6\rvert = 2\lvert x-3\rvert$.
2. Force this below $\varepsilon$: $2\lvert x-3\rvert < \varepsilon \iff \lvert x-3\rvert < \frac{\varepsilon}{2}$.
3. **Proof** (write it forwards): let $\varepsilon>0$ and choose $\delta = \frac{\varepsilon}{2}$.
4. If $0<\lvert x-3\rvert<\delta$ then $\lvert (2x+1)-7\rvert = 2\lvert x-3\rvert < 2\delta = \varepsilon$.
5. Therefore the limit is $7$. $\blacksquare$

**For nonlinear $f$.** Bound the extra factor first.
For $\lim_{x\to2}x^2 = 4$: $\lvert x^2-4\rvert = \lvert x-2\rvert\lvert x+2\rvert$, and restricting to $\delta\le1$ gives $\lvert x+2\rvert<5$, so $\delta = \min\left(1,\frac{\varepsilon}{5}\right)$ works.

---

## L18. Showing a limit does not exist

**Trigger.** You suspect there is no limit, or the expression oscillates.

**Method (single variable).** Exhibit two sequences $x_n\to a$ whose function values converge to different numbers.

**Example.** Show $\displaystyle\lim_{x\to 0}\sin\frac{1}{x}$ does not exist.

*Steps.*

1. Take $x_n = \frac{1}{n\pi}$, so $x_n\to0$ and $\sin\frac{1}{x_n} = \sin(n\pi) = 0$ for every $n$.
2. Take $y_n = \frac{1}{2n\pi + \pi/2}$, so $y_n\to0$ and $\sin\frac{1}{y_n} = 1$ for every $n$.
3. Two sequences approaching $0$ give limits $0$ and $1$.
4. A limit, if it existed, would be unique, so no limit exists.

**Method (two variables).** Approach along different paths.

**Example.** Show $\displaystyle\lim_{(x,y)\to(0,0)}\frac{xy}{x^2+y^2}$ does not exist.

1. Along $y=0$: the value is $0$ for every $x\ne0$.
2. Along $y=x$: the value is $\frac{x^2}{2x^2} = \frac12$.
3. Different paths give different values, so the limit does not exist.

**Warning about paths.** Agreement along every straight line does **not** prove existence.
For $\frac{x^2y}{x^4+y^2}$, every line through the origin gives $0$ but the parabola $y=x^2$ gives $\frac12$.
To *prove* a multivariable limit exists, convert to polar coordinates and squeeze, or bound $\lvert f-L\rvert$ by a function of $r$ alone.

**Example (proving existence in polar form).** $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^3}{x^2+y^2}$.

1. Substitute $x=r\cos\theta$, $y=r\sin\theta$; then $x^2+y^2 = r^2$.
2. The expression becomes $\dfrac{r^3\cos^3\theta}{r^2} = r\cos^3\theta$.
3. Bound: $\lvert r\cos^3\theta\rvert \le r$, and $r\to 0$ independently of $\theta$.
4. The limit is $0$.

---

## L19. Recognizing a Riemann sum

**Trigger.** $\lim_{n\to\infty}$ of a sum whose terms contain $\frac{i}{n}$ and an overall $\frac1n$.

**The template.** $\displaystyle\lim_{n\to\infty}\sum_{i=1}^{n}f\!\left(\frac{i}{n}\right)\frac{1}{n} = \int_0^1 f(x)\,dx$.

**Example.** Evaluate $\displaystyle\lim_{n\to\infty}\sum_{i=1}^{n}\frac{n}{n^2+i^2}$.

*Steps.*

1. Factor $n^2$ out of the denominator: $\dfrac{n}{n^2\left(1+\frac{i^2}{n^2}\right)} = \dfrac{1}{n}\cdot\dfrac{1}{1+\left(\frac{i}{n}\right)^2}$.
2. Read off $f(x) = \frac{1}{1+x^2}$ with sample points $x_i = \frac{i}{n}$ and width $\frac1n$ on $[0,1]$.
3. The limit is $\displaystyle\int_0^1\frac{dx}{1+x^2} = \arctan(1)-\arctan(0)$.
4. The value is $\dfrac{\pi}{4}$.

**Second example.** $\displaystyle\lim_{n\to\infty}\frac{1}{n}\sum_{i=1}^{n}\sqrt{\frac{i}{n}} = \int_0^1\sqrt{x}\,dx = \frac{2}{3}$.

---

## L20. Sequence-specific tools

Sequences allow techniques that functions of a real variable do not.

**(a) Monotone convergence.** A bounded monotone sequence converges.

**Example.** $a_1 = \sqrt{2}$, $a_{n+1} = \sqrt{2+a_n}$.

1. Show it is bounded above by $2$ by induction: if $a_n<2$ then $a_{n+1}=\sqrt{2+a_n}<\sqrt4=2$.
2. Show it is increasing: $a_{n+1}>a_n \iff 2+a_n > a_n^2 \iff (a_n-2)(a_n+1)<0$, true for $0<a_n<2$.
3. Bounded and increasing, so the limit $L$ exists.
4. Take limits in the recursion: $L = \sqrt{2+L}$, so $L^2-L-2 = 0$, giving $L=2$ or $L=-1$.
5. The sequence is positive, so $L=2$.

Step 3 is the load-bearing one.
Solving the fixed-point equation first proves nothing, because a divergent sequence can have a fixed point too.

**(b) Growth hierarchy.** As $n\to\infty$, each term is dominated by the next:
$$\ln n \ll n^{a} \ll b^{n} \ll n! \ll n^{n} \quad (a>0,\ b>1).$$
Any ratio across this chain has limit $0$ downward and $\infty$ upward.

**(c) Stolz-Cesaro** (the discrete L'Hopital).
If $b_n$ is strictly increasing and unbounded, then $\displaystyle\lim\frac{a_n}{b_n} = \lim\frac{a_{n+1}-a_n}{b_{n+1}-b_n}$ when the right side exists.

**Example.** $\displaystyle\lim_{n\to\infty}\frac{1+\frac12+\cdots+\frac1n}{\ln n}$.

1. Take $a_n = H_n$ and $b_n = \ln n$, with $b_n$ increasing and unbounded.
2. Differences: $a_{n+1}-a_n = \frac{1}{n+1}$ and $b_{n+1}-b_n = \ln\left(1+\frac1n\right)$.
3. The ratio is $\dfrac{1/(n+1)}{\ln(1+1/n)}$, and $\ln(1+\frac1n)\approx\frac1n$ for large $n$.
4. The ratio $\to 1$, so the limit is $1$.

**(d) The ratio test for a sequence limit.** If $\left\lvert\frac{a_{n+1}}{a_n}\right\rvert \to r < 1$ then $a_n \to 0$.
This settles things like $\frac{3^n}{n!}\to0$ in one line.

---

# Part 2 - Techniques for Evaluating Derivatives

Differentiation is mechanical in a way integration is not: every elementary function has an elementary derivative, and the rules below cover all of them.
The skill is *decomposition*, meaning seeing which rule sits at the outermost layer of the expression.

**The decomposition question.** Before writing anything, ask what the top-level operation is:

| Outermost structure | Rule |
| :--- | :--- |
| A sum or difference | D2, then recurse on each piece |
| A product of two factors | D3, then recurse |
| A quotient | D4 (or rewrite as a product with a negative power) |
| A function evaluated at an expression | D5, then recurse |
| A variable in the exponent | D9 |
| $y$ appearing on both sides | D8 |

---

## D1. The definition (first principles)

**Trigger.** The question says "using the definition", or the function is not built from table entries.

**Definition.**
$$f'(x) = \lim_{h\to 0}\frac{f(x+h)-f(x)}{h}.$$

**Example.** Differentiate $f(x) = \sqrt{x}$ from first principles.

*Steps.*

1. Write the difference quotient: $\dfrac{\sqrt{x+h}-\sqrt{x}}{h}$.
2. Substituting $h=0$ gives $\frac00$, and there is a root, so use L3 and multiply by the conjugate $\sqrt{x+h}+\sqrt{x}$.
3. Numerator becomes $(x+h)-x = h$.
4. The quotient is $\dfrac{h}{h\left(\sqrt{x+h}+\sqrt{x}\right)} = \dfrac{1}{\sqrt{x+h}+\sqrt{x}}$.
5. Let $h\to0$: $\dfrac{1}{2\sqrt{x}}$.

**Example ($1/x$).** $\dfrac{\frac{1}{x+h}-\frac1x}{h} = \dfrac{x-(x+h)}{hx(x+h)} = \dfrac{-1}{x(x+h)} \to -\dfrac{1}{x^2}$.

**The alternate form**, useful for a derivative at one specific point:
$$f'(a) = \lim_{x\to a}\frac{f(x)-f(a)}{x-a}.$$

**Differentiability check.** A function is differentiable at $a$ only if the left and right difference quotients agree.
$f(x)=\lvert x\rvert$ is continuous at $0$ but its quotients give $+1$ and $-1$ (this is L13 in disguise), so it is not differentiable there.

**MATH265 exam question (Q7.1) — a trig derivative from the definition.** Use the limit definition to find $\dfrac{d}{dx}\cot x$.

1. Write the definition: $\dfrac{d}{dx}\cot x = \displaystyle\lim_{h\to0}\frac{\cot(x+h)-\cot x}{h}$.
2. Convert to sine and cosine and combine over a common denominator: $\dfrac{\cos(x+h)\sin x - \cos x\sin(x+h)}{h\,\sin(x+h)\sin x}$.
3. Recognize the numerator as the sine difference identity $\sin(A-B)$ with $A=x$, $B=x+h$: it collapses to $\sin(-h) = -\sin h$.
4. Split off the special limit: $\displaystyle\lim_{h\to0}\left(-\frac{\sin h}{h}\right)\cdot\frac{1}{\sin(x+h)\sin x} = (-1)\cdot\frac{1}{\sin^2x}$.
5. Result: $\dfrac{d}{dx}\cot x = -\dfrac{1}{\sin^2x} = -\csc^2x$, matching the D6 table entry.

**The sign trap.** Writing $\sin\big(x-(x+h)\big)=\sin(h)$ loses the minus sign (sine is odd) and turns the answer into $+\csc^2x$.

---

## D2. Power, constant multiple, and sum rules

$$\frac{d}{dx}x^{n} = nx^{n-1}, \qquad (cf)' = cf', \qquad (f\pm g)' = f'\pm g'.$$

The power rule holds for every real $n$, not just integers, which is what makes rewriting worthwhile.

**Example.** Differentiate $\displaystyle f(x) = 3x^4 - \frac{2}{x^3} + 5\sqrt[3]{x} - 7$.

*Steps.*

1. Rewrite every term as a power: $3x^4 - 2x^{-3} + 5x^{1/3} - 7$.
2. Apply the power rule term by term: $12x^3 + 6x^{-4} + \frac53 x^{-2/3}$.
3. The constant differentiates to $0$.
4. Restore radical form if the answer must match a textbook: $12x^3 + \dfrac{6}{x^4} + \dfrac{5}{3\sqrt[3]{x^2}}$.

**Step 1 is the whole technique.** Most "hard" derivatives in this family are easy ones written in a disguise that the power rule cannot see.

**MATH265 exam question (Q8.1a).** Differentiate $y = 4x^5+3x^4-6x^3+6$.

1. Multiply each coefficient by its exponent and drop the exponent by one: $20x^4+12x^3-18x^2$.
2. The constant $6$ differentiates to $0$.
3. Result: $y' = 20x^4+12x^3-18x^2$.

---

## D3. The product rule

$$(fg)' = f'g + fg'.$$

**Example.** Differentiate $y = x^2 e^{x}$.

*Steps.*

1. Identify $f = x^2$ and $g = e^x$.
2. Compute $f' = 2x$ and $g' = e^x$.
3. Assemble: $2x\,e^x + x^2 e^x$.
4. Factor for a usable form: $e^x\left(x^2+2x\right)$.

**Three factors.** $(fgh)' = f'gh + fg'h + fgh'$: differentiate each factor in turn, leaving the others alone.

**Example.** $\dfrac{d}{dx}\left[x\sin x\cos x\right] = \sin x\cos x + x\cos^2 x - x\sin^2 x$.

**MATH265 exam question (Q8.3a) — a product whose second factor is three chain-rule layers deep.** Differentiate $y = \sin x\cdot\cos\left(\sin x^2\right)$.

1. The outer structure is a product, so the product rule runs first, leaving the hard part (differentiating the second factor) for after.
2. Differentiate $\cos\left(\sin x^2\right)$ through its three layers — cosine, then sine, then $x^2$: $-\sin\left(\sin x^2\right)\cdot\cos\left(x^2\right)\cdot2x$.
3. Assemble the product rule: $y' = \cos x\cos\left(\sin x^2\right) - \sin x\,\sin\left(\sin x^2\right)\cos\left(x^2\right)(2x)$.

**The notation trap.** $\sin x^2$ means $\sin\left(x^2\right)$, not $(\sin x)^2$; the inner derivative is $\cos\left(x^2\right)\cdot2x$, not $2\sin x\cos x$.

---

## D4. The quotient rule

$$\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^{2}}.$$

The order in the numerator matters, unlike the product rule.
The mnemonic "low d-high minus high d-low, over low squared" fixes it.

**Example.** Differentiate $\displaystyle y = \frac{2x+1}{x^2+3}$.

*Steps.*

1. $f = 2x+1$, $f' = 2$; $g = x^2+3$, $g' = 2x$.
2. Numerator: $2(x^2+3) - (2x+1)(2x) = 2x^2+6-4x^2-2x$.
3. Simplify: $-2x^2-2x+6$.
4. Result: $\dfrac{-2x^2-2x+6}{\left(x^2+3\right)^2}$.

**When not to use it.** If the denominator is a single power, rewrite instead.
$\frac{x^3+1}{x} = x^2 + x^{-1}$ differentiates to $2x - x^{-2}$ with no rule at all.

**MATH265 exam question (Q8.1b) — cancel a common factor after the quotient rule, before expanding.** Differentiate $\displaystyle y = \frac{2x-16}{(x+3)^2}$.

1. $f=2x-16$, $f'=2$; $g=(x+3)^2$, $g'=2(x+3)$ by the chain rule.
2. Quotient rule: $y' = \dfrac{2(x+3)^2 - (2x-16)\cdot2(x+3)}{(x+3)^4}$.
3. Every term in the numerator carries a factor of $(x+3)$: cancel one against the $(x+3)^4$ in the denominator **before** expanding, dropping it to $(x+3)^3$.
4. $y' = \dfrac{2(x+3)-2(2x-16)}{(x+3)^3} = \dfrac{38-2x}{(x+3)^3}$.

Doing the cancellation in step 3 first avoids expanding a $(x+3)^2$ that was only going to be thrown away.

**MATH265 exam question (Q8.4a) — naming the rules as you stack them.** Differentiate $\displaystyle\frac{d}{dx}\frac{\tan(2x)}{\sqrt{x}}$, stating which rules apply.

1. Quotient rule on the outside; chain rule on $\tan(2x)$; power rule on $\sqrt{x}=x^{1/2}$.
2. $f=\tan(2x)$, $f'=2\sec^2(2x)$; $g=x^{1/2}$, $g'=\dfrac{1}{2\sqrt{x}}$.
3. Assemble: $\dfrac{2\sec^2(2x)\sqrt{x} - \tan(2x)\cdot\frac{1}{2\sqrt{x}}}{x}$, using $g^2=x$ in the denominator.

**MATH265 exam question (Q8.2c) — a quotient whose two pieces each need their own product/chain-rule work first.** Differentiate $\displaystyle\frac{d}{dx}\frac{x^2-\cos(3x)}{x\sin(2x)}$.

1. Name the pieces: $f = x^2-\cos(3x)$, $g = x\sin(2x)$.
2. Differentiate each on its own before assembling: $f' = 2x+3\sin(3x)$ (the derivative of $-\cos(3x)$ is $+3\sin(3x)$); $g' = \sin(2x)+2x\cos(2x)$ by the product rule.
3. Assemble the quotient rule: $\dfrac{\big(2x+3\sin(3x)\big)\big(x\sin(2x)\big) - \big(x^2-\cos(3x)\big)\big(\sin(2x)+2x\cos(2x)\big)}{\big(x\sin(2x)\big)^2}$. No simplification is required.

**MATH265 exam question (Q8.2d) — a quotient rule evaluated at a point from function values alone.** Find $\left.\dfrac{d}{dx}\dfrac{f(x)}{g(x)}\right|_{x=1}$ where $f(1)=3$, $g(1)=6$, $f'(x)=\sqrt{x}$, $g'(x)=3\sin\left(\dfrac{\pi x}{3}\right)$.

1. Write the quotient rule at the point: $\left.\left(\dfrac{f}{g}\right)'\right|_{x=1} = \dfrac{f'(1)g(1)-f(1)g'(1)}{\big(g(1)\big)^2}$.
2. Evaluate the two derivatives at $x=1$: $f'(1)=\sqrt1=1$; $g'(1)=3\sin\left(\dfrac\pi3\right)=3\cdot\dfrac{\sqrt3}{2}=\dfrac{3\sqrt3}{2}$ — read in radians, not degrees.
3. Substitute all four numbers: $\dfrac{(1)(6)-(3)\left(\frac{3\sqrt3}{2}\right)}{36} = \dfrac{6-\frac{9\sqrt3}{2}}{36} = \dfrac{4-3\sqrt3}{24} \approx -0.04984$.

**MATH265 exam question (Q8.3d) — a root sitting inside a quotient rule.** Differentiate $\displaystyle y = \frac{\sqrt{x^2-1}}{x^2-2x-8}$.

1. Let $f=\sqrt{x^2-1}$, $g=x^2-2x-8$.
2. Differentiate $f$ with the chain rule: $f' = \dfrac{2x}{2\sqrt{x^2-1}} = \dfrac{x}{\sqrt{x^2-1}}$; and $g'=2x-2$.
3. Assemble the quotient rule directly, without clearing the inner root: $y' = \dfrac{\frac{x}{\sqrt{x^2-1}}\left(x^2-2x-8\right) - \sqrt{x^2-1}\,(2x-2)}{\left(x^2-2x-8\right)^2}$.

---

## D5. The chain rule

$$\frac{d}{dx}f\!\left(g(x)\right) = f'\!\left(g(x)\right)\cdot g'(x).$$

**The procedure.** Differentiate the outer function leaving the inside untouched, then multiply by the derivative of the inside.
Repeat for every layer.

**Example (two layers).** Differentiate $y = \sin\left(3x^2+1\right)$.

*Steps.*

1. Outer is $\sin(\square)$, inner is $\square = 3x^2+1$.
2. Derivative of the outer, inside unchanged: $\cos\left(3x^2+1\right)$.
3. Derivative of the inner: $6x$.
4. Multiply: $6x\cos\left(3x^2+1\right)$.

**Example (three layers).** Differentiate $y = \sqrt{1+\tan 2x}$.

1. Layers, outermost first: square root, then $1+\tan(\cdot)$, then $2x$.
2. Square root layer: $\dfrac{1}{2\sqrt{1+\tan 2x}}$.
3. Tangent layer: $\sec^2 2x$.
4. Innermost layer: $2$.
5. Multiply all three: $\dfrac{2\sec^{2}2x}{2\sqrt{1+\tan 2x}} = \dfrac{\sec^{2}2x}{\sqrt{1+\tan 2x}}$.

**The most common slip.** Forgetting the innermost factor.
$\frac{d}{dx}\sin(2x)$ is $2\cos 2x$, not $\cos 2x$.

**MATH265 exam question (Q8.3c) — a root nested inside a root.** Differentiate $y = \sqrt{1+\sqrt{1+x}}$.

1. Layers, outermost first: a square root, then $1+\sqrt{\cdot}$, then $1+x$.
2. Peel the outer root: $y' = \dfrac{1}{2\sqrt{1+\sqrt{1+x}}}\cdot v'$ where $v=1+\sqrt{1+x}$.
3. Differentiate the inner root: $v' = \dfrac{1}{2\sqrt{1+x}}$ (the constant $1$ contributes nothing).
4. Multiply the two layers: $y' = \dfrac{1}{4\sqrt{1+x}\,\sqrt{1+\sqrt{1+x}}}$.

**MATH265 exam question (Q8.4b) — chain rule evaluated at a point using exact trig values.** Find $\left.\dfrac{d}{dx}\cos^3\left(x^2\right)\right|_{x=\sqrt\pi/2}$.

1. Read the notation first: $\cos^3\left(x^2\right)$ means $\left[\cos\left(x^2\right)\right]^3$, three layers (cube, cosine, $x^2$).
2. Differentiate: $3\left[\cos\left(x^2\right)\right]^2\cdot\left(-\sin\left(x^2\right)\right)\cdot2x = -6x\cos^2\left(x^2\right)\sin\left(x^2\right)$.
3. Find the inner value *before* substituting the trig functions, which is what makes the arithmetic clean: $x^2 = \left(\frac{\sqrt\pi}{2}\right)^2 = \frac\pi4$.
4. Use the exact values at $\frac\pi4$: $\cos^2\frac\pi4=\frac12$, $\sin\frac\pi4=\frac{\sqrt2}{2}$.
5. Substitute: $-6\cdot\dfrac{\sqrt\pi}{2}\cdot\dfrac12\cdot\dfrac{\sqrt2}{2} = -\dfrac{3\sqrt{2\pi}}{4} \approx -1.87997$.

**MATH265 exam question (Q8.1c) — plain two-layer chain rule.** Differentiate $y = \sin\left(2x^2-x+1\right)$.

1. Outer is $\sin(\cdot)$, whose derivative is $\cos(\cdot)$; inner is $2x^2-x+1$, whose derivative is $4x-1$.
2. Multiply: $y' = \cos\left(2x^2-x+1\right)\cdot(4x-1)$.

**MATH265 exam question (Q8.1d) — the power rule wrapping a polynomial.** Differentiate $y = \left(-4x^3-x^2+3x+7\right)^4$.

1. Outer is $(\cdot)^4$, giving $4(\cdot)^3$; inner derivative is $-12x^2-2x+3$.
2. Multiply: $y' = 4\left(-4x^3-x^2+3x+7\right)^3\left(-12x^2-2x+3\right)$.

**MATH265 exam question (Q8.3b) — a fractional outer power wrapping a quotient rule.** Differentiate $y = \left(\dfrac{1+x^3}{1-x^2}\right)^{1/3}$.

1. Let $u = \dfrac{1+x^3}{1-x^2}$, so $y=u^{1/3}$ and $y' = \dfrac13 u^{-2/3}u'$ by the chain rule.
2. Differentiate $u$ with the quotient rule: $u' = \dfrac{3x^2\left(1-x^2\right) - \left(1+x^3\right)(-2x)}{\left(1-x^2\right)^2}$, which expands to $\dfrac{-x^4+3x^2+2x}{\left(1-x^2\right)^2}$.
3. Assemble: $y' = \dfrac13\left(\dfrac{1+x^3}{1-x^2}\right)^{-2/3}\cdot\dfrac{-x^4+3x^2+2x}{\left(1-x^2\right)^2}$.

**MATH265 exam question (Q8.3e) — a square wrapping a secant wrapping a quotient.** Differentiate $y = \sec^2\left(\dfrac{x+1}{x-2}\right)$.

1. Read the layers: $y=(\sec u)^2$ with $u=\dfrac{x+1}{x-2}$ — a square, then a secant, then a quotient.
2. Differentiate the inner quotient: $u' = \dfrac{(1)(x-2)-(x+1)(1)}{(x-2)^2} = \dfrac{-3}{(x-2)^2}$.
3. Outer layers: $\dfrac{d}{dx}(\sec u)^2 = 2\sec u\cdot\sec u\tan u\cdot u' = 2\sec^2u\tan u\cdot u'$.
4. Substitute: $y' = \dfrac{-6\sec^2\left(\frac{x+1}{x-2}\right)\tan\left(\frac{x+1}{x-2}\right)}{(x-2)^2}$.

---

## D6. The named-function tables

**Trigonometric.**

| $f$ | $f'$ | $f$ | $f'$ |
| :--- | :--- | :--- | :--- |
| $\sin x$ | $\cos x$ | $\csc x$ | $-\csc x\cot x$ |
| $\cos x$ | $-\sin x$ | $\sec x$ | $\sec x\tan x$ |
| $\tan x$ | $\sec^2 x$ | $\cot x$ | $-\csc^2 x$ |

Every co-function derivative carries a minus sign, which is the only thing that needs memorizing once you know the first column.

**Exponential and logarithmic.**

| $f$ | $f'$ |
| :--- | :--- |
| $e^{x}$ | $e^{x}$ |
| $a^{x}$ | $a^{x}\ln a$ |
| $\ln x$ | $\dfrac{1}{x}$ |
| $\log_a x$ | $\dfrac{1}{x\ln a}$ |
| $\ln\lvert u\rvert$ | $\dfrac{u'}{u}$ |

**Example.** Differentiate $y = 5^{x^2}$.

1. This is $a^{u}$ with $a=5$ and $u=x^2$.
2. Table plus chain rule: $5^{x^2}\ln 5 \cdot 2x$.
3. Result: $2x\ln 5 \cdot 5^{x^2}$.

**Example.** $\dfrac{d}{dx}\ln\left(x^2+1\right) = \dfrac{2x}{x^2+1}$, which is the $\frac{u'}{u}$ row.

**MATH265 exam question (Q8.2b) — the secant row plus the chain rule.** Differentiate $\sec\left(x^2-3x\right)$.

1. Table entry: $\dfrac{d}{dx}\sec u = \sec u\tan u$, with $u=x^2-3x$ and $u'=2x-3$.
2. Result: $\sec\left(x^2-3x\right)\tan\left(x^2-3x\right)(2x-3)$.

---

## D7. Inverse trigonometric and hyperbolic derivatives

| $f$ | $f'$ | $f$ | $f'$ |
| :--- | :--- | :--- | :--- |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1-x^2}}$ | $\sinh x$ | $\cosh x$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1-x^2}}$ | $\cosh x$ | $\sinh x$ |
| $\arctan x$ | $\dfrac{1}{1+x^2}$ | $\tanh x$ | $\operatorname{sech}^2 x$ |
| $\operatorname{arcsec} x$ | $\dfrac{1}{\lvert x\rvert\sqrt{x^2-1}}$ | $\operatorname{arcsinh} x$ | $\dfrac{1}{\sqrt{x^2+1}}$ |

Note $\frac{d}{dx}\cosh x = +\sinh x$: unlike the circular case, no minus sign appears.

**Example.** Differentiate $y = \arctan\left(x^2\right)$.

1. Outer derivative with the inside intact: $\dfrac{1}{1+\left(x^2\right)^2} = \dfrac{1}{1+x^4}$.
2. Inner derivative: $2x$.
3. Result: $\dfrac{2x}{1+x^4}$.

**Deriving one, in case the table is unavailable.** For $y=\arcsin x$: write $\sin y = x$, differentiate implicitly to get $\cos y\, y' = 1$, so $y' = \frac{1}{\cos y} = \frac{1}{\sqrt{1-\sin^2 y}} = \frac{1}{\sqrt{1-x^2}}$.

---

## D8. Implicit differentiation

**Trigger.** $y$ is defined by an equation you cannot (or do not want to) solve for $y$.

**Method.** Differentiate both sides with respect to $x$, treating $y$ as a function of $x$ so every $y$ term picks up a $\frac{dy}{dx}$ by the chain rule, then solve algebraically for $\frac{dy}{dx}$.

**Example.** Find $\dfrac{dy}{dx}$ for $x^2+y^2 = 25$.

*Steps.*

1. Differentiate both sides: $2x + 2y\dfrac{dy}{dx} = 0$.
2. The $2y\frac{dy}{dx}$ comes from the chain rule, because $y^2$ is a composite of squaring with $y(x)$.
3. Solve: $\dfrac{dy}{dx} = -\dfrac{x}{y}$.

**Example (folium of Descartes).** Find $\dfrac{dy}{dx}$ for $x^3+y^3 = 6xy$.

1. Differentiate: $3x^2 + 3y^2 y' = 6y + 6xy'$ (the right side needs the product rule).
2. Collect the $y'$ terms: $3y^2y' - 6xy' = 6y - 3x^2$.
3. Factor: $y'\left(3y^2-6x\right) = 6y-3x^2$.
4. Solve: $y' = \dfrac{6y-3x^2}{3y^2-6x} = \dfrac{2y-x^2}{y^2-2x}$.

**Second derivative implicitly.** Differentiate $y'$ again, then substitute the expression for $y'$ back in.
For the circle: $y'' = \frac{d}{dx}\left(-\frac{x}{y}\right) = -\frac{y - xy'}{y^2} = -\frac{y + \frac{x^2}{y}}{y^2} = -\frac{x^2+y^2}{y^3} = -\frac{25}{y^3}$.

**MATH265 exam question (Q10.1) — every term needs the product or chain rule.** Find $y'$ for $x^3y+xy^2=4xy+7$.

1. Differentiate term by term: $\dfrac{d}{dx}\left(x^3y\right)=3x^2y+x^3y'$ (product rule); $\dfrac{d}{dx}\left(xy^2\right)=y^2+2xyy'$ (product then chain); $\dfrac{d}{dx}(4xy)=4y+4xy'$ (product rule); the constant $7$ vanishes.
2. Collect: $3x^2y+x^3y'+y^2+2xyy' = 4y+4xy'$.
3. Move every $y'$ term to one side: $y'\left(x^3+2xy-4x\right) = 4y-3x^2y-y^2$.
4. Solve: $y' = \dfrac{4y-3x^2y-y^2}{x^3+2xy-4x}$.

**The trap.** Differentiating $xy^2$ as just $2xyy'$ and dropping the $y^2$ term that the product rule also produces.

**MATH265 exam question (Q10.2) — substitute the point immediately, not at the end.** Find the tangent line to $y^3+yx^2+x^2=3y^2$ at $(1,1)$.

1. Confirm the point lies on the curve first: both sides equal $3$ at $(1,1)$.
2. Differentiate implicitly: $3y^2y'+\left(y'x^2+2xy\right)+2x = 6yy'$.
3. Because only one point is needed, substitute $x=1,y=1$ **now** rather than solving for $y'$ symbolically first: $3y'+y'+2+2=6y'$.
4. Solve the now-numerical equation: $4y'+4=6y' \implies y'=2$.
5. Point-slope form: $y-1=2(x-1)$, so the tangent line is $y=2x-1$.

Substituting early (step 3) is faster and loses fewer terms than carrying the full symbolic $y'$ formula to the end.

---

## D9. Logarithmic differentiation

**Trigger.** The variable is in the exponent *and* in the base, or the expression is a long product/quotient/power stack.

**Method.** Take $\ln$ of both sides, use log laws to break the expression apart, differentiate implicitly, then multiply by $y$.

**Example (variable in both places).** Differentiate $y = x^{\sin x}$.

*Steps.*

1. Neither the power rule (exponent is not constant) nor the $a^x$ rule (base is not constant) applies.
2. Take logs: $\ln y = \sin x\ln x$.
3. Differentiate both sides, product rule on the right: $\dfrac{y'}{y} = \cos x\ln x + \dfrac{\sin x}{x}$.
4. Multiply by $y$ and restore it: $y' = x^{\sin x}\left(\cos x\ln x + \dfrac{\sin x}{x}\right)$.

**Example (product/quotient stack).** Differentiate $\displaystyle y = \frac{x^{3}\sqrt{x^2+1}}{(3x+2)^{5}}$.

1. Take logs and expand: $\ln y = 3\ln x + \frac12\ln\left(x^2+1\right) - 5\ln(3x+2)$.
2. Differentiate: $\dfrac{y'}{y} = \dfrac{3}{x} + \dfrac{x}{x^2+1} - \dfrac{15}{3x+2}$.
3. Multiply back: $y' = \dfrac{x^{3}\sqrt{x^2+1}}{(3x+2)^{5}}\left(\dfrac{3}{x} + \dfrac{x}{x^2+1} - \dfrac{15}{3x+2}\right)$.

The quotient and product rules would give the same answer after considerably more algebra.

---

## D10. The inverse function derivative

**Trigger.** You need $(f^{-1})'$ at a point but inverting $f$ is hard or impossible in closed form.

**Formula.** If $f(a) = b$ then
$$\left(f^{-1}\right)'(b) = \frac{1}{f'(a)}.$$

**Example.** For $f(x) = x^3+2x+1$, find $\left(f^{-1}\right)'(4)$.

*Steps.*

1. Find the $a$ with $f(a) = 4$: try small integers, and $f(1) = 1+2+1 = 4$, so $a=1$.
2. Differentiate $f$: $f'(x) = 3x^2+2$.
3. Evaluate: $f'(1) = 5$.
4. Reciprocate: $\left(f^{-1}\right)'(4) = \dfrac{1}{5}$.

Step 1 is solved by inspection or by a solver, never by inverting the cubic.

---

## D11. Parametric and polar derivatives

**Parametric.** For $x = x(t)$, $y = y(t)$:
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt}, \qquad \frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{dx/dt}.$$

The second-derivative formula is *not* $\frac{y''(t)}{x''(t)}$, which is the standard error here.

**Example.** For $x = t^2$, $y = t^3-3t$, find both derivatives at $t=2$.

*Steps.*

1. $\dfrac{dx}{dt} = 2t$ and $\dfrac{dy}{dt} = 3t^2-3$.
2. $\dfrac{dy}{dx} = \dfrac{3t^2-3}{2t}$, which at $t=2$ is $\dfrac{9}{4}$.
3. Differentiate that with respect to $t$: write it as $\frac32 t - \frac32 t^{-1}$, so the $t$-derivative is $\frac32 + \frac32 t^{-2}$.
4. Divide by $\frac{dx}{dt} = 2t$: $\dfrac{d^2y}{dx^2} = \dfrac{\frac32+\frac{3}{2t^2}}{2t}$.
5. At $t=2$: $\dfrac{\frac32+\frac38}{4} = \dfrac{15/8}{4} = \dfrac{15}{32}$.

**Polar.** With $r = r(\theta)$, use $x = r\cos\theta$, $y = r\sin\theta$ as a parametrization in $\theta$:
$$\frac{dy}{dx} = \frac{r'\sin\theta + r\cos\theta}{r'\cos\theta - r\sin\theta}.$$

**Example.** For $r = 1+\cos\theta$ at $\theta = \frac{\pi}{2}$: $r = 1$, $r' = -\sin\theta = -1$, so $\frac{dy}{dx} = \frac{(-1)(1)+(1)(0)}{(-1)(0)-(1)(1)} = \frac{-1}{-1} = 1$.

---

## D12. Higher-order derivatives and the Leibniz rule

**Trigger.** An $n$th derivative, a pattern, or a Taylor coefficient.

**Method for a pattern.** Compute the first three or four derivatives, write them in a form that exposes the structure, then state and check the general term.

**Example.** Find the $n$th derivative of $f(x) = xe^{x}$.

*Steps.*

1. $f' = e^x + xe^x = (x+1)e^x$.
2. $f'' = e^x + (x+1)e^x = (x+2)e^x$.
3. $f''' = (x+3)e^x$.
4. Conjecture $f^{(n)} = (x+n)e^{x}$.
5. Confirm by induction: differentiating $(x+n)e^x$ gives $e^x + (x+n)e^x = (x+n+1)e^x$, which is the formula at $n+1$.

**Leibniz rule** (the product rule iterated):
$$(fg)^{(n)} = \sum_{k=0}^{n}\binom{n}{k}f^{(k)}g^{(n-k)}.$$

It is most useful when one factor is a polynomial, because that factor's derivatives terminate.

**Example.** Find the $10$th derivative of $x^2\sin x$.

1. Take $f = x^2$: only $k=0,1,2$ contribute, since $f'''=0$.
2. Terms: $\binom{10}{0}x^2 g^{(10)} + \binom{10}{1}(2x)g^{(9)} + \binom{10}{2}(2)g^{(8)}$, with $g=\sin x$.
3. Cyclic derivatives of $\sin$: $g^{(8)} = \sin x$, $g^{(9)} = \cos x$, $g^{(10)} = -\sin x$.
4. Result: $-x^2\sin x + 20x\cos x + 90\sin x$.

**MATH265 exam question (Q8.2a) — a second derivative via the chain rule twice.** Find $\dfrac{d^2}{dx^2}\cot(2x)$.

1. First derivative: $\dfrac{d}{dx}\cot u=-\csc^2u$ with $u=2x$, so $\dfrac{d}{dx}\cot(2x) = -2\csc^2(2x)$.
2. Differentiate again: write $\csc^2(2x)=\left[\csc(2x)\right]^2$ and chain twice: $\dfrac{d}{dx}\csc(2x)=-2\csc(2x)\cot(2x)$, so $\dfrac{d}{dx}\csc^2(2x)=2\csc(2x)\cdot\left(-2\csc(2x)\cot(2x)\right)=-4\csc^2(2x)\cot(2x)$.
3. Apply the leading $-2$ from step 1: $-2\cdot\left(-4\csc^2(2x)\cot(2x)\right)=8\csc^2(2x)\cot(2x)$.
4. Result: $\dfrac{d^2}{dx^2}\cot(2x)=8\csc^2(2x)\cot(2x)$, positive despite the two minus signs along the way.

---

## D13. Related rates

**Trigger.** Two or more quantities changing in time, with one rate given and another asked for.

**The procedure that prevents the usual mistakes.**

1. Draw and label; name every varying quantity as a function of $t$.
2. Write the relation between the quantities, valid for **all** $t$.
3. Differentiate the relation with respect to $t$ (implicitly).
4. **Only now** substitute the instantaneous values.
5. Solve for the wanted rate and attach units.

**Example.** A $10\,\text{ft}$ ladder leans on a wall.
The base slides out at $2\,\text{ft/s}$.
How fast is the top falling when the base is $6\,\text{ft}$ from the wall?

*Steps.*

1. Let $x$ be the base distance and $y$ the height; $\frac{dx}{dt} = 2$, and we want $\frac{dy}{dt}$.
2. Relation, true at every instant: $x^2+y^2 = 100$.
3. Differentiate in $t$: $2x\dfrac{dx}{dt} + 2y\dfrac{dy}{dt} = 0$.
4. At the instant of interest $x=6$, so $y = \sqrt{100-36} = 8$.
5. Substitute: $2(6)(2) + 2(8)\dfrac{dy}{dt} = 0$, so $24 + 16\dfrac{dy}{dt} = 0$.
6. Solve: $\dfrac{dy}{dt} = -\dfrac{3}{2}\,\text{ft/s}$; the negative sign says the top is descending.

**Why step 4 comes after step 3.** Substituting $x=6$ before differentiating makes it a constant, its derivative becomes $0$, and the answer collapses to nonsense.

**MATH265 exam question (Q11.1) — eliminate the second variable before differentiating.** Gravel forms a cone whose base diameter always equals its height; $\dfrac{dV}{dt}=0.5\ \text{m}^3/\text{min}$. Find $\dfrac{dh}{dt}$ when $h=4$ m.

1. Geometry: $V=\dfrac13\pi r^2h$, with the constraint "diameter equals height", i.e. $2r=h$, so $r=\dfrac h2$.
2. Use the constraint to eliminate $r$ **before** differentiating, since there is no given rate for $r$: $V=\dfrac13\pi\left(\dfrac h2\right)^2h=\dfrac{\pi h^3}{12}$.
3. Differentiate in $t$: $\dfrac{dV}{dt}=\dfrac{\pi h^2}{4}\dfrac{dh}{dt}$.
4. Substitute $h=4$ and $\dfrac{dV}{dt}=0.5$: $0.5=4\pi\dfrac{dh}{dt}$.
5. Solve: $\dfrac{dh}{dt}=\dfrac{1}{8\pi}\approx0.0398$ m/min.

**The trap.** Reading "diameter equals height" as $r=h$ instead of $r=\frac h2$; that makes the final rate four times too small.

**MATH265 exam question (Q11.2) — the hypotenuse is the one that changes.** A rocket rises vertically, tracked by radar $5$ mi from the pad. Find $\dfrac{dy}{dt}$ when the height $y=4$ mi and the line-of-sight distance $z$ changes at $\dfrac{dz}{dt}=2000$ mi/h.

1. Relation: $z^2 = 5^2+y^2$, with the $5$ a fixed constant, which is what makes the problem solvable.
2. Find the missing side at the instant of interest: $z=\sqrt{25+16}=\sqrt{41}$.
3. Differentiate in $t$: $2z\dfrac{dz}{dt}=2y\dfrac{dy}{dt}$, i.e. $z\dfrac{dz}{dt}=y\dfrac{dy}{dt}$.
4. Substitute: $\sqrt{41}(2000)=4\dfrac{dy}{dt}$, so $\dfrac{dy}{dt}=500\sqrt{41}\approx3201.6$ mi/h.
5. Sanity check: the rocket's true speed must exceed the line-of-sight rate, since only part of its motion is along the sightline, and indeed $3201.6 > 2000$.

**The trap.** Swapping the leg and the hypotenuse (using $z=4$, $y=\sqrt{41}$); the hypotenuse is always the longest side.

---

## D14. Differentials and linear approximation

**Trigger.** Estimate a function value near a point you know exactly, or propagate a small error.

**Formulas.** $dy = f'(x)\,dx$, and the tangent-line approximation
$$f(x) \approx f(a) + f'(a)(x-a).$$

**Example.** Approximate $\sqrt{4.1}$.

*Steps.*

1. Take $f(x) = \sqrt{x}$ and the nearby exact point $a = 4$.
2. $f(4) = 2$ and $f'(x) = \frac{1}{2\sqrt x}$, so $f'(4) = \frac14$.
3. Apply: $\sqrt{4.1} \approx 2 + \frac14(0.1) = 2.025$.
4. Compare: the true value is $2.0248456\ldots$, so the error is about $1.5\times10^{-4}$.

**Error propagation.** If a sphere's radius is measured as $10\,\text{cm}$ with error up to $0.05\,\text{cm}$, then from $V = \frac43\pi r^3$ and $dV = 4\pi r^2\,dr$ the volume error is at most $4\pi(100)(0.05) \approx 62.8\,\text{cm}^3$.
The *relative* error is cleaner: $\frac{dV}{V} = 3\frac{dr}{r}$, so a $0.5\%$ radius error gives a $1.5\%$ volume error.

**MATH265 exam question (Q12.1) — a square root near a perfect square.** Use differentials to approximate $\sqrt{9.2}$.

1. Choose $f(x)=\sqrt x$, base point $a=9$ (nearest perfect square), $dx=0.2$.
2. $f(9)=3$ and $f'(x)=\dfrac{1}{2\sqrt x}$, so $f'(9)=\dfrac16$.
3. $\sqrt{9.2}\approx 3+\dfrac16(0.2) = 3+\dfrac{1}{30} = \dfrac{91}{30}\approx3.0333$.
4. The true value is $3.03315\ldots$, so the estimate is high by about $2\times10^{-4}$, consistent with $\sqrt x$ being concave down (its tangent line lies above the curve).

**MATH265 exam question (Q12.2) — an angle, so the step must be converted to radians first.** Use linearization to estimate $\sin(62^\circ)$.

1. Base point $a=60^\circ=\dfrac\pi3$ (nearest angle with exact values); the step is $dx=2^\circ=\dfrac{\pi}{90}\approx0.0349066$ — this conversion is the step that decides the whole answer, since the derivative formulas are only valid in radians.
2. Linearization: $\sin(a+dx)\approx\sin a+\cos a\,dx = \dfrac{\sqrt3}{2}+\dfrac12\cdot\dfrac{\pi}{90}$.
3. Evaluate: $\approx0.8660254+0.0174533=0.8834787$.
4. The true value is $0.8829476$, high by about $5\times10^{-4}$; the companion question (MATH265 Q12.3a, $\cos 62^\circ$) uses the same $dx$ but the *opposite* sign flips which side the estimate lands on, since cosine is decreasing where sine is increasing here.

**The trap common to both.** Using $dx=2$ instead of $dx=\frac{\pi}{90}$, which gives an impossible value like $1.87$ for a sine.

**MATH265 exam question (Q12.3) — the two four-decimal-place estimates promised above.**

**(a)** Estimate $\cos\left(62^\circ\right)$. Base point $a=\frac\pi3$, $dx=\frac{\pi}{90}$; $f'(x)=-\sin x$ so $f'\left(\frac\pi3\right)=-\frac{\sqrt3}{2}$. $\cos(62^\circ)\approx\frac12-\frac{\sqrt3}{2}\cdot\frac{\pi}{90}\approx0.5-0.0302300=0.4698$ (four decimal places: $0.4698$). The true value is $0.4694716$ — the estimate is now high, the error sign having flipped relative to Q12.2 because cosine is decreasing here.

**(b)** Estimate $\sqrt{16.4}$. Base point $a=16$, $dx=0.4$; $f'(16)=\dfrac{1}{2\sqrt{16}}=\dfrac18$. $\sqrt{16.4}\approx4+\dfrac18(0.4)=4.0500$ (four decimal places, so the trailing zero is required). The true value is $4.0496913$, high by about $0.0003$.

---

## D15. Partial derivatives

**Trigger.** A function of more than one variable.

**Method.** Differentiate with respect to one variable while treating every other variable as a constant.

**Example.** For $f(x,y) = x^3y^2 + e^{xy}$, find $f_x$, $f_y$, and $f_{xy}$.

*Steps.*

1. $f_x$: treat $y$ as constant, so $x^3y^2 \to 3x^2y^2$ and $e^{xy} \to ye^{xy}$ (chain rule, inner derivative $y$).
   Result: $f_x = 3x^2y^2 + ye^{xy}$.
2. $f_y$: treat $x$ as constant: $f_y = 2x^3y + xe^{xy}$.
3. $f_{xy} = \partial_y(f_x)$: differentiate $3x^2y^2 + ye^{xy}$ in $y$, needing the product rule on the second term.
   $\partial_y\left(ye^{xy}\right) = e^{xy} + xye^{xy}$.
   Result: $f_{xy} = 6x^2y + e^{xy}(1+xy)$.
4. Check with Clairaut's theorem by computing $f_{yx}$ from $f_y$: $\partial_x\left(2x^3y + xe^{xy}\right) = 6x^2y + e^{xy} + xye^{xy}$, which matches.

Clairaut's theorem ($f_{xy} = f_{yx}$ when both are continuous) is a free correctness check on every mixed partial you compute.

---

## D16. Multivariable chain rule, gradient, and directional derivative

**Chain rule.** For $z = f(x,y)$ with $x = x(t)$, $y = y(t)$:
$$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}.$$

Draw the dependency tree, then sum over every path from $z$ down to $t$, multiplying along each path.

**Example.** $z = x^2y$ with $x = \cos t$, $y = \sin t$; find $\frac{dz}{dt}$ at $t=0$.

1. $f_x = 2xy$, $f_y = x^2$.
2. $x' = -\sin t$, $y' = \cos t$.
3. Combine: $\frac{dz}{dt} = 2xy(-\sin t) + x^2\cos t$.
4. At $t=0$: $x=1$, $y=0$, giving $0 + 1 = 1$.

**Gradient and directional derivative.**
$$\nabla f = \langle f_x, f_y, f_z\rangle, \qquad D_{\mathbf{u}}f = \nabla f\cdot\mathbf{u} \quad (\lVert\mathbf{u}\rVert = 1).$$

**Example.** For $f(x,y) = x^2+3xy$ at $(1,2)$ in the direction of $\langle 3,4\rangle$.

1. $\nabla f = \langle 2x+3y,\ 3x\rangle$, so at $(1,2)$ it is $\langle 8, 3\rangle$.
2. Normalize the direction: $\lVert\langle3,4\rangle\rVert = 5$, so $\mathbf{u} = \langle\frac35,\frac45\rangle$.
3. Dot: $8\cdot\frac35 + 3\cdot\frac45 = \frac{24+12}{5} = \frac{36}{5}$.

Skipping the normalization in step 2 is the standard error, and it silently scales the answer.

**Implicit differentiation, multivariable form.** If $F(x,y) = 0$ defines $y$ implicitly, then $\dfrac{dy}{dx} = -\dfrac{F_x}{F_y}$.
For $x^3+y^3-6xy = 0$: $F_x = 3x^2-6y$, $F_y = 3y^2-6x$, giving $-\frac{3x^2-6y}{3y^2-6x} = \frac{2y-x^2}{y^2-2x}$, matching D8.

---

## D17. Differentiating an integral

**Trigger.** The variable appears in a limit of integration or inside the integrand as a parameter.

**Fundamental Theorem of Calculus, part 1.**
$$\frac{d}{dx}\int_{a}^{x}f(t)\,dt = f(x).$$

**With a variable upper limit that is a function.** Chain rule applies:
$$\frac{d}{dx}\int_{a}^{g(x)}f(t)\,dt = f\!\left(g(x)\right)g'(x).$$

**Example.** $\displaystyle\frac{d}{dx}\int_{1}^{x^{2}}\sqrt{1+t^{3}}\,dt$.

1. The integrand evaluated at the upper limit: $\sqrt{1+\left(x^2\right)^3} = \sqrt{1+x^6}$.
2. Times the derivative of the upper limit: $2x$.
3. Result: $2x\sqrt{1+x^6}$.

**Both limits variable.** Split at a constant $c$ and apply the rule twice, with a sign flip on the lower one:
$$\frac{d}{dx}\int_{u(x)}^{v(x)}f(t)\,dt = f(v)v' - f(u)u'.$$

**Example.** $\displaystyle\frac{d}{dx}\int_{x}^{x^{2}}\frac{dt}{t} = \frac{1}{x^2}(2x) - \frac{1}{x}(1) = \frac{2}{x}-\frac{1}{x} = \frac{1}{x}$.
Sanity check: the integral equals $\ln x^2 - \ln x = \ln x$, whose derivative is indeed $\frac1x$.

**Leibniz's general rule** (parameter inside the integrand too):
$$\frac{d}{dx}\int_{u(x)}^{v(x)}f(x,t)\,dt = f(x,v)v' - f(x,u)u' + \int_{u}^{v}\frac{\partial f}{\partial x}\,dt.$$

This rule read backwards is the integration technique I20.

**MATH265 exam question (Q18.1) — both limits variable, worked from the split rule directly.** Evaluate $\displaystyle\frac{d}{dx}\int_{2x}^{x}\sin\left(t^2\right)dt$.

1. Both limits depend on $x$, so the basic FTC-1 form does not apply directly; split at any constant $c$: $\displaystyle\int_{2x}^x = \int_c^x - \int_c^{2x}$.
2. Differentiate the first piece (upper limit is exactly $x$): $\sin\left(x^2\right)$.
3. Differentiate the second piece with the chain rule (upper limit is $2x$): evaluate the integrand at $2x$ and multiply by $\frac{d}{dx}(2x)=2$: $\sin\left((2x)^2\right)\cdot2 = 2\sin\left(4x^2\right)$.
4. Subtract: $\dfrac{d}{dx}\displaystyle\int_{2x}^x\sin\left(t^2\right)dt = \sin\left(x^2\right) - 2\sin\left(4x^2\right)$.

**The trap.** Writing $(2x)^2$ as $2x^2$ instead of $4x^2$, and dropping the chain-rule factor of $2$ — both errors hide inside the same term.

---

## D18. Numerical differentiation

**Trigger.** No formula: only sampled data, or a function available solely as a black box.

**Forward difference.** $f'(x)\approx\dfrac{f(x+h)-f(x)}{h}$, with error $O(h)$.

**Central difference.** $f'(x)\approx\dfrac{f(x+h)-f(x-h)}{2h}$, with error $O(h^2)$, so it is the default choice.

**Second derivative.** $f''(x)\approx\dfrac{f(x+h)-2f(x)+f(x-h)}{h^{2}}$.

**Example.** Estimate $f'(1)$ for $f(x) = \ln x$ with $h = 0.01$.

1. $f(1.01) = 0.00995033\ldots$ and $f(0.99) = -0.01005034\ldots$.
2. Central difference: $\dfrac{0.00995033-(-0.01005034)}{0.02} = \dfrac{0.02000067}{0.02}$.
3. Estimate $1.0000333$, against the exact $f'(1) = 1$.
4. The error is about $3.3\times10^{-5}$, consistent with the $O(h^2)$ prediction $\frac{h^2}{3} = 3.3\times10^{-5}$.

**The step-size floor.** Shrinking $h$ reduces truncation error but amplifies floating-point cancellation, so the total error bottoms out near $h\approx\sqrt{\epsilon_{\text{mach}}}\approx10^{-8}$ for a central difference.
Going smaller makes the answer *worse*.

**The complex-step derivative** dodges that entirely for real-analytic $f$:
$$f'(x) \approx \frac{\operatorname{Im}\left[f(x+ih)\right]}{h}.$$
There is no subtraction of nearby values, so $h = 10^{-20}$ is fine and the result is accurate to machine precision.

---

# Part 3 - Techniques for Evaluating Integrals

Integration is search, not mechanics.
There is no algorithm that turns an arbitrary elementary integrand into an elementary antiderivative, because most integrands do not have one.
So the working method is: **match the integrand against a short list of recognizable shapes**, and the list is what follows.

**The routing order that solves most integrals.** Try these in sequence, and stop at the first that fits.

1. Is it a table entry already, or a table entry after algebraic rewriting? (I1)
2. Is there an inner function whose derivative is also present, up to a constant? (I2)
3. Is it a product of two unlike types? (I3, I4)
4. Is it powers of trig functions? (I5)
5. Does it contain $\sqrt{a^2\pm x^2}$ or $\sqrt{x^2-a^2}$? (I6, after I7 if the quadratic is not centered)
6. Is it a rational function? (I9 if improper, then I8)
7. Is it rational in $\sin$ and $\cos$? (I10)
8. Does it contain a root of a linear expression? (I11)
9. Is the answer non-elementary? (I18, I19, I20)

**Always verify.** Differentiating the answer is a complete, cheap, and independent check.
It catches sign errors, missing chain-rule factors, and dropped constants, and it is the one habit that makes integration self-correcting.

---

## I1. Reverse the derivative table

Every derivative rule read backwards is an integration rule.

| Integral | Result |
| :--- | :--- |
| $\displaystyle\int x^{n}\,dx$ | $\dfrac{x^{n+1}}{n+1}+C$, $n\ne-1$ |
| $\displaystyle\int \frac{dx}{x}$ | $\ln\lvert x\rvert + C$ |
| $\displaystyle\int e^{x}\,dx$ | $e^{x}+C$ |
| $\displaystyle\int a^{x}\,dx$ | $\dfrac{a^{x}}{\ln a}+C$ |
| $\displaystyle\int \sin x\,dx$ | $-\cos x + C$ |
| $\displaystyle\int \cos x\,dx$ | $\sin x + C$ |
| $\displaystyle\int \sec^{2}x\,dx$ | $\tan x + C$ |
| $\displaystyle\int \sec x\tan x\,dx$ | $\sec x + C$ |
| $\displaystyle\int \tan x\,dx$ | $\ln\lvert\sec x\rvert + C$ |
| $\displaystyle\int \sec x\,dx$ | $\ln\lvert\sec x+\tan x\rvert + C$ |
| $\displaystyle\int \frac{dx}{\sqrt{a^{2}-x^{2}}}$ | $\arcsin\dfrac{x}{a}+C$ |
| $\displaystyle\int \frac{dx}{a^{2}+x^{2}}$ | $\dfrac{1}{a}\arctan\dfrac{x}{a}+C$ |
| $\displaystyle\int \frac{dx}{x\sqrt{x^{2}-a^{2}}}$ | $\dfrac{1}{a}\operatorname{arcsec}\dfrac{\lvert x\rvert}{a}+C$ |

**Example (algebra first).** Evaluate $\displaystyle\int\frac{x^{3}+2\sqrt{x}}{x}\,dx$.

*Steps.*

1. There is no quotient rule for integrals, so split the fraction term by term: $x^2 + 2x^{-1/2}$.
2. Power rule on each: $\dfrac{x^3}{3} + 2\cdot\dfrac{x^{1/2}}{1/2}$.
3. Result: $\dfrac{x^3}{3} + 4\sqrt{x} + C$.

**The $\frac{u'}{u}$ pattern.** $\displaystyle\int\frac{f'(x)}{f(x)}\,dx = \ln\lvert f(x)\rvert + C$ is worth recognizing on sight; it is where $\int\tan x\,dx$ comes from.

**MATH265 exam question (Q16.1a) — pull the constant out of the root, then it is pure power rule.** Evaluate $\displaystyle\int\left(x^2-x\right)\sqrt{3x}\,dx$.

1. There is no substitution here; the work is algebraic. Write $\sqrt{3x}=\sqrt3\,x^{1/2}$.
2. Distribute: $\left(x^2-x\right)\sqrt3\,x^{1/2} = \sqrt3\left(x^{5/2}-x^{3/2}\right)$.
3. Power rule on each term: $\displaystyle\int x^{5/2}dx=\frac27x^{7/2}$, $\displaystyle\int x^{3/2}dx=\frac25x^{5/2}$.
4. Result: $\sqrt3\left(\dfrac27x^{7/2}-\dfrac25x^{5/2}\right)+C$.

**MATH265 exam question (Q16.1d) — expand before reaching for substitution.** Evaluate $\displaystyle\int\left(x^2-4\right)^2dx$.

1. There is no inner-derivative factor available, so a substitution $u=x^2-4$ would leave a stray $x$ behind; expand instead.
2. $\left(x^2-4\right)^2 = x^4-8x^2+16$.
3. Integrate term by term: $\dfrac{x^5}{5}-\dfrac{8x^3}{3}+16x+C$.

**The trap.** Writing $\dfrac{\left(x^2-4\right)^3}{3}$ as if the chain rule ran backwards — that shortcut needs the inner derivative $2x$ to be present in the integrand, and it is not.

**MATH265 exam question (Q16.2c) — split the fraction term by term before reaching for a technique.** Evaluate $\displaystyle\int\frac{x^3+\sqrt{5x}-4}{x^2}\,dx$, naming the technique.

1. Technique: algebraic rewriting, then the power rule — there is no quotient rule for integrals.
2. Split term by term: $\dfrac{x^3}{x^2}=x$; $\dfrac{\sqrt{5x}}{x^2}=\dfrac{\sqrt5\,x^{1/2}}{x^2}=\sqrt5\,x^{-3/2}$; $\dfrac{-4}{x^2}=-4x^{-2}$.
3. Integrate each piece: $\displaystyle\int x\,dx=\dfrac{x^2}{2}$; $\displaystyle\int\sqrt5\,x^{-3/2}dx=-2\sqrt5\,x^{-1/2}$; $\displaystyle\int-4x^{-2}dx=\dfrac4x$.
4. Result: $\dfrac{x^2}{2}-\dfrac{2\sqrt5}{\sqrt{x}}+\dfrac4x+C$.

**The trap.** Trying to integrate the numerator and denominator separately — divide through first.

---

## I2. $u$-substitution

**Trigger.** The integrand contains a composite function *and* (a constant multiple of) the derivative of its inner function.

**Method.** Set $u$ = the inner function, compute $du = u'(x)\,dx$, and rewrite so that **no $x$ remains**.
If an $x$ survives, either solve $u$ back for $x$ or the substitution was the wrong choice.

**Example (indefinite).** Evaluate $\displaystyle\int 2x\sqrt{x^{2}+1}\,dx$.

*Steps.*

1. Inner function: $u = x^2+1$.
2. Differential: $du = 2x\,dx$, and $2x\,dx$ is exactly what sits outside the root.
3. Rewrite: $\displaystyle\int\sqrt{u}\,du = \int u^{1/2}\,du$.
4. Power rule: $\dfrac{2}{3}u^{3/2}$.
5. Back-substitute: $\dfrac{2}{3}\left(x^{2}+1\right)^{3/2}+C$.
6. Verify by differentiating: $\frac23\cdot\frac32(x^2+1)^{1/2}\cdot 2x = 2x\sqrt{x^2+1}$, which is the integrand.

**Example (definite: change the limits).** Evaluate $\displaystyle\int_{0}^{\pi/2}\sin^{3}x\cos x\,dx$.

1. $u = \sin x$, $du = \cos x\,dx$.
2. Convert the limits rather than back-substituting: $x=0\Rightarrow u=0$ and $x=\frac{\pi}{2}\Rightarrow u=1$.
3. The integral becomes $\displaystyle\int_{0}^{1}u^{3}\,du$.
4. Evaluate: $\left[\frac{u^4}{4}\right]_0^1 = \dfrac{1}{4}$.

Converting the limits in step 2 is safer than back-substituting, because it removes the chance of evaluating the old limits in the new variable.

**Example (an $x$ left over).** $\displaystyle\int x\sqrt{x+1}\,dx$: take $u = x+1$, so $x = u-1$ and $dx = du$.
Then $\int (u-1)\sqrt{u}\,du = \int\left(u^{3/2}-u^{1/2}\right)du = \frac25 u^{5/2}-\frac23 u^{3/2}+C$.

**MATH265 exam question (Q16.1e) — the same leftover-$x$ pattern, as a definite integral.** Evaluate $\displaystyle\int_{2}^{4}x\sqrt{x-1}\,dx$.

1. Let $u=x-1$, so $x=u+1$ and $dx=du$.
2. Convert the limits rather than back-substituting: $x=2\Rightarrow u=1$, $x=4\Rightarrow u=3$.
3. Rewrite: $\displaystyle\int_1^3(u+1)u^{1/2}\,du = \int_1^3\left(u^{3/2}+u^{1/2}\right)du = \left[\frac25u^{5/2}+\frac23u^{3/2}\right]_1^3$.
4. Using $3^{5/2}=9\sqrt3$ and $3^{3/2}=3\sqrt3$: at $u=3$ the bracket is $\dfrac{28\sqrt3}{5}$; at $u=1$ it is $\dfrac{16}{15}$.
5. Subtract: $\dfrac{28\sqrt3}{5}-\dfrac{16}{15} = \dfrac{84\sqrt3-16}{15} \approx 8.6328$.

**MATH265 exam question (Q16.2a) — solving for the exact piece that appears, rather than isolating $dx$ alone.** Evaluate $\displaystyle\int\frac{\cos\left(\sqrt{2x}\right)}{\sqrt{x}}\,dx$.

1. Let $u=\sqrt{2x}=\sqrt2\,x^{1/2}$, the inside of the cosine.
2. Differentiate: $du = \dfrac{\sqrt2}{2\sqrt x}\,dx$.
3. Rather than solving for $dx$ alone, solve for exactly the combination that appears in the integrand: $\dfrac{dx}{\sqrt x} = \sqrt2\,du$.
4. Rewrite and integrate: $\displaystyle\int\cos(u)\sqrt2\,du = \sqrt2\sin(u)+C = \sqrt2\sin\left(\sqrt{2x}\right)+C$.
5. Verify by differentiating: $\sqrt2\cos\left(\sqrt{2x}\right)\cdot\dfrac{\sqrt2}{2\sqrt x} = \dfrac{\cos\left(\sqrt{2x}\right)}{\sqrt x}$, the original integrand.

---

## I3. Integration by parts

**Trigger.** A product of two functions of *different types* (a polynomial and an exponential, a log and a power, an inverse trig and a power).

**Formula.** From the product rule, $\displaystyle\int u\,dv = uv - \int v\,du$.

**Choosing $u$: LIATE.** Pick $u$ as the first type that appears in this list, and $dv$ as the rest.

| Letter | Type |
| :--- | :--- |
| L | Logarithmic ($\ln x$) |
| I | Inverse trig ($\arctan x$) |
| A | Algebraic ($x^n$) |
| T | Trigonometric ($\sin x$) |
| E | Exponential ($e^x$) |

The rationale: things early in the list get *simpler* when differentiated, and things late in the list stay manageable when integrated.

**Example.** Evaluate $\displaystyle\int x e^{x}\,dx$.

*Steps.*

1. LIATE: $x$ is Algebraic and $e^x$ is Exponential, so $u=x$ and $dv = e^x dx$.
2. Compute the pieces: $du = dx$ and $v = e^x$.
3. Apply: $xe^{x} - \displaystyle\int e^{x}\,dx$.
4. Finish: $xe^{x} - e^{x} + C = (x-1)e^{x}+C$.
5. Verify: $\frac{d}{dx}\left[(x-1)e^x\right] = e^x + (x-1)e^x = xe^x$.

**Example (the "$dv = dx$" trick).** Evaluate $\displaystyle\int\ln x\,dx$.

1. There is only one factor, so take $u = \ln x$ and $dv = dx$.
2. $du = \frac{dx}{x}$ and $v = x$.
3. Apply: $x\ln x - \displaystyle\int x\cdot\frac{1}{x}\,dx = x\ln x - \int dx$.
4. Result: $x\ln x - x + C$.

The same trick gives $\int\arctan x\,dx = x\arctan x - \frac12\ln\left(1+x^2\right)+C$.

**Example (cyclic, where the integral returns).** Evaluate $\displaystyle I = \int e^{x}\sin x\,dx$.

1. Parts once with $u=\sin x$, $dv=e^x dx$: $I = e^{x}\sin x - \displaystyle\int e^{x}\cos x\,dx$.
2. Parts again on the new integral with $u=\cos x$: $\int e^x\cos x\,dx = e^{x}\cos x + \int e^{x}\sin x\,dx = e^x\cos x + I$.
3. Substitute back: $I = e^{x}\sin x - e^{x}\cos x - I$.
4. Solve algebraically for $I$: $2I = e^{x}(\sin x - \cos x)$.
5. Result: $I = \dfrac{e^{x}(\sin x-\cos x)}{2}+C$.

The critical detail in step 2 is keeping the *same* choice of type for $u$ both times.
Switching (taking $u=e^x$ on the second pass) unwinds the first step and returns $I=I$.

---

## I4. Tabular integration

**Trigger.** A polynomial times something that integrates repeatedly without getting worse ($e^{ax}$, $\sin ax$, $\cos ax$).

**Method.** Two columns: differentiate the polynomial down to $0$, integrate the other factor the same number of times, then multiply along the diagonals with alternating signs $+,-,+,-$.

**Example.** Evaluate $\displaystyle\int x^{3}e^{2x}\,dx$.

*Steps.*

1. Build the table.

| Sign | Differentiate $x^3$ | Integrate $e^{2x}$ |
| :--- | :--- | :--- |
| $+$ | $x^3$ | $\frac{1}{2}e^{2x}$ |
| $-$ | $3x^2$ | $\frac{1}{4}e^{2x}$ |
| $+$ | $6x$ | $\frac{1}{8}e^{2x}$ |
| $-$ | $6$ | $\frac{1}{16}e^{2x}$ |
| | $0$ | |

2. Multiply each row's derivative by the *next* row's integral, with the row's sign:
$$+\,x^3\cdot\tfrac12 e^{2x} \;-\; 3x^2\cdot\tfrac14 e^{2x} \;+\; 6x\cdot\tfrac18 e^{2x} \;-\; 6\cdot\tfrac{1}{16}e^{2x}.$$
3. Collect: $e^{2x}\left(\dfrac{x^{3}}{2} - \dfrac{3x^{2}}{4} + \dfrac{3x}{4} - \dfrac{3}{8}\right)+C$.
4. Verify by differentiating: the $e^{2x}$ terms cancel in pairs and leave $x^3e^{2x}$.

This replaces four rounds of integration by parts with one table.

---

## I5. Trigonometric integrals

**Case A: $\displaystyle\int\sin^{m}x\cos^{n}x\,dx$ with an odd power.**
Peel one factor off the odd power, convert the rest with $\sin^2+\cos^2=1$, and substitute.

**Example.** Evaluate $\displaystyle\int\sin^{3}x\cos^{2}x\,dx$.

1. The sine power is odd, so split off one $\sin x$: $\sin^2 x\cos^2 x\cdot\sin x$.
2. Convert the even part: $\sin^2 x = 1-\cos^2 x$.
3. Substitute $u=\cos x$, $du = -\sin x\,dx$: $\displaystyle-\int\left(1-u^{2}\right)u^{2}\,du$.
4. Expand and integrate: $-\displaystyle\int\left(u^2-u^4\right)du = -\dfrac{u^{3}}{3}+\dfrac{u^{5}}{5}$.
5. Back-substitute: $-\dfrac{\cos^{3}x}{3}+\dfrac{\cos^{5}x}{5}+C$.

**Case B: both powers even.** Use the half-angle identities $\sin^2 x = \frac{1-\cos 2x}{2}$ and $\cos^2 x = \frac{1+\cos 2x}{2}$ to lower the degree.

**Example.** $\displaystyle\int\sin^{2}x\,dx = \int\frac{1-\cos 2x}{2}\,dx = \frac{x}{2}-\frac{\sin 2x}{4}+C$.

**Case C: $\displaystyle\int\sec^{m}x\tan^{n}x\,dx$.**
If the secant power is even, save $\sec^2 x$ and substitute $u=\tan x$.
If the tangent power is odd, save $\sec x\tan x$ and substitute $u=\sec x$.

**Example (the one to memorize).** $\displaystyle\int\sec^{3}x\,dx$ fits neither pattern, so use parts with $u=\sec x$, $dv = \sec^2 x\,dx$.
It is cyclic like the $e^x\sin x$ example, and solving for the integral gives
$$\int\sec^{3}x\,dx = \frac{1}{2}\sec x\tan x + \frac{1}{2}\ln\lvert\sec x+\tan x\rvert + C.$$

**Case D: products of different frequencies.** Use the product-to-sum identities.
$$\sin A\cos B = \tfrac12\left[\sin(A-B)+\sin(A+B)\right],$$
$$\sin A\sin B = \tfrac12\left[\cos(A-B)-\cos(A+B)\right],$$
$$\cos A\cos B = \tfrac12\left[\cos(A-B)+\cos(A+B)\right].$$

**Example.** $\displaystyle\int\sin 3x\cos 5x\,dx = \frac12\int\left[\sin(-2x)+\sin 8x\right]dx = \frac{\cos 2x}{4}-\frac{\cos 8x}{16}+C$.

This is also the calculation behind the orthogonality relations in Fourier series.

**MATH265 exam question (Q16.1b) — mismatched frequencies removed with a double-angle identity, then Case A.** Evaluate $\displaystyle\int\sin(2x)\cos x\,dx$.

1. The two different arguments $2x$ and $x$ block a direct substitution, so first rewrite $\sin(2x)=2\sin x\cos x$: the integral becomes $\displaystyle\int2\sin x\cos^2x\,dx$.
2. This is now Case A with an odd power of sine: substitute $u=\cos x$, $du=-\sin x\,dx$: $-2\displaystyle\int u^2\,du$.
3. Integrate and back-substitute: $-\dfrac{2}{3}\cos^3x+C$.
4. Verify: $\dfrac{d}{dx}\left(-\frac23\cos^3x\right) = 2\sin x\cos^2x = \sin(2x)\cos x$. Confirmed.

**MATH265 exam question (Q16.2b) — Case C recognized directly, as a definite integral.** Evaluate $\displaystyle\int_{0}^{\pi/3}\tan x\sec^2x\,dx$.

1. $\sec^2x$ is exactly the derivative of $\tan x$, the Case C signal for an even secant power: $u=\tan x$, $du=\sec^2x\,dx$.
2. Convert the limits: $x=0\Rightarrow u=0$; $x=\frac\pi3\Rightarrow u=\tan\frac\pi3=\sqrt3$.
3. The integral becomes $\displaystyle\int_0^{\sqrt3}u\,du = \left[\frac{u^2}{2}\right]_0^{\sqrt3} = \frac32$.

**MATH265 exam question (Q16.2d) — Case C with the hint already split out.** Evaluate $\displaystyle\int\sec^3x\tan x\,dx$, using $\sec^3x\tan x=\sec^2x\cdot(\sec x\tan x)$.

1. The hint isolates the piece that will become $du$: let $u=\sec x$, so $du=\sec x\tan x\,dx$.
2. Rewrite: $\displaystyle\int\sec^2x\left(\sec x\tan x\,dx\right) = \int u^2\,du$.
3. Integrate and back-substitute: $\dfrac{u^3}{3}+C = \dfrac{\sec^3x}{3}+C$.
4. Verify: $\dfrac{d}{dx}\dfrac{\sec^3x}{3} = \sec^2x\cdot\sec x\tan x = \sec^3x\tan x$. Confirmed.

---

## I6. Trigonometric substitution

**Trigger.** A quadratic under a root, in one of three shapes.

| Integrand contains | Substitute | Identity used | $dx$ |
| :--- | :--- | :--- | :--- |
| $\sqrt{a^{2}-x^{2}}$ | $x = a\sin\theta$ | $1-\sin^2 = \cos^2$ | $a\cos\theta\,d\theta$ |
| $\sqrt{a^{2}+x^{2}}$ | $x = a\tan\theta$ | $1+\tan^2 = \sec^2$ | $a\sec^2\theta\,d\theta$ |
| $\sqrt{x^{2}-a^{2}}$ | $x = a\sec\theta$ | $\sec^2-1 = \tan^2$ | $a\sec\theta\tan\theta\,d\theta$ |

**Example.** Evaluate $\displaystyle\int\sqrt{9-x^{2}}\,dx$.

*Steps.*

1. Shape is $\sqrt{a^2-x^2}$ with $a=3$, so set $x = 3\sin\theta$ and $dx = 3\cos\theta\,d\theta$.
2. The root becomes $\sqrt{9-9\sin^2\theta} = 3\sqrt{\cos^2\theta} = 3\cos\theta$ (taking $\theta\in\left[-\frac\pi2,\frac\pi2\right]$ so cosine is non-negative).
3. The integral is $\displaystyle\int 3\cos\theta\cdot3\cos\theta\,d\theta = 9\int\cos^{2}\theta\,d\theta$.
4. Half-angle (I5 case B): $9\left(\dfrac{\theta}{2}+\dfrac{\sin 2\theta}{4}\right)$.
5. Convert back with a reference triangle: $\sin\theta = \frac{x}{3}$ gives $\theta = \arcsin\frac{x}{3}$, and $\sin 2\theta = 2\sin\theta\cos\theta = 2\cdot\frac{x}{3}\cdot\frac{\sqrt{9-x^2}}{3}$.
6. Result: $\dfrac{9}{2}\arcsin\dfrac{x}{3} + \dfrac{x\sqrt{9-x^{2}}}{2}+C$.

**Example (a root in the denominator).** Evaluate $\displaystyle\int\frac{dx}{x^{2}\sqrt{x^{2}+4}}$.

1. Shape is $\sqrt{a^2+x^2}$ with $a=2$: set $x = 2\tan\theta$, $dx = 2\sec^2\theta\,d\theta$, and $\sqrt{x^2+4} = 2\sec\theta$.
2. Substitute everything: $\displaystyle\int\frac{2\sec^{2}\theta\,d\theta}{4\tan^{2}\theta\cdot2\sec\theta} = \frac{1}{4}\int\frac{\sec\theta}{\tan^{2}\theta}\,d\theta$.
3. Convert to sines and cosines: $\dfrac{\sec\theta}{\tan^2\theta} = \dfrac{\cos\theta}{\sin^2\theta}$.
4. Substitute $w=\sin\theta$: $\dfrac14\displaystyle\int\frac{dw}{w^{2}} = -\dfrac{1}{4\sin\theta}$.
5. Reference triangle: $\tan\theta = \frac{x}{2}$, so $\sin\theta = \frac{x}{\sqrt{x^2+4}}$.
6. Result: $-\dfrac{\sqrt{x^{2}+4}}{4x}+C$.

**Step 5 is where marks are lost.** Draw the triangle: opposite $=x$, adjacent $=a$ (for the tangent case), hypotenuse $=\sqrt{x^2+a^2}$, and read every trig function off it.

**Hyperbolic alternative.** $x = a\sinh t$ for $\sqrt{a^2+x^2}$ and $x=a\cosh t$ for $\sqrt{x^2-a^2}$ avoid the back-substitution triangle at the price of hyperbolic identities.

---

## I7. Completing the square

**Trigger.** An irreducible quadratic that has a linear term, under a root or in a denominator.

**Method.** Rewrite $ax^2+bx+c$ as $a\left(x+\frac{b}{2a}\right)^2 + \left(c-\frac{b^2}{4a}\right)$, then substitute $u = x+\frac{b}{2a}$ to reach a centered form the table (I1) or I6 can handle.

**Example.** Evaluate $\displaystyle\int\frac{dx}{x^{2}+4x+13}$.

*Steps.*

1. Complete the square: $x^2+4x+13 = \left(x^2+4x+4\right)+9 = (x+2)^2+9$.
2. Substitute $u = x+2$, $du = dx$: $\displaystyle\int\frac{du}{u^{2}+9}$.
3. Table entry with $a=3$: $\dfrac{1}{3}\arctan\dfrac{u}{3}$.
4. Back-substitute: $\dfrac{1}{3}\arctan\dfrac{x+2}{3}+C$.

**With a linear numerator.** Split it into "a multiple of the derivative of the denominator" plus "a constant".
For $\displaystyle\int\frac{2x+7}{x^2+4x+13}\,dx$: write $2x+7 = (2x+4) + 3$, so the first piece is a $\frac{u'}{u}$ log and the second is the arctangent above.
The result is $\ln\left(x^2+4x+13\right) + \arctan\dfrac{x+2}{3}+C$.

---

## I8. Partial fractions

**Trigger.** A rational function $\frac{P(x)}{Q(x)}$ with $\deg P < \deg Q$ (otherwise do I9 first).

**The four decomposition cases.** Factor $Q$ completely over the reals, then assign terms:

| Factor of $Q$ | Contributes |
| :--- | :--- |
| Distinct linear $(x-a)$ | $\dfrac{A}{x-a}$ |
| Repeated linear $(x-a)^{k}$ | $\dfrac{A_1}{x-a}+\dfrac{A_2}{(x-a)^{2}}+\cdots+\dfrac{A_k}{(x-a)^{k}}$ |
| Distinct irreducible quadratic $(x^{2}+bx+c)$ | $\dfrac{Ax+B}{x^{2}+bx+c}$ |
| Repeated irreducible quadratic, power $k$ | one such term for each power up to $k$ |

**Example (distinct linear).** Evaluate $\displaystyle\int\frac{3x+11}{x^{2}-x-6}\,dx$.

*Steps.*

1. Factor the denominator: $(x-3)(x+2)$.
2. Set up: $\dfrac{3x+11}{(x-3)(x+2)} = \dfrac{A}{x-3}+\dfrac{B}{x+2}$.
3. Clear denominators: $3x+11 = A(x+2)+B(x-3)$.
4. Use strategic values (the cover-up method).
   Put $x=3$: $20 = 5A$, so $A=4$.
   Put $x=-2$: $5 = -5B$, so $B=-1$.
5. Integrate term by term: $4\ln\lvert x-3\rvert - \ln\lvert x+2\rvert + C$.

**Example (irreducible quadratic).** Evaluate $\displaystyle\int\frac{2x+3}{(x-1)\left(x^{2}+1\right)}\,dx$.

1. Set up with a *linear* numerator over the quadratic: $\dfrac{A}{x-1}+\dfrac{Bx+C}{x^{2}+1}$.
2. Clear: $2x+3 = A\left(x^{2}+1\right)+(Bx+C)(x-1)$.
3. Put $x=1$: $5 = 2A$, so $A = \frac52$.
4. Match $x^2$ coefficients: $0 = A+B$, so $B = -\frac52$.
5. Match constants: $3 = A - C$, so $C = \frac52-3 = -\frac12$.
6. Integrate the three pieces, the middle one by $u=x^2+1$ and the last by the arctangent entry:
$$\frac{5}{2}\ln\lvert x-1\rvert - \frac{5}{4}\ln\left(x^{2}+1\right) - \frac{1}{2}\arctan x + C.$$

**Splitting a $\frac{Bx+C}{x^2+1}$ term.** Always break it into $\frac{B}{2}\cdot\frac{2x}{x^2+1}$ (a log) plus $\frac{C}{x^2+1}$ (an arctangent).
Trying to integrate it whole is the usual dead end.

---

## I9. Long division first

**Trigger.** A rational function whose numerator degree is greater than or equal to the denominator degree.

**Example.** Evaluate $\displaystyle\int\frac{x^{3}}{x^{2}+1}\,dx$.

*Steps.*

1. Degrees are $3$ and $2$, so partial fractions does not apply yet.
2. Divide: $\dfrac{x^{3}}{x^{2}+1} = x - \dfrac{x}{x^{2}+1}$.
   (Check by multiplying back: $x(x^2+1) - x = x^3$.)
3. Integrate the polynomial part: $\dfrac{x^{2}}{2}$.
4. Integrate the remainder with $u = x^2+1$: $-\dfrac{1}{2}\ln\left(x^{2}+1\right)$.
5. Result: $\dfrac{x^{2}}{2}-\dfrac{1}{2}\ln\left(x^{2}+1\right)+C$.

---

## I10. The Weierstrass substitution $t=\tan\frac{x}{2}$

**Trigger.** A rational function of $\sin x$ and $\cos x$ that none of the trig techniques reach.

**The conversions.**
$$\sin x = \frac{2t}{1+t^{2}},\qquad \cos x = \frac{1-t^{2}}{1+t^{2}},\qquad dx = \frac{2\,dt}{1+t^{2}}.$$

This turns *any* such integrand into an ordinary rational function of $t$, which I8 then finishes.
It is the universal fallback for this family, and it is usually messier than a clever alternative, so reach for it last.

**Example.** Evaluate $\displaystyle\int\frac{dx}{1+\sin x}$.

*Steps.*

1. Substitute all three conversions:
$$\int\frac{\frac{2\,dt}{1+t^{2}}}{1+\frac{2t}{1+t^{2}}}.$$
2. Multiply numerator and denominator by $1+t^2$: $\displaystyle\int\frac{2\,dt}{1+t^{2}+2t}$.
3. Recognize the perfect square: $1+2t+t^2 = (1+t)^2$.
4. Integrate: $\displaystyle\int\frac{2\,dt}{(1+t)^{2}} = -\frac{2}{1+t}$.
5. Back-substitute: $-\dfrac{2}{1+\tan\frac{x}{2}}+C$.

**Cross-check by another route.** Multiplying the original integrand by $\frac{1-\sin x}{1-\sin x}$ gives $\frac{1-\sin x}{\cos^2 x} = \sec^2 x - \sec x\tan x$, whose integral is $\tan x - \sec x + C$.
The two answers differ by a constant, which is exactly what antiderivatives are allowed to do.

---

## I11. Rationalizing substitutions

**Trigger.** An $n$th root of a linear expression, or several roots of $x$ with different indices.

**Method.** Set $u$ equal to the root itself (or, for mixed indices, to $x^{1/L}$ where $L$ is the least common multiple of the indices).

**Example.** Evaluate $\displaystyle\int\frac{dx}{1+\sqrt{x}}$.

*Steps.*

1. Let $u = \sqrt{x}$, so $x = u^2$ and $dx = 2u\,du$.
2. Substitute: $\displaystyle\int\frac{2u}{1+u}\,du$.
3. This is improper as a rational function, so divide (I9): $\dfrac{2u}{1+u} = 2 - \dfrac{2}{1+u}$.
4. Integrate: $2u - 2\ln\lvert 1+u\rvert$.
5. Back-substitute: $2\sqrt{x} - 2\ln\left(1+\sqrt{x}\right)+C$.

**Mixed indices.** For $\displaystyle\int\frac{dx}{\sqrt{x}+\sqrt[3]{x}}$ take $u = x^{1/6}$, since $\operatorname{lcm}(2,3)=6$; then $\sqrt{x}=u^3$, $\sqrt[3]{x}=u^2$, and $dx = 6u^5\,du$, leaving a rational function of $u$.

---

## I12. Reduction formulas

**Trigger.** A power left symbolic, or a power high enough that repeated parts would be tedious.

**Derivation.** Apply integration by parts once and arrange the result to reference the same integral at a lower power.

**Key formulas.**
$$\int\sin^{n}x\,dx = -\frac{\sin^{n-1}x\cos x}{n}+\frac{n-1}{n}\int\sin^{n-2}x\,dx,$$
$$\int x^{n}e^{x}\,dx = x^{n}e^{x}-n\int x^{n-1}e^{x}\,dx,$$
$$\int\sec^{n}x\,dx = \frac{\sec^{n-2}x\tan x}{n-1}+\frac{n-2}{n-1}\int\sec^{n-2}x\,dx.$$

**Example.** Evaluate $\displaystyle\int\sin^{4}x\,dx$.

*Steps.*

1. Apply the formula with $n=4$: $-\dfrac{\sin^{3}x\cos x}{4}+\dfrac{3}{4}\displaystyle\int\sin^{2}x\,dx$.
2. Apply it again with $n=2$, or reuse the half-angle result: $\displaystyle\int\sin^{2}x\,dx = \frac{x}{2}-\frac{\sin 2x}{4}$.
3. Combine: $-\dfrac{\sin^{3}x\cos x}{4}+\dfrac{3x}{8}-\dfrac{3\sin 2x}{16}+C$.

**Wallis's formula** is the definite-integral version, and it collapses the recursion to a single product:
$$\int_{0}^{\pi/2}\sin^{n}x\,dx = \begin{cases}\dfrac{(n-1)!!}{n!!}\cdot\dfrac{\pi}{2} & n \text{ even}\\[2mm] \dfrac{(n-1)!!}{n!!} & n \text{ odd}\end{cases}$$

So $\int_0^{\pi/2}\sin^4 x\,dx = \frac{3\cdot1}{4\cdot2}\cdot\frac{\pi}{2} = \frac{3\pi}{16}$.

---

## I13. Symmetry and periodicity

**Trigger.** A definite integral over an interval symmetric about $0$ (or about the center of a period).

**The rules.**
$$\int_{-a}^{a}f(x)\,dx = 0 \text{ if } f \text{ is odd}, \qquad \int_{-a}^{a}f(x)\,dx = 2\int_{0}^{a}f(x)\,dx \text{ if } f \text{ is even}.$$

**Example.** Evaluate $\displaystyle\int_{-2}^{2}\left(x^{3}\cos x + x^{2}\right)dx$.

*Steps.*

1. Split by parity: $x^3\cos x$ is odd (odd times even), and $x^2$ is even.
2. The odd part contributes $0$ without any antidifferentiation, and $x^3\cos x$ has a genuinely tedious antiderivative, so this is real work saved.
3. The even part doubles: $2\displaystyle\int_{0}^{2}x^{2}\,dx = 2\cdot\dfrac{8}{3}$.
4. Result: $\dfrac{16}{3}$.

**Periodicity.** If $f$ has period $T$, then $\int_{a}^{a+T}f = \int_{0}^{T}f$ for every $a$, so you may slide the window to wherever the algebra is easiest.

---

## I14. The reflection (king) property

**Trigger.** A definite integral where substituting $x\mapsto a+b-x$ produces something that combines with the original.

**Property.** $\displaystyle\int_{a}^{b}f(x)\,dx = \int_{a}^{b}f(a+b-x)\,dx$.

**Example.** Evaluate $\displaystyle I = \int_{0}^{\pi/2}\frac{\sin x}{\sin x+\cos x}\,dx$.

*Steps.*

1. No standard technique applies cleanly, so reflect with $x\mapsto\frac{\pi}{2}-x$.
2. Under that map $\sin x\to\cos x$ and $\cos x\to\sin x$, so
$$I = \int_{0}^{\pi/2}\frac{\cos x}{\cos x+\sin x}\,dx.$$
3. Add the two expressions for $I$; the denominators are identical, so the numerators add:
$$2I = \int_{0}^{\pi/2}\frac{\sin x+\cos x}{\sin x+\cos x}\,dx = \int_{0}^{\pi/2}1\,dx = \frac{\pi}{2}.$$
4. Therefore $I = \dfrac{\pi}{4}$.

The antiderivative of the original integrand exists but is unpleasant; the reflection never computes it at all.

---

## I15. The Fundamental Theorem of Calculus, part 2

**Statement.** If $F' = f$ on $[a,b]$ and $f$ is continuous there, then
$$\int_{a}^{b}f(x)\,dx = F(b)-F(a).$$

**Example.** Evaluate $\displaystyle\int_{1}^{2}\left(3x^{2}-2x\right)dx$.

*Steps.*

1. Antidifferentiate: $F(x) = x^{3}-x^{2}$.
2. Evaluate at the top: $F(2) = 8-4 = 4$.
3. Evaluate at the bottom: $F(1) = 1-1 = 0$.
4. Subtract: $4-0 = 4$.

**The trap: a discontinuity inside the interval.**
Writing $\int_{-1}^{1}\frac{dx}{x^{2}} = \left[-\frac1x\right]_{-1}^{1} = -2$ is wrong, and visibly so since the integrand is positive everywhere.
The integrand blows up at $0$, which is inside the interval, so the theorem does not apply and the integral must be treated as improper (I17).
It diverges.

**Net change.** $\int_a^b f'(x)\,dx = f(b)-f(a)$ is the same statement read as "the integral of a rate is the total change", which is where displacement, total growth, and accumulated cost all come from.

**MATH265 exam question (Q16.1c) — symbolic limits are still just numbers once evaluated.** Evaluate $\displaystyle\int_{a}^{b}\left(x+\cos(2x)\right)dx$.

1. Antidifferentiate term by term: $\displaystyle\int x\,dx=\frac{x^2}{2}$, and $\displaystyle\int\cos(2x)\,dx=\frac{\sin(2x)}{2}$ (the $\frac12$ comes from the inner derivative of $2x$).
2. Apply the limits: $\left[\dfrac{x^2}{2}+\dfrac{\sin(2x)}{2}\right]_a^b$.
3. Result: $\dfrac{b^2-a^2}{2}+\dfrac{\sin(2b)-\sin(2a)}{2}$.

**The trap.** This is a **definite** integral, so no $+C$ — the letters $a,b$ make it look symbolic, but it is a number as soon as they are assigned values.

**MATH265 exam question (Q19.1) — a plain FTC-2 evaluation, dressed as an area-between-curves problem.** Find the area between $y=x$ and $y=2-x^2$.

1. Intersect: $x=2-x^2 \implies x^2+x-2=0=(x+2)(x-1)$, giving $x=-2,\,1$.
2. Test a point between them ($x=0$): the parabola ($2$) sits above the line ($0$) on the whole interval, so no split is needed.
3. Set up top minus bottom: $A=\displaystyle\int_{-2}^{1}\left[(2-x^2)-x\right]dx$.
4. Antidifferentiate and evaluate: $\left[2x-\dfrac{x^2}{2}-\dfrac{x^3}{3}\right]_{-2}^{1} = \dfrac76-\left(-\dfrac{10}{3}\right) = \dfrac{27}{6}=\dfrac92$.

**The trap.** Integrating line minus parabola returns $-\frac92$; an area is positive, so a negative result means the top and bottom were swapped.

**MATH265 exam question (Q19.3) — the "net change" reading of FTC-2, applied directly.** Water drains from a tank at $r(t)=180-6t$ L/min for $0\le t\le50$. Find the amount that leaves during the first $15$ minutes.

1. A **rate** is given and a **total** is wanted — exactly the net-change reading above — so integrate the rate: $\text{Amount}=\displaystyle\int_0^{15}(180-6t)\,dt$.
2. Antidifferentiate and evaluate: $\left[180t-3t^2\right]_0^{15} = 2700-675 = 2025$ litres.
3. Sanity check: the rate falls linearly from $180$ to $90$ L/min, averaging $135$ L/min, and $135\times15=2025$ agrees.

---

## I16. Riemann sums from the definition

**Trigger.** The question says "using the definition of the definite integral".

**Definition.** With $\Delta x = \frac{b-a}{n}$ and $x_i = a+i\Delta x$,
$$\int_{a}^{b}f(x)\,dx = \lim_{n\to\infty}\sum_{i=1}^{n}f(x_i)\,\Delta x.$$

**Example.** Evaluate $\displaystyle\int_{0}^{1}x^{2}\,dx$ from the definition.

*Steps.*

1. Set up: $\Delta x = \frac{1}{n}$ and $x_i = \frac{i}{n}$.
2. The sum is $\displaystyle\sum_{i=1}^{n}\left(\frac{i}{n}\right)^{2}\frac{1}{n} = \frac{1}{n^{3}}\sum_{i=1}^{n}i^{2}$.
3. Use the closed form $\displaystyle\sum_{i=1}^{n}i^{2} = \frac{n(n+1)(2n+1)}{6}$.
4. Simplify: $\dfrac{n(n+1)(2n+1)}{6n^{3}} = \dfrac{2n^{3}+3n^{2}+n}{6n^{3}}$.
5. Take the limit by degree comparison (L8): $\dfrac{2}{6} = \dfrac{1}{3}$.

**The sums needed for this technique.**
$$\sum_{i=1}^{n}1 = n,\quad \sum_{i=1}^{n}i = \frac{n(n+1)}{2},\quad \sum_{i=1}^{n}i^{2} = \frac{n(n+1)(2n+1)}{6},\quad \sum_{i=1}^{n}i^{3} = \left[\frac{n(n+1)}{2}\right]^{2}.$$

Read in the other direction, this technique is L19.

---

## I17. Improper integrals and convergence tests

**Trigger.** An infinite limit of integration, or an integrand that blows up somewhere on the interval.

**Method.** Replace the offending endpoint with a variable and take a limit.
If the blow-up is interior, split at it and require *both* pieces to converge independently.

**Example (infinite interval).** Evaluate $\displaystyle\int_{1}^{\infty}\frac{dx}{x^{2}}$.

*Steps.*

1. Rewrite as a limit: $\displaystyle\lim_{b\to\infty}\int_{1}^{b}x^{-2}\,dx$.
2. Antidifferentiate: $\left[-\dfrac{1}{x}\right]_{1}^{b} = -\dfrac{1}{b}+1$.
3. Take the limit: $0+1 = 1$.
4. The integral converges to $1$.

**Example (blow-up at an endpoint).** $\displaystyle\int_{0}^{1}\frac{dx}{\sqrt{x}} = \lim_{a\to0^{+}}\left[2\sqrt{x}\right]_{a}^{1} = 2-0 = 2$, which converges even though the integrand is unbounded.

**The $p$-tests, which settle most cases by inspection.**

| Integral | Converges when |
| :--- | :--- |
| $\displaystyle\int_{1}^{\infty}\frac{dx}{x^{p}}$ | $p>1$ |
| $\displaystyle\int_{0}^{1}\frac{dx}{x^{p}}$ | $p<1$ |

The two conditions are opposite, which is the point: at infinity you need fast decay, near zero you need mild blow-up.

**Comparison test.** If $0\le f\le g$ and $\int g$ converges, so does $\int f$; if $\int f$ diverges, so does $\int g$.

**Limit comparison test.** If $\lim_{x\to\infty}\frac{f(x)}{g(x)} = L$ with $0<L<\infty$, then $\int f$ and $\int g$ do the same thing.

**Example.** Does $\displaystyle\int_{1}^{\infty}\frac{dx}{\sqrt{x^{3}+1}}$ converge?

1. For large $x$ the integrand behaves like $x^{-3/2}$.
2. Limit comparison against $g = x^{-3/2}$: the ratio is $\frac{x^{3/2}}{\sqrt{x^3+1}}\to 1$, a finite positive number.
3. $\int_1^\infty x^{-3/2}dx$ converges because $p = \frac32 > 1$.
4. Therefore the given integral converges.

---

## I18. Numerical quadrature

**Trigger.** No elementary antiderivative exists ($e^{-x^2}$, $\frac{\sin x}{x}$, $\sqrt{1+x^4}$), or you only have data points.

**The three rules**, with $h = \frac{b-a}{n}$:

| Rule | Formula | Error |
| :--- | :--- | :--- |
| Midpoint | $h\sum f\!\left(\bar{x}_i\right)$ | $O(h^{2})$ |
| Trapezoid | $\dfrac{h}{2}\left[f_0+2f_1+\cdots+2f_{n-1}+f_n\right]$ | $O(h^{2})$ |
| Simpson ($n$ even) | $\dfrac{h}{3}\left[f_0+4f_1+2f_2+4f_3+\cdots+4f_{n-1}+f_n\right]$ | $O(h^{4})$ |

Simpson's coefficient pattern is $1,4,2,4,\ldots,4,1$: the endpoints get $1$, odd indices get $4$, even interior indices get $2$.

**Example.** Approximate $\displaystyle\int_{0}^{1}e^{-x^{2}}\,dx$ with Simpson's rule and $n=4$.

*Steps.*

1. $h = 0.25$, and the nodes are $0,\ 0.25,\ 0.5,\ 0.75,\ 1$.
2. Evaluate: $f_0 = 1$, $f_1 = 0.9394131$, $f_2 = 0.7788008$, $f_3 = 0.5697828$, $f_4 = 0.3678794$.
3. Weighted sum: $1 + 4(0.9394131) + 2(0.7788008) + 4(0.5697828) + 0.3678794 = 8.9622646$.
4. Multiply by $\frac{h}{3} = \frac{1}{12}$: the estimate is $0.7468554$.
5. The true value is $0.7468241$, so the error is about $3.1\times10^{-5}$ from five function evaluations.

**Error bounds**, which is what makes these usable rather than merely plausible:
$$\lvert E_{\text{trap}}\rvert\le\frac{K(b-a)^{3}}{12n^{2}},\qquad \lvert E_{\text{Simpson}}\rvert\le\frac{M(b-a)^{5}}{180n^{4}},$$
where $K\ge\lvert f''\rvert$ and $M\ge\left\lvert f^{(4)}\right\rvert$ on the interval.

**Why Simpson wins.** Doubling $n$ cuts the trapezoid error by $4$ and Simpson's by $16$.
Simpson is exact for cubics, despite being built from parabolas, which is the pleasant surprise in its error term.

---

## I19. Term-by-term series integration

**Trigger.** The integrand has a known power series and no elementary antiderivative.

**Method.** Substitute the series, integrate term by term inside its radius of convergence, and truncate when the next term is below your tolerance.

**Example.** Evaluate $\displaystyle\int_{0}^{1}\frac{\sin x}{x}\,dx$.

*Steps.*

1. Expand: $\sin x = x - \frac{x^3}{6}+\frac{x^5}{120}-\frac{x^7}{5040}+\cdots$.
2. Divide by $x$: $\dfrac{\sin x}{x} = 1 - \dfrac{x^{2}}{6}+\dfrac{x^{4}}{120}-\dfrac{x^{6}}{5040}+\cdots$ (note this removes the apparent singularity at $0$).
3. Integrate term by term on $[0,1]$: $1 - \dfrac{1}{18}+\dfrac{1}{600}-\dfrac{1}{35280}+\cdots$.
4. The general term is $\dfrac{(-1)^{n}}{(2n+1)(2n+1)!}$.
5. Sum four terms: $1 - 0.0555556 + 0.0016667 - 0.0000283 = 0.9460828$.
6. The series alternates with decreasing terms, so the truncation error is below the first omitted term, about $3\times10^{-7}$.

The true value is $\operatorname{Si}(1) = 0.9460831$, inside that bound.

---

## I20. Differentiation under the integral sign (Feynman's trick)

**Trigger.** A definite integral with a parameter in it, or one where you can *introduce* a parameter so that differentiating simplifies the integrand.

**Method.** Define $I(a)$, differentiate under the integral sign (Leibniz, D17), evaluate the easier integral, then integrate back in $a$ and fix the constant using a value of $a$ where $I$ is known.

**Example.** Evaluate $\displaystyle\int_{0}^{1}\frac{x^{a}-1}{\ln x}\,dx$ for $a>-1$.

*Steps.*

1. Call it $I(a)$, and note the easy anchor $I(0) = \int_0^1 0\,dx = 0$.
2. Differentiate under the integral sign with respect to $a$.
   Since $\frac{\partial}{\partial a}x^{a} = x^{a}\ln x$, the awkward $\ln x$ in the denominator cancels:
$$I'(a) = \int_{0}^{1}\frac{x^{a}\ln x}{\ln x}\,dx = \int_{0}^{1}x^{a}\,dx = \frac{1}{a+1}.$$
3. Integrate back: $I(a) = \ln(a+1)+C$.
4. Apply the anchor $I(0)=0$: $0 = \ln 1 + C$, so $C = 0$.
5. Result: $I(a) = \ln(a+1)$.

Check at $a=1$: $\int_0^1\frac{x-1}{\ln x}dx = \ln 2 \approx 0.693147$.

**Second classic.** $\displaystyle\int_{0}^{\infty}\frac{e^{-ax}-e^{-bx}}{x}\,dx = \ln\frac{b}{a}$, obtained the same way by differentiating with respect to $a$.

---

## I21. Multiple integrals and change of variables

**Iterated integrals (Fubini).** A double integral over a region is computed as two single integrals, inner first.
The inner limits may depend on the outer variable; the outer limits must be constants.

**Example (swapping the order to make it doable).** Evaluate $\displaystyle\int_{0}^{1}\int_{x}^{1}e^{y^{2}}\,dy\,dx$.

*Steps.*

1. The inner integral $\int e^{y^2}dy$ has no elementary antiderivative, so the given order is a dead end.
2. Describe the region: $0\le x\le 1$ and $x\le y\le 1$, which is the triangle below $y=1$ and above $y=x$.
3. Re-describe it with $y$ outside: $0\le y\le 1$ and $0\le x\le y$.
4. Rewrite: $\displaystyle\int_{0}^{1}\int_{0}^{y}e^{y^{2}}\,dx\,dy = \int_{0}^{1}y\,e^{y^{2}}\,dy$.
5. Now $u = y^2$ works: $\left[\frac{1}{2}e^{y^{2}}\right]_{0}^{1}$.
6. Result: $\dfrac{e-1}{2}$.

Sketching the region in step 2 is not optional; the new limits cannot be read off the old ones by symbol shuffling.

**Change of variables.** With $x=g(u,v)$, $y=h(u,v)$,
$$\iint_{R}f(x,y)\,dA = \iint_{S}f\left(g,h\right)\left\lvert\frac{\partial(x,y)}{\partial(u,v)}\right\rvert du\,dv,$$
where the Jacobian is $\left\lvert\begin{smallmatrix}x_u & x_v\\ y_u & y_v\end{smallmatrix}\right\rvert$.

**The three standard coordinate systems and their factors.**

| System | Substitution | Area/volume element |
| :--- | :--- | :--- |
| Polar | $x=r\cos\theta$, $y=r\sin\theta$ | $r\,dr\,d\theta$ |
| Cylindrical | $x=r\cos\theta$, $y=r\sin\theta$, $z=z$ | $r\,dr\,d\theta\,dz$ |
| Spherical | $x=\rho\sin\phi\cos\theta$, $y=\rho\sin\phi\sin\theta$, $z=\rho\cos\phi$ | $\rho^{2}\sin\phi\,d\rho\,d\phi\,d\theta$ |

Forgetting the $r$ or the $\rho^2\sin\phi$ is the defining error of this technique.

**Example (polar).** Evaluate $\displaystyle\iint_{x^{2}+y^{2}\le1}\sqrt{x^{2}+y^{2}}\,dA$.

1. The region is a disk and the integrand depends only on distance, so polar is indicated.
2. Convert: $\sqrt{x^2+y^2} = r$, and $dA = r\,dr\,d\theta$.
3. Set limits: $0\le r\le1$, $0\le\theta\le2\pi$.
4. Integrate: $\displaystyle\int_{0}^{2\pi}\!\!\int_{0}^{1}r\cdot r\,dr\,d\theta = \int_{0}^{2\pi}\frac{1}{3}\,d\theta$.
5. Result: $\dfrac{2\pi}{3}$.

**The Gaussian integral**, which is a single integral solved by going up to two dimensions.

1. Let $I = \int_{-\infty}^{\infty}e^{-x^{2}}dx$; no elementary antiderivative exists.
2. Square it and rename the second variable: $I^{2} = \iint_{\mathbb{R}^{2}}e^{-\left(x^{2}+y^{2}\right)}dA$.
3. Convert to polar: $\displaystyle\int_{0}^{2\pi}\!\!\int_{0}^{\infty}e^{-r^{2}}r\,dr\,d\theta$.
4. The $r$ from the Jacobian is exactly the factor that makes the inner integral elementary: $\int_0^\infty re^{-r^2}dr = \frac12$.
5. So $I^{2} = 2\pi\cdot\frac12 = \pi$, and $I = \sqrt{\pi}$.

---

## I22. Vector-calculus shortcuts

**Trigger.** A line or surface integral where a theorem replaces the parametrization with an easier one.

**Line integral, by parametrization.** $\displaystyle\int_{C}f\,ds = \int_{a}^{b}f\left(\mathbf{r}(t)\right)\lVert\mathbf{r}'(t)\rVert\,dt$.

**Fundamental theorem for line integrals.** If $\mathbf{F} = \nabla f$ (conservative), then $\displaystyle\int_{C}\mathbf{F}\cdot d\mathbf{r} = f(\text{end}) - f(\text{start})$, and the path is irrelevant.
Test for conservativeness in the plane: $P_y = Q_x$.

**Green's theorem** converts a closed line integral into a double integral:
$$\oint_{C}P\,dx+Q\,dy = \iint_{D}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA.$$

**Example.** Evaluate $\displaystyle\oint_{C}\left(y^{2}\,dx + 3xy\,dy\right)$ around the unit circle, counterclockwise.

1. Parametrizing directly gives a messy trig integral, so apply Green's theorem.
2. Identify $P = y^2$ and $Q = 3xy$.
3. Compute the integrand: $Q_x - P_y = 3y - 2y = y$.
4. So the answer is $\displaystyle\iint_{D}y\,dA$ over the unit disk.
5. The disk is symmetric about $y=0$ and $y$ is odd in $y$, so by symmetry (I13) the value is $0$.

**Stokes' theorem** ($\oint_C\mathbf{F}\cdot d\mathbf{r} = \iint_S(\nabla\times\mathbf{F})\cdot d\mathbf{S}$) and the **divergence theorem** ($\iint_S\mathbf{F}\cdot d\mathbf{S} = \iiint_E\nabla\cdot\mathbf{F}\,dV$) are the same trade in higher dimensions: swap a hard integral over a boundary for an easier one over the interior, or the reverse.

**Example (divergence theorem).** For $\mathbf{F} = \langle x,y,z\rangle$ over the unit sphere: $\nabla\cdot\mathbf{F} = 3$, so the flux is $3\cdot\text{Vol} = 3\cdot\frac{4\pi}{3} = 4\pi$, with no surface integral computed at all.

---

# Part 4 - MATH265 Exam Questions: Precalculus, Sketching, Optimization, and Integration Applications

Parts 1-3 above weave individual **MATH265 exam question** examples into the technique that solves them.
That covers every exam question whose subject is a limit, a derivative, or an integral technique proper.
The questions below don't fit that technique-catalog shape - they are precalculus foundations, graph transformations, sketching-from-conditions, and the applied optimization/integration word problems - so they are carried over verbatim from the course question bank at `MATH265.md` (Part 5: every exam question, restated and solved), grouped the same way that file groups them.

`Q19.1` (area between a line and a parabola) and `Q19.3` (net change, water flowing from a tank) already appear above as worked examples under **I15. The Fundamental Theorem of Calculus, part 2**, so they are not repeated here.

## 1. Functions and precalculus foundations

### Q1.1 - Exact value of a cosine

**Question.**
Give the exact value of $\cos\left(-\dfrac{\pi}{12}\right)$.

**Step 1: kill the minus sign.**
Cosine is even, so $\cos(-x) = \cos x$.

$$\cos\left(-\frac{\pi}{12}\right) = \cos\left(\frac{\pi}{12}\right)$$

**Step 2: recognise the angle.**
$\dfrac{\pi}{12} = 15^\circ$, which is not one of the five memorized angles, but it is $45^\circ - 30^\circ$.

**Step 3: apply the cosine difference formula.**
The formula is $\cos(A - B) = \cos A\cos B + \sin A\sin B$.
Note the sign flips: a minus inside gives a plus outside.

$$\cos\left(\frac{\pi}{4} - \frac{\pi}{6}\right) = \cos\frac{\pi}{4}\cos\frac{\pi}{6} + \sin\frac{\pi}{4}\sin\frac{\pi}{6}$$

**Step 4: substitute the five memorized values.**

$$= \frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2} + \frac{\sqrt2}{2}\cdot\frac{1}{2} = \frac{\sqrt6}{4} + \frac{\sqrt2}{4}$$

**Step 5: combine over one denominator.**

**Answer.**

$$\cos\left(-\frac{\pi}{12}\right) = \frac{\sqrt6 + \sqrt2}{4} \approx 0.9659258263$$

**Möbius:** `(sqrt(6)+sqrt(2))/4`

**Trap.** Typing `sqrt(6)+sqrt(2)/4` parses as $\sqrt6 + \dfrac{\sqrt2}{4} \approx 2.80$, which is not even in range for a cosine. Bracket the whole numerator.

### Q1.2 - Composite functions and their domains

**Question.**
Let $f(x) = 2x^{2} - 5$ and $g(x) = \dfrac{x+5}{2x-9}$.
Find the composite functions and their domains.

- a. $f\big(g(x)\big)$
- b. $g\big(f(x)\big)$

**Part a, step 1: substitute $g$ into $f$.**
Everywhere $f$ has an $x$, write the whole of $g(x)$.

$$f\big(g(x)\big) = 2\left(\frac{x+5}{2x-9}\right)^{2} - 5$$

**Part a, step 2: expand if you want a single fraction.**

$$= \frac{2(x+5)^{2}}{(2x-9)^{2}} - 5 = \frac{2(x+5)^{2} - 5(2x-9)^{2}}{(2x-9)^{2}}$$

**Part a, step 3: the domain.**
The domain of a composite keeps the restrictions of the inner function *and* of the result.
Here $g$ needs $2x - 9 \neq 0$, and $f$ itself restricts nothing because a polynomial accepts every real number.

$$2x - 9 \neq 0 \implies x \neq \frac{9}{2}$$

**Answer a.**

$$f\big(g(x)\big) = 2\left(\frac{x+5}{2x-9}\right)^{2} - 5, \qquad \text{domain } \left(-\infty, \tfrac{9}{2}\right)\cup\left(\tfrac{9}{2}, \infty\right)$$

**Möbius:** `2*((x+5)/(2*x-9))^2-5`, domain `x != 9/2`

**Part b, step 1: substitute $f$ into $g$.**

$$g\big(f(x)\big) = \frac{\left(2x^{2}-5\right)+5}{2\left(2x^{2}-5\right)-9}$$

**Part b, step 2: simplify.**
The numerator collapses because $-5 + 5 = 0$, and the denominator is $4x^{2} - 10 - 9$.

$$= \frac{2x^{2}}{4x^{2}-19}$$

**Part b, step 3: the domain.**
The inner function $f$ is a polynomial, so it restricts nothing.
The result needs a non-zero denominator.

$$4x^{2} - 19 \neq 0 \implies x^{2} \neq \frac{19}{4} \implies x \neq \pm\frac{\sqrt{19}}{2}$$

**Answer b.**

$$g\big(f(x)\big) = \frac{2x^{2}}{4x^{2}-19}, \qquad \text{domain } x \neq \pm\frac{\sqrt{19}}{2}$$

**Möbius:** `2*x^2/(4*x^2-19)`, domain `x != sqrt(19)/2 and x != -sqrt(19)/2`

**Trap.** The numerator simplifying to $2x^{2}$ tempts you to say the domain is all reals. It is not: the *denominator* still bans $\pm\dfrac{\sqrt{19}}{2}$.

### Q1.3 - Which equations define a function of x

**Question.**
Determine which of the following equations are well defined functions with independent variable $x$, and explain.

- a. $\dfrac{2y}{x^{2} - 3\lvert x\rvert} = 1$
- b. $y^{2} + x^{2} = 10$

**Part a, step 1: solve for $y$.**
Multiply both sides by the denominator.

$$2y = x^{2} - 3\lvert x\rvert \implies y = \frac{x^{2} - 3\lvert x\rvert}{2}$$

**Part a, step 2: test the definition.**
Each $x$ now produces exactly one $y$, because the right-hand side is a single arithmetic expression with no $\pm$.
So this **is** a function.

**Part a, step 3: state the domain.**
The original equation had a denominator, and that restriction survives.

$$x^{2} - 3\lvert x\rvert = 0 \implies \lvert x\rvert\big(\lvert x\rvert - 3\big) = 0 \implies x = 0,\ x = 3,\ x = -3$$

**Answer a.**
Yes, it is a function of $x$:

$$y = \frac{x^{2} - 3\lvert x\rvert}{2}, \qquad \text{domain } x \neq 0,\ x \neq \pm 3$$

**Möbius:** `(x^2-3*abs(x))/2`, domain `x != 0, x != 3, x != -3`

**Part b, step 1: solve for $y$.**

$$y^{2} = 10 - x^{2} \implies y = \pm\sqrt{10 - x^{2}}$$

**Part b, step 2: test the definition.**
The $\pm$ is fatal.
At $x = 1$ the equation gives both $y = 3$ and $y = -3$, so one input has two outputs.

**Part b, step 3: the graphical reason.**
$x^{2} + y^{2} = 10$ is a circle of radius $\sqrt{10}$ centred at the origin, and a vertical line through $x = 1$ cuts it twice, so it fails the vertical line test.

**Answer b.**
No, it is **not** a function of $x$, because $y = \pm\sqrt{10-x^{2}}$ assigns two values of $y$ to each $x$ in $\left(-\sqrt{10}, \sqrt{10}\right)$.

**Möbius:** not a function; the relation is `x^2+y^2=10`, a circle of radius `sqrt(10)`

### Q1.4 - Volume of a cone as a function of its radius

**Question.**
A cone has height double its radius, so $h = 2r$.
The volume of a cone is $V = \dfrac{\pi r^{2}h}{3}$.

- a. Express $V$ as a function of $r$.
- b. Find the domain.
- c. Compute $V$ for $r = 3$.

**Part a, step 1: write the constraint.**
"Height is double the radius" is $h = 2r$.

**Part a, step 2: eliminate $h$.**
Substitute $h = 2r$ into the volume formula, so only $r$ remains.

$$V(r) = \frac{\pi r^{2}(2r)}{3} = \frac{2\pi r^{3}}{3}$$

**Answer a.**

$$V(r) = \frac{2\pi r^{3}}{3}$$

**Möbius:** `2*pi*r^3/3`

**Part b: the domain.**
Algebraically $\dfrac{2\pi r^{3}}{3}$ accepts every real number, but a radius is a physical length.
A cone with radius $0$ or negative radius is not a cone, so the model requires a strictly positive radius.

**Answer b.**

$$r > 0, \qquad \text{that is } (0, \infty)$$

**Möbius:** `r>0`

**Part c: evaluate at $r = 3$.**

$$V(3) = \frac{2\pi (3)^{3}}{3} = \frac{2\pi \cdot 27}{3} = 18\pi$$

**Answer c.**

$$V(3) = 18\pi \approx 56.55\ \text{cubic units}$$

**Möbius:** `18*pi`

**Trap.** Leaving the answer as $\dfrac{54\pi}{3}$ is unsimplified, and answering $56.55$ when the question did not ask for a decimal throws away the exact form.

---

## 2. Graph transformations

### Q2.1 - Graph a shifted parabola by transformations

**Question.**
Give a labeled graph of $g(x) = 3(x+4)^{2}$ by starting from a basic function and applying transformations, explaining the procedure.
No credit for any other method.

**Step 1: name the parent function.**

$$y = x^{2}$$

This is the basic parabola, vertex at $(0,0)$, opening upward, passing through $(\pm 1, 1)$ and $(\pm 2, 4)$.

**Step 2: match the general form.**
Compare against $y = a\,f\big(b(x-h)\big) + k$.

$$g(x) = 3(x+4)^{2} \quad\text{gives}\quad a = 3,\ b = 1,\ h = -4,\ k = 0$$

**Step 3: horizontal shift, first.**
$(x+4)$ means $h = -4$, so the graph moves **left 4**, not right.
The shift is inside the function, and inside operations run backwards.

$$y = x^{2} \longrightarrow y = (x+4)^{2}, \qquad \text{vertex } (0,0) \to (-4, 0)$$

**Step 4: vertical stretch, second.**
The factor $a = 3$ is outside, so it multiplies every output by 3.
This makes the parabola three times steeper, and it does **not** move the vertex, because $3 \times 0 = 0$.

$$y = (x+4)^{2} \longrightarrow y = 3(x+4)^{2}$$

**Step 5: no reflection and no vertical shift.**
$a = 3$ is positive, so nothing flips.
$k = 0$, so nothing moves up or down.

**Answer.**
Order of transformations: **shift left 4, then stretch vertically by 3.**

Key points to label on the sketch:

$$\text{vertex } (-4, 0), \qquad (-3, 3), \qquad (-5, 3), \qquad (-2, 12), \qquad (-6, 12)$$

The curve opens upward, is symmetric about the vertical line $x = -4$, and its axis of symmetry should be drawn and labeled.

**Möbius:** vertex `(-4,0)`, axis of symmetry `x=-4`, function `3*(x+4)^2`

**Trap.** Shifting right 4 because the sign says $+4$. Set the bracket to zero: $x + 4 = 0$ gives $x = -4$, which is where the vertex lands.

### Q2.2 - Graph a reflected absolute value by transformations

**Question.**
State the transformations, in order, applied to the basic graph of $\lvert x\rvert$ to obtain $f(x) = -3\lvert x-2\rvert$, then sketch.
No credit for any other method.

**Step 1: name the parent function.**

$$y = \lvert x\rvert$$

A V shape with its corner at $(0,0)$, slope $-1$ on the left and $+1$ on the right.

**Step 2: match the general form.**

$$f(x) = -3\lvert x - 2\rvert \quad\text{gives}\quad a = -3,\ b = 1,\ h = 2,\ k = 0$$

**Step 3: horizontal shift, first.**
$(x - 2)$ means $h = +2$, so the graph moves **right 2**.

$$y = \lvert x\rvert \longrightarrow y = \lvert x - 2\rvert, \qquad \text{corner } (0,0) \to (2, 0)$$

**Step 4: vertical stretch by 3, second.**
The magnitude of $a$ is $3$, so outputs triple and the V becomes narrower.

$$y = \lvert x-2\rvert \longrightarrow y = 3\lvert x-2\rvert$$

**Step 5: reflection in the $x$-axis, third.**
The sign of $a$ is negative, so the whole graph flips over the $x$-axis and the V now opens **downward**.

$$y = 3\lvert x-2\rvert \longrightarrow y = -3\lvert x-2\rvert$$

**Step 6: no vertical shift.**
$k = 0$, so the corner stays on the $x$-axis.

**Answer.**
Order: **shift right 2, stretch vertically by 3, reflect in the $x$-axis.**

Key points to label:

$$\text{corner } (2, 0), \qquad (1, -3), \qquad (3, -3), \qquad (0, -6), \qquad (4, -6)$$

The corner at $(2,0)$ is the **maximum**, the arms have slopes $+3$ on the left and $-3$ on the right, and the function is continuous everywhere but not differentiable at $x = 2$.

**Möbius:** corner `(2,0)`, function `-3*abs(x-2)`

**Trap.** Reflecting before stretching gives the same picture here, but reflecting before *shifting* does not. Always do the inside horizontal move first.

---

## 5. Graphical interpretation and sketching from conditions

These three questions are marked on the *features* of your sketch, so the answer below lists exactly what a marker looks for.

### Q5.1 - Sketch a function from four conditions

**Question.**
Sketch the graph of a single function $f(x)$ satisfying all of:

- $\displaystyle\lim_{x\to 0}f(x)$ does not exist
- $f(0) = 0$
- $\displaystyle\lim_{x\to\infty}f(x) = -1$
- $f$ is not differentiable at $x = -2$

**Condition 1: the limit at 0 does not exist.**
Meaning: the left and right pieces approach different heights, so the graph **jumps** at $x = 0$.
Draw a jump discontinuity: for instance the left piece rising to an open circle at $(0, 2)$ and the right piece starting at an open circle at $(0, -3)$.

**Condition 2: $f(0) = 0$.**
Meaning: despite the jump, the function *is* defined at $0$, and its value is exactly $0$.
Draw a **filled dot at the origin** $(0,0)$, sitting on neither branch.
This is the condition students drop; the two open circles need a third, solid point at $(0,0)$.

**Condition 3: $\displaystyle\lim_{x\to\infty}f(x) = -1$.**
Meaning: far to the right the graph flattens onto the horizontal line $y = -1$.
Draw the dashed asymptote $y = -1$ and have the right branch approach it without crossing repeatedly.

**Condition 4: not differentiable at $x = -2$.**
Meaning: the graph exists there but has no single tangent.
The cheapest legal choice is a **sharp corner** at $x = -2$, like the vertex of a V.
A cusp or a vertical tangent would also satisfy it; a hole or jump would too, but a corner is easiest to draw convincingly.

**Answer: the checklist your sketch must show.**

$$\text{jump at } x=0; \quad \text{solid dot } (0,0); \quad \text{dashed } y=-1 \text{ as } x\to\infty; \quad \text{corner at } x=-2$$

**Möbius:** sketch question, no typed answer; the four features above are the marks.

**Trap.** Making $x = -2$ a hole *and* calling it non-differentiable is technically fine but weaker, since a marker wants to see you know a corner is continuous-but-not-differentiable.

### Q5.2 - Interpret five conditions, then sketch

**Question.**
Interpret each condition in terms of the graph of $f$, then sketch one function satisfying all of them.

- a. $\displaystyle\lim_{x\to\infty}f(x) = 3$
- b. $f(0) = 0$
- c. $\displaystyle\lim_{x\to -1}f(x) = 2$
- d. $\displaystyle\lim_{x\to 1}f(x) = \infty$
- e. $f$ is continuous but not differentiable at $x = 0$

**Interpretation a.**
As $x$ grows without bound the outputs settle at height $3$.
Graphically: a **horizontal asymptote** $y = 3$ on the right.

**Interpretation b.**
The graph passes through the origin.
Graphically: the point $(0, 0)$ is on the curve.

**Interpretation c.**
Approaching $x = -1$ from either side the outputs approach $2$.
Note the condition says nothing about $f(-1)$ itself, so the point may be filled at $(-1,2)$, or a hole with the actual value elsewhere.
Graphically: the curve funnels to height $2$ at $x = -1$.

**Interpretation d.**
As $x$ approaches $1$ the outputs increase without bound on both sides.
Graphically: a **vertical asymptote** $x = 1$, with the curve going to $+\infty$ on *both* sides.

**Interpretation e.**
Continuous at $0$ means no break, so the limit exists and equals $f(0) = 0$.
Not differentiable means no unique tangent line there.
Graphically: a **corner** at the origin, like $\lvert x\rvert$.

**Answer: the checklist your sketch must show.**

$$\text{dashed } y=3 \text{ on the right}; \quad \text{through } (0,0) \text{ with a corner}; \quad \text{value } 2 \text{ at } x=-1; \quad \text{dashed } x=1 \text{ with } +\infty \text{ both sides}$$

A workable shape: a V-corner at the origin, the left arm passing through height $2$ at $x = -1$, the branch just left of $x=1$ climbing to $+\infty$, and a separate branch for $x > 1$ dropping from $+\infty$ and flattening onto $y = 3$.

**Möbius:** sketch question; the five interpretations above are the marks.

**Trap.** Condition d says $\infty$, not $-\infty$ and not "does not exist", so **both** sides must go up. Drawing a sign change at $x=1$ contradicts the condition.

### Q5.3 - Interpret six conditions, then sketch

**Question.**
Give the graphical interpretation of each, then sketch $f(x)$.

- a. $f(0) = -3$
- b. $\displaystyle\lim_{x\to\infty}f(x) = -2$
- c. $\displaystyle\lim_{x\to 3}f(x) = \infty$
- d. $f'(x) < 0$ on $[3, \infty)$
- e. $f'(x) < 0$ on $(-\infty, -2)$
- f. $f''(x) > 0$ on $[4, \infty)$

**Interpretation a.**
The curve passes through $(0, -3)$.

**Interpretation b.**
Far to the right the curve levels off at height $-2$: a horizontal asymptote $y = -2$.

**Interpretation c.**
At $x = 3$ the outputs blow up to $+\infty$ from both sides: a vertical asymptote $x = 3$, upward on both sides.

**Interpretation d.**
On $[3,\infty)$ the function is **decreasing**.
Combined with c and b, the branch to the right of $x = 3$ starts at $+\infty$ and falls, levelling onto $y = -2$.

**Interpretation e.**
On $(-\infty, -2)$ the function is also **decreasing**, so on the far left the curve falls as you read left to right.

**Interpretation f.**
On $[4,\infty)$ the curve is **concave up**, holding water.
This is consistent with d: a decreasing, concave-up branch flattens onto its asymptote from above, which is exactly how it must meet $y=-2$.

**Step: check the conditions are consistent.**
Right branch: decreasing from $+\infty$ (d), concave up from $x=4$ on (f), approaching $y=-2$ (b). These agree.
Nothing is said about $f'$ on $(-2, 3)$, so you are free there, which is where you route the curve through $(0,-3)$ (a) and up to the asymptote at $x=3$ (c).

**Answer: the checklist your sketch must show.**

$$\text{through } (0,-3); \quad \text{dashed } y=-2; \quad \text{dashed } x=3 \text{ with } +\infty \text{ both sides}$$

$$\text{falling on } (-\infty,-2) \text{ and on } [3,\infty); \quad \text{concave up on } [4,\infty)$$

A workable shape: on the far left the curve falls toward a local minimum near $x = -2$, rises through $(0,-3)$ and continues up to $+\infty$ as $x \to 3^{-}$; on the right of $x=3$ it comes down from $+\infty$, decreasing throughout, and flattens onto $y = -2$ from above, curving upward from $x = 4$ on.

**Möbius:** sketch question; the six interpretations above are the marks.

**Trap.** Approaching $y=-2$ from *below* on the right. That branch is decreasing and concave up, so it must sit **above** $-2$ and settle down onto it.

---
## 6. Rates of change - interpretation

### Q6.1 - Average and instantaneous rate of population change

**Question.**
The population $P$ of a city in year $y$ is $P(y)$.
Write a sentence in layman's terms explaining the meaning of:

- a. $\dfrac{P(15) - P(2)}{13} = 1431$
- b. $P'(10) = 14000$

**Part a, step 1: recognise the structure.**
This is $\dfrac{\Delta P}{\Delta y}$, a change in population divided by a change in years.
The denominator $13$ is exactly $15 - 2$, so this is a slope between two points on the population curve.

**Part a, step 2: name it.**
A slope between two separated points is the **average rate of change**, the slope of the secant line.

**Part a, step 3: attach units.**
Population divided by years gives people per year.

**Answer a.**
Between year 2 and year 15, the city's population grew by an average of $1{,}431$ people per year.
That is the average over the whole 13-year stretch, so it says nothing about any single year; the population might have surged in some years and shrunk in others and still average this.

**Möbius:** average rate of change `= 1431` people per year over `[2,15]`

**Part b, step 1: recognise the structure.**
The prime is a derivative evaluated at one instant, not a difference over an interval.

**Part b, step 2: name it.**
This is the **instantaneous rate of change** at year 10, the slope of the tangent line to the population curve there.

**Answer b.**
In year 10, the city's population was growing at a rate of $14{,}000$ people per year at that instant.
It is the growth rate at that moment, so if the city kept growing at exactly that pace for a full year it would add about $14{,}000$ people, but the actual increase over that year may differ because the rate itself keeps changing.

**Möbius:** instantaneous rate of change `= 14000` people per year at `y=10`

**Trap.** Saying "the population increased by 14,000 in year 10". A derivative is a rate, not a total. Part a is an actual average over 13 years; part b is a speed at a single instant.

---

## 9. Tangent lines

### Q9.1 - Tangent line perpendicular to a given line

**Question.**
Find the values of $x$ where the tangent line to $f(x) = 3x^{2}+4x-3$ is perpendicular to the line $y = 6x+2$.

**Step 1: read the slope of the given line.**
In $y = mx+b$ form, $m = 6$.

**Step 2: convert perpendicular into a number.**
Perpendicular slopes are negative reciprocals, so the tangent must have slope

$$m_{\perp} = -\frac{1}{6}$$

**Step 3: the tangent slope is the derivative.**

$$f'(x) = 6x+4$$

**Step 4: set the derivative equal to the required slope.**
This is the equation the question is really asking you to solve.

$$6x + 4 = -\frac{1}{6}$$

**Step 5: solve.**

$$6x = -\frac{1}{6} - 4 = -\frac{1}{6} - \frac{24}{6} = -\frac{25}{6}$$

$$x = -\frac{25}{36}$$

**Answer.**

$$x = -\frac{25}{36} \approx -0.6944$$

**Möbius:** `-25/36`

**Check.** $f'\left(-\dfrac{25}{36}\right) = 6\left(-\dfrac{25}{36}\right)+4 = -\dfrac{25}{6}+\dfrac{24}{6} = -\dfrac{1}{6}$, and $6 \times \left(-\dfrac{1}{6}\right) = -1$, which confirms perpendicularity.

**Trap.** Setting $f'(x) = 6$, which finds where the tangent is **parallel** to the line, not perpendicular. The question asks for the negative reciprocal.

---

## 13. Newton's method

### Q13.1 - Approximate a root with Newton's method

**Question.**
Use Newton's method to approximate the solution of

$$x^{4} + 2x - 5 = 0 \quad\text{in } [1, 2]$$

**Step 1: confirm a root exists in the interval.**
Check the sign change, which is the Intermediate Value Theorem justification.

$$f(1) = 1 + 2 - 5 = -2, \qquad f(2) = 16 + 4 - 5 = 15$$

The sign changes from negative to positive, and $f$ is continuous, so a root lies in $(1,2)$.

**Step 2: write the derivative and the iteration formula.**

$$f'(x) = 4x^{3} + 2$$

$$x_{n+1} = x_{n} - \frac{f(x_{n})}{f'(x_{n})} = x_{n} - \frac{x_{n}^{4} + 2x_{n} - 5}{4x_{n}^{3} + 2}$$

**Step 3: choose a starting value.**
Take $x_{0} = 1$, an endpoint of the given interval.

**Step 4: iterate, keeping all decimals.**

$$x_{1} = 1 - \frac{-2}{6} = 1 + \frac{1}{3} = 1.333333333$$

$$x_{2} = 1.333333333 - \frac{f(1.333333333)}{f'(1.333333333)} = 1.261290323$$

$$x_{3} = 1.255964749$$

$$x_{4} = 1.255937549$$

$$x_{5} = 1.255937548$$

**Step 5: stop when the digits stop moving.**
$x_{4}$ and $x_{5}$ agree to eight decimal places, so the method has converged.

**Answer.**

$$x \approx 1.2559$$

To more places, $x \approx 1.255937548$.

**Möbius:** `1.2559`

**Check.** $f(1.255937548) \approx 0$ to eleven decimal places, and $1.2559$ lies inside $[1,2]$ as required.

**Trap.** Rounding to four decimals *between* iterations. Newton's method converges by doubling correct digits each step, and rounding early throws that away. Keep the full display and round only the final answer.

---

## 14. Curve sketching with calculus

### Q14.1 - Sketch two curves with a full calculus analysis

**Question.**
Sketch each graph, stating all critical points, cusps, vertical asymptotes and points of inflection.

- a. $f(x) = \dfrac{x^{2}}{x^{2}-1}$
- b. $f(x) = x + \sin x$

**Part a, step 1: domain and vertical asymptotes.**

$$x^{2} - 1 = 0 \implies x = \pm 1$$

Neither factor cancels, so both are genuine vertical asymptotes.

$$\text{Domain: } x \neq \pm 1$$

**Part a, step 2: horizontal asymptote.**
Equal degrees, so take the ratio of leading coefficients.

$$\lim_{x\to\pm\infty}\frac{x^{2}}{x^{2}-1} = 1 \implies y = 1$$

**Part a, step 3: first derivative, by the quotient rule.**

$$f'(x) = \frac{2x\left(x^{2}-1\right) - x^{2}(2x)}{\left(x^{2}-1\right)^{2}} = \frac{2x^{3}-2x-2x^{3}}{\left(x^{2}-1\right)^{2}} = \frac{-2x}{\left(x^{2}-1\right)^{2}}$$

**Part a, step 4: critical points.**
$f'(x) = 0$ requires $-2x = 0$, so $x = 0$.
$f'$ is undefined at $x = \pm 1$, but $f$ is undefined there too, so those are asymptotes, not critical points.

$$f(0) = \frac{0}{-1} = 0 \implies \text{critical point } (0,0)$$

**Part a, step 5: classify it.**
The denominator $\left(x^{2}-1\right)^{2}$ is always positive, so the sign of $f'$ is the sign of $-2x$.

$$f' > 0 \text{ for } x < 0, \qquad f' < 0 \text{ for } x > 0$$

Increasing then decreasing, so $(0,0)$ is a **local maximum**.

**Part a, step 6: second derivative.**

$$f''(x) = \frac{6x^{2}+2}{\left(x^{2}-1\right)^{3}}$$

**Part a, step 7: inflection points.**
An inflection needs $f'' = 0$ with a sign change.

$$6x^{2} + 2 = 0 \implies x^{2} = -\frac{1}{3}$$

This has **no real solution**, so the numerator never vanishes.

$$\textbf{There are no points of inflection.}$$

Concavity is decided entirely by the denominator: $f'' > 0$ when $\lvert x\rvert > 1$ (concave up) and $f'' < 0$ when $\lvert x\rvert < 1$ (concave down).
The sign does change across $x = \pm 1$, but those are not inflection points because $f$ is not defined there.

**Answer a.**

$$\text{Vertical asymptotes } x = -1,\ x = 1; \quad \text{horizontal asymptote } y = 1$$

$$\text{Critical point } (0,0), \text{ a local maximum}; \quad \text{no cusps}; \quad \text{no inflection points}$$

Shape: three branches. The outer two sit above $y=1$ and fall toward it as $\lvert x\rvert$ grows; the middle branch is a downward cap through $(0,0)$, dropping to $-\infty$ at both $x=-1^{+}$ and $x=1^{-}$.

**Möbius:** VA `x=-1, x=1`; HA `y=1`; critical point `(0,0)` local max; inflection points: `none`

**Part b, step 1: domain.**
$x + \sin x$ is defined for all real $x$; no asymptotes, no cusps.

**Part b, step 2: first derivative.**

$$f'(x) = 1 + \cos x$$

**Part b, step 3: critical points.**

$$1 + \cos x = 0 \implies \cos x = -1 \implies x = \pi + 2k\pi, \quad k \in \mathbb{Z}$$

**Part b, step 4: classify them.**
Since $\cos x \ge -1$ always, $f'(x) = 1 + \cos x \ge 0$ **everywhere**.
So $f$ is increasing on all of $\mathbb{R}$ and never turns around.

$$\text{These are horizontal tangents, not maxima or minima.}$$

At $x = \pi$, $f(\pi) = \pi + 0 = \pi$, so $(\pi, \pi)$ is a critical point where the curve momentarily flattens and then keeps climbing.

**Part b, step 5: second derivative and inflection points.**

$$f''(x) = -\sin x$$

$$-\sin x = 0 \implies x = k\pi, \quad k \in \mathbb{Z}$$

The sign of $-\sin x$ genuinely alternates across each $k\pi$, so **every** $x = k\pi$ is an inflection point.

$$f(k\pi) = k\pi + \sin(k\pi) = k\pi \implies \text{inflection points } (k\pi,\ k\pi)$$

Every inflection point lies exactly on the line $y = x$.

**Part b, step 6: concavity.**
$f'' = -\sin x > 0$ where $\sin x < 0$, that is on $(\pi, 2\pi)$ and its $2\pi$-translates: concave up.
Concave down on $(0, \pi)$ and its translates.

**Answer b.**

$$\text{No asymptotes, no cusps, no maxima or minima}$$

$$\text{Critical points at } x = \pi + 2k\pi \text{ (horizontal tangents on an increasing curve)}$$

$$\text{Inflection points at } (k\pi,\ k\pi) \text{ for every integer } k$$

Shape: a staircase-like curve rising forever, weaving around the line $y = x$, touching it at every multiple of $\pi$, with a flat spot at $x = \pi, 3\pi, 5\pi, \dots$

**Möbius:** critical points `x=pi+2*k*pi`; inflection points `(k*pi, k*pi)`; no asymptotes; increasing everywhere

**Trap.** Calling $x = \pi$ a local maximum because $f'(\pi) = 0$. The first derivative does not change sign there, so it is neither a max nor a min.

---

## 15. Extreme values and optimization

### Q15.1 - All maxima and minima on closed intervals

**Question.**
Find all maxima and minima on the indicated intervals.

- a. $f(x) = 2x^{5/3} - 5x^{4/3}$ on $[-1, 20]$
- b. $f(x) = x + \cos x$ on $[-\pi, 2\pi]$

**Part a, step 1: differentiate.**

$$f'(x) = \frac{10}{3}x^{2/3} - \frac{20}{3}x^{1/3}$$

**Part a, step 2: factor.**
Pull out the common $\dfrac{10}{3}x^{1/3}$.

$$f'(x) = \frac{10}{3}x^{1/3}\left(x^{1/3} - 2\right)$$

**Part a, step 3: find the critical numbers.**

$$x^{1/3} = 0 \implies x = 0$$

$$x^{1/3} = 2 \implies x = 8$$

Both lie in $[-1, 20]$.
Note $f'$ is defined everywhere here, since $x^{1/3}$ and $x^{2/3}$ accept negatives.

**Part a, step 4: evaluate at critical numbers and endpoints.**
For $x = -1$, use the real cube root: $(-1)^{1/3} = -1$, so $(-1)^{5/3} = -1$ and $(-1)^{4/3} = 1$.

$$f(-1) = 2(-1) - 5(1) = -7$$

$$f(0) = 0$$

$$f(8) = 2(32) - 5(16) = 64 - 80 = -16$$

$$f(20) = 2\cdot 20^{5/3} - 5\cdot 20^{4/3} \approx 294.72 - 271.44 = 23.28$$

**Part a, step 5: compare.**

**Answer a.**

$$\text{Absolute maximum } f(20) = 2\cdot 20^{5/3} - 5\cdot 20^{4/3} \approx 23.281 \text{ at } x = 20$$

$$\text{Absolute minimum } f(8) = -16 \text{ at } x = 8$$

Also present: a **local maximum** at $(0, 0)$, since $f$ rises on $[-1,0]$, falls on $[0,8]$, then rises again on $[8,20]$.

**Möbius:** max `2*20^(5/3)-5*20^(4/3)` at `x=20`; min `-16` at `x=8`

**Trap.** Treating $(-1)^{4/3}$ as undefined or negative. Read it as $\left((-1)^{1/3}\right)^{4} = (-1)^{4} = 1$; the even outer power makes it positive.

**Part b, step 1: differentiate.**

$$f'(x) = 1 - \sin x$$

**Part b, step 2: critical numbers.**

$$1 - \sin x = 0 \implies \sin x = 1 \implies x = \frac{\pi}{2} + 2k\pi$$

Within $[-\pi, 2\pi]$ the only such value is $x = \dfrac{\pi}{2}$.

**Part b, step 3: note the monotonicity.**
$\sin x \le 1$ always, so $f'(x) = 1 - \sin x \ge 0$ everywhere.
The function is **increasing** on the whole interval, touching slope zero only at $x = \dfrac{\pi}{2}$.
This already tells you the extremes must be the endpoints.

**Part b, step 4: evaluate.**

$$f(-\pi) = -\pi + \cos(-\pi) = -\pi - 1 \approx -4.1416$$

$$f\left(\frac{\pi}{2}\right) = \frac{\pi}{2} + 0 = \frac{\pi}{2} \approx 1.5708$$

$$f(2\pi) = 2\pi + \cos(2\pi) = 2\pi + 1 \approx 7.2832$$

**Answer b.**

$$\text{Absolute maximum } f(2\pi) = 2\pi + 1 \approx 7.283 \text{ at } x = 2\pi$$

$$\text{Absolute minimum } f(-\pi) = -\pi - 1 \approx -4.142 \text{ at } x = -\pi$$

The critical number $x = \dfrac{\pi}{2}$ gives neither: it is a horizontal tangent on a curve that keeps rising.

**Möbius:** max `2*pi+1` at `x=2*pi`; min `-pi-1` at `x=-pi`

### Q15.2 - Rectangle of least perimeter

**Question.**
Find the dimensions of the rectangle of area $220\ \text{cm}^{2}$ with the smallest perimeter, and give that perimeter.

**Step 1: name the variables and write both equations.**

$$\text{Constraint: } xy = 220 \qquad \text{Minimize: } P = 2x + 2y$$

**Step 2: use the constraint to eliminate one variable.**

$$y = \frac{220}{x} \implies P(x) = 2x + \frac{440}{x}, \qquad x > 0$$

**Step 3: differentiate.**

$$P'(x) = 2 - \frac{440}{x^{2}}$$

**Step 4: set to zero and solve.**

$$2 = \frac{440}{x^{2}} \implies x^{2} = 220 \implies x = \sqrt{220} = 2\sqrt{55}$$

Only the positive root is physical.

**Step 5: confirm it is a minimum.**

$$P''(x) = \frac{880}{x^{3}} > 0 \text{ for } x > 0$$

Concave up everywhere on the domain, so this critical point is the absolute minimum.

**Step 6: find the other dimension.**

$$y = \frac{220}{\sqrt{220}} = \sqrt{220} = 2\sqrt{55}$$

The rectangle is a **square**, which is the general result for fixed area and least perimeter.

**Step 7: compute the perimeter.**

$$P = 4\sqrt{220} = 8\sqrt{55}$$

**Answer.**

$$\text{Dimensions } 2\sqrt{55} \times 2\sqrt{55} \approx 14.83\ \text{cm} \times 14.83\ \text{cm}$$

$$\text{Minimum perimeter } 8\sqrt{55} \approx 59.33\ \text{cm}$$

**Möbius:** side `2*sqrt(55)`, perimeter `8*sqrt(55)`

**Trap.** Answering with the side length when the question also explicitly asks "What is the perimeter?". Both are marked.

### Q15.3 - Absolute extremes by the Extreme Value Theorem

**Question.**
Use the Extreme Value Theorem to find the absolute extreme values of

$$f(x) = \frac{1}{x^{2}+1} \quad\text{on } [-1, 1]$$

**Step 1: check the theorem applies.**
The Extreme Value Theorem needs a continuous function on a closed, bounded interval.
Here $x^{2} + 1 \ge 1 > 0$, so the denominator never vanishes and $f$ is continuous on all of $\mathbb{R}$, in particular on $[-1,1]$.
Therefore $f$ **attains** both an absolute maximum and an absolute minimum on $[-1,1]$.

**Step 2: differentiate.**
Write $f(x) = \left(x^{2}+1\right)^{-1}$ and use the chain rule.

$$f'(x) = -\left(x^{2}+1\right)^{-2}(2x) = \frac{-2x}{\left(x^{2}+1\right)^{2}}$$

**Step 3: find the critical numbers.**
The denominator is never zero, so $f'$ is defined everywhere.

$$-2x = 0 \implies x = 0$$

**Step 4: evaluate at the critical number and both endpoints.**

$$f(-1) = \frac{1}{2}, \qquad f(0) = \frac{1}{1} = 1, \qquad f(1) = \frac{1}{2}$$

**Step 5: compare.**

**Answer.**

$$\text{Absolute maximum } f(0) = 1 \text{ at } x = 0$$

$$\text{Absolute minimum } f(-1) = f(1) = \frac{1}{2} \text{ at both } x = -1 \text{ and } x = 1$$

**Möbius:** max `1` at `x=0`; min `1/2` at `x=-1` and `x=1`

**Note.** The minimum is attained at two points. Reporting only one endpoint is an incomplete answer.

### Q15.4 - Cheapest rectangular box

**Question.**
A rectangular box has base length twice its width and volume $120\ \text{cm}^{3}$.
Material costs \$1.20 per $\text{cm}^{2}$; the lid costs \$1.50 per $\text{cm}^{2}$.
Find the dimensions of the cheapest box and the minimum cost.

**Step 1: name the variables using the constraint immediately.**

$$\text{width } = w, \qquad \text{length } = 2w, \qquad \text{height } = h$$

**Step 2: write the volume constraint.**

$$V = (2w)(w)(h) = 2w^{2}h = 120 \implies h = \frac{60}{w^{2}}$$

**Step 3: itemise the surfaces, keeping the lid separate.**
This separation is the entire difficulty of the problem.

- base: $\;2w\cdot w = 2w^{2}$ square cm, charged at \$1.20

- four sides: $\;2(wh) + 2(2wh) = 6wh$ square cm, charged at \$1.20

- lid: $\;2w^{2}$ square cm, charged at \$1.50

**Step 4: write the cost function.**

$$C = 1.20\left(2w^{2} + 6wh\right) + 1.50\left(2w^{2}\right) = 2.4w^{2} + 7.2wh + 3w^{2} = 5.4w^{2} + 7.2wh$$

**Step 5: eliminate $h$.**

$$C(w) = 5.4w^{2} + 7.2w\cdot\frac{60}{w^{2}} = 5.4w^{2} + \frac{432}{w}, \qquad w > 0$$

**Step 6: differentiate and solve.**

$$C'(w) = 10.8w - \frac{432}{w^{2}} = 0 \implies 10.8w^{3} = 432 \implies w^{3} = 40$$

$$w = \sqrt[3]{40} = 2\sqrt[3]{5} \approx 3.4200$$

**Step 7: confirm it is a minimum.**

$$C''(w) = 10.8 + \frac{864}{w^{3}} > 0 \text{ for } w > 0$$

Concave up on the whole domain, so this is the absolute minimum.
Numerically $C''\left(\sqrt[3]{40}\right) = 32.4 > 0$.

**Step 8: recover the other dimensions.**

$$\text{length} = 2w = 2\sqrt[3]{40} \approx 6.8399$$

$$h = \frac{60}{w^{2}} = \frac{60}{40^{2/3}} = 3\sqrt[3]{5} \approx 5.1299$$

**Step 9: compute the minimum cost.**

$$C = 5.4\left(40^{2/3}\right) + \frac{432}{40^{1/3}} = \frac{324\sqrt[3]{25}}{5}$$

$$\approx 63.159 + 126.317 = 189.476$$

**Answer.**

$$\text{width } \sqrt[3]{40} \approx 3.42\ \text{cm}, \quad \text{length } 2\sqrt[3]{40} \approx 6.84\ \text{cm}, \quad \text{height } 3\sqrt[3]{5} \approx 5.13\ \text{cm}$$

Minimum cost: approximately \$189.48

**Möbius:** width `40^(1/3)`, length `2*40^(1/3)`, height `3*5^(1/3)`, cost `324*5^(2/3)/5` or `189.48`

**Trap.** Charging the lid at \$1.20 as well, or forgetting the base entirely. The box has a base at \$1.20, four sides at \$1.20, and a lid at \$1.50: six faces, two prices.

### Q15.5 - Absolute extremes of a function with a cusp

**Question.**
Find the absolute extreme values of

$$f(x) = \left(x^{2}+2x\right)^{2/3} \quad\text{on } [-2, 3]$$

**Step 1: differentiate with the chain rule.**

$$f'(x) = \frac{2}{3}\left(x^{2}+2x\right)^{-1/3}(2x+2) = \frac{2(2x+2)}{3\sqrt[3]{x^{2}+2x}}$$

**Step 2: critical numbers where $f' = 0$.**

$$2x + 2 = 0 \implies x = -1$$

**Step 3: critical numbers where $f'$ is undefined.**
The denominator vanishes when the inside is zero.

$$x^{2}+2x = 0 \implies x(x+2) = 0 \implies x = 0,\ x = -2$$

At these points $f$ **is** defined (it equals $0$) but $f'$ is not, so they are **cusps** and count as critical numbers.
This is the feature the question is built around.

**Step 4: evaluate at every critical number and both endpoints.**
Note the two-thirds power is $\left(\text{cube root}\right)^{2}$, so the result is never negative.

$$f(-2) = \left(4-4\right)^{2/3} = 0$$

$$f(-1) = \left(1-2\right)^{2/3} = (-1)^{2/3} = 1$$

$$f(0) = 0$$

$$f(3) = \left(9+6\right)^{2/3} = 15^{2/3} \approx 6.0822$$

**Step 5: compare.**

**Answer.**

$$\text{Absolute maximum } f(3) = 15^{2/3} \approx 6.082 \text{ at } x = 3$$

$$\text{Absolute minimum } 0, \text{ attained at both } x = -2 \text{ and } x = 0$$

There is also a **local maximum** of $1$ at $x = -1$, sitting between the two cusps.

**Möbius:** max `15^(2/3)` at `x=3`; min `0` at `x=-2` and `x=0`

**Trap.** Missing $x = 0$ and $x = -2$ because $f'$ is undefined there rather than zero. A critical number is any point where $f'$ is zero **or** undefined while $f$ is defined, and here those points supply the minimum.

---
## 17. Properties of the definite integral

All three of these use the same bounding property, so learn it once:

$$\text{if } m \le f(x) \le M \text{ on } [a,b], \text{ then } m(b-a) \le \int_{a}^{b}f(x)\,dx \le M(b-a)$$

### Q17.1 - Interval containing a secant integral

**Question.**
Use the properties of the integral to find an interval containing

$$\int_{0}^{\pi/3}\sec x\,dx$$

**Step 1: identify the interval and its width.**

$$[a,b] = \left[0, \frac{\pi}{3}\right], \qquad b - a = \frac{\pi}{3}$$

**Step 2: find the extreme values of $\sec x$ on that interval.**
On $\left[0, \dfrac{\pi}{3}\right]$, cosine decreases from $1$ to $\dfrac{1}{2}$, so its reciprocal $\sec x$ **increases** from $1$ to $2$.

$$\sec 0 = 1 \quad(\text{minimum}), \qquad \sec\frac{\pi}{3} = 2 \quad(\text{maximum})$$

The interval stops short of $\dfrac{\pi}{2}$, so $\sec x$ stays finite and this is legitimate.

**Step 3: apply the bounding property.**

$$1\cdot\frac{\pi}{3} \le \int_{0}^{\pi/3}\sec x\,dx \le 2\cdot\frac{\pi}{3}$$

**Answer.**

$$\frac{\pi}{3} \le \int_{0}^{\pi/3}\sec x\,dx \le \frac{2\pi}{3}$$

Numerically $1.047 \le I \le 2.094$.

**Möbius:** interval `[pi/3, 2*pi/3]`

**Verification.** The exact value is $\ln\left(2+\sqrt3\right) \approx 1.3170$, which does sit inside $[1.047, 2.094]$.

### Q17.2 - Estimate an integral from its properties

**Question.**
Use the properties of the definite integral to estimate

$$\int_{-1}^{1}\frac{1}{x^{2}+1}\,dx$$

**Step 1: identify the interval and its width.**

$$[a,b] = [-1,1], \qquad b-a = 2$$

The width is $2$, not $1$; this is the most common slip on this question.

**Step 2: find the extreme values of the integrand.**
This is the same function as Q15.3, so reuse that analysis.
$f(x) = \dfrac{1}{x^{2}+1}$ is largest where $x^{2}$ is smallest.

$$\text{maximum } f(0) = 1, \qquad \text{minimum } f(\pm 1) = \frac{1}{2}$$

**Step 3: apply the bounding property.**

$$\frac{1}{2}(2) \le \int_{-1}^{1}\frac{dx}{x^{2}+1} \le 1(2)$$

**Answer.**

$$1 \le \int_{-1}^{1}\frac{1}{x^{2}+1}dx \le 2$$

**Möbius:** interval `[1, 2]`

**Verification.** The exact value is $\arctan(1) - \arctan(-1) = \dfrac{\pi}{2} \approx 1.5708$, comfortably inside $[1,2]$.

### Q17.3 - Bound an integral from its properties

**Question.**
Use the properties of definite integrals to bound

$$\int_{-2}^{3}\left(x^{2}+2x\right)^{2/3}dx$$

**Step 1: identify the interval and its width.**

$$[a,b] = [-2,3], \qquad b-a = 5$$

**Step 2: find the extreme values of the integrand.**
This is exactly the function from Q15.5 on exactly that interval, so the work is already done.

$$\text{minimum } 0 \text{ at } x=-2 \text{ and } x=0, \qquad \text{maximum } 15^{2/3} \text{ at } x=3$$

**Step 3: apply the bounding property.**

$$0\cdot 5 \le \int_{-2}^{3}\left(x^{2}+2x\right)^{2/3}dx \le 15^{2/3}\cdot 5$$

**Answer.**

$$0 \le \int_{-2}^{3}\left(x^{2}+2x\right)^{2/3}dx \le 5\cdot 15^{2/3} \approx 30.41$$

**Möbius:** interval `[0, 5*15^(2/3)]`

**Verification.** The true value is about $10.67$, which lies inside $[0, 30.41]$.
The bound is loose because the integrand only reaches its maximum at the single right endpoint, which is normal for this method: it gives a guaranteed range, not a sharp estimate.

**Trap.** Concluding the lower bound is negative. The exponent $\dfrac{2}{3}$ is an even power of a cube root, so the integrand is never negative, and $0$ is the correct floor.

---

### Q19.2 - Area between a cosine and a horizontal line

**Question.**
Find the area between $y = \cos x$ and the horizontal line $y = \dfrac{1}{\sqrt2}$ on $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$.

**Step 1: find where the curves cross.**

$$\cos x = \frac{1}{\sqrt2} = \frac{\sqrt2}{2} \implies x = \pm\frac{\pi}{4}$$

Both crossings lie strictly inside the given interval, so the integral **must** be split.

**Step 2: decide which is on top in each piece.**
Test one point in each region.

$$x=0:\ \cos 0 = 1 > \tfrac{1}{\sqrt2} \implies \text{cosine on top on } \left(-\tfrac{\pi}{4}, \tfrac{\pi}{4}\right)$$

$$x=\tfrac{\pi}{2}:\ \cos\tfrac{\pi}{2} = 0 < \tfrac{1}{\sqrt2} \implies \text{line on top on } \left(\tfrac{\pi}{4}, \tfrac{\pi}{2}\right)$$

By symmetry the same holds on $\left(-\dfrac{\pi}{2}, -\dfrac{\pi}{4}\right)$.

**Step 3: write the total area as three integrals.**

$$A = \int_{-\pi/2}^{-\pi/4}\left(\tfrac{1}{\sqrt2}-\cos x\right)dx + \int_{-\pi/4}^{\pi/4}\left(\cos x - \tfrac{1}{\sqrt2}\right)dx + \int_{\pi/4}^{\pi/2}\left(\tfrac{1}{\sqrt2}-\cos x\right)dx$$

**Step 4: evaluate the middle piece.**
The antiderivative is $\sin x - \dfrac{x}{\sqrt2}$.

$$\left[\sin x - \frac{x}{\sqrt2}\right]_{-\pi/4}^{\pi/4} = \left(\frac{\sqrt2}{2} - \frac{\pi}{4\sqrt2}\right) - \left(-\frac{\sqrt2}{2} + \frac{\pi}{4\sqrt2}\right) = \sqrt2 - \frac{\pi}{2\sqrt2}$$

Numerically $1.41421 - 1.11072 = 0.30349$.

**Step 5: evaluate the right piece.**
The antiderivative is $\dfrac{x}{\sqrt2} - \sin x$.

$$\left[\frac{x}{\sqrt2}-\sin x\right]_{\pi/4}^{\pi/2} = \left(\frac{\pi}{2\sqrt2}-1\right) - \left(\frac{\pi}{4\sqrt2}-\frac{\sqrt2}{2}\right) = \frac{\pi}{4\sqrt2} - 1 + \frac{\sqrt2}{2}$$

Numerically $0.55536 - 1 + 0.70711 = 0.26247$.

**Step 6: the left piece equals the right by symmetry.**
Both $\cos x$ and the constant line are even, so the region is symmetric about the $y$-axis.

$$\text{left piece} = 0.26247$$

**Step 7: add all three.**
The $\pi$ terms cancel exactly between the middle and outer pieces.

$$A = \left(\sqrt2 - \frac{\pi}{2\sqrt2}\right) + 2\left(\frac{\pi}{4\sqrt2} - 1 + \frac{\sqrt2}{2}\right) = \sqrt2 + \sqrt2 - 2$$

**Answer.**

$$A = 2\sqrt2 - 2 \approx 0.8284 \text{ square units}$$

**Möbius:** `2*sqrt(2)-2`

**Note on reading the question.** Because an explicit interval $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$ is given, the answer is the **total** area over that whole interval, which is $2\sqrt2-2$.
If a version of this question instead asks only for the region **enclosed** by the two curves, that is the middle piece alone:

$$\sqrt2 - \frac{\pi}{2\sqrt2} = \sqrt2 - \frac{\pi\sqrt2}{4} \approx 0.3035$$

Read which one is wanted before you set up.

**Trap.** Integrating $\cos x - \dfrac{1}{\sqrt2}$ straight across $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$ without splitting. That returns $2 - \dfrac{\pi}{\sqrt2} \approx -0.221$, a signed value in which the outer negative regions cancel part of the middle positive region.

### Q19.4 - Work, raising one end of a chain

**Question.**
A chain lying on the ground is 10 m long with mass 80 kg.
Find the work required to raise one end to a height of 6 m.

**Step 1: find the linear density.**

$$\rho = \frac{80\ \text{kg}}{10\ \text{m}} = 8\ \text{kg/m}$$

**Step 2: picture the final configuration.**
Raising one end to 6 m lifts only the top 6 m of chain into the air; the remaining 4 m stays flat on the ground and is never lifted.
This is why the integral runs to 6, not to 10.

**Step 3: slice by final height.**
Let $y$ be the final height of a small piece, $0 \le y \le 6$.
The piece of chain that ends at height $y$ started on the ground, so it is lifted a distance $y$.

$$dm = \rho\,dy = 8\,dy$$

$$dW = (dm)g\,y = 8(9.8)y\,dy = 78.4\,y\,dy$$

**Step 4: integrate.**

$$W = \int_{0}^{6}78.4\,y\,dy = 78.4\left[\frac{y^{2}}{2}\right]_{0}^{6} = 78.4\cdot 18$$

**Answer.**

$$W = 1411.2\ \text{J}$$

**Möbius:** `1411.2` (using $g = 9.8$)

**Note.** With $g = 9.81$ the answer is $1412.64$ J. State which $g$ you used.

**Trap.** Integrating from $0$ to $10$, which treats the whole chain as lifted and gives $3920$ J. Only 6 m of chain leaves the ground.

### Q19.5 - Work, stretching a spring

**Question.**
$20$ ft-lb of work stretches a spring $1$ ft beyond its natural length.

- a. Find the spring constant.
- b. Find the work needed to stretch it $2$ ft beyond natural length.

**Part a, step 1: write Hooke's Law and the work integral.**

$$F(x) = kx, \qquad W = \int_{0}^{d}kx\,dx = \frac{1}{2}kd^{2}$$

**Part a, step 2: substitute the given data, $W = 20$ and $d = 1$.**

$$20 = \frac{1}{2}k(1)^{2} = \frac{k}{2}$$

**Part a, step 3: solve.**

$$k = 40$$

**Answer a.**

$$k = 40\ \text{lb/ft}$$

**Möbius:** `40`

**Part b, step 1: use the same formula with $d = 2$.**

$$W = \int_{0}^{2}40x\,dx = \left[20x^{2}\right]_{0}^{2} = 20(4)$$

**Answer b.**

$$W = 80\ \text{ft-lb}$$

**Möbius:** `80`

**Note.** Doubling the stretch **quadruples** the work, because $W \propto d^{2}$. Answering $40$ ft-lb by assuming proportionality is the trap this question is built to catch.

### Q19.6 - Average temperature of a metal rod

**Question.**
A rod 6 m long has temperature $3x$ degrees centigrade at distance $x$ metres from one end.
Find the average temperature.

**Step 1: write the average value formula.**

$$f_{\text{avg}} = \frac{1}{b-a}\int_{a}^{b}f(x)\,dx$$

**Step 2: identify the pieces.**

$$f(x) = 3x, \qquad [a,b] = [0,6], \qquad b-a = 6$$

**Step 3: integrate.**

$$\int_{0}^{6}3x\,dx = \left[\frac{3x^{2}}{2}\right]_{0}^{6} = \frac{3(36)}{2} = 54$$

**Step 4: divide by the width.**

$$f_{\text{avg}} = \frac{54}{6} = 9$$

**Answer.**

$$9\ ^\circ\text{C}$$

**Möbius:** `9`

**Sanity check.** The temperature runs linearly from $0$ at one end to $18$ at the other, and the average of a linear function is its midpoint value: $\dfrac{0+18}{2} = 9$. Confirmed.

### Q19.7 - Find k from an average value

**Question.**
Find a positive number $k$ such that the average value of $f(x) = \dfrac{5}{x^{2}}$ over the interval between $1$ and $k$ is $32$.

**Step 1: write the average value equation.**

$$\frac{1}{k-1}\int_{1}^{k}\frac{5}{x^{2}}dx = 32$$

**Step 2: integrate.**

$$\int_{1}^{k}5x^{-2}dx = \left[-\frac{5}{x}\right]_{1}^{k} = -\frac{5}{k} + 5 = 5\left(1 - \frac{1}{k}\right)$$

**Step 3: simplify the numerator into a single fraction.**
This is the step that makes the whole problem collapse.

$$5\left(\frac{k-1}{k}\right)$$

**Step 4: divide by the width and watch $(k-1)$ cancel.**

$$\frac{1}{k-1}\cdot\frac{5(k-1)}{k} = \frac{5}{k}$$

**Step 5: solve.**

$$\frac{5}{k} = 32 \implies k = \frac{5}{32}$$

**Answer.**

$$k = \frac{5}{32} = 0.15625$$

**Möbius:** `5/32`

**Note.** $k$ is positive, as required, but it is **less than 1**, so the interval is really $\left[\dfrac{5}{32}, 1\right]$.
The phrase "between 1 and $k$" allows this, and the algebra is identical either way: reversing the limits flips the sign of both the integral and the width, and the two flips cancel.

**Verification.** On $\left[\dfrac{5}{32}, 1\right]$, the average of $\dfrac{5}{x^{2}}$ is exactly $32$, confirmed by direct computation.

**Trap.** Rejecting $k = \dfrac{5}{32}$ because it is smaller than 1 and hunting for a larger root. There is no other solution: the average simplifies to exactly $\dfrac{5}{k}$, which is one-to-one.

### Q19.8 - Displacement and distance travelled

**Question.**
A particle moves with velocity $v(t) = t^{2}-3t+2$ m/s.

- a. Find the displacement on $[0,3]$.
- b. Find the distance travelled on $[0,3]$.

**Part a, step 1: displacement is the plain integral of velocity.**
Signs are kept, so backward motion subtracts.

$$s = \int_{0}^{3}\left(t^{2}-3t+2\right)dt$$

**Part a, step 2: antidifferentiate and evaluate.**

$$= \left[\frac{t^{3}}{3} - \frac{3t^{2}}{2} + 2t\right]_{0}^{3} = 9 - \frac{27}{2} + 6 = 15 - 13.5 = \frac{3}{2}$$

**Answer a.**

$$\text{Displacement} = \frac{3}{2} = 1.5\ \text{m}$$

**Möbius:** `3/2`

**Part b, step 1: distance needs the absolute value.**

$$d = \int_{0}^{3}\lvert v(t)\rvert\,dt$$

**Part b, step 2: find where the velocity changes sign.**

$$t^{2}-3t+2 = (t-1)(t-2) = 0 \implies t = 1,\ t = 2$$

Both lie inside $[0,3]$, so split there.

**Part b, step 3: determine the sign on each piece.**

$$t=0.5:\ v>0 \qquad t=1.5:\ v<0 \qquad t=2.5:\ v>0$$

The particle moves forward, reverses, then moves forward again.

**Part b, step 4: integrate each piece.**

$$\int_{0}^{1}v\,dt = \frac{1}{3} - \frac{3}{2} + 2 = \frac{5}{6}$$

$$\int_{1}^{2}v\,dt = -\frac{1}{6}$$

$$\int_{2}^{3}v\,dt = \frac{5}{6}$$

**Part b, step 5: add the absolute values.**

$$d = \frac{5}{6} + \left\lvert-\frac{1}{6}\right\rvert + \frac{5}{6} = \frac{5+1+5}{6} = \frac{11}{6}$$

**Answer b.**

$$\text{Distance} = \frac{11}{6} \approx 1.833\ \text{m}$$

**Möbius:** `11/6`

**Check.** The three signed pieces sum to $\dfrac{5}{6}-\dfrac{1}{6}+\dfrac{5}{6} = \dfrac{9}{6} = \dfrac{3}{2}$, matching part a.
Distance always exceeds displacement when the velocity changes sign, and $\dfrac{11}{6} > \dfrac{3}{2}$ as expected.

### Q19.9 - Sprinter with piecewise acceleration

**Question.**
A sprinter in a 100 m race accelerates at $4\ \text{m/s}^{2}$ for 2 seconds, then accelerates at zero for the rest of the race.
Find her time for the race.

**Step 1: phase 1 velocity.**
Integrate the acceleration, with $v(0) = 0$ from a standing start.

$$v(t) = \int 4\,dt = 4t \implies v(2) = 8\ \text{m/s}$$

**Step 2: phase 1 distance.**
Integrate the velocity over the first 2 seconds.

$$d_{1} = \int_{0}^{2}4t\,dt = \left[2t^{2}\right]_{0}^{2} = 8\ \text{m}$$

**Step 3: phase 2 setup.**
Zero acceleration means constant velocity, and it holds at the value reached at the end of phase 1.

$$v = 8\ \text{m/s} \text{ for the rest of the race}$$

**Step 4: remaining distance.**

$$100 - 8 = 92\ \text{m}$$

**Step 5: time for phase 2.**

$$t_{2} = \frac{92}{8} = 11.5\ \text{s}$$

**Step 6: total time.**

$$T = 2 + 11.5 = 13.5\ \text{s}$$

**Answer.**

$$T = 13.5\ \text{seconds}$$

**Möbius:** `13.5`

**Trap.** Dividing the full $100$ m by $8$ m/s to get $12.5$ s. That ignores the 8 m already covered while accelerating, and it ignores that she was slower than 8 m/s for those first 2 seconds.

---

# Closing: the two habits that matter most

**1. Verify every antiderivative by differentiating it.**

**2. Substitute before you choose a technique.**
