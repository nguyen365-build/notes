# Limit Formulas Reference

This is a reference sheet of the formal rules, laws, and theorem statements that govern limits in calculus.
It is the "formula sheet" layer, not the "memorize this numeric value" layer or the "which technique do I use" layer.

Companion files in this folder cover the other two layers, so this file does not repeat their content:
- `Special-Limits.md` - the specific memorize-outright limit values (sin x / x -> 1, e^x definitions, growth-rate hierarchy, etc.)
- `Calculus-Techniques-Limits-Derivatives-Integrals.md` - the L1-L20 technique catalog (factor-and-cancel, conjugate multiplication, Taylor expansion, and when each applies)

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
