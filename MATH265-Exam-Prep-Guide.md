# MATH 265 Exam Prep Guide

This file is a phone-friendly study guide for the MATH 265 midterm and final.
It covers the full concept list you gave, plus the extra topics your own notes and sample exams actually test.

## How to read the two notations in this file

Every formula in this guide is given twice, on purpose.

- The **backtick line** is the Möbius / calculator form: the flat, one-line text you actually type into an answer box.
- The **Math line** under it is the same formula in ordinary mathematical symbols, the way it is printed in the textbook and the way you should write it on a paper exam.

Example of the pairing you will see everywhere below:

- `(f/g)' = (f' g - f g') / g^2`.
  - Math: $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^{2}}$

Read the Math line to understand the formula.
Read the backtick line when you are about to type it.
The two always say the same thing.

## What I analyzed

- The course folder at `Coursework\_Archive\Degree\Athabasca\_MATH265 - Calculus 1`.
- The question notes in `notes\Q01.1` through `notes\Q19.9`.
- The review and cheat-sheet files in `notes\MATH265`.
- The four sample exams, the all-exam question bank, and the AU reference sheets.
- The question bank `notes\MATH265.md`, which supplies the exact wording of every question restated in Part 5.

Key findings from the files:

- The midterm covers Units 1 to 4.
- The final covers Units 3 to 7.
- Both exams are 3 hours, closed-book, and need 50 percent to pass.
- You may bring one 8.5 by 11 inch note sheet, both sides, and a simple scientific calculator.
- The sample papers split cleanly: midterms stop at differentials and related rates.
- Finals add integration, curve sketching, extrema, optimization, Newton's method, and applications of integration.
- The reference sheet notes that the published sample exams use no integration by parts, but you asked for it, so it is included below as insurance.

## Exam facts that matter

- Midterm is 25 percent of the final grade.
- Final is 40 percent of the final grade.
- Assignments are the rest.
- You must pass each exam on its own, so do not rely on assignments to rescue you.
- Questions are worth several points because several steps are required.
- Show every step and justify every answer.
- Use radians unless the question says degrees.
- Use exact form unless the question asks for rounding.
- Do the questions you are confident about first.
- Budget roughly 10 to 15 minutes per question.

## Möbius answer-entry rules

The live delivery is machine-marked, and it grades by mathematical equivalence.
A correct answer is never rejected for its form, only for being parsed differently than you meant it.

- Multiplication is explicit: write `2*x`, never `2x`.
- Roots are functions: write `sqrt(6)`, never a root glyph and never `6^.5`.
- Bracket whole numerators: write `(sqrt(6)+sqrt(2))/4`, never `sqrt(6)+sqrt(2)/4`.
- Natural log is `ln(x)`, never `log(x)`.
- Exact form beats decimals: write `(sqrt(6)+sqrt(2))/4`, never `0.9659`.
- Powers use a caret: write `x^(3/2)`, and bracket any compound exponent.
- Always click the preview icon before you submit.
- An empty preview modal means broken syntax, not wrong mathematics.

---

# Part 1: The big picture and limits

## 1. Calculus is all about performing two operations on functions

Concept:

- Calculus has two main operations: differentiation and integration.
- Differentiation finds how fast a function changes.
- Integration adds up how much a function accumulates.
- The two operations are inverses, which is the Fundamental Theorem of Calculus.

Know:

- Derivative = rate of change = slope.
- Integral = accumulation = area under a curve.
- Most exam problems are one of these two operations applied to a function.

Practice:

- Say, in one sentence, whether a word problem wants a derivative or an integral.
- Example: water flowing from a tank asks for total amount, so integrate the rate.
- Example: population growing at an instant asks for a derivative.

## 2. Rate of change as slope of a straight line

Concept:

- A straight line has one slope, the same everywhere.
- Slope = rise over run = change in y divided by change in x.

Know:

- Average rate of change on an interval is the slope of the secant line.
- For a line through two points, the slope is `(y2 - y1) / (x2 - x1)`.
  - Math: $m = \dfrac{y_{2} - y_{1}}{x_{2} - x_{1}} = \dfrac{\Delta y}{\Delta x}$

Practice:

- Interpret `(P(15) - P(2)) / 13 = 1,431` in plain words.
  - Math: $\dfrac{P(15) - P(2)}{13} = 1431$
- Say the population grew by an average of 1,431 people per year between year 2 and year 15.
- See `Q06.1`.

## 3. The dilemma of the slope of a curvy line

Concept:

- A curve does not have one slope because its steepness changes point to point.
- A straight secant between two far points only gives an average.

Know:

- To get steepness at a single point, you have to zoom in.
- The slope at one point is the slope of the tangent line there.

Practice:

- Draw a parabola and mark a secant between two points.
- Then draw the tangent line at one of those points.
- Explain why the secant slope is not the same as the tangent slope.

## 4. The slope between very close points

Concept:

- Move the two points closer and closer together.
- The secant slope gets closer to the tangent slope.

Know:

- The difference quotient is `(f(x + h) - f(x)) / h`.
  - Math: $\dfrac{f(x+h) - f(x)}{h}$
- As `h` approaches 0, this quotient approaches the derivative.
  - Math: $\displaystyle\lim_{h \to 0}\dfrac{f(x+h) - f(x)}{h} = f'(x)$

Practice:

- Write the difference quotient for `f(x) = x^2`.
  - Math: $f(x) = x^{2}$
- Simplify it to `2x + h`, then let `h` go to 0 to get `2x`.
  - Math: $\dfrac{(x+h)^{2} - x^{2}}{h} = 2x + h \longrightarrow 2x$

## 5. The limit

Concept:

- A limit is the value a function approaches as the input approaches a value.
- The function does not have to actually reach that value.

Know:

- Direct substitution is the first thing to try.
- `0/0` means factor, rationalize, use a common denominator, or use a trig identity.
  - Math: $\dfrac{0}{0}$ is an indeterminate form, so the expression must be rewritten before the limit is read off.
- `k/0` with `k` not zero usually means the limit is infinite or does not exist.
  - Math: $\dfrac{k}{0}$ with $k \neq 0$ gives $\pm\infty$, so check the sign from each side.
- `infinity/infinity` means divide by the highest power in the denominator.
  - Math: $\dfrac{\infty}{\infty}$ is indeterminate, so divide numerator and denominator by the highest power of $x$ in the denominator.
- Bounded times zero, such as `(something going to 0) * sin(x)`, is squeezed to 0.
  - Math: if $\displaystyle\lim_{x\to a} g(x) = 0$ and $\lvert b(x)\rvert \le M$, then $\displaystyle\lim_{x\to a} g(x)\,b(x) = 0$.

Practice:

- Do every limit in `Q03.1`, `Q03.2`, and `Q03.3`.
- Also do `Q04.1` to connect limits to asymptotes.

## 6. The derivative, and differentials of x and y

Concept:

- The derivative is the limit of the difference quotient.
- It measures instantaneous rate of change.

Know:

- `f'(x) = lim(h -> 0) [f(x + h) - f(x)] / h`.
  - Math: $f'(x) = \displaystyle\lim_{h \to 0}\dfrac{f(x+h) - f(x)}{h}$
- The derivative is a function, not a single number.
- `dy/dx` means the derivative of `y` with respect to `x`.
  - Math: $\dfrac{dy}{dx}$

Practice:

- Use the definition to find the derivative of `x^2`, `1/x`, and `cot x`.
  - Math: $x^{2}$, $\dfrac{1}{x}$, $\cot x$
- See `Q07.1` for the cotangent derivation.

## 7. Differential notation

Concept:

- `dy/dx` is one notation for the derivative.
- `dy` and `dx` are called differentials.

Know:

- `dy = f'(x) dx`.
  - Math: $dy = f'(x)\,dx$
- Treat `dx` as a small change in `x`.
- Treat `dy` as the approximate resulting change in `y`.
- Differential notation is used in linear approximation and related rates.

Practice:

- Approximate `sqrt(9.2)` by choosing `x = 9` and `dx = 0.2`.
  - Math: $\sqrt{9.2}$ with $a = 9$ and $dx = 0.2$
- See `Q12.1`.

---
# Part 2: Derivative rules

## 8. The constant rule of differentiation

Concept:

- The derivative of a constant is zero.

Know:

- `d/dx [c] = 0`.
  - Math: $\dfrac{d}{dx}(c) = 0$
- A constant function has a flat graph, so its slope is zero.

Practice:

- Find `d/dx [7]`.
  - Math: $\dfrac{d}{dx}(7)$
- Answer: `0`.
  - Math: $0$

## 9. The power rule of differentiation

Concept:

- Bring the exponent down and reduce the exponent by one.

Know:

- `d/dx [x^n] = n x^(n - 1)`.
  - Math: $\dfrac{d}{dx}\left(x^{n}\right) = n\,x^{n-1}$
- Works for negative and fractional powers too.

Practice:

- Differentiate `x^5`, `x^(-2)`, `sqrt(x)`, and `1/x`.
  - Math: $x^{5}$, $x^{-2}$, $\sqrt{x}$, $\dfrac{1}{x}$
- Answers: `5x^4`, `-2x^(-3)`, `(1/2)x^(-1/2)`, `-x^(-2)`.
  - Math: $5x^{4}$, $-2x^{-3}$, $\tfrac{1}{2}x^{-1/2}$, $-x^{-2}$

## 10. Visual interpretation of the power rule

Concept:

- Each derivative lowers the degree of a polynomial by one.
- The graph of the derivative has one fewer turn than the original.

Know:

- A cubic has a quadratic derivative.
- A quadratic has a linear derivative.
- A line has a constant derivative.

Practice:

- Sketch `y = x^3` and `y = 3x^2` together.
  - Math: $y = x^{3}$ and $y = 3x^{2}$
- Notice the cubic's flat points correspond to where `3x^2 = 0`.
  - Math: $3x^{2} = 0$

## 11. The addition and subtraction rule of differentiation

Concept:

- Differentiate term by term.

Know:

- `d/dx [f(x) + g(x)] = f'(x) + g'(x)`.
  - Math: $\dfrac{d}{dx}\big(f(x) + g(x)\big) = f'(x) + g'(x)$
- `d/dx [f(x) - g(x)] = f'(x) - g'(x)`.
  - Math: $\dfrac{d}{dx}\big(f(x) - g(x)\big) = f'(x) - g'(x)$

Practice:

- Differentiate `4x^5 + 3x^4 - 6x^3 + 6`.
  - Math: $4x^{5} + 3x^{4} - 6x^{3} + 6$
- Answer: `20x^4 + 12x^3 - 18x^2`.
  - Math: $20x^{4} + 12x^{3} - 18x^{2}$

## 12. The product rule of differentiation

Concept:

- For a product of two functions, use first derivative times second plus first times second derivative.

Know:

- `(fg)' = f' g + f g'`.
  - Math: $(fg)' = f'g + fg'$
- Say it: "first prime times second, plus first times second prime."

Practice:

- Differentiate `x cos(sqrt(x - 3))`.
  - Math: $x\cos\left(\sqrt{x-3}\right)$
- Identify `f = x` and `g = cos(sqrt(x - 3))`.
  - Math: $f = x$ and $g = \cos\left(\sqrt{x-3}\right)$

## 13. Combining rules of differentiation to find the derivative of a polynomial

Concept:

- Polynomials use only the power, constant, and sum rules.
- More complicated functions layer product, quotient, and chain rules.

Know:

- Work from the outside in.
- Name the rule you are using at each step.

Practice:

- Differentiate a polynomial like `3x^4 - 2x^3 + x - 5`.
  - Math: $3x^{4} - 2x^{3} + x - 5$
- Then move on to mixed expressions in `Q08.1` through `Q08.4`.

## 14. Differentiation super-shortcuts for polynomials

Concept:

- For a polynomial, multiply each coefficient by its exponent and drop the degree by one.

Know:

- `y = ax^n` becomes `y' = a n x^(n - 1)`.
  - Math: $y = ax^{n}$ becomes $y' = an\,x^{n-1}$
- The constant term disappears.

Practice:

- Differentiate `y = 4x^5 + 3x^4 - 6x^3 + 6` without rewriting every step.
  - Math: $y = 4x^{5} + 3x^{4} - 6x^{3} + 6$
- Answer: `20x^4 + 12x^3 - 18x^2`.
  - Math: $20x^{4} + 12x^{3} - 18x^{2}$

## 15. Solving optimization problems with derivatives

Concept:

- Maxima and minima happen where the derivative is zero or undefined, or at endpoints.

Know:

- Draw and label the situation.
- Write the quantity to optimize.
- Write the constraint.
- Use the constraint to eliminate one variable.
- Differentiate, set the derivative to zero, and solve.
  - Math: solve $f'(x) = 0$
- Check endpoints and state the answer with units.

Practice:

- Rectangle of fixed area and least perimeter.
- Cheapest rectangular box with different lid cost.
- See `Q15.2`, `Q15.4`, and `Q15.1`.

## 16. The second derivative

Concept:

- The second derivative is the derivative of the derivative.

Know:

- `f'(x)` tells slope and velocity.
  - Math: $f'(x)$
- `f''(x)` tells concavity and acceleration.
  - Math: $f''(x) = \dfrac{d^{2}f}{dx^{2}}$
- `f'' > 0` means concave up.
  - Math: $f''(x) > 0$
- `f'' < 0` means concave down.
  - Math: $f''(x) < 0$

Practice:

- Find `d^2/dx^2 [cot(2x)]`.
  - Math: $\dfrac{d^{2}}{dx^{2}}\cot(2x)$
- See `Q08.2`.

## 17. Trig rules of differentiation for sine and cosine

Concept:

- The derivative of sine is cosine.
- The derivative of cosine is negative sine.

Know:

- `d/dx [sin x] = cos x`.
  - Math: $\dfrac{d}{dx}(\sin x) = \cos x$
- `d/dx [cos x] = -sin x`.
  - Math: $\dfrac{d}{dx}(\cos x) = -\sin x$
- The minus sign on cosine is the most common lost mark.

Practice:

- Differentiate `sin(2x^2 - x + 1)`.
  - Math: $\sin\left(2x^{2} - x + 1\right)$
- Remember the chain rule: multiply by the inside derivative `4x - 1`.
  - Math: multiply by $4x - 1$

## 18. Knowledge test: product rule example

Concept:

- This is a self-test to confirm you can apply the product rule correctly.

Know:

- For `y = x^2 sin x`, let `f = x^2` and `g = sin x`.
  - Math: for $y = x^{2}\sin x$, let $f = x^{2}$ and $g = \sin x$
- `f' = 2x` and `g' = cos x`.
  - Math: $f' = 2x$ and $g' = \cos x$
- `y' = 2x sin x + x^2 cos x`.
  - Math: $y' = 2x\sin x + x^{2}\cos x$

Practice:

- Differentiate `x^2 sin x` on paper.
  - Math: $x^{2}\sin x$
- Then check your answer against `2x sin x + x^2 cos x`.
  - Math: $2x\sin x + x^{2}\cos x$

## 19. The chain rule for differentiation

Concept:

- Differentiate the outside function, then multiply by the derivative of the inside.

Know:

- `d/dx [f(g(x))] = f'(g(x)) * g'(x)`.
  - Math: $\dfrac{d}{dx}f\big(g(x)\big) = f'\big(g(x)\big)\,g'(x)$
- Work outside to inside.
- Missing the inside derivative is the single most common error.

Practice:

- Differentiate `sin(2x^2 - x + 1)`.
  - Math: $\sin\left(2x^{2} - x + 1\right)$
- Differentiate `( -4x^3 - x^2 + 3x + 7 )^4`.
  - Math: $\left(-4x^{3} - x^{2} + 3x + 7\right)^{4}$
- See `Q08.1` and `Q08.3`.

## 20. The quotient rule for differentiation

Concept:

- For a fraction, use low d-high minus high d-low over low squared.

Know:

- `(f/g)' = (f' g - f g') / g^2`.
  - Math: $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^{2}}$
- The numerator order is the whole mark.
- Never write `g f' - f g'`.
  - Math: never write $\dfrac{gf' - fg'}{g^{2}}$ with the terms swapped, and never drop the square on the denominator.

Practice:

- Differentiate `(2x - 16) / (x + 3)^2`.
  - Math: $\dfrac{2x - 16}{(x+3)^{2}}$
