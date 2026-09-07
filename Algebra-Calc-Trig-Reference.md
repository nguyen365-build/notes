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