- Differentiate `(sqrt(x^2 - 1)) / (x^2 - 2x - 8)`.
  - Math: $\dfrac{\sqrt{x^{2} - 1}}{x^{2} - 2x - 8}$

## 21. The derivative of the other trig functions

Concept:

- Tangent, cotangent, secant, and cosecant each have their own derivative.

Know:

- `d/dx [tan x] = sec^2 x`.
  - Math: $\dfrac{d}{dx}(\tan x) = \sec^{2}x$
- `d/dx [cot x] = -csc^2 x`.
  - Math: $\dfrac{d}{dx}(\cot x) = -\csc^{2}x$
- `d/dx [sec x] = sec x tan x`.
  - Math: $\dfrac{d}{dx}(\sec x) = \sec x\tan x$
- `d/dx [csc x] = -csc x cot x`.
  - Math: $\dfrac{d}{dx}(\csc x) = -\csc x\cot x$
- Every co-function derivative has a minus sign: cosine, cotangent, cosecant.

Practice:

- Differentiate `sec(x^2 - 3x)`.
  - Math: $\sec\left(x^{2} - 3x\right)$
- Differentiate `cot(2x)` twice.
  - Math: $\cot(2x)$
- See `Q08.2`.

## 22. Algebra overview: exponentials and logarithms

Concept:

- Exponentials grow by repeated multiplication.
- Logarithms undo exponentials.

Know:

- `e^x` is the natural exponential.
  - Math: $e^{x}$
- `ln x` is the natural logarithm, the inverse of `e^x`.
  - Math: $\ln x$ is the inverse of $e^{x}$
- `ln(e^x) = x` and `e^(ln x) = x`.
  - Math: $\ln\left(e^{x}\right) = x$ and $e^{\ln x} = x$
- Exponent rules: `x^a x^b = x^(a+b)`, `1/x^n = x^(-n)`, and `nth-root(x^m) = x^(m/n)`.
  - Math: $x^{a}x^{b} = x^{a+b}$, $\dfrac{1}{x^{n}} = x^{-n}$, and $\sqrt[n]{x^{m}} = x^{m/n}$

Practice:

- Rewrite `sqrt(3x)` as `sqrt(3) x^(1/2)`.
  - Math: $\sqrt{3x} = \sqrt{3}\,x^{1/2}$
- Rewrite `sqrt(5x) / x^2` as `sqrt(5) x^(-3/2)`.
  - Math: $\dfrac{\sqrt{5x}}{x^{2}} = \sqrt{5}\,x^{-3/2}$

## 23. Differentiation rules for exponents

Concept:

- The natural exponential is its own derivative.

Know:

- `d/dx [e^x] = e^x`.
  - Math: $\dfrac{d}{dx}\left(e^{x}\right) = e^{x}$
- For a general base, `d/dx [a^x] = a^x ln a`.
  - Math: $\dfrac{d}{dx}\left(a^{x}\right) = a^{x}\ln a$
- For a composite exponential, use the chain rule.
  - Math: $\dfrac{d}{dx}e^{g(x)} = e^{g(x)}g'(x)$

Practice:

- Differentiate `e^(2x)`.
  - Math: $e^{2x}$
- Answer: `2 e^(2x)`.
  - Math: $2e^{2x}$

## 24. Differentiation rules for logarithms

Concept:

- The derivative of natural log is one over x.

Know:

- `d/dx [ln x] = 1/x`.
  - Math: $\dfrac{d}{dx}(\ln x) = \dfrac{1}{x}$
- `d/dx [ln(g(x))] = g'(x) / g(x)`.
  - Math: $\dfrac{d}{dx}\ln\big(g(x)\big) = \dfrac{g'(x)}{g(x)}$

Practice:

- Differentiate `ln(x^2 + 1)`.
  - Math: $\ln\left(x^{2} + 1\right)$
- Answer: `2x / (x^2 + 1)`.
  - Math: $\dfrac{2x}{x^{2} + 1}$

---
# Part 3: Antiderivatives and integration

## 25. The anti-derivative, also called the integral

Concept:

- An antiderivative reverses a derivative.
- If `F'(x) = f(x)`, then `F(x)` is an antiderivative of `f(x)`.
  - Math: if $F'(x) = f(x)$, then $F(x)$ is an antiderivative of $f(x)$.

Know:

- Integration asks: what function gives this derivative?
- There are infinitely many antiderivatives because constants vanish under differentiation.

Practice:

- Find an antiderivative of `3x^2`.
  - Math: $3x^{2}$
- Answer: `x^3 + C`.
  - Math: $x^{3} + C$

## 26. The power rule for integration

Concept:

- Reverse the power rule: add one to the exponent, then divide by the new exponent.

Know:

- `∫ x^n dx = x^(n + 1) / (n + 1) + C`, for `n` not equal to `-1`.
  - Math: $\displaystyle\int x^{n}\,dx = \dfrac{x^{n+1}}{n+1} + C$, for $n \neq -1$

Practice:

- Integrate `x^4`, `x^(1/2)`, and `x^(-2)`.
  - Math: $x^{4}$, $x^{1/2}$, $x^{-2}$
- Answers: `x^5/5 + C`, `(2/3)x^(3/2) + C`, `-x^(-1) + C`.
  - Math: $\dfrac{x^{5}}{5} + C$, $\dfrac{2}{3}x^{3/2} + C$, $-x^{-1} + C$

## 27. The power rule for integration will not work for 1/x

Concept:

- `1/x = x^(-1)`, and the power rule would divide by zero.
  - Math: $\dfrac{1}{x} = x^{-1}$, and $n + 1 = 0$ here.

Know:

- `∫ 1/x dx = ln|x| + C`.
  - Math: $\displaystyle\int \dfrac{1}{x}\,dx = \ln\lvert x\rvert + C$
- Use the absolute value because the logarithm needs a positive argument.

Practice:

- Integrate `1/x` and `4/x`.
  - Math: $\dfrac{1}{x}$ and $\dfrac{4}{x}$
- Answers: `ln|x| + C` and `4 ln|x| + C`.
  - Math: $\ln\lvert x\rvert + C$ and $4\ln\lvert x\rvert + C$

## 28. The constant of integration, plus C

Concept:

- Indefinite integrals always get `+ C`.
- Definite integrals never get `+ C`.

Know:

- `+ C` represents the whole family of antiderivatives.
- Forgetting `+ C` on an indefinite integral loses the mark.
- Adding `+ C` to a definite integral is also wrong.

Practice:

- Integrate `x^2` both ways.
  - Math: $x^{2}$
- Indefinite: `x^3/3 + C`.
  - Math: $\displaystyle\int x^{2}\,dx = \dfrac{x^{3}}{3} + C$
- Definite from 0 to 1: `1/3`.
  - Math: $\displaystyle\int_{0}^{1} x^{2}\,dx = \dfrac{1}{3}$

## 29. Anti-derivative notation

Concept:

- `∫ f(x) dx` means the general antiderivative.
  - Math: $\displaystyle\int f(x)\,dx$
- `∫[a to b] f(x) dx` means the definite integral.
  - Math: $\displaystyle\int_{a}^{b} f(x)\,dx$

Know:

- The `dx` tells you the variable of integration.
- The limits `a` and `b` appear only on definite integrals.

Practice:

- Write an indefinite integral for `cos x`.
  - Math: $\displaystyle\int \cos x\,dx = \sin x + C$
- Write a definite integral for area from 0 to 1.
  - Math: $\displaystyle\int_{0}^{1} f(x)\,dx$

## 30. The integral as the area under a curve using the limit

Concept:

- A definite integral is the limit of a sum of rectangle areas.

Know:

- Chop the interval into thin slices.
- Each rectangle has area `f(x) * dx`.
  - Math: $f(x_{i}^{*})\,\Delta x$
- Add the rectangles and let the width go to 0.
  - Math: $\displaystyle\int_{a}^{b} f(x)\,dx = \lim_{n \to \infty}\sum_{i=1}^{n} f(x_{i}^{*})\,\Delta x$

Practice:

- Draw `y = x` from 0 to 2.
  - Math: $y = x$ on $[0, 2]$
- Approximate the area with four rectangles, then with more.
- See that the limit approaches the triangle area 2.

## 31. Evaluating definite integrals

Concept:

- Find an antiderivative, then subtract its values at the endpoints.

Know:

- `∫[a to b] f(x) dx = F(b) - F(a)`.
  - Math: $\displaystyle\int_{a}^{b} f(x)\,dx = F(b) - F(a)$
- This is the Fundamental Theorem of Calculus, part 2.

Practice:

- Evaluate `∫[0 to 1] x^2 dx`.
  - Math: $\displaystyle\int_{0}^{1} x^{2}\,dx$
- Answer: `1/3`.
  - Math: $\dfrac{1}{3}$

## 32. Definite and indefinite integrals compared

Concept:

- Indefinite integrals return a family of functions.
- Definite integrals return a number.

Know:

- Indefinite: `∫ f(x) dx = F(x) + C`.
  - Math: $\displaystyle\int f(x)\,dx = F(x) + C$
- Definite: `∫[a to b] f(x) dx = F(b) - F(a)`.
  - Math: $\displaystyle\int_{a}^{b} f(x)\,dx = F(b) - F(a)$

Practice:

- Integrate `2x` indefinitely, then from 1 to 3.
  - Math: $2x$
- Answers: `x^2 + C` and `8`.
  - Math: $x^{2} + C$ and $\displaystyle\int_{1}^{3} 2x\,dx = 8$

## 33. The definite integral and signed area

Concept:

- Area above the x-axis counts positive.
- Area below the x-axis counts negative.
- The definite integral reports signed area.

Know:

- To get true distance or total area, integrate the absolute value, or split at the zeros.
  - Math: total area $= \displaystyle\int_{a}^{b} \lvert f(x)\rvert\,dx$

Practice:

- For `v(t) = t^2 - 3t + 2` on `[0, 3]`, find displacement and distance.
  - Math: $v(t) = t^{2} - 3t + 2$ on $[0, 3]$
- See `Q19.8`.

## 34. The Fundamental Theorem of Calculus visualized

Concept:

- Differentiation and integration undo each other.

Know:

- FTC part 1: `d/dx ∫[a to x] f(t) dt = f(x)`.
  - Math: $\dfrac{d}{dx}\displaystyle\int_{a}^{x} f(t)\,dt = f(x)$
- FTC part 2: `∫[a to b] f'(x) dx = f(b) - f(a)`.
  - Math: $\displaystyle\int_{a}^{b} f'(x)\,dx = f(b) - f(a)$
- If the area function grows, its derivative is the height of the curve.

Practice:

- Differentiate `∫[2x to x] sin(t^2) dt`.
  - Math: $\dfrac{d}{dx}\displaystyle\int_{2x}^{x} \sin\left(t^{2}\right)dt$
- Answer: `sin(x^2) - 2 sin(4x^2)`.
  - Math: $\sin\left(x^{2}\right) - 2\sin\left(4x^{2}\right)$
- See `Q18.1`.

## 35. The integral as a running total of its derivative

Concept:

- An integral accumulates a rate.
- A derivative measures the rate of accumulation.

Know:

- Total water = integral of flow rate.
- Distance = integral of velocity.
- Velocity = derivative of position.
  - Math: $s(b) - s(a) = \displaystyle\int_{a}^{b} v(t)\,dt$ and $v(t) = s'(t)$

Practice:

- Water flows at `r(t) = 180 - 6t` liters per minute.
  - Math: $r(t) = 180 - 6t$
- Find the amount that flows in the first 15 minutes.
  - Math: $\displaystyle\int_{0}^{15}(180 - 6t)\,dt$
- Answer: `2025 L`.
  - Math: $2025$ litres
- See `Q19.3`.

## 36. The trig rule for integration, sine and cosine

Concept:

- Integration flips the derivative signs.

Know:

- `∫ sin x dx = -cos x + C`.
  - Math: $\displaystyle\int \sin x\,dx = -\cos x + C$
- `∫ cos x dx = sin x + C`.
  - Math: $\displaystyle\int \cos x\,dx = \sin x + C$
- The minus now sits on sine, the opposite of differentiation.

Practice:

- Integrate `sin x` and `cos x`.
  - Math: $\sin x$ and $\cos x$
- Then integrate `x + cos(2x)` from `a` to `b`.
  - Math: $\displaystyle\int_{a}^{b}\big(x + \cos(2x)\big)\,dx$

## 37. Definite integral example problem

Concept:

- A worked example of the full evaluate step.

Know:

- Problem: evaluate `∫[0 to pi] sin x dx`.
  - Math: $\displaystyle\int_{0}^{\pi} \sin x\,dx$
- Antiderivative: `-cos x`.
  - Math: $-\cos x$
- Evaluate: `-cos(pi) - (-cos(0))`.
  - Math: $-\cos(\pi) - \big(-\cos(0)\big)$
- `-cos(pi) = 1`, so the answer is `1 - (-1) = 2`.
  - Math: $-\cos(\pi) = 1$, so the answer is $1 - (-1) = 2$

Practice:

- Repeat this problem without notes.
- Then do `∫[0 to pi/3] tan x sec^2 x dx`.
  - Math: $\displaystyle\int_{0}^{\pi/3} \tan x\,\sec^{2}x\,dx$
- Answer: `3/2`.
  - Math: $\dfrac{3}{2}$

## 38. u-Substitution

Concept:

- Choose `u` equal to the inside function.
- Replace `dx` and the limits, then integrate.

Know:

- You need the derivative of `u` present, up to a constant.
  - Math: $\displaystyle\int f\big(g(x)\big)g'(x)\,dx = \int f(u)\,du$ with $u = g(x)$, $du = g'(x)\,dx$
- For definite integrals, change the limits and never convert back.
  - Math: $\displaystyle\int_{a}^{b} f\big(g(x)\big)g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$

Practice:

- `∫ sin x cos x dx` with `u = sin x`.
  - Math: $\displaystyle\int \sin x\cos x\,dx$ with $u = \sin x$
- `∫ cos(sqrt(2x)) / sqrt(x) dx` with `u = sqrt(2x)`.
  - Math: $\displaystyle\int \dfrac{\cos\left(\sqrt{2x}\right)}{\sqrt{x}}\,dx$ with $u = \sqrt{2x}$
- `∫ sec^3 x tan x dx` with `u = sec x`.
  - Math: $\displaystyle\int \sec^{3}x\,\tan x\,dx$ with $u = \sec x$
- See `Q16.1` and `Q16.2`.

## 39. Integration by parts

Concept:

- Integration by parts reverses the product rule.

Know:

- `∫ u dv = uv - ∫ v du`.
  - Math: $\displaystyle\int u\,dv = uv - \int v\,du$
- Pick `u` so that its derivative is simpler.
- Pick `dv` so that you can integrate it.

Practice:

- Integrate `x e^x dx` with `u = x` and `dv = e^x dx`.
  - Math: $\displaystyle\int xe^{x}\,dx$ with $u = x$, $dv = e^{x}dx$
- Integrate `x cos x dx` with `u = x` and `dv = cos x dx`.
  - Math: $\displaystyle\int x\cos x\,dx$ with $u = x$, $dv = \cos x\,dx$

## 40. The DI method for integration by parts

Concept:

- The DI table organizes repeated integration by parts.

Know:

- Column D holds derivatives of `u`.
- Column I holds antiderivatives of `dv`.
- Multiply diagonally, alternating signs, and add the final integral row.

Practice:

- Use a DI table for `x^2 e^x dx`.
  - Math: $\displaystyle\int x^{2}e^{x}\,dx$
- D column: `x^2`, `2x`, `2`, `0`.
  - Math: $x^{2}$, $2x$, $2$, $0$
- I column: `e^x`, `e^x`, `e^x`, `e^x`.
  - Math: $e^{x}$, $e^{x}$, $e^{x}$, $e^{x}$
- Answer: `x^2 e^x - 2x e^x + 2 e^x + C`.
  - Math: $x^{2}e^{x} - 2xe^{x} + 2e^{x} + C$

---
# Part 4: Other must-know topics from your exams

These topics are not in your requested list, but they appear repeatedly in the AU sample papers and in your notes.

## Functions, domains, and composition

Concept:

- A function gives one output for each input.

Know:

- Vertical line test: a graph is a function if every vertical line hits it at most once.
- Domain excludes zero denominators, negatives under even roots, and non-positive log arguments.
- For `f(g(x))`, keep the domain restrictions of both `g` and `f(g(x))`.
  - Math: for $f\big(g(x)\big)$, keep the restrictions of both $g$ and $f\circ g$.

Practice:

- `Q01.2`, `Q01.3`, and `Q01.4`.

## Exact trig values

Concept:

- Memorize the unit circle values for `0`, `pi/6`, `pi/4`, `pi/3`, and `pi/2`.
  - Math: $0$, $\dfrac{\pi}{6}$, $\dfrac{\pi}{4}$, $\dfrac{\pi}{3}$, $\dfrac{\pi}{2}$

Know:

- `sin`: `0`, `1/2`, `sqrt(2)/2`, `sqrt(3)/2`, `1`.
  - Math: $\sin$: $0$, $\dfrac{1}{2}$, $\dfrac{\sqrt2}{2}$, $\dfrac{\sqrt3}{2}$, $1$
- `cos`: `1`, `sqrt(3)/2`, `sqrt(2)/2`, `1/2`, `0`.
  - Math: $\cos$: $1$, $\dfrac{\sqrt3}{2}$, $\dfrac{\sqrt2}{2}$, $\dfrac{1}{2}$, $0$
- `tan`: `0`, `1/sqrt(3)`, `1`, `sqrt(3)`, undefined.
  - Math: $\tan$: $0$, $\dfrac{\sqrt3}{3}$, $1$, $\sqrt3$, undefined
- Use ASTC for quadrant signs.
- Use sum, difference, and half-angle formulas for 15 and 22.5 degree angles.

The three tools that generate everything outside the five memorized rows:

- Difference: `cos(A - B) = cos A cos B + sin A sin B`.
  - Math: $\cos(A-B) = \cos A\cos B + \sin A\sin B$
- Sum: `sin(A + B) = sin A cos B + cos A sin B`.
  - Math: $\sin(A+B) = \sin A\cos B + \cos A\sin B$
- Half angle: `cos(x/2) = +-sqrt((1 + cos x)/2)`.
  - Math: $\cos\dfrac{x}{2} = \pm\sqrt{\dfrac{1 + \cos x}{2}}$, sign chosen by the quadrant of $\dfrac{x}{2}$

Parity, which decides the sign before you look anything up:

- `cos(-x) = cos(x)` and `sec(-x) = sec(x)` are even.
  - Math: $\cos(-x) = \cos x$ and $\sec(-x) = \sec x$
- `sin(-x) = -sin(x)`, `tan(-x) = -tan(x)`, `csc(-x) = -csc(x)`, `cot(-x) = -cot(x)` are odd.
  - Math: $\sin(-x) = -\sin x$, $\tan(-x) = -\tan x$, $\csc(-x) = -\csc x$, $\cot(-x) = -\cot x$

The two tables below are the full reference, carried over from `Q01.1`.
They are split into two five-column tables so each one fits a phone screen held sideways.
Note the header marks $\cos$ and $\sec$ as the even functions, which is the first move on any negative angle.

Do not try to memorize 33 rows.
Reduce your angle to a reference angle in $[0^\circ, 90^\circ]$, read the magnitude off the top of the table, then attach the sign from ASTC.

### Table 1 of 2 - sine, cosine and tangent

| deg | rad | $\sin x$ | $\cos x$ (even) | $\tan x$ |
| ---: | :--- | :--- | :--- | :--- |
| 0 | $0$ | $0$ | $1$ | $0$ |
| 15 | $\frac{\pi}{12}$ | $\frac{\sqrt6-\sqrt2}{4}$ | $\frac{\sqrt6+\sqrt2}{4}$ | $2-\sqrt3$ |
| 22.5 | $\frac{\pi}{8}$ | $\frac{\sqrt{2-\sqrt2}}{2}$ | $\frac{\sqrt{2+\sqrt2}}{2}$ | $\sqrt2-1$ |
| 30 | $\frac{\pi}{6}$ | $\frac12$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt3}{3}$ |
| 45 | $\frac{\pi}{4}$ | $\frac{\sqrt2}{2}$ | $\frac{\sqrt2}{2}$ | $1$ |
| 60 | $\frac{\pi}{3}$ | $\frac{\sqrt3}{2}$ | $\frac12$ | $\sqrt3$ |
| 67.5 | $\frac{3\pi}{8}$ | $\frac{\sqrt{2+\sqrt2}}{2}$ | $\frac{\sqrt{2-\sqrt2}}{2}$ | $\sqrt2+1$ |
| 75 | $\frac{5\pi}{12}$ | $\frac{\sqrt6+\sqrt2}{4}$ | $\frac{\sqrt6-\sqrt2}{4}$ | $2+\sqrt3$ |
| 90 | $\frac{\pi}{2}$ | $1$ | $0$ | undefined |
| 105 | $\frac{7\pi}{12}$ | $\frac{\sqrt6+\sqrt2}{4}$ | $-\frac{\sqrt6-\sqrt2}{4}$ | $-(2+\sqrt3)$ |
| 112.5 | $\frac{5\pi}{8}$ | $\frac{\sqrt{2+\sqrt2}}{2}$ | $-\frac{\sqrt{2-\sqrt2}}{2}$ | $-(\sqrt2+1)$ |
| 120 | $\frac{2\pi}{3}$ | $\frac{\sqrt3}{2}$ | $-\frac12$ | $-(\sqrt3)$ |
| 135 | $\frac{3\pi}{4}$ | $\frac{\sqrt2}{2}$ | $-\frac{\sqrt2}{2}$ | $-(1)$ |
| 150 | $\frac{5\pi}{6}$ | $\frac12$ | $-\frac{\sqrt3}{2}$ | $-\frac{\sqrt3}{3}$ |
| 157.5 | $\frac{7\pi}{8}$ | $\frac{\sqrt{2-\sqrt2}}{2}$ | $-\frac{\sqrt{2+\sqrt2}}{2}$ | $-(\sqrt2-1)$ |
| 165 | $\frac{11\pi}{12}$ | $\frac{\sqrt6-\sqrt2}{4}$ | $-\frac{\sqrt6+\sqrt2}{4}$ | $-(2-\sqrt3)$ |
| 180 | $\pi$ | $0$ | $-(1)$ | $0$ |
| 195 | $\frac{13\pi}{12}$ | $-\frac{\sqrt6-\sqrt2}{4}$ | $-\frac{\sqrt6+\sqrt2}{4}$ | $2-\sqrt3$ |
| 202.5 | $\frac{9\pi}{8}$ | $-\frac{\sqrt{2-\sqrt2}}{2}$ | $-\frac{\sqrt{2+\sqrt2}}{2}$ | $\sqrt2-1$ |
| 210 | $\frac{7\pi}{6}$ | $-\frac12$ | $-\frac{\sqrt3}{2}$ | $\frac{\sqrt3}{3}$ |
| 225 | $\frac{5\pi}{4}$ | $-\frac{\sqrt2}{2}$ | $-\frac{\sqrt2}{2}$ | $1$ |
| 240 | $\frac{4\pi}{3}$ | $-\frac{\sqrt3}{2}$ | $-\frac12$ | $\sqrt3$ |
| 247.5 | $\frac{11\pi}{8}$ | $-\frac{\sqrt{2+\sqrt2}}{2}$ | $-\frac{\sqrt{2-\sqrt2}}{2}$ | $\sqrt2+1$ |
| 255 | $\frac{17\pi}{12}$ | $-\frac{\sqrt6+\sqrt2}{4}$ | $-\frac{\sqrt6-\sqrt2}{4}$ | $2+\sqrt3$ |
| 270 | $\frac{3\pi}{2}$ | $-(1)$ | $0$ | undefined |
| 285 | $\frac{19\pi}{12}$ | $-\frac{\sqrt6+\sqrt2}{4}$ | $\frac{\sqrt6-\sqrt2}{4}$ | $-(2+\sqrt3)$ |
| 292.5 | $\frac{13\pi}{8}$ | $-\frac{\sqrt{2+\sqrt2}}{2}$ | $\frac{\sqrt{2-\sqrt2}}{2}$ | $-(\sqrt2+1)$ |
| 300 | $\frac{5\pi}{3}$ | $-\frac{\sqrt3}{2}$ | $\frac12$ | $-(\sqrt3)$ |
| 315 | $\frac{7\pi}{4}$ | $-\frac{\sqrt2}{2}$ | $\frac{\sqrt2}{2}$ | $-(1)$ |
| 330 | $\frac{11\pi}{6}$ | $-\frac12$ | $\frac{\sqrt3}{2}$ | $-\frac{\sqrt3}{3}$ |
| 337.5 | $\frac{15\pi}{8}$ | $-\frac{\sqrt{2-\sqrt2}}{2}$ | $\frac{\sqrt{2+\sqrt2}}{2}$ | $-(\sqrt2-1)$ |
| 345 | $\frac{23\pi}{12}$ | $-\frac{\sqrt6-\sqrt2}{4}$ | $\frac{\sqrt6+\sqrt2}{4}$ | $-(2-\sqrt3)$ |
| 360 | $2\pi$ | $0$ | $1$ | $0$ |

### Table 2 of 2 - cosecant, secant and cotangent

| deg | rad | $\csc x$ | $\sec x$ (even) | $\cot x$ |
| ---: | :--- | :--- | :--- | :--- |
| 0 | $0$ | undefined | $1$ | undefined |
| 15 | $\frac{\pi}{12}$ | $\sqrt6+\sqrt2$ | $\sqrt6-\sqrt2$ | $2+\sqrt3$ |
| 22.5 | $\frac{\pi}{8}$ | $\sqrt{4+2\sqrt2}$ | $\sqrt{4-2\sqrt2}$ | $\sqrt2+1$ |
| 30 | $\frac{\pi}{6}$ | $2$ | $\frac{2\sqrt3}{3}$ | $\sqrt3$ |
| 45 | $\frac{\pi}{4}$ | $\sqrt2$ | $\sqrt2$ | $1$ |
| 60 | $\frac{\pi}{3}$ | $\frac{2\sqrt3}{3}$ | $2$ | $\frac{\sqrt3}{3}$ |
| 67.5 | $\frac{3\pi}{8}$ | $\sqrt{4-2\sqrt2}$ | $\sqrt{4+2\sqrt2}$ | $\sqrt2-1$ |
| 75 | $\frac{5\pi}{12}$ | $\sqrt6-\sqrt2$ | $\sqrt6+\sqrt2$ | $2-\sqrt3$ |
| 90 | $\frac{\pi}{2}$ | $1$ | undefined | $0$ |
| 105 | $\frac{7\pi}{12}$ | $\sqrt6-\sqrt2$ | $-(\sqrt6+\sqrt2)$ | $-(2-\sqrt3)$ |
| 112.5 | $\frac{5\pi}{8}$ | $\sqrt{4-2\sqrt2}$ | $-(\sqrt{4+2\sqrt2})$ | $-(\sqrt2-1)$ |
| 120 | $\frac{2\pi}{3}$ | $\frac{2\sqrt3}{3}$ | $-(2)$ | $-\frac{\sqrt3}{3}$ |
| 135 | $\frac{3\pi}{4}$ | $\sqrt2$ | $-(\sqrt2)$ | $-(1)$ |
| 150 | $\frac{5\pi}{6}$ | $2$ | $-\frac{2\sqrt3}{3}$ | $-(\sqrt3)$ |
| 157.5 | $\frac{7\pi}{8}$ | $\sqrt{4+2\sqrt2}$ | $-(\sqrt{4-2\sqrt2})$ | $-(\sqrt2+1)$ |
| 165 | $\frac{11\pi}{12}$ | $\sqrt6+\sqrt2$ | $-(\sqrt6-\sqrt2)$ | $-(2+\sqrt3)$ |
| 180 | $\pi$ | undefined | $-(1)$ | undefined |
| 195 | $\frac{13\pi}{12}$ | $-(\sqrt6+\sqrt2)$ | $-(\sqrt6-\sqrt2)$ | $2+\sqrt3$ |
| 202.5 | $\frac{9\pi}{8}$ | $-(\sqrt{4+2\sqrt2})$ | $-(\sqrt{4-2\sqrt2})$ | $\sqrt2+1$ |
| 210 | $\frac{7\pi}{6}$ | $-(2)$ | $-\frac{2\sqrt3}{3}$ | $\sqrt3$ |
| 225 | $\frac{5\pi}{4}$ | $-(\sqrt2)$ | $-(\sqrt2)$ | $1$ |
| 240 | $\frac{4\pi}{3}$ | $-\frac{2\sqrt3}{3}$ | $-(2)$ | $\frac{\sqrt3}{3}$ |
| 247.5 | $\frac{11\pi}{8}$ | $-(\sqrt{4-2\sqrt2})$ | $-(\sqrt{4+2\sqrt2})$ | $\sqrt2-1$ |
| 255 | $\frac{17\pi}{12}$ | $-(\sqrt6-\sqrt2)$ | $-(\sqrt6+\sqrt2)$ | $2-\sqrt3$ |
| 270 | $\frac{3\pi}{2}$ | $-(1)$ | undefined | $0$ |
| 285 | $\frac{19\pi}{12}$ | $-(\sqrt6-\sqrt2)$ | $\sqrt6+\sqrt2$ | $-(2-\sqrt3)$ |
| 292.5 | $\frac{13\pi}{8}$ | $-(\sqrt{4-2\sqrt2})$ | $\sqrt{4+2\sqrt2}$ | $-(\sqrt2-1)$ |
| 300 | $\frac{5\pi}{3}$ | $-\frac{2\sqrt3}{3}$ | $2$ | $-\frac{\sqrt3}{3}$ |
| 315 | $\frac{7\pi}{4}$ | $-(\sqrt2)$ | $\sqrt2$ | $-(1)$ |
| 330 | $\frac{11\pi}{6}$ | $-(2)$ | $\frac{2\sqrt3}{3}$ | $-(\sqrt3)$ |
| 337.5 | $\frac{15\pi}{8}$ | $-(\sqrt{4+2\sqrt2})$ | $\sqrt{4-2\sqrt2}$ | $-(\sqrt2+1)$ |
| 345 | $\frac{23\pi}{12}$ | $-(\sqrt6+\sqrt2)$ | $\sqrt6-\sqrt2$ | $-(2+\sqrt3)$ |
| 360 | $2\pi$ | undefined | $1$ | undefined |

How to read the two tables:

- The five rows to have cold are $0$, $30$, $45$, $60$, $90$.
- Everything else is one of those five with a sign change from ASTC, or a member of the 15-degree family or the 22.5-degree family.
- The 15-degree family uses only $\dfrac{\sqrt6+\sqrt2}{4}$ and $\dfrac{\sqrt6-\sqrt2}{4}$ for sine and cosine, and only $2+\sqrt3$ and $2-\sqrt3$ for tangent.
- The 22.5-degree family uses only $\dfrac{\sqrt{2+\sqrt2}}{2}$ and $\dfrac{\sqrt{2-\sqrt2}}{2}$, and only $\sqrt2+1$ and $\sqrt2-1$.
- Table 2 is Table 1 turned upside down, sign and all, because a reciprocal keeps the sign of what it came from.
- $\lvert\csc\rvert$ and $\lvert\sec\rvert$ are never less than $1$, which is a free sanity check.
- $\tan$ and $\sec$ are undefined at $90^\circ$ and $270^\circ$, where cosine is zero.
- $\cot$ and $\csc$ are undefined at $0^\circ$, $180^\circ$ and $360^\circ$, where sine is zero.
- Tangent and cotangent repeat every $180^\circ$ with no sign change, which is why $15^\circ$ and $195^\circ$ share $\tan = 2-\sqrt3$.
- For an angle outside $[0^\circ, 360^\circ]$, add or subtract full turns first: $\dfrac{25\pi}{12} = 375^\circ$ is coterminal with $15^\circ$.

Practice:

- `Q01.1`.

## Graph transformations

Concept:

- Transform a parent graph in a fixed order.

Know:

- For `y = a f(b(x - h)) + k`, work inside out.
  - Math: $y = a\,f\big(b(x - h)\big) + k$
- Horizontal shift first, then horizontal stretch or reflection.
- Then vertical stretch, then vertical reflection, then vertical shift.
- The horizontal shift feels backwards: `(x + 4)` means left 4.
  - Math: $(x + 4)$ means a shift left by $4$

Practice:

- `Q02.1` and `Q02.2`.

## Limits and continuity

Concept:

- A function is continuous at a point if the limit equals the function value.

Know:

- Continuity needs three things: `f(a)` exists, the limit exists, and they are equal.
  - Math: $f(a)$ is defined, $\displaystyle\lim_{x\to a}f(x)$ exists, and $\displaystyle\lim_{x\to a}f(x) = f(a)$
- Differentiable implies continuous, but not the reverse.
- `|x|` is continuous but not differentiable at 0.
  - Math: $\lvert x\rvert$ is continuous at $0$ but not differentiable there.

Practice:

- `Q03.1`, `Q03.2`, `Q03.3`.

## Asymptotes

Concept:

- Vertical asymptotes come from remaining denominator zeros.
- Horizontal asymptotes come from limits at infinity.

Know:

- Factor and cancel first.
- A canceled factor is a hole, not an asymptote.
- For a rational function, compare degrees for the horizontal asymptote.
  - Math: if $\deg$ numerator $<$ $\deg$ denominator then $y = 0$; if equal then $y$ is the ratio of leading coefficients; if greater then there is no horizontal asymptote.

Practice:

- `Q04.1`.

## Tangent lines and perpendicular slopes

Concept:

- The slope of the tangent line at `a` is `f'(a)`.
  - Math: the slope at $x = a$ is $f'(a)$

Know:

- Parallel means equal slopes.
- Perpendicular means negative reciprocal slopes.
- Perpendicular to slope `m` means `f'(x) = -1/m`.
  - Math: $f'(x) = -\dfrac{1}{m}$
- Point-slope form of the tangent line: `y - f(a) = f'(a)(x - a)`.
  - Math: $y - f(a) = f'(a)(x - a)$

Practice:

- `Q09.1`.

## Implicit differentiation

Concept:

- Differentiate both sides with respect to `x`.
- Every `y` produces a `y'` by the chain rule.
  - Math: $\dfrac{d}{dx}\big(y^{n}\big) = n\,y^{n-1}y'$

Know:

- Products of `x` and `y` need the product rule.
  - Math: $\dfrac{d}{dx}(xy) = y + xy'$
- Collect all `y'` terms, factor, and solve.

Practice:

- `Q10.1` and `Q10.2`.

## Related rates

Concept:

- Variables change with time.
- Differentiate an equation with respect to `t`.
  - Math: differentiate with respect to $t$

Know:

- Name the variables and write what is given and wanted as derivatives with respect to `t`.
  - Math: given $\dfrac{dA}{dt}$, wanted $\dfrac{dB}{dt}$
- Eliminate variables you have no rate for before differentiating.
- Substitute numbers only after differentiating.

Practice:

- Gravel cone: `Q11.1`.
- Rocket and radar: `Q11.2`.

## Linear approximation and differentials

Concept:

- Use the tangent line to estimate nearby values.

Know:

- `f(a + dx) ≈ f(a) + f'(a) dx`.
  - Math: $f(a + dx) \approx f(a) + f'(a)\,dx$
- Choose `a` as the nearest value you know exactly.
- Convert degrees to radians for trig problems.
  - Math: $1^\circ = \dfrac{\pi}{180}$ radians

Practice:

- `Q12.1`, `Q12.2`, and `Q12.3`.

## Newton's method

Concept:

- Approximate a root with repeated tangent-line steps.

Know:

- `x_(n+1) = x_n - f(x_n) / f'(x_n)`.
  - Math: $x_{n+1} = x_{n} - \dfrac{f(x_{n})}{f'(x_{n})}$
- Keep all decimals between steps and round only at the end.

Practice:

- `Q13.1`.

## Curve sketching with calculus

Concept:

- Use domain, asymptotes, `f'`, and `f''` to build an accurate graph.
  - Math: use $f'$ and $f''$

Know:

- `f' = 0` gives critical points.
  - Math: $f'(x) = 0$
- `f'` undefined while `f` is defined gives a cusp or vertical tangent.
- Sign of `f'` gives increasing and decreasing.
- Sign of `f''` gives concavity and inflection points.

Practice:

- `Q14.1`.

## Extreme values on a closed interval

Concept:

- On a closed interval, absolute extrema happen at critical numbers or endpoints.

Know:

- List all critical numbers where `f' = 0` or `f'` is undefined.
  - Math: $f'(c) = 0$ or $f'(c)$ does not exist
- Evaluate `f` at those numbers and at both endpoints.
- The largest value is the absolute max and the smallest is the absolute min.

Practice:

- `Q15.1`, `Q15.3`, and `Q15.5`.

## Optimization

Concept:

- Convert a word problem into a one-variable function and optimize it.

Know:

- Fixed area and least perimeter give a square.
- Fixed volume and cheapest cost require including all differently priced surfaces.

Practice:

- `Q15.2` and `Q15.4`.

## Properties of the definite integral and bounding

Concept:

- Bounds on a function produce bounds on its integral.

Know:

- If `m <= f(x) <= M` on `[a, b]`, then `m(b - a) <= ∫ f <= M(b - a)`.
  - Math: if $m \le f(x) \le M$ on $[a,b]$, then $m(b-a) \le \displaystyle\int_{a}^{b} f(x)\,dx \le M(b-a)$
- The width is `b - a`, not just `b`.
  - Math: the width is $b - a$

Practice:

- `Q17.1`, `Q17.2`, and `Q17.3`.

## Area between curves

Concept:

- Integrate upper curve minus lower curve.

Know:

- Find intersection points by setting the curves equal.
  - Math: $A = \displaystyle\int_{a}^{b}\big(y_{\text{top}} - y_{\text{bottom}}\big)\,dx$
- If the curves cross inside the interval, split the integral.

Practice:

- `Q19.1` and `Q19.2`.

## Net change and motion

Concept:

- Net change equals the integral of a rate.

Know:

- Displacement is `∫ v dt`.
  - Math: displacement $= \displaystyle\int_{a}^{b} v(t)\,dt$
- Distance is `∫ |v| dt`.
  - Math: distance $= \displaystyle\int_{a}^{b} \lvert v(t)\rvert\,dt$
- Split distance at the zeros of velocity.

Practice:

- `Q19.3`, `Q19.8`, and `Q19.9`.

## Work

Concept:

- Work equals force integrated over distance.

Know:

- Spring: `F = kx`, so `W = (1/2) k d^2`.
  - Math: $F = kx$, so $W = \displaystyle\int_{0}^{d} kx\,dx = \tfrac{1}{2}kd^{2}$
- Chain: integrate the weight of each small piece over the height it is lifted.
  - Math: $W = \displaystyle\int \rho\,g\,y\,dy$

Practice:

- `Q19.4` and `Q19.5`.

## Average value of a function

Concept:

- Average value is the integral divided by the interval width.

Know:

- `f_avg = (1 / (b - a)) ∫[a to b] f(x) dx`.
  - Math: $f_{\text{avg}} = \dfrac{1}{b-a}\displaystyle\int_{a}^{b} f(x)\,dx$

Practice:

- `Q19.6` and `Q19.7`.

---
# Part 5: Every exam question, restated and solved

This part restates all 49 questions from the question bank `notes\MATH265.md` in ordinary mathematical symbols, then works each one step by step.

How each entry is laid out:

- **Question** is the question restated in mathematical symbols.
- **Steps** are the working, with the reason for each move.
- **Answer** is the result in mathematical symbols.
- **Möbius** is the same result flattened into the text you type into the answer box.

Every numeric and symbolic result below was independently recomputed in Python with `sympy` before it was written down.
Where a sketch is the answer, the entry describes exactly what the sketch must show, because a machine cannot mark a drawing and a human marker will look for those features.

---

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

## 3. Limits and continuity

### Q3.1 - Five limits, algebraic and trigonometric

**Question.**
Evaluate each limit; if it does not exist, explain why.

- a. $\displaystyle\lim_{x\to 2}\left(3x^{2} - 2x + 1\right)$
- b. $\displaystyle\lim_{x\to -2}\dfrac{3x^{2} - 2x - 16}{(x+2)^{2}}$
- c. $\displaystyle\lim_{x\to 3}\dfrac{2x^{2} - x + 1}{x - 3}$
- d. $\displaystyle\lim_{x\to 2}\dfrac{\sqrt{6-x} - 2}{\sqrt{3-x} - 1}$
- e. $\displaystyle\lim_{x\to 0}\dfrac{\sin(3x)}{x^{2} - x}$

**Part a.**
A polynomial is continuous everywhere, so direct substitution is legal.

$$3(2)^{2} - 2(2) + 1 = 12 - 4 + 1 = 9$$

**Answer a.** $9$. **Möbius:** `9`

**Part b, step 1: substitute and diagnose.**
Numerator at $x = -2$: $3(4) - 2(-2) - 16 = 12 + 4 - 16 = 0$.
Denominator: $0$.
So this is $\dfrac{0}{0}$ and must be rewritten.

**Part b, step 2: factor the numerator.**
The roots of $3x^{2} - 2x - 16$ are $x = \dfrac{2 \pm 14}{6}$, that is $\dfrac{8}{3}$ and $-2$.

$$3x^{2} - 2x - 16 = (x+2)(3x-8)$$

**Part b, step 3: cancel one factor.**

$$\frac{(x+2)(3x-8)}{(x+2)^{2}} = \frac{3x-8}{x+2}$$

**Part b, step 4: re-diagnose.**
Now the numerator tends to $3(-2) - 8 = -14$, which is not zero, while the denominator tends to $0$.
This is the $\dfrac{k}{0}$ case, so check each side.

$$x \to -2^{-}:\ x+2 \to 0^{-},\ \frac{-14}{0^{-}} \to +\infty$$

$$x \to -2^{+}:\ x+2 \to 0^{+},\ \frac{-14}{0^{+}} \to -\infty$$

**Answer b.**
The limit **does not exist**, because the left limit is $+\infty$ and the right limit is $-\infty$, so the two one-sided limits disagree.

**Möbius:** `DNE`

**Part c, step 1: substitute and diagnose.**
Numerator: $2(9) - 3 + 1 = 16$, not zero.
Denominator: $0$.
This is $\dfrac{k}{0}$ with $k \neq 0$, so there is nothing to cancel; go straight to the sides.

$$x \to 3^{-}:\ \frac{16}{0^{-}} \to -\infty \qquad x \to 3^{+}:\ \frac{16}{0^{+}} \to +\infty$$

**Answer c.**
The limit **does not exist**; the function drops to $-\infty$ on the left of $3$ and rises to $+\infty$ on the right, so $x = 3$ is a vertical asymptote with opposite behaviour on the two sides.

**Möbius:** `DNE`

**Part d, step 1: substitute and diagnose.**
Numerator: $\sqrt{4} - 2 = 0$. Denominator: $\sqrt{1} - 1 = 0$.
This is $\dfrac{0}{0}$, and the presence of roots says rationalize.

**Part d, step 2: multiply by both conjugates at once.**
Multiply top and bottom by $\left(\sqrt{6-x}+2\right)$ and by $\left(\sqrt{3-x}+1\right)$.

The numerator conjugate product is $(6-x) - 4 = 2-x$.
The denominator conjugate product is $(3-x) - 1 = 2-x$.

$$\frac{\sqrt{6-x}-2}{\sqrt{3-x}-1} = \frac{(2-x)\left(\sqrt{3-x}+1\right)}{(2-x)\left(\sqrt{6-x}+2\right)}$$

**Part d, step 3: cancel the common $(2-x)$.**
This is the whole trick: the same factor $2-x$ appears top and bottom.

$$= \frac{\sqrt{3-x}+1}{\sqrt{6-x}+2}$$

**Part d, step 4: now substitute.**

$$= \frac{\sqrt{1}+1}{\sqrt{4}+2} = \frac{2}{4} = \frac{1}{2}$$

**Answer d.** $\dfrac{1}{2}$. **Möbius:** `1/2`

**Part e, step 1: diagnose.**
$\sin(0) = 0$ and $0^{2} - 0 = 0$, so it is $\dfrac{0}{0}$, and the $\sin$ says use the special limit.

**Part e, step 2: factor the denominator and build the special limit.**
The special limit is $\displaystyle\lim_{u\to 0}\frac{\sin u}{u} = 1$, so force a $3x$ under the $\sin(3x)$.

$$\frac{\sin(3x)}{x^{2}-x} = \frac{\sin(3x)}{x(x-1)} = \frac{\sin(3x)}{3x}\cdot\frac{3x}{x(x-1)} = \frac{\sin(3x)}{3x}\cdot\frac{3}{x-1}$$

**Part e, step 3: take the limit of each factor.**

$$\to 1 \cdot \frac{3}{0-1} = -3$$

**Answer e.** $-3$. **Möbius:** `-3`

### Q3.2 - Six limits, with justification required

**Question.**
Evaluate each limit; if it does not exist, explain why.
No credit for unjustified answers.

- a. $\displaystyle\lim_{x\to 1}\dfrac{x^{2}-1}{x^{3}-1}$
- b. $\displaystyle\lim_{x\to 0}\dfrac{x^{2}}{1-\cos(2x)}$
- c. $\displaystyle\lim_{x\to 0}\dfrac{6x-9}{x^{3}-12x+3}$
- d. $\displaystyle\lim_{x\to\infty}\dfrac{5-2x^{3}}{x^{2}+2}$
- e. $\displaystyle\lim_{x\to-\pi/3}\dfrac{\tan(2x)}{3x+\pi}$
- f. $\displaystyle\lim_{x\to 2}\dfrac{\cos(\pi x)}{(x-2)^{2}}$

**Part a, step 1: diagnose.**
Both $x^{2}-1$ and $x^{3}-1$ vanish at $x=1$, so it is $\dfrac{0}{0}$ and $(x-1)$ is a common factor.

**Part a, step 2: factor both.**

$$x^{2}-1 = (x-1)(x+1), \qquad x^{3}-1 = (x-1)\left(x^{2}+x+1\right)$$

**Part a, step 3: cancel and substitute.**

$$\frac{(x-1)(x+1)}{(x-1)\left(x^{2}+x+1\right)} = \frac{x+1}{x^{2}+x+1} \to \frac{2}{3}$$

**Answer a.** $\dfrac{2}{3}$. **Möbius:** `2/3`

**Part b, step 1: diagnose.**
$1 - \cos 0 = 0$ and $0^{2}=0$, so $\dfrac{0}{0}$.

**Part b, step 2: replace the cosine with an identity.**
Use $1 - \cos(2\theta) = 2\sin^{2}\theta$ with $\theta = x$.
This is cleaner than the half-angle route because it removes the cosine entirely.

$$\frac{x^{2}}{1-\cos(2x)} = \frac{x^{2}}{2\sin^{2}x}$$

**Part b, step 3: build the special limit.**

$$= \frac{1}{2}\left(\frac{x}{\sin x}\right)^{2} \to \frac{1}{2}(1)^{2} = \frac{1}{2}$$

**Answer b.** $\dfrac{1}{2}$. **Möbius:** `1/2`

**Part c, step 1: substitute.**
This one is not indeterminate at all, which is the point of including it.

$$\frac{6(0)-9}{0-0+3} = \frac{-9}{3} = -3$$

**Answer c.** $-3$. **Möbius:** `-3`

**Part d, step 1: diagnose.**
Both parts grow without bound, so it is $\dfrac{\infty}{\infty}$.

**Part d, step 2: divide by the highest power in the denominator, $x^{2}$.**

$$\frac{5-2x^{3}}{x^{2}+2} = \frac{\frac{5}{x^{2}} - 2x}{1 + \frac{2}{x^{2}}}$$

**Part d, step 3: take the limit.**
The numerator behaves like $-2x \to -\infty$ and the denominator tends to $1$.

**Answer d.**

$$\lim_{x\to\infty}\frac{5-2x^{3}}{x^{2}+2} = -\infty$$

The degree of the numerator exceeds the degree of the denominator, so there is no horizontal asymptote, and the negative leading coefficient sends it to $-\infty$.

**Möbius:** `-infinity`

**Part e, step 1: substitute carefully.**
The denominator $3x + \pi \to 3\left(-\dfrac{\pi}{3}\right) + \pi = 0$.
For the numerator, $2x \to -\dfrac{2\pi}{3}$, and

$$\tan\left(-\frac{2\pi}{3}\right) = -\tan\left(\frac{2\pi}{3}\right) = -\left(-\sqrt3\right) = \sqrt3$$

**Part e, step 2: diagnose.**
This is $\dfrac{\sqrt3}{0}$, not $\dfrac{0}{0}$, so there is nothing to cancel.
Check the sides.

$$x \to \left(-\tfrac{\pi}{3}\right)^{-}: 3x+\pi \to 0^{-}, \quad \frac{\sqrt3}{0^{-}} \to -\infty$$

$$x \to \left(-\tfrac{\pi}{3}\right)^{+}: 3x+\pi \to 0^{+}, \quad \frac{\sqrt3}{0^{+}} \to +\infty$$

**Answer e.**
The limit **does not exist**, because the numerator tends to $\sqrt3 \neq 0$ while the denominator tends to $0$ through both signs, giving $-\infty$ from the left and $+\infty$ from the right.

**Möbius:** `DNE`

**Trap.** This looks like it should be a $\dfrac{0}{0}$ tangent limit, so people reach for $\dfrac{\tan u}{u} \to 1$. Check the numerator first: $\tan\left(-\dfrac{2\pi}{3}\right) = \sqrt3$, not $0$, so that tool does not apply.

**Part f, step 1: substitute.**
Numerator: $\cos(2\pi) = 1$.
Denominator: $(2-2)^{2} = 0$, and because it is squared it approaches $0$ from the **positive** side only.

**Part f, step 2: read the sign.**

$$\frac{1}{0^{+}} \to +\infty \quad\text{from both sides}$$

**Answer f.**

$$\lim_{x\to 2}\frac{\cos(\pi x)}{(x-2)^{2}} = +\infty$$

The limit does not exist as a finite number, but because the squared denominator is positive on both sides the function goes to $+\infty$ from both directions, so we may write the limit as $+\infty$.

**Möbius:** `infinity`

### Q3.3 - Two limits, at infinity and at an asymptote

**Question.**
Evaluate; no credit for unjustified answers.

- a. $\displaystyle\lim_{x\to\infty}\left(\dfrac{3x^{2}-4}{4+2x+2x^{4}}\right)\sin x$
- b. $\displaystyle\lim_{x\to 5\pi/2}\tan x$

**Part a, step 1: split the product.**
The $\sin x$ has no limit at infinity, so do not try to evaluate the product directly.
Handle the rational factor on its own.

**Part a, step 2: limit of the rational factor.**
The denominator has degree 4 and the numerator degree 2, so the fraction dies.

$$\lim_{x\to\infty}\frac{3x^{2}-4}{2x^{4}+2x+4} = \lim_{x\to\infty}\frac{\frac{3}{x^{2}} - \frac{4}{x^{4}}}{2 + \frac{2}{x^{3}} + \frac{4}{x^{4}}} = \frac{0}{2} = 0$$

**Part a, step 3: bound the oscillating factor.**

$$-1 \le \sin x \le 1 \quad\text{for all } x$$

**Part a, step 4: apply the Squeeze Theorem.**
Let $R(x)$ be the rational factor. Then

$$-\lvert R(x)\rvert \le R(x)\sin x \le \lvert R(x)\rvert$$

Both outer bounds tend to $0$, so the middle is squeezed to $0$.

**Answer a.** $0$, by the Squeeze Theorem: a bounded factor times a factor going to zero goes to zero.

**Möbius:** `0`

**Part b, step 1: locate the angle.**

$$\frac{5\pi}{2} = 2\pi + \frac{\pi}{2}$$

so this is coterminal with $\dfrac{\pi}{2}$, where $\cos x = 0$ and $\tan x$ is undefined.

**Part b, step 2: check both sides.**
Write $\tan x = \dfrac{\sin x}{\cos x}$, with $\sin\left(\dfrac{5\pi}{2}\right) = 1$.

$$x \to \left(\tfrac{5\pi}{2}\right)^{-}: \cos x \to 0^{+}, \quad \tan x \to +\infty$$

$$x \to \left(\tfrac{5\pi}{2}\right)^{+}: \cos x \to 0^{-}, \quad \tan x \to -\infty$$

**Answer b.**
The limit **does not exist**, because $\tan x \to +\infty$ from the left and $\tan x \to -\infty$ from the right; $x = \dfrac{5\pi}{2}$ is a vertical asymptote of the tangent.

**Möbius:** `DNE`

---

## 4. Asymptotes

### Q4.1 - Vertical and horizontal asymptotes of a rational function

**Question.**
Find the vertical and horizontal asymptotes of

$$f(x) = \frac{x^{2}-3x-4}{x^{2}-16}$$

**Step 1: factor both parts before doing anything else.**
This is the whole question; unfactored, you will report an asymptote that is not there.

$$x^{2}-3x-4 = (x-4)(x+1), \qquad x^{2}-16 = (x-4)(x+4)$$

**Step 2: note the original domain.**
Before cancelling, the denominator bans $x = 4$ and $x = -4$.

$$f(x) = \frac{(x-4)(x+1)}{(x-4)(x+4)}$$

**Step 3: cancel, and record what the cancellation means.**

$$f(x) = \frac{x+1}{x+4}, \qquad x \neq 4$$

A cancelled factor is a **hole**, not an asymptote.
The hole sits at

$$x = 4, \qquad y = \frac{4+1}{4+4} = \frac{5}{8}$$

**Step 4: vertical asymptote from the surviving denominator zero.**

$$x + 4 = 0 \implies x = -4$$

Confirm it really blows up, since the numerator there is $-4+1 = -3 \neq 0$.

$$x \to -4^{-}: \frac{-3}{0^{-}} \to +\infty \qquad x \to -4^{+}: \frac{-3}{0^{+}} \to -\infty$$

**Step 5: horizontal asymptote by comparing degrees.**
Numerator and denominator of the original both have degree 2, so the limit is the ratio of leading coefficients.

$$\lim_{x\to\pm\infty}\frac{x^{2}-3x-4}{x^{2}-16} = \frac{1}{1} = 1$$

**Answer.**

$$\text{Vertical asymptote: } x = -4 \qquad \text{Horizontal asymptote: } y = 1$$

$$\text{Hole at } \left(4, \tfrac{5}{8}\right), \text{ which is not an asymptote}$$

**Möbius:** VA `x=-4`, HA `y=1`, hole at `(4,5/8)`

**Trap.** Reporting $x = 4$ as a vertical asymptote. The factor $(x-4)$ cancels, so the graph has a removable discontinuity there, a single missing point, not a blow-up.

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

## 7. The derivative from its definition

### Q7.1 - Derivative of cotangent from the definition

**Question.**
Use the definition of the derivative as a limit to compute the derivative of $\cot x$.

**Step 1: write the definition.**
The word "definition" means the limit must appear; a table lookup earns zero.

$$\frac{d}{dx}\cot x = \lim_{h\to 0}\frac{\cot(x+h) - \cot x}{h}$$

**Step 2: convert to sine and cosine.**
Cotangent addition formulas are ugly; the sine and cosine form is far cleaner.

$$\cot(x+h) - \cot x = \frac{\cos(x+h)}{\sin(x+h)} - \frac{\cos x}{\sin x}$$

**Step 3: combine over a common denominator.**

$$= \frac{\cos(x+h)\sin x - \cos x\,\sin(x+h)}{\sin(x+h)\sin x}$$

**Step 4: recognise the sine difference identity.**
The numerator is exactly $\sin(A - B) = \sin A\cos B - \cos A\sin B$ with $A = x$ and $B = x+h$.

$$\cos(x+h)\sin x - \cos x\sin(x+h) = \sin\big(x - (x+h)\big) = \sin(-h) = -\sin h$$

This collapse is the whole point of the question.

**Step 5: put it back into the limit.**

$$\frac{d}{dx}\cot x = \lim_{h\to 0}\frac{1}{h}\cdot\frac{-\sin h}{\sin(x+h)\sin x}$$

**Step 6: separate the special limit.**

$$= \lim_{h\to 0}\left(-\frac{\sin h}{h}\right)\cdot\frac{1}{\sin(x+h)\sin x}$$

**Step 7: evaluate each factor.**
The first factor tends to $-1$ by the special limit $\displaystyle\lim_{h\to0}\frac{\sin h}{h} = 1$.
The second tends to $\dfrac{1}{\sin x\,\sin x}$ because sine is continuous.

$$= -1\cdot\frac{1}{\sin^{2}x} = -\frac{1}{\sin^{2}x}$$

**Step 8: convert to the standard form.**
Since $\csc x = \dfrac{1}{\sin x}$:

**Answer.**

$$\frac{d}{dx}\cot x = -\frac{1}{\sin^{2}x} = -\csc^{2}x$$

**Möbius:** `-csc(x)^2` or equivalently `-1/sin(x)^2`

**Trap.** Writing $\sin(x-(x+h)) = \sin(h)$ and losing the minus sign, which turns the answer into $+\csc^{2}x$. The argument is $-h$, and sine is odd.

---

## 8. Derivative rules and computation

### Q8.1 - Four derivatives, power chain and quotient rules

**Question.**
Compute the derivatives. Simplification is not required.

- a. $y = 4x^{5} + 3x^{4} - 6x^{3} + 6$
- b. $y = \dfrac{2x-16}{(x+3)^{2}}$
- c. $y = \sin\left(2x^{2} - x + 1\right)$
- d. $y = \left(-4x^{3} - x^{2} + 3x + 7\right)^{4}$

**Part a: power rule term by term.**
Multiply each coefficient by its exponent and drop the exponent by one; the constant $6$ dies.

$$y' = 20x^{4} + 12x^{3} - 18x^{2}$$

**Answer a.** $y' = 20x^{4} + 12x^{3} - 18x^{2}$. **Möbius:** `20*x^4+12*x^3-18*x^2`

**Part b, step 1: set up the quotient rule.**
Let $f = 2x-16$ and $g = (x+3)^{2}$, so $f' = 2$ and $g' = 2(x+3)$ by the chain rule.

$$y' = \frac{f'g - fg'}{g^{2}} = \frac{2(x+3)^{2} - (2x-16)\cdot 2(x+3)}{(x+3)^{4}}$$

**Part b, step 2: cancel one factor of $(x+3)$.**
Every term on top carries an $(x+3)$, so one cancels against the bottom.

$$= \frac{2(x+3) - 2(2x-16)}{(x+3)^{3}}$$

**Part b, step 3: expand the numerator.**

$$= \frac{2x + 6 - 4x + 32}{(x+3)^{3}} = \frac{38 - 2x}{(x+3)^{3}}$$

**Answer b.**

$$y' = \frac{38 - 2x}{(x+3)^{3}}$$

**Möbius:** `(38-2*x)/(x+3)^3`

**Part c: chain rule.**
Outside is $\sin(\;)$, whose derivative is $\cos(\;)$; inside is $2x^{2}-x+1$, whose derivative is $4x-1$.

$$y' = \cos\left(2x^{2}-x+1\right)\cdot(4x-1)$$

**Answer c.** **Möbius:** `cos(2*x^2-x+1)*(4*x-1)`

**Part d: chain rule with the power rule outside.**
Outside is $(\;)^{4}$, giving $4(\;)^{3}$; inside derivative is $-12x^{2}-2x+3$.

$$y' = 4\left(-4x^{3}-x^{2}+3x+7\right)^{3}\left(-12x^{2}-2x+3\right)$$

**Answer d.** **Möbius:** `4*(-4*x^3-x^2+3*x+7)^3*(-12*x^2-2*x+3)`

### Q8.2 - Four derivatives, including a second derivative

**Question.**
Find each derivative, showing work. Simplification is not required.

- a. $\dfrac{d^{2}}{dx^{2}}\cot(2x)$
- b. $\dfrac{d}{dx}\sec\left(x^{2}-3x\right)$
- c. $\dfrac{d}{dx}\dfrac{x^{2}-\cos(3x)}{x\sin(2x)}$
- d. $\left.\dfrac{d}{dx}\dfrac{f(x)}{g(x)}\right|_{x=1}$ where $f(1)=3$, $g(1)=6$, $f'(x)=\sqrt{x}$, $g'(x)=3\sin\left(\dfrac{\pi x}{3}\right)$

**Part a, step 1: first derivative.**
$\dfrac{d}{dx}\cot u = -\csc^{2}u$ with $u = 2x$, so multiply by $u' = 2$.

$$\frac{d}{dx}\cot(2x) = -2\csc^{2}(2x)$$

**Part a, step 2: differentiate again.**
Write $\csc^{2}(2x)$ as $\big(\csc(2x)\big)^{2}$ and use the chain rule twice.

$$\frac{d}{dx}\big(\csc(2x)\big)^{2} = 2\csc(2x)\cdot\frac{d}{dx}\csc(2x)$$

$$\frac{d}{dx}\csc(2x) = -\csc(2x)\cot(2x)\cdot 2$$

**Part a, step 3: combine.**

$$\frac{d}{dx}\csc^{2}(2x) = 2\csc(2x)\cdot\big(-2\csc(2x)\cot(2x)\big) = -4\csc^{2}(2x)\cot(2x)$$

**Part a, step 4: apply the leading $-2$.**

$$\frac{d^{2}}{dx^{2}}\cot(2x) = -2\cdot\big(-4\csc^{2}(2x)\cot(2x)\big) = 8\csc^{2}(2x)\cot(2x)$$

**Answer a.**

$$\frac{d^{2}}{dx^{2}}\cot(2x) = 8\csc^{2}(2x)\cot(2x)$$

**Möbius:** `8*csc(2*x)^2*cot(2*x)`

**Trap.** Two minus signs and two inner 2s appear here; the final answer is **positive**. Losing one factor of 2 gives $4$ instead of $8$.

**Part b: chain rule with the secant rule.**
$\dfrac{d}{dx}\sec u = \sec u\tan u$, with $u = x^{2}-3x$ and $u' = 2x-3$.

$$\frac{d}{dx}\sec\left(x^{2}-3x\right) = \sec\left(x^{2}-3x\right)\tan\left(x^{2}-3x\right)(2x-3)$$

**Answer b.** **Möbius:** `sec(x^2-3*x)*tan(x^2-3*x)*(2*x-3)`

**Part c, step 1: name the pieces.**

$$f = x^{2}-\cos(3x), \qquad g = x\sin(2x)$$

**Part c, step 2: differentiate each.**
For $f$, the derivative of $-\cos(3x)$ is $+3\sin(3x)$.
For $g$, use the product rule on $x$ times $\sin(2x)$.

$$f' = 2x + 3\sin(3x), \qquad g' = \sin(2x) + 2x\cos(2x)$$

**Part c, step 3: assemble the quotient rule.**

$$\frac{d}{dx}\frac{f}{g} = \frac{\big(2x+3\sin(3x)\big)\big(x\sin(2x)\big) - \big(x^{2}-\cos(3x)\big)\big(\sin(2x)+2x\cos(2x)\big)}{\big(x\sin(2x)\big)^{2}}$$

**Answer c.** As above; no simplification required.

**Möbius:** `((2*x+3*sin(3*x))*(x*sin(2*x))-(x^2-cos(3*x))*(sin(2*x)+2*x*cos(2*x)))/(x*sin(2*x))^2`

**Part d, step 1: write the quotient rule at a point.**

$$\left.\left(\frac{f}{g}\right)'\right|_{x=1} = \frac{f'(1)g(1) - f(1)g'(1)}{\big(g(1)\big)^{2}}$$

**Part d, step 2: evaluate the two derivatives at $x=1$.**

$$f'(1) = \sqrt{1} = 1$$

$$g'(1) = 3\sin\left(\frac{\pi}{3}\right) = 3\cdot\frac{\sqrt3}{2} = \frac{3\sqrt3}{2}$$

**Part d, step 3: substitute all four numbers.**

$$= \frac{(1)(6) - (3)\left(\frac{3\sqrt3}{2}\right)}{6^{2}} = \frac{6 - \frac{9\sqrt3}{2}}{36}$$

**Part d, step 4: clear the inner fraction.**
Multiply numerator and denominator by 2.

$$= \frac{12 - 9\sqrt3}{72} = \frac{4 - 3\sqrt3}{24}$$

**Answer d.**

$$\left.\frac{d}{dx}\frac{f}{g}\right|_{x=1} = \frac{4-3\sqrt3}{24} \approx -0.04984$$

**Möbius:** `(4-3*sqrt(3))/24`

**Trap.** $\sin\left(\dfrac{\pi x}{3}\right)$ at $x=1$ is $\sin\left(\dfrac{\pi}{3}\right) = \dfrac{\sqrt3}{2}$, in radians. Reading it as $\sin(1^\circ)$ or forgetting the outer 3 both break the answer.

### Q8.3 - Five derivatives, nested chain and quotient rules

**Question.**
Compute the derivatives. Simplification is not required.

- a. $y = \sin x\cdot\cos\left(\sin x^{2}\right)$
- b. $y = \left(\dfrac{1+x^{3}}{1-x^{2}}\right)^{1/3}$
- c. $y = \sqrt{1+\sqrt{1+x}}$
- d. $y = \dfrac{\sqrt{x^{2}-1}}{x^{2}-2x-8}$
- e. $y = \sec^{2}\left(\dfrac{x+1}{x-2}\right)$

**Part a, step 1: identify the outer structure.**
This is a **product** of $\sin x$ and $\cos\left(\sin x^{2}\right)$, so the product rule runs first.

**Part a, step 2: differentiate the second factor, which is three layers deep.**
Layers: $\cos(\;)$, then $\sin(\;)$, then $x^{2}$.

$$\frac{d}{dx}\cos\left(\sin x^{2}\right) = -\sin\left(\sin x^{2}\right)\cdot\cos\left(x^{2}\right)\cdot 2x$$

**Part a, step 3: assemble the product rule.**

$$y' = \cos x\cos\left(\sin x^{2}\right) - \sin x\,\sin\left(\sin x^{2}\right)\cos\left(x^{2}\right)(2x)$$

**Answer a.** **Möbius:** `cos(x)*cos(sin(x^2))-sin(x)*sin(sin(x^2))*cos(x^2)*2*x`

**Trap.** $\sin x^{2}$ means $\sin\left(x^{2}\right)$, not $(\sin x)^{2}$. The inner derivative is $\cos\left(x^{2}\right)\cdot 2x$.

**Part b, step 1: outer power rule.**
Let $u = \dfrac{1+x^{3}}{1-x^{2}}$, so $y = u^{1/3}$ and $y' = \dfrac{1}{3}u^{-2/3}u'$.

**Part b, step 2: quotient rule on $u$.**

$$u' = \frac{3x^{2}\left(1-x^{2}\right) - \left(1+x^{3}\right)(-2x)}{\left(1-x^{2}\right)^{2}}$$

**Part b, step 3: expand the numerator.**

$$3x^{2} - 3x^{4} + 2x + 2x^{4} = -x^{4} + 3x^{2} + 2x$$

**Part b, step 4: assemble.**

$$y' = \frac{1}{3}\left(\frac{1+x^{3}}{1-x^{2}}\right)^{-2/3}\cdot\frac{-x^{4}+3x^{2}+2x}{\left(1-x^{2}\right)^{2}}$$

**Answer b.** **Möbius:** `(1/3)*((1+x^3)/(1-x^2))^(-2/3)*(-x^4+3*x^2+2*x)/(1-x^2)^2`

**Part c, step 1: peel the outer root.**
With $y = \sqrt{v}$ and $v = 1+\sqrt{1+x}$:

$$y' = \frac{1}{2\sqrt{1+\sqrt{1+x}}}\cdot v'$$

**Part c, step 2: differentiate the inner root.**
$\dfrac{d}{dx}\sqrt{1+x} = \dfrac{1}{2\sqrt{1+x}}$, and the derivative of the constant $1$ is zero.

**Part c, step 3: multiply.**

$$y' = \frac{1}{2\sqrt{1+\sqrt{1+x}}}\cdot\frac{1}{2\sqrt{1+x}} = \frac{1}{4\sqrt{1+x}\sqrt{1+\sqrt{1+x}}}$$

**Answer c.**

$$y' = \frac{1}{4\sqrt{1+x}\,\sqrt{1+\sqrt{1+x}}}$$

**Möbius:** `1/(4*sqrt(1+x)*sqrt(1+sqrt(1+x)))`

**Part d, step 1: quotient rule with a chain rule inside.**
Let $f = \sqrt{x^{2}-1}$ and $g = x^{2}-2x-8$.

$$f' = \frac{2x}{2\sqrt{x^{2}-1}} = \frac{x}{\sqrt{x^{2}-1}}, \qquad g' = 2x-2$$

**Part d, step 2: assemble.**

$$y' = \frac{\dfrac{x}{\sqrt{x^{2}-1}}\left(x^{2}-2x-8\right) - \sqrt{x^{2}-1}\,(2x-2)}{\left(x^{2}-2x-8\right)^{2}}$$

**Answer d.** **Möbius:** `((x/sqrt(x^2-1))*(x^2-2*x-8)-sqrt(x^2-1)*(2*x-2))/(x^2-2*x-8)^2`

**Part e, step 1: read the layers.**
$y = \big(\sec u\big)^{2}$ with $u = \dfrac{x+1}{x-2}$: a square, then a secant, then a quotient.

**Part e, step 2: differentiate the inner quotient.**

$$u' = \frac{(1)(x-2) - (x+1)(1)}{(x-2)^{2}} = \frac{x-2-x-1}{(x-2)^{2}} = \frac{-3}{(x-2)^{2}}$$

**Part e, step 3: outer layers.**

$$\frac{d}{dx}\big(\sec u\big)^{2} = 2\sec u\cdot\sec u\tan u\cdot u' = 2\sec^{2}u\tan u\cdot u'$$

**Part e, step 4: substitute.**

$$y' = 2\sec^{2}\left(\frac{x+1}{x-2}\right)\tan\left(\frac{x+1}{x-2}\right)\cdot\frac{-3}{(x-2)^{2}} = \frac{-6\sec^{2}\left(\frac{x+1}{x-2}\right)\tan\left(\frac{x+1}{x-2}\right)}{(x-2)^{2}}$$

**Answer e.** **Möbius:** `-6*sec((x+1)/(x-2))^2*tan((x+1)/(x-2))/(x-2)^2`

### Q8.4 - Two derivatives, naming the rules used

**Question.**
Give the derivatives and **state which rules** you apply. Simplification is not required.

- a. $\dfrac{d}{dx}\dfrac{\tan(2x)}{\sqrt{x}}$
- b. $\left.\dfrac{d}{dx}\cos^{3}\left(x^{2}\right)\right|_{x=\sqrt{\pi}/2}$

**Part a, step 1: name the rules.**
**Quotient rule** on the outside, **chain rule** on $\tan(2x)$, **power rule** on $\sqrt{x} = x^{1/2}$.

**Part a, step 2: the pieces.**

$$f = \tan(2x), \quad f' = 2\sec^{2}(2x), \qquad g = x^{1/2}, \quad g' = \frac{1}{2\sqrt{x}}$$

**Part a, step 3: assemble, noting $g^{2} = x$.**

$$\frac{d}{dx}\frac{\tan(2x)}{\sqrt{x}} = \frac{2\sec^{2}(2x)\sqrt{x} - \tan(2x)\cdot\dfrac{1}{2\sqrt{x}}}{x}$$

**Answer a.** Rules used: quotient, chain, power.

**Möbius:** `(2*sec(2*x)^2*sqrt(x)-tan(2*x)/(2*sqrt(x)))/x`

**Part b, step 1: name the rules.**
**Chain rule twice**: the outer cube, then the cosine, then the inner $x^{2}$.
Read the notation first: $\cos^{3}\left(x^{2}\right)$ means $\left[\cos\left(x^{2}\right)\right]^{3}$.

**Part b, step 2: differentiate.**

$$\frac{d}{dx}\left[\cos\left(x^{2}\right)\right]^{3} = 3\left[\cos\left(x^{2}\right)\right]^{2}\cdot\left(-\sin\left(x^{2}\right)\right)\cdot 2x$$

$$= -6x\cos^{2}\left(x^{2}\right)\sin\left(x^{2}\right)$$

**Part b, step 3: evaluate at $x = \dfrac{\sqrt\pi}{2}$.**
First find the inner value, which is the move that makes this clean.

$$x^{2} = \left(\frac{\sqrt\pi}{2}\right)^{2} = \frac{\pi}{4}$$

**Part b, step 4: use the exact values at $\dfrac{\pi}{4}$.**

$$\cos\frac{\pi}{4} = \frac{\sqrt2}{2} \implies \cos^{2}\frac{\pi}{4} = \frac{1}{2}, \qquad \sin\frac{\pi}{4} = \frac{\sqrt2}{2}$$

**Part b, step 5: substitute.**

$$-6\cdot\frac{\sqrt\pi}{2}\cdot\frac{1}{2}\cdot\frac{\sqrt2}{2} = -\frac{6\sqrt2\sqrt\pi}{8} = -\frac{3\sqrt{2\pi}}{4}$$

**Answer b.**

$$\left.\frac{d}{dx}\cos^{3}\left(x^{2}\right)\right|_{x=\sqrt\pi/2} = -\frac{3\sqrt{2\pi}}{4} \approx -1.87997$$

Rules used: chain rule, twice.

**Möbius:** `-3*sqrt(2*pi)/4`

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

## 10. Implicit differentiation

### Q10.1 - Find the derivative implicitly

**Question.**
Find $y'$ by implicit differentiation:

$$x^{3}y + xy^{2} = 4xy + 7$$

**Step 1: differentiate both sides with respect to $x$.**
Every term with a $y$ in it needs the product rule, the chain rule, or both.

**Step 2: term by term.**

$$\frac{d}{dx}\left(x^{3}y\right) = 3x^{2}y + x^{3}y' \qquad\text{(product rule)}$$

$$\frac{d}{dx}\left(xy^{2}\right) = y^{2} + x\cdot 2yy' = y^{2} + 2xyy' \qquad\text{(product then chain)}$$

$$\frac{d}{dx}(4xy) = 4y + 4xy' \qquad\text{(product rule)}$$

$$\frac{d}{dx}(7) = 0$$

**Step 3: write the differentiated equation.**

$$3x^{2}y + x^{3}y' + y^{2} + 2xyy' = 4y + 4xy'$$

**Step 4: move every $y'$ term to the left and everything else to the right.**

$$x^{3}y' + 2xyy' - 4xy' = 4y - 3x^{2}y - y^{2}$$

**Step 5: factor out $y'$.**

$$y'\left(x^{3} + 2xy - 4x\right) = 4y - 3x^{2}y - y^{2}$$

**Step 6: divide.**

**Answer.**

$$y' = \frac{4y - 3x^{2}y - y^{2}}{x^{3} + 2xy - 4x}$$

Equivalently, factoring $y$ out of the top and $x$ out of the bottom:

$$y' = \frac{y\left(4 - 3x^{2} - y\right)}{x\left(x^{2} + 2y - 4\right)}$$

**Möbius:** `(4*y-3*x^2*y-y^2)/(x^3+2*x*y-4*x)`

**Trap.** Differentiating $xy^{2}$ as $2xyy'$ and forgetting the $y^{2}$ from the product rule. Both the "derivative of $x$" term and the "derivative of $y^{2}$" term must appear.

### Q10.2 - Tangent line to an implicit curve

**Question.**
Find the equation of the tangent line to

$$y^{3} + yx^{2} + x^{2} = 3y^{2}$$

at the point $(1,1)$.

**Step 1: confirm the point is on the curve.**
Always do this first; if it is not on the curve, the question has been misread.

$$1^{3} + (1)(1)^{2} + 1^{2} = 1+1+1 = 3, \qquad 3(1)^{2} = 3$$

Both sides equal $3$, so the point does lie on the curve.

**Step 2: differentiate both sides implicitly.**

$$\frac{d}{dx}\left(y^{3}\right) = 3y^{2}y'$$

$$\frac{d}{dx}\left(yx^{2}\right) = y'x^{2} + 2xy \qquad\text{(product rule)}$$

$$\frac{d}{dx}\left(x^{2}\right) = 2x, \qquad \frac{d}{dx}\left(3y^{2}\right) = 6yy'$$

**Step 3: write the differentiated equation.**

$$3y^{2}y' + x^{2}y' + 2xy + 2x = 6yy'$$

**Step 4: substitute the point now, rather than solving symbolically.**
Because only one point is needed, plugging in $x=1$, $y=1$ immediately is far faster and less error-prone.

$$3(1)y' + (1)y' + 2(1)(1) + 2(1) = 6(1)y'$$

$$3y' + y' + 2 + 2 = 6y'$$

**Step 5: solve for $y'$.**

$$4y' + 4 = 6y' \implies 4 = 2y' \implies y' = 2$$

**Step 6: build the tangent line with point-slope form.**

$$y - 1 = 2(x-1)$$

**Answer.**

$$y = 2x - 1$$

**Möbius:** `2*x-1`, slope `2` at `(1,1)`

**Trap.** Solving for $y'$ in full symbolic generality and then substituting. It works, but it is slower and every extra algebra step is a chance to lose a term.

---
## 11. Related rates

### Q11.1 - Gravel cone growing in height

**Question.**
Gravel is dumped at $\dfrac{dV}{dt} = 0.5\ \text{m}^{3}/\text{min}$.
It forms a cone whose base diameter and height are always equal.
Find $\dfrac{dh}{dt}$ when $h = 4$ m.

**Step 1: write down what is given and what is wanted, as rates.**

$$\text{Given } \frac{dV}{dt} = 0.5, \qquad \text{Want } \frac{dh}{dt} \text{ when } h = 4$$

**Step 2: write the geometry.**

$$V = \frac{1}{3}\pi r^{2}h$$

**Step 3: use the constraint to eliminate $r$.**
"Base diameter equals height" means $2r = h$, so $r = \dfrac{h}{2}$.
This must be done **before** differentiating, because there is no given rate for $r$.

$$V = \frac{1}{3}\pi\left(\frac{h}{2}\right)^{2}h = \frac{1}{3}\pi\cdot\frac{h^{2}}{4}\cdot h = \frac{\pi h^{3}}{12}$$

**Step 4: differentiate with respect to $t$.**

$$\frac{dV}{dt} = \frac{\pi}{12}\cdot 3h^{2}\frac{dh}{dt} = \frac{\pi h^{2}}{4}\frac{dh}{dt}$$

**Step 5: substitute the numbers, only now.**

$$0.5 = \frac{\pi (4)^{2}}{4}\frac{dh}{dt} = 4\pi\frac{dh}{dt}$$

**Step 6: solve.**

$$\frac{dh}{dt} = \frac{0.5}{4\pi} = \frac{1}{8\pi}$$

**Answer.**

$$\frac{dh}{dt} = \frac{1}{8\pi} \approx 0.0398\ \text{m/min}$$

**Möbius:** `1/(8*pi)`

**Trap.** Reading "diameter equals height" as $r = h$. The diameter is $2r$, so $r = \dfrac{h}{2}$; using $r = h$ makes the answer four times too small.

### Q11.2 - Rocket tracked by a radar station

**Question.**
A rocket rises vertically, tracked by a radar station $5$ mi from the pad.
Find $\dfrac{dy}{dt}$ when $y = 4$ mi and $\dfrac{dz}{dt} = 2000$ mi/h, where $z$ is the rocket's distance from the station.

**Step 1: name the variables and draw the triangle.**
The horizontal leg is fixed at $5$; the vertical leg $y$ is the rocket's height; the hypotenuse $z$ is the radar distance.

$$\text{Given } \frac{dz}{dt} = 2000, \qquad \text{Want } \frac{dy}{dt} \text{ when } y = 4$$

**Step 2: write the relationship.**
The $5$ is a constant, not a variable, which is what makes this solvable.

$$z^{2} = 5^{2} + y^{2} = 25 + y^{2}$$

**Step 3: find the missing side at that instant.**

$$z = \sqrt{25 + 16} = \sqrt{41}$$

**Step 4: differentiate with respect to $t$.**

$$2z\frac{dz}{dt} = 2y\frac{dy}{dt}$$

$$z\frac{dz}{dt} = y\frac{dy}{dt}$$

**Step 5: substitute and solve.**

$$\sqrt{41}\,(2000) = 4\frac{dy}{dt} \implies \frac{dy}{dt} = \frac{2000\sqrt{41}}{4} = 500\sqrt{41}$$

**Answer.**

$$\frac{dy}{dt} = 500\sqrt{41} \approx 3201.6\ \text{mi/h}$$

**Möbius:** `500*sqrt(41)`

**Sanity check.** The rocket must rise faster than the radar distance grows, because only part of its motion is along the line of sight. $3201.6 > 2000$, as required.

**Trap.** Using $z = 4$ and $y = \sqrt{41}$, that is, swapping the leg and the hypotenuse. The hypotenuse is always the largest side.

---

## 12. Linear approximation and differentials

### Q12.1 - Approximate a square root with differentials

**Question.**
Use differentials to approximate $\sqrt{9.2}$.

**Step 1: choose the function and the base point.**
Pick $a$ as the nearest value whose root you know exactly.

$$f(x) = \sqrt{x}, \qquad a = 9, \qquad dx = 0.2$$

**Step 2: write the differential formula.**

$$f(a + dx) \approx f(a) + f'(a)\,dx$$

**Step 3: compute the derivative at the base point.**

$$f'(x) = \frac{1}{2\sqrt{x}} \implies f'(9) = \frac{1}{2\cdot 3} = \frac{1}{6}$$

**Step 4: assemble.**

$$\sqrt{9.2} \approx 3 + \frac{1}{6}(0.2) = 3 + \frac{0.2}{6} = 3 + \frac{1}{30}$$

**Answer.**

$$\sqrt{9.2} \approx 3 + \frac{1}{30} = \frac{91}{30} \approx 3.0333$$

The true value is $3.03315$, so the estimate is high by about $0.0002$, which is expected: $\sqrt{x}$ is concave down, so its tangent line lies above the curve.

**Möbius:** `91/30` or `3.0333`

### Q12.2 - Estimate a sine with linearization

**Question.**
Use linearization to estimate $\sin\left(62^\circ\right)$.

**Step 1: choose the base point.**
$60^\circ$ is the nearest angle with exact values.

$$f(x) = \sin x, \qquad a = 60^\circ = \frac{\pi}{3}$$

**Step 2: convert the step to radians.**
This is the step that decides the whole answer; calculus trig formulas are only valid in radians.

$$dx = 2^\circ = 2\cdot\frac{\pi}{180} = \frac{\pi}{90} \approx 0.0349066$$

**Step 3: write the linearization.**

$$\sin(a + dx) \approx \sin a + \cos a\,dx$$

**Step 4: substitute the exact values.**

$$\sin\left(62^\circ\right) \approx \frac{\sqrt3}{2} + \frac{1}{2}\cdot\frac{\pi}{90}$$

**Step 5: evaluate.**

$$\approx 0.8660254 + 0.0174533 = 0.8834787$$

**Answer.**

$$\sin\left(62^\circ\right) \approx \frac{\sqrt3}{2} + \frac{\pi}{180} \approx 0.8835$$

The true value is $0.8829476$, so the estimate is high by about $0.0005$, again because sine is concave down on this stretch.

**Möbius:** `sqrt(3)/2+pi/180` or `0.8835`

**Trap.** Using $dx = 2$ instead of $dx = \dfrac{\pi}{90}$. That gives $\approx 1.87$, which is impossible for a sine.

### Q12.3 - Two estimates to four decimal places

**Question.**
Use differentials to estimate to four decimal places, showing the process.

- a. $\cos\left(62^\circ\right)$
- b. $\sqrt{16.4}$

**Part a, step 1: base point and step.**

$$f(x) = \cos x, \qquad a = \frac{\pi}{3}, \qquad dx = \frac{\pi}{90}$$

**Part a, step 2: the derivative carries a minus sign.**

$$f'(x) = -\sin x \implies f'\left(\frac{\pi}{3}\right) = -\frac{\sqrt3}{2}$$

**Part a, step 3: assemble.**

$$\cos\left(62^\circ\right) \approx \frac{1}{2} - \frac{\sqrt3}{2}\cdot\frac{\pi}{90}$$

**Part a, step 4: evaluate.**

$$\approx 0.5 - 0.8660254(0.0349066) = 0.5 - 0.0302300 = 0.4697700$$

**Answer a.**

$$\cos\left(62^\circ\right) \approx 0.4698$$

The true value is $0.4694716$. Note the estimate is now **high**, and the sign of the error flipped versus Q12.2 because cosine is decreasing here.

**Möbius:** `1/2-sqrt(3)*pi/180` or `0.4698`

**Part b, step 1: base point and step.**

$$f(x) = \sqrt{x}, \qquad a = 16, \qquad dx = 0.4$$

**Part b, step 2: derivative at the base point.**

$$f'(16) = \frac{1}{2\sqrt{16}} = \frac{1}{8}$$

**Part b, step 3: assemble and evaluate.**

$$\sqrt{16.4} \approx 4 + \frac{1}{8}(0.4) = 4 + 0.05 = 4.05$$

**Answer b.**

$$\sqrt{16.4} \approx 4.0500$$

The true value is $4.0496913$, so the estimate is high by about $0.0003$.

**Möbius:** `4.05` or `81/20`

**Trap.** The question says four decimal places, so write $4.0500$, not $4.05$. Trailing zeros are the requested precision.

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
## 16. Antiderivatives and integration techniques

### Q16.1 - Five integrals

**Question.**
Compute each integral.

- a. $\displaystyle\int\left(x^{2}-x\right)\sqrt{3x}\,dx$
- b. $\displaystyle\int\sin(2x)\cos x\,dx$
- c. $\displaystyle\int_{a}^{b}\big(x+\cos(2x)\big)\,dx$
- d. $\displaystyle\int\left(x^{2}-4\right)^{2}dx$
- e. $\displaystyle\int_{2}^{4}x\sqrt{x-1}\,dx$

**Part a, step 1: pull the constant out of the root.**
There is no substitution here; the work is algebraic.

$$\sqrt{3x} = \sqrt3\,x^{1/2}$$

**Part a, step 2: distribute.**

$$\left(x^{2}-x\right)\sqrt3\,x^{1/2} = \sqrt3\left(x^{5/2} - x^{3/2}\right)$$

**Part a, step 3: apply the power rule to each term.**

$$\int x^{5/2}dx = \frac{2}{7}x^{7/2}, \qquad \int x^{3/2}dx = \frac{2}{5}x^{5/2}$$

**Answer a.**

$$\int\left(x^{2}-x\right)\sqrt{3x}\,dx = \sqrt3\left(\frac{2}{7}x^{7/2} - \frac{2}{5}x^{5/2}\right) + C$$

**Möbius:** `sqrt(3)*((2/7)*x^(7/2)-(2/5)*x^(5/2))+C`

**Part b, step 1: remove the double angle.**
The two different arguments, $2x$ and $x$, block substitution, so use $\sin(2x) = 2\sin x\cos x$.

$$\int\sin(2x)\cos x\,dx = \int 2\sin x\cos^{2}x\,dx$$

**Part b, step 2: substitute.**

$$u = \cos x, \qquad du = -\sin x\,dx$$

$$= 2\int \cos^{2}x\,\sin x\,dx = -2\int u^{2}du$$

**Part b, step 3: integrate and back-substitute.**

$$= -\frac{2u^{3}}{3} + C = -\frac{2}{3}\cos^{3}x + C$$

**Answer b.**

$$\int\sin(2x)\cos x\,dx = -\frac{2}{3}\cos^{3}x + C$$

**Möbius:** `-(2/3)*cos(x)^3+C`

**Check.** $\dfrac{d}{dx}\left(-\dfrac{2}{3}\cos^{3}x\right) = -2\cos^{2}x(-\sin x) = 2\sin x\cos^{2}x = \sin(2x)\cos x$. Confirmed.

**Part c, step 1: integrate term by term with symbolic limits.**

$$\int x\,dx = \frac{x^{2}}{2}, \qquad \int\cos(2x)\,dx = \frac{\sin(2x)}{2}$$

The $\dfrac{1}{2}$ on the sine comes from the inside derivative of $2x$.

**Part c, step 2: apply the limits.**

$$\left[\frac{x^{2}}{2} + \frac{\sin(2x)}{2}\right]_{a}^{b}$$

**Answer c.**

$$\int_{a}^{b}\big(x+\cos(2x)\big)dx = \frac{b^{2}-a^{2}}{2} + \frac{\sin(2b)-\sin(2a)}{2}$$

**Möbius:** `(b^2-a^2)/2+(sin(2*b)-sin(2*a))/2`

**Trap.** This is a **definite** integral, so no $+C$. The limits are letters, but it is still a number once $a$ and $b$ are known.

**Part d, step 1: expand first.**
Do not reach for substitution; there is no inner derivative available.

$$\left(x^{2}-4\right)^{2} = x^{4} - 8x^{2} + 16$$

**Part d, step 2: integrate term by term.**

**Answer d.**

$$\int\left(x^{2}-4\right)^{2}dx = \frac{x^{5}}{5} - \frac{8x^{3}}{3} + 16x + C$$

**Möbius:** `x^5/5-8*x^3/3+16*x+C`

**Trap.** Writing $\dfrac{\left(x^{2}-4\right)^{3}}{3}$ by treating the bracket as if the chain rule ran backwards. That requires the inner derivative $2x$ to be present, and it is not.

**Part e, step 1: substitute.**

$$u = x-1 \implies x = u+1, \quad dx = du$$

**Part e, step 2: change the limits.**
For a definite integral, convert the limits and never convert back.

$$x = 2 \implies u = 1, \qquad x = 4 \implies u = 3$$

**Part e, step 3: rewrite the integrand.**

$$\int_{1}^{3}(u+1)u^{1/2}du = \int_{1}^{3}\left(u^{3/2} + u^{1/2}\right)du$$

**Part e, step 4: integrate.**

$$= \left[\frac{2}{5}u^{5/2} + \frac{2}{3}u^{3/2}\right]_{1}^{3}$$

**Part e, step 5: evaluate, using $3^{5/2} = 9\sqrt3$ and $3^{3/2} = 3\sqrt3$.**

$$\text{at } u=3: \frac{2}{5}(9\sqrt3) + \frac{2}{3}(3\sqrt3) = \frac{18\sqrt3}{5} + 2\sqrt3 = \frac{28\sqrt3}{5}$$

$$\text{at } u=1: \frac{2}{5} + \frac{2}{3} = \frac{16}{15}$$

**Part e, step 6: subtract.**

$$\frac{28\sqrt3}{5} - \frac{16}{15} = \frac{84\sqrt3 - 16}{15}$$

**Answer e.**

$$\int_{2}^{4}x\sqrt{x-1}\,dx = \frac{84\sqrt3 - 16}{15} \approx 8.6328$$

**Möbius:** `(84*sqrt(3)-16)/15`

**Trap.** Substituting $u = x-1$ but leaving the stray $x$ in the integrand. You must also replace $x$ by $u+1$.

### Q16.2 - Four integrals, naming the technique

**Question.**
Integrate each, indicating the technique used.

- a. $\displaystyle\int\dfrac{\cos\left(\sqrt{2x}\right)}{\sqrt{x}}\,dx$
- b. $\displaystyle\int_{0}^{\pi/3}\tan x\,\sec^{2}x\,dx$
- c. $\displaystyle\int\dfrac{x^{3}+\sqrt{5x}-4}{x^{2}}\,dx$
- d. $\displaystyle\int\sec^{3}x\,\tan x\,dx$, with the hint $\sec^{3}x\tan x = \sec^{2}x\,\sec x\tan x$

**Part a. Technique: u-substitution.**

**Step 1: choose $u$ as the inside of the cosine.**

$$u = \sqrt{2x} = \sqrt2\,x^{1/2}$$

**Step 2: differentiate.**

$$du = \frac{\sqrt2}{2}x^{-1/2}dx = \frac{\sqrt2}{2\sqrt{x}}dx$$

**Step 3: solve for the piece that appears in the integral.**

$$\frac{dx}{\sqrt{x}} = \frac{2}{\sqrt2}du = \sqrt2\,du$$

**Step 4: rewrite and integrate.**

$$\int\cos(u)\sqrt2\,du = \sqrt2\sin(u) + C$$

**Answer a.**

$$\int\frac{\cos\left(\sqrt{2x}\right)}{\sqrt{x}}dx = \sqrt2\,\sin\left(\sqrt{2x}\right) + C$$

**Möbius:** `sqrt(2)*sin(sqrt(2*x))+C`

**Check.** $\dfrac{d}{dx}\sqrt2\sin\left(\sqrt{2x}\right) = \sqrt2\cos\left(\sqrt{2x}\right)\cdot\dfrac{\sqrt2}{2\sqrt{x}} = \dfrac{\cos\left(\sqrt{2x}\right)}{\sqrt{x}}$. Confirmed.

**Part b. Technique: u-substitution with changed limits.**

**Step 1: choose $u$.**
$\sec^{2}x$ is exactly the derivative of $\tan x$, which is the signal.

$$u = \tan x, \qquad du = \sec^{2}x\,dx$$

**Step 2: change the limits.**

$$x = 0 \implies u = \tan 0 = 0$$

$$x = \frac{\pi}{3} \implies u = \tan\frac{\pi}{3} = \sqrt3$$

**Step 3: integrate.**

$$\int_{0}^{\sqrt3}u\,du = \left[\frac{u^{2}}{2}\right]_{0}^{\sqrt3} = \frac{3}{2} - 0$$

**Answer b.**

$$\int_{0}^{\pi/3}\tan x\sec^{2}x\,dx = \frac{3}{2}$$

**Möbius:** `3/2`

**Part c. Technique: algebraic rewriting, then the power rule.**

**Step 1: split the fraction term by term.**

$$\frac{x^{3}}{x^{2}} = x, \qquad \frac{\sqrt{5x}}{x^{2}} = \frac{\sqrt5\,x^{1/2}}{x^{2}} = \sqrt5\,x^{-3/2}, \qquad \frac{-4}{x^{2}} = -4x^{-2}$$

**Step 2: integrate each piece.**

$$\int x\,dx = \frac{x^{2}}{2}$$

$$\int\sqrt5\,x^{-3/2}dx = \sqrt5\cdot\frac{x^{-1/2}}{-\frac12} = -2\sqrt5\,x^{-1/2}$$

$$\int -4x^{-2}dx = -4\cdot\frac{x^{-1}}{-1} = \frac{4}{x}$$

**Answer c.**

$$\int\frac{x^{3}+\sqrt{5x}-4}{x^{2}}dx = \frac{x^{2}}{2} - \frac{2\sqrt5}{\sqrt{x}} + \frac{4}{x} + C$$

**Möbius:** `x^2/2-2*sqrt(5)/sqrt(x)+4/x+C`

**Trap.** Trying to integrate the numerator and denominator separately. There is no quotient rule for integrals; divide through first.

**Part d. Technique: u-substitution, guided by the hint.**

**Step 1: read the hint as a split.**

$$\sec^{3}x\tan x = \sec^{2}x\cdot\big(\sec x\tan x\big)$$

**Step 2: choose $u$ so the bracketed part is $du$.**

$$u = \sec x, \qquad du = \sec x\tan x\,dx$$

**Step 3: rewrite.**

$$\int\sec^{2}x\big(\sec x\tan x\,dx\big) = \int u^{2}du$$

**Step 4: integrate and back-substitute.**

$$= \frac{u^{3}}{3} + C = \frac{\sec^{3}x}{3} + C$$

**Answer d.**

$$\int\sec^{3}x\tan x\,dx = \frac{\sec^{3}x}{3} + C$$

**Möbius:** `sec(x)^3/3+C`

**Check.** $\dfrac{d}{dx}\dfrac{\sec^{3}x}{3} = \sec^{2}x\cdot\sec x\tan x = \sec^{3}x\tan x$. Confirmed.

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

## 18. The Fundamental Theorem of Calculus

### Q18.1 - Differentiate an integral with variable limits

**Question.**
Use the Fundamental Theorem of Calculus to evaluate

$$\frac{d}{dx}\int_{2x}^{x}\sin\left(t^{2}\right)dt$$

**Step 1: recall the basic form of FTC part 1.**

$$\frac{d}{dx}\int_{a}^{x}f(t)\,dt = f(x), \qquad a \text{ constant}$$

Here **both** limits are variable, so the basic form does not apply directly.

**Step 2: split at a constant.**
Introduce any convenient constant $c$ and use the additivity of the integral.

$$\int_{2x}^{x} = \int_{2x}^{c} + \int_{c}^{x} = \int_{c}^{x} - \int_{c}^{2x}$$

**Step 3: differentiate the first piece.**
The upper limit is exactly $x$, so this is the basic form.

$$\frac{d}{dx}\int_{c}^{x}\sin\left(t^{2}\right)dt = \sin\left(x^{2}\right)$$

**Step 4: differentiate the second piece with the chain rule.**
The upper limit is $2x$, so evaluate the integrand at $2x$ and multiply by the derivative of $2x$.

$$\frac{d}{dx}\int_{c}^{2x}\sin\left(t^{2}\right)dt = \sin\left((2x)^{2}\right)\cdot 2 = 2\sin\left(4x^{2}\right)$$

**Step 5: subtract.**

**Answer.**

$$\frac{d}{dx}\int_{2x}^{x}\sin\left(t^{2}\right)dt = \sin\left(x^{2}\right) - 2\sin\left(4x^{2}\right)$$

**Möbius:** `sin(x^2)-2*sin(4*x^2)`

**General rule worth memorizing.**

$$\frac{d}{dx}\int_{g(x)}^{h(x)}f(t)\,dt = f\big(h(x)\big)h'(x) - f\big(g(x)\big)g'(x)$$

**Trap.** Forgetting that $(2x)^{2} = 4x^{2}$, not $2x^{2}$, and forgetting the factor $2$ from the chain rule. Both errors hide in the same term.

---

## 19. Applications of integration

### Q19.1 - Area between a line and a parabola

**Question.**
Find the area between $y = x$ and $y = 2-x^{2}$.

**Step 1: find the intersection points.**
No interval is given, so the curves themselves supply the limits.

$$x = 2 - x^{2} \implies x^{2}+x-2 = 0 \implies (x+2)(x-1) = 0$$

$$x = -2, \qquad x = 1$$

**Step 2: decide which curve is on top.**
Test any point strictly between, say $x = 0$.

$$\text{parabola: } 2-0 = 2, \qquad \text{line: } 0$$

The parabola is above the line on all of $(-2,1)$, and the curves meet only at the endpoints, so no split is needed.

**Step 3: set up the integral of top minus bottom.**

$$A = \int_{-2}^{1}\left[\left(2-x^{2}\right) - x\right]dx = \int_{-2}^{1}\left(2 - x - x^{2}\right)dx$$

**Step 4: antidifferentiate.**

$$= \left[2x - \frac{x^{2}}{2} - \frac{x^{3}}{3}\right]_{-2}^{1}$$

**Step 5: evaluate at the top limit.**

$$2 - \frac{1}{2} - \frac{1}{3} = \frac{12-3-2}{6} = \frac{7}{6}$$

**Step 6: evaluate at the bottom limit.**

$$-4 - \frac{4}{2} - \frac{-8}{3} = -4 - 2 + \frac{8}{3} = -6 + \frac{8}{3} = -\frac{10}{3}$$

**Step 7: subtract.**

$$A = \frac{7}{6} - \left(-\frac{10}{3}\right) = \frac{7}{6} + \frac{20}{6} = \frac{27}{6} = \frac{9}{2}$$

**Answer.**

$$A = \frac{9}{2} = 4.5 \text{ square units}$$

**Möbius:** `9/2`

**Trap.** Integrating line minus parabola, which returns $-\dfrac{9}{2}$. An area is positive; if you get a negative number you had the order backwards.

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

### Q19.3 - Net change, water flowing from a tank

**Question.**
Water flows from a tank at $r(t) = 180 - 6t$ litres per minute for $0 \le t \le 50$.
Find the amount that flows out during the first 15 minutes.

**Step 1: recognise the question type.**
A **rate** is given and a **total** is wanted, so integrate.

$$\text{Amount} = \int_{0}^{15}r(t)\,dt$$

**Step 2: set up.**

$$= \int_{0}^{15}(180 - 6t)\,dt$$

**Step 3: antidifferentiate.**

$$= \left[180t - 3t^{2}\right]_{0}^{15}$$

**Step 4: evaluate.**

$$= \left(180(15) - 3(225)\right) - 0 = 2700 - 675 = 2025$$

**Answer.**

$$2025 \text{ litres}$$

**Möbius:** `2025`

**Sanity check.** The rate starts at $180$ L/min and falls to $180-90 = 90$ L/min at $t=15$.
Since the rate is linear, the average is $\dfrac{180+90}{2} = 135$ L/min, and $135 \times 15 = 2025$. The two methods agree.

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
# Part 6: The one-page formula card

Memorize these before each exam.
Each entry gives the Möbius typing form first and the printed mathematical form under it.

Derivative rules:

- Constant: `d/dx [c] = 0`.
  - Math: $\dfrac{d}{dx}(c) = 0$
- Power: `d/dx [x^n] = n x^(n - 1)`.
  - Math: $\dfrac{d}{dx}\left(x^{n}\right) = n\,x^{n-1}$
- Sum: `(f + g)' = f' + g'`.
  - Math: $(f+g)' = f' + g'$
- Product: `(fg)' = f'g + fg'`.
  - Math: $(fg)' = f'g + fg'$
- Quotient: `(f/g)' = (f'g - fg') / g^2`.
  - Math: $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^{2}}$
- Chain: `d/dx [f(g(x))] = f'(g(x)) g'(x)`.
  - Math: $\dfrac{d}{dx}f\big(g(x)\big) = f'\big(g(x)\big)g'(x)$

Trig derivatives:

- `sin x -> cos x`.
  - Math: $\dfrac{d}{dx}\sin x = \cos x$
- `cos x -> -sin x`.
  - Math: $\dfrac{d}{dx}\cos x = -\sin x$
- `tan x -> sec^2 x`.
  - Math: $\dfrac{d}{dx}\tan x = \sec^{2}x$
- `cot x -> -csc^2 x`.
  - Math: $\dfrac{d}{dx}\cot x = -\csc^{2}x$
- `sec x -> sec x tan x`.
  - Math: $\dfrac{d}{dx}\sec x = \sec x\tan x$
- `csc x -> -csc x cot x`.
  - Math: $\dfrac{d}{dx}\csc x = -\csc x\cot x$

Exponential and log:

- `e^x -> e^x`.
  - Math: $\dfrac{d}{dx}e^{x} = e^{x}$
- `a^x -> a^x ln a`.
  - Math: $\dfrac{d}{dx}a^{x} = a^{x}\ln a$
- `ln x -> 1/x`.
  - Math: $\dfrac{d}{dx}\ln x = \dfrac{1}{x}$

Integrals:

- `∫ x^n dx = x^(n + 1) / (n + 1) + C`, for `n ≠ -1`.
  - Math: $\displaystyle\int x^{n}dx = \dfrac{x^{n+1}}{n+1} + C$, $n \neq -1$
- `∫ 1/x dx = ln|x| + C`.
  - Math: $\displaystyle\int \dfrac{1}{x}dx = \ln\lvert x\rvert + C$
- `∫ sin x dx = -cos x + C`.
  - Math: $\displaystyle\int \sin x\,dx = -\cos x + C$
- `∫ cos x dx = sin x + C`.
  - Math: $\displaystyle\int \cos x\,dx = \sin x + C$
- `∫ sec^2 x dx = tan x + C`.
  - Math: $\displaystyle\int \sec^{2}x\,dx = \tan x + C$
- `∫ csc^2 x dx = -cot x + C`.
  - Math: $\displaystyle\int \csc^{2}x\,dx = -\cot x + C$
- `∫ sec x tan x dx = sec x + C`.
  - Math: $\displaystyle\int \sec x\tan x\,dx = \sec x + C$
- `∫ csc x cot x dx = -csc x + C`.
  - Math: $\displaystyle\int \csc x\cot x\,dx = -\csc x + C$

Fundamental Theorem:

- `d/dx ∫[a to x] f(t) dt = f(x)`.
  - Math: $\dfrac{d}{dx}\displaystyle\int_{a}^{x}f(t)\,dt = f(x)$
- `∫[a to b] f(x) dx = F(b) - F(a)`.
  - Math: $\displaystyle\int_{a}^{b}f(x)\,dx = F(b) - F(a)$
- Both limits variable: `d/dx ∫[g(x) to h(x)] f(t) dt = f(h(x)) h'(x) - f(g(x)) g'(x)`.
  - Math: $\dfrac{d}{dx}\displaystyle\int_{g(x)}^{h(x)}f(t)\,dt = f\big(h(x)\big)h'(x) - f\big(g(x)\big)g'(x)$

Average value:

- `f_avg = (1 / (b - a)) ∫[a to b] f(x) dx`.
  - Math: $f_{\text{avg}} = \dfrac{1}{b-a}\displaystyle\int_{a}^{b}f(x)\,dx$

Bounding a definite integral:

- `m(b - a) <= ∫[a to b] f <= M(b - a)`.
  - Math: $m(b-a) \le \displaystyle\int_{a}^{b}f(x)\,dx \le M(b-a)$ when $m \le f \le M$

Special limits:

- `lim(u -> 0) sin(u)/u = 1`.
  - Math: $\displaystyle\lim_{u\to 0}\dfrac{\sin u}{u} = 1$
- `lim(u -> 0) (1 - cos(u))/u = 0`.
  - Math: $\displaystyle\lim_{u\to 0}\dfrac{1-\cos u}{u} = 0$

Key identities:

- `sin^2 x + cos^2 x = 1`.
  - Math: $\sin^{2}x + \cos^{2}x = 1$
- `1 + tan^2 x = sec^2 x`.
  - Math: $1 + \tan^{2}x = \sec^{2}x$
- `1 + cot^2 x = csc^2 x`.
  - Math: $1 + \cot^{2}x = \csc^{2}x$
- `sin(2x) = 2 sin x cos x`.
  - Math: $\sin(2x) = 2\sin x\cos x$
- `cos(2x) = cos^2 x - sin^2 x = 1 - 2 sin^2 x = 2 cos^2 x - 1`.
  - Math: $\cos(2x) = \cos^{2}x - \sin^{2}x = 1 - 2\sin^{2}x = 2\cos^{2}x - 1$
- `1 - cos(2x) = 2 sin^2 x`.
  - Math: $1 - \cos(2x) = 2\sin^{2}x$
- `1 + cos(2x) = 2 cos^2 x`.
  - Math: $1 + \cos(2x) = 2\cos^{2}x$
- `sin(A + B) = sin A cos B + cos A sin B`.
  - Math: $\sin(A+B) = \sin A\cos B + \cos A\sin B$
- `cos(A - B) = cos A cos B + sin A sin B`.
  - Math: $\cos(A-B) = \cos A\cos B + \sin A\sin B$

Applications:

- Spring work: `W = (1/2) k d^2`.
  - Math: $W = \dfrac{1}{2}kd^{2}$
- Chain work: `W = ∫ rho g y dy`.
  - Math: $W = \displaystyle\int \rho\,g\,y\,dy$
- Displacement: `∫ v dt`, distance: `∫ |v| dt`.
  - Math: $\displaystyle\int_{a}^{b}v\,dt$ and $\displaystyle\int_{a}^{b}\lvert v\rvert\,dt$
- Newton's method: `x_(n+1) = x_n - f(x_n)/f'(x_n)`.
  - Math: $x_{n+1} = x_{n} - \dfrac{f(x_{n})}{f'(x_{n})}$
- Linearization: `f(a + dx) ≈ f(a) + f'(a) dx`.
  - Math: $f(a+dx) \approx f(a) + f'(a)\,dx$
- Cone volume: `V = pi r^2 h / 3`.
  - Math: $V = \dfrac{\pi r^{2}h}{3}$

---

# Part 7: Practice map

Use this map to drill every question note against the topic.
Every question listed here is fully worked in Part 5.

Foundations:

- Exact trig values: `Q01.1`.
- Composite domains: `Q01.2`.
- Function definition: `Q01.3`.
- Modeling a cone: `Q01.4`.
- Transformations: `Q02.1`, `Q02.2`.

Limits and graphs:

- Limits: `Q03.1`, `Q03.2`, `Q03.3`.
- Asymptotes: `Q04.1`.
- Sketching from conditions: `Q05.1`, `Q05.2`, `Q05.3`.
- Rate interpretation: `Q06.1`.

Derivatives:

- Definition of derivative: `Q07.1`.
- Derivative rules: `Q08.1`, `Q08.2`, `Q08.3`, `Q08.4`.
- Tangent line: `Q09.1`.
- Implicit differentiation: `Q10.1`, `Q10.2`.
- Related rates: `Q11.1`, `Q11.2`.
- Differentials: `Q12.1`, `Q12.2`, `Q12.3`.
- Newton's method: `Q13.1`.
- Curve sketching: `Q14.1`.
- Extrema and optimization: `Q15.1` through `Q15.5`.

Integration:

- Antiderivatives: `Q16.1`, `Q16.2`.
- Bounding integrals: `Q17.1`, `Q17.2`, `Q17.3`.
- Fundamental Theorem: `Q18.1`.
- Applications: `Q19.1` through `Q19.9`.

Questions that reuse each other, so learn them as pairs:

- `Q15.3` and `Q17.2` use the same function $\dfrac{1}{x^{2}+1}$ on the same interval.
- `Q15.5` and `Q17.3` use the same function $\left(x^{2}+2x\right)^{2/3}$ on the same interval.
- `Q12.2` and `Q12.3a` are the same linearization at $60^\circ$, once for sine and once for cosine.
- `Q14.1b` and `Q15.1b` are $x+\sin x$ and $x+\cos x$, and both hinge on the derivative never going negative.

Sample exams:

- `Sample Midterm Exam 1` and `Sample Midterm Exam 2` in the course folder.
- `Sample Final Exam 1` and `Sample Final Exam 2` in the course folder.
- The all-exam question bank is `MATH265-All-Exam-Questions.md`.

---

# Part 8: Weekly practice plan

Week 1:

- Master exact trig values and domains.
- Do `Q01.1` through `Q01.4`.

Week 2:

- Master limits, asymptotes, and graph transformations.
- Do `Q02.1` through `Q05.3`.

Week 3:

- Master derivative rules and the chain rule.
- Do `Q06.1` through `Q08.4`.

Week 4:

- Master tangent lines, implicit differentiation, related rates, and differentials.
- Do `Q09.1` through `Q12.3`.
- Take Sample Midterm 1 and 2 under timed conditions.

Week 5:

- Master curve sketching, extrema, and optimization.
- Do `Q13.1` through `Q15.5`.

Week 6:

- Master antiderivatives, substitution, and the Fundamental Theorem.
- Do `Q16.1` through `Q18.1`.

Week 7:

- Master applications of integration.
- Do `Q19.1` through `Q19.9`.
- Take Sample Final 1 and 2 under timed conditions.

How to use Part 5 while drilling: cover everything below the **Question** line, work the problem cold, then uncover the steps.
Reading a worked solution is not practice; reproducing it is.

---

# Part 9: Final checklist before exam day

- Calculator is set to radians.
- You know the derivative and integral tables cold.
- You know the special trig limits.
- You know the exact unit circle values.
- You can sketch from limit and derivative conditions.
- You can do a chain rule problem without dropping the inside derivative.
- You can write the quotient rule in the correct order.
- You add `+ C` only to indefinite integrals.
- You split distance problems at the zeros of velocity.
- You use `b - a` as the interval width when bounding or averaging.
- You convert degrees to radians before any linearization.
- You check whether a critical number comes from `f' = 0` or from `f'` being undefined.
- You cancel common factors before declaring a vertical asymptote.
- You bracket whole numerators when typing into Möbius, and you click preview.
- You have timed yourself on a full sample paper.

## The ten most expensive single mistakes in this course

Each of these is drawn from a specific question in Part 5.

1. `sqrt(6)+sqrt(2)/4` instead of `(sqrt(6)+sqrt(2))/4`, which is off by a factor of nearly 3. See `Q01.1`.
2. Reporting a cancelled factor as a vertical asymptote instead of a hole. See `Q04.1`.
3. Using $dx = 2$ instead of $dx = \dfrac{\pi}{90}$ in a degree linearization. See `Q12.2`.
4. Reading "diameter equals height" as $r = h$ rather than $r = \dfrac{h}{2}$. See `Q11.1`.
5. Missing critical numbers where $f'$ is undefined rather than zero. See `Q15.5`.
6. Integrating across a crossing point without splitting, which cancels area. See `Q19.2`.
7. Forgetting the chain-rule factor on a variable limit of integration. See `Q18.1`.
8. Rounding between Newton iterations. See `Q13.1`.
9. Assuming work scales linearly with spring stretch, when it scales with the square. See `Q19.5`.
10. Calling a horizontal tangent a maximum when $f'$ does not change sign. See `Q14.1b`.
