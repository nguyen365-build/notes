# MATH 265 Exam Prep Guide

This file is a phone-friendly study guide for the MATH 265 midterm and final.
It covers the full concept list you gave, plus the extra topics your own notes and sample exams actually test.

## What I analyzed

- The course folder at `Coursework\_Archive\Degree\Athabasca\_MATH265 - Calculus 1`.
- The question notes in `notes\Q01.1` through `notes\Q19.9`.
- The review and cheat-sheet files in `notes\MATH265`.
- The four sample exams, the all-exam question bank, and the AU reference sheets.

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

Practice:

- Interpret `(P(15) - P(2)) / 13 = 1,431` in plain words.
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
- As `h` approaches 0, this quotient approaches the derivative.

Practice:

- Write the difference quotient for `f(x) = x^2`.
- Simplify it to `2x + h`, then let `h` go to 0 to get `2x`.

## 5. The limit

Concept:

- A limit is the value a function approaches as the input approaches a value.
- The function does not have to actually reach that value.

Know:

- Direct substitution is the first thing to try.
- `0/0` means factor, rationalize, use a common denominator, or use a trig identity.
- `k/0` with `k` not zero usually means the limit is infinite or does not exist.
- `infinity/infinity` means divide by the highest power in the denominator.
- Bounded times zero, such as `(something going to 0) * sin(x)`, is squeezed to 0.

Practice:

- Do every limit in `Q03.1`, `Q03.2`, and `Q03.3`.
- Also do `Q04.1` to connect limits to asymptotes.

## 6. The derivative, and differentials of x and y

Concept:

- The derivative is the limit of the difference quotient.
- It measures instantaneous rate of change.

Know:

- `f'(x) = lim(h -> 0) [f(x + h) - f(x)] / h`.
- The derivative is a function, not a single number.
- `dy/dx` means the derivative of `y` with respect to `x`.

Practice:

- Use the definition to find the derivative of `x^2`, `1/x`, and `cot x`.
- See `Q07.1` for the cotangent derivation.

## 7. Differential notation

Concept:

- `dy/dx` is one notation for the derivative.
- `dy` and `dx` are called differentials.

Know:

- `dy = f'(x) dx`.
- Treat `dx` as a small change in `x`.
- Treat `dy` as the approximate resulting change in `y`.
- Differential notation is used in linear approximation and related rates.

Practice:

- Approximate `sqrt(9.2)` by choosing `x = 9` and `dx = 0.2`.
- See `Q12.1`.

---

# Part 2: Derivative rules

## 8. The constant rule of differentiation

Concept:

- The derivative of a constant is zero.

Know:

- `d/dx [c] = 0`.
- A constant function has a flat graph, so its slope is zero.

Practice:

- Find `d/dx [7]`.
- Answer: `0`.

## 9. The power rule of differentiation

Concept:

- Bring the exponent down and reduce the exponent by one.

Know:

- `d/dx [x^n] = n x^(n - 1)`.
- Works for negative and fractional powers too.

Practice:

- Differentiate `x^5`, `x^(-2)`, `sqrt(x)`, and `1/x`.
- Answers: `5x^4`, `-2x^(-3)`, `(1/2)x^(-1/2)`, `-x^(-2)`.

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
- Notice the cubic's flat points correspond to where `3x^2 = 0`.

## 11. The addition and subtraction rule of differentiation

Concept:

- Differentiate term by term.

Know:

- `d/dx [f(x) + g(x)] = f'(x) + g'(x)`.
- `d/dx [f(x) - g(x)] = f'(x) - g'(x)`.

Practice:

- Differentiate `4x^5 + 3x^4 - 6x^3 + 6`.
- Answer: `20x^4 + 12x^3 - 18x^2`.

## 12. The product rule of differentiation

Concept:

- For a product of two functions, use first derivative times second plus first times second derivative.

Know:

- `(fg)' = f' g + f g'`.
- Say it: "first prime times second, plus first times second prime."

Practice:

- Differentiate `x cos(sqrt(x - 3))`.
- Identify `f = x` and `g = cos(sqrt(x - 3))`.

## 13. Combining rules of differentiation to find the derivative of a polynomial

Concept:

- Polynomials use only the power, constant, and sum rules.
- More complicated functions layer product, quotient, and chain rules.

Know:

- Work from the outside in.
- Name the rule you are using at each step.

Practice:

- Differentiate a polynomial like `3x^4 - 2x^3 + x - 5`.
- Then move on to mixed expressions in `Q08.1` through `Q08.4`.

## 14. Differentiation super-shortcuts for polynomials

Concept:

- For a polynomial, multiply each coefficient by its exponent and drop the degree by one.

Know:

- `y = ax^n` becomes `y' = a n x^(n - 1)`.
- The constant term disappears.

Practice:

- Differentiate `y = 4x^5 + 3x^4 - 6x^3 + 6` without rewriting every step.
- Answer: `20x^4 + 12x^3 - 18x^2`.

## 15. Solving optimization problems with derivatives

Concept:

- Maxima and minima happen where the derivative is zero or undefined, or at endpoints.

Know:

- Draw and label the situation.
- Write the quantity to optimize.
- Write the constraint.
- Use the constraint to eliminate one variable.
- Differentiate, set the derivative to zero, and solve.
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
- `f''(x)` tells concavity and acceleration.
- `f'' > 0` means concave up.
- `f'' < 0` means concave down.

Practice:

- Find `d^2/dx^2 [cot(2x)]`.
- See `Q08.2`.

## 17. Trig rules of differentiation for sine and cosine

Concept:

- The derivative of sine is cosine.
- The derivative of cosine is negative sine.

Know:

- `d/dx [sin x] = cos x`.
- `d/dx [cos x] = -sin x`.
- The minus sign on cosine is the most common lost mark.

Practice:

- Differentiate `sin(2x^2 - x + 1)`.
- Remember the chain rule: multiply by the inside derivative `4x - 1`.

## 18. Knowledge test: product rule example

Concept:

- This is a self-test to confirm you can apply the product rule correctly.

Know:

- For `y = x^2 sin x`, let `f = x^2` and `g = sin x`.
- `f' = 2x` and `g' = cos x`.
- `y' = 2x sin x + x^2 cos x`.

Practice:

- Differentiate `x^2 sin x` on paper.
- Then check your answer against `2x sin x + x^2 cos x`.

## 19. The chain rule for differentiation

Concept:

- Differentiate the outside function, then multiply by the derivative of the inside.

Know:

- `d/dx [f(g(x))] = f'(g(x)) * g'(x)`.
- Work outside to inside.
- Missing the inside derivative is the single most common error.

Practice:

- Differentiate `sin(2x^2 - x + 1)`.
- Differentiate `( -4x^3 - x^2 + 3x + 7 )^4`.
- See `Q08.1` and `Q08.3`.

## 20. The quotient rule for differentiation

Concept:

- For a fraction, use low d-high minus high d-low over low squared.

Know:

- `(f/g)' = (f' g - f g') / g^2`.
- The numerator order is the whole mark.
- Never write `g f' - f g'`.

Practice:

- Differentiate `(2x - 16) / (x + 3)^2`.
- Differentiate `(sqrt(x^2 - 1)) / (x^2 - 2x - 8)`.

## 21. The derivative of the other trig functions

Concept:

- Tangent, cotangent, secant, and cosecant each have their own derivative.

Know:

- `d/dx [tan x] = sec^2 x`.
- `d/dx [cot x] = -csc^2 x`.
- `d/dx [sec x] = sec x tan x`.
- `d/dx [csc x] = -csc x cot x`.
- Every co-function derivative has a minus sign: cosine, cotangent, cosecant.

Practice:

- Differentiate `sec(x^2 - 3x)`.
- Differentiate `cot(2x)` twice.
- See `Q08.2`.

## 22. Algebra overview: exponentials and logarithms

Concept:

- Exponentials grow by repeated multiplication.
- Logarithms undo exponentials.

Know:

- `e^x` is the natural exponential.
- `ln x` is the natural logarithm, the inverse of `e^x`.
- `ln(e^x) = x` and `e^(ln x) = x`.
- Exponent rules: `x^a x^b = x^(a+b)`, `1/x^n = x^(-n)`, and `nth-root(x^m) = x^(m/n)`.

Practice:

- Rewrite `sqrt(3x)` as `sqrt(3) x^(1/2)`.
- Rewrite `sqrt(5x) / x^2` as `sqrt(5) x^(-3/2)`.

## 23. Differentiation rules for exponents

Concept:

- The natural exponential is its own derivative.

Know:

- `d/dx [e^x] = e^x`.
- For a general base, `d/dx [a^x] = a^x ln a`.
- For a composite exponential, use the chain rule.

Practice:

- Differentiate `e^(2x)`.
- Answer: `2 e^(2x)`.

## 24. Differentiation rules for logarithms

Concept:

- The derivative of natural log is one over x.

Know:

- `d/dx [ln x] = 1/x`.
- `d/dx [ln(g(x))] = g'(x) / g(x)`.

Practice:

- Differentiate `ln(x^2 + 1)`.
- Answer: `2x / (x^2 + 1)`.

---

# Part 3: Antiderivatives and integration

## 25. The anti-derivative, also called the integral

Concept:

- An antiderivative reverses a derivative.
- If `F'(x) = f(x)`, then `F(x)` is an antiderivative of `f(x)`.

Know:

- Integration asks: what function gives this derivative?
- There are infinitely many antiderivatives because constants vanish under differentiation.

Practice:

- Find an antiderivative of `3x^2`.
- Answer: `x^3 + C`.

## 26. The power rule for integration

Concept:

- Reverse the power rule: add one to the exponent, then divide by the new exponent.

Know:

- `∫ x^n dx = x^(n + 1) / (n + 1) + C`, for `n` not equal to `-1`.

Practice:

- Integrate `x^4`, `x^(1/2)`, and `x^(-2)`.
- Answers: `x^5/5 + C`, `(2/3)x^(3/2) + C`, `-x^(-1) + C`.

## 27. The power rule for integration will not work for 1/x

Concept:

- `1/x = x^(-1)`, and the power rule would divide by zero.

Know:

- `∫ 1/x dx = ln|x| + C`.
- Use the absolute value because the logarithm needs a positive argument.

Practice:

- Integrate `1/x` and `4/x`.
- Answers: `ln|x| + C` and `4 ln|x| + C`.

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
- Indefinite: `x^3/3 + C`.
- Definite from 0 to 1: `1/3`.

## 29. Anti-derivative notation

Concept:

- `∫ f(x) dx` means the general antiderivative.
- `∫[a to b] f(x) dx` means the definite integral.

Know:

- The `dx` tells you the variable of integration.
- The limits `a` and `b` appear only on definite integrals.

Practice:

- Write an indefinite integral for `cos x`.
- Write a definite integral for area from 0 to 1.

## 30. The integral as the area under a curve using the limit

Concept:

- A definite integral is the limit of a sum of rectangle areas.

Know:

- Chop the interval into thin slices.
- Each rectangle has area `f(x) * dx`.
- Add the rectangles and let the width go to 0.

Practice:

- Draw `y = x` from 0 to 2.
- Approximate the area with four rectangles, then with more.
- See that the limit approaches the triangle area 2.

## 31. Evaluating definite integrals

Concept:

- Find an antiderivative, then subtract its values at the endpoints.

Know:

- `∫[a to b] f(x) dx = F(b) - F(a)`.
- This is the Fundamental Theorem of Calculus, part 2.

Practice:

- Evaluate `∫[0 to 1] x^2 dx`.
- Answer: `1/3`.

## 32. Definite and indefinite integrals compared

Concept:

- Indefinite integrals return a family of functions.
- Definite integrals return a number.

Know:

- Indefinite: `∫ f(x) dx = F(x) + C`.
- Definite: `∫[a to b] f(x) dx = F(b) - F(a)`.

Practice:

- Integrate `2x` indefinitely, then from 1 to 3.
- Answers: `x^2 + C` and `8`.

## 33. The definite integral and signed area

Concept:

- Area above the x-axis counts positive.
- Area below the x-axis counts negative.
- The definite integral reports signed area.

Know:

- To get true distance or total area, integrate the absolute value, or split at the zeros.

Practice:

- For `v(t) = t^2 - 3t + 2` on `[0, 3]`, find displacement and distance.
- See `Q19.8`.

## 34. The Fundamental Theorem of Calculus visualized

Concept:

- Differentiation and integration undo each other.

Know:

- FTC part 1: `d/dx ∫[a to x] f(t) dt = f(x)`.
- FTC part 2: `∫[a to b] f'(x) dx = f(b) - f(a)`.
- If the area function grows, its derivative is the height of the curve.

Practice:

- Differentiate `∫[2x to x] sin(t^2) dt`.
- Answer: `sin(x^2) - 2 sin(4x^2)`.
- See `Q18.1`.

## 35. The integral as a running total of its derivative

Concept:

- An integral accumulates a rate.
- A derivative measures the rate of accumulation.

Know:

- Total water = integral of flow rate.
- Distance = integral of velocity.
- Velocity = derivative of position.

Practice:

- Water flows at `r(t) = 180 - 6t` liters per minute.
- Find the amount that flows in the first 15 minutes.
- Answer: `2025 L`.
- See `Q19.3`.

## 36. The trig rule for integration, sine and cosine

Concept:

- Integration flips the derivative signs.

Know:

- `∫ sin x dx = -cos x + C`.
- `∫ cos x dx = sin x + C`.
- The minus now sits on sine, the opposite of differentiation.

Practice:

- Integrate `sin x` and `cos x`.
- Then integrate `x + cos(2x)` from `a` to `b`.

## 37. Definite integral example problem

Concept:

- A worked example of the full evaluate step.

Know:

- Problem: evaluate `∫[0 to pi] sin x dx`.
- Antiderivative: `-cos x`.
- Evaluate: `-cos(pi) - (-cos(0))`.
- `-cos(pi) = 1`, so the answer is `1 - (-1) = 2`.

Practice:

- Repeat this problem without notes.
- Then do `∫[0 to pi/3] tan x sec^2 x dx`.
- Answer: `3/2`.

## 38. u-Substitution

Concept:

- Choose `u` equal to the inside function.
- Replace `dx` and the limits, then integrate.

Know:

- You need the derivative of `u` present, up to a constant.
- For definite integrals, change the limits and never convert back.

Practice:

- `∫ sin x cos x dx` with `u = sin x`.
- `∫ cos(sqrt(2x)) / sqrt(x) dx` with `u = sqrt(2x)`.
- `∫ sec^3 x tan x dx` with `u = sec x`.
- See `Q16.1` and `Q16.2`.

## 39. Integration by parts

Concept:

- Integration by parts reverses the product rule.

Know:

- `∫ u dv = uv - ∫ v du`.
- Pick `u` so that its derivative is simpler.
- Pick `dv` so that you can integrate it.

Practice:

- Integrate `x e^x dx` with `u = x` and `dv = e^x dx`.
- Integrate `x cos x dx` with `u = x` and `dv = cos x dx`.

## 40. The DI method for integration by parts

Concept:

- The DI table organizes repeated integration by parts.

Know:

- Column D holds derivatives of `u`.
- Column I holds antiderivatives of `dv`.
- Multiply diagonally, alternating signs, and add the final integral row.

Practice:

- Use a DI table for `x^2 e^x dx`.
- D column: `x^2`, `2x`, `2`, `0`.
- I column: `e^x`, `e^x`, `e^x`, `e^x`.
- Answer: `x^2 e^x - 2x e^x + 2 e^x + C`.

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

Practice:

- `Q01.2`, `Q01.3`, and `Q01.4`.

## Exact trig values

Concept:

- Memorize the unit circle values for `0`, `pi/6`, `pi/4`, `pi/3`, and `pi/2`.

Know:

- `sin`: `0`, `1/2`, `sqrt(2)/2`, `sqrt(3)/2`, `1`.
- `cos`: `1`, `sqrt(3)/2`, `sqrt(2)/2`, `1/2`, `0`.
- `tan`: `0`, `1/sqrt(3)`, `1`, `sqrt(3)`, undefined.
- Use ASTC for quadrant signs.
- Use sum, difference, and half-angle formulas for 15 and 22.5 degree angles.

Practice:

- `Q01.1`.

## Graph transformations

Concept:

- Transform a parent graph in a fixed order.

Know:

- For `y = a f(b(x - h)) + k`, work inside out.
- Horizontal shift first, then horizontal stretch or reflection.
- Then vertical stretch, then vertical reflection, then vertical shift.
- The horizontal shift feels backwards: `(x + 4)` means left 4.

Practice:

- `Q02.1` and `Q02.2`.

## Limits and continuity

Concept:

- A function is continuous at a point if the limit equals the function value.

Know:

- Continuity needs three things: `f(a)` exists, the limit exists, and they are equal.
- Differentiable implies continuous, but not the reverse.
- `|x|` is continuous but not differentiable at 0.

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

Practice:

- `Q04.1`.

## Tangent lines and perpendicular slopes

Concept:

- The slope of the tangent line at `a` is `f'(a)`.

Know:

- Parallel means equal slopes.
- Perpendicular means negative reciprocal slopes.
- Perpendicular to slope `m` means `f'(x) = -1/m`.

Practice:

- `Q09.1`.

## Implicit differentiation

Concept:

- Differentiate both sides with respect to `x`.
- Every `y` produces a `y'` by the chain rule.

Know:

- Products of `x` and `y` need the product rule.
- Collect all `y'` terms, factor, and solve.

Practice:

- `Q10.1` and `Q10.2`.

## Related rates

Concept:

- Variables change with time.
- Differentiate an equation with respect to `t`.

Know:

- Name the variables and write what is given and wanted as derivatives with respect to `t`.
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
- Choose `a` as the nearest value you know exactly.
- Convert degrees to radians for trig problems.

Practice:

- `Q12.1`, `Q12.2`, and `Q12.3`.

## Newton's method

Concept:

- Approximate a root with repeated tangent-line steps.

Know:

- `x_(n+1) = x_n - f(x_n) / f'(x_n)`.
- Keep all decimals between steps and round only at the end.

Practice:

- `Q13.1`.

## Curve sketching with calculus

Concept:

- Use domain, asymptotes, `f'`, and `f''` to build an accurate graph.

Know:

- `f' = 0` gives critical points.
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
- The width is `b - a`, not just `b`.

Practice:

- `Q17.1`, `Q17.2`, and `Q17.3`.

## Area between curves

Concept:

- Integrate upper curve minus lower curve.

Know:

- Find intersection points by setting the curves equal.
- If the curves cross inside the interval, split the integral.

Practice:

- `Q19.1` and `Q19.2`.

## Net change and motion

Concept:

- Net change equals the integral of a rate.

Know:

- Displacement is `∫ v dt`.
- Distance is `∫ |v| dt`.
- Split distance at the zeros of velocity.

Practice:

- `Q19.3`, `Q19.8`, and `Q19.9`.

## Work

Concept:

- Work equals force integrated over distance.

Know:

- Spring: `F = kx`, so `W = (1/2) k d^2`.
- Chain: integrate the weight of each small piece over the height it is lifted.

Practice:

- `Q19.4` and `Q19.5`.

## Average value of a function

Concept:

- Average value is the integral divided by the interval width.

Know:

- `f_avg = (1 / (b - a)) ∫[a to b] f(x) dx`.

Practice:

- `Q19.6` and `Q19.7`.

---

# Part 5: The one-page formula card

Memorize these before each exam.

Derivative rules:

- Constant: `d/dx [c] = 0`.
- Power: `d/dx [x^n] = n x^(n - 1)`.
- Sum: `(f + g)' = f' + g'`.
- Product: `(fg)' = f'g + fg'`.
- Quotient: `(f/g)' = (f'g - fg') / g^2`.
- Chain: `d/dx [f(g(x))] = f'(g(x)) g'(x)`.

Trig derivatives:

- `sin x -> cos x`.
- `cos x -> -sin x`.
- `tan x -> sec^2 x`.
- `cot x -> -csc^2 x`.
- `sec x -> sec x tan x`.
- `csc x -> -csc x cot x`.

Exponential and log:

- `e^x -> e^x`.
- `a^x -> a^x ln a`.
- `ln x -> 1/x`.

Integrals:

- `∫ x^n dx = x^(n + 1) / (n + 1) + C`, for `n ≠ -1`.
- `∫ 1/x dx = ln|x| + C`.
- `∫ sin x dx = -cos x + C`.
- `∫ cos x dx = sin x + C`.
- `∫ sec^2 x dx = tan x + C`.
- `∫ csc^2 x dx = -cot x + C`.
- `∫ sec x tan x dx = sec x + C`.
- `∫ csc x cot x dx = -csc x + C`.

Fundamental Theorem:

- `d/dx ∫[a to x] f(t) dt = f(x)`.
- `∫[a to b] f(x) dx = F(b) - F(a)`.

Average value:

- `f_avg = (1 / (b - a)) ∫[a to b] f(x) dx`.

Special limits:

- `lim(u -> 0) sin(u)/u = 1`.
- `lim(u -> 0) (1 - cos(u))/u = 0`.

Key identities:

- `sin^2 x + cos^2 x = 1`.
- `1 + tan^2 x = sec^2 x`.
- `1 + cot^2 x = csc^2 x`.
- `sin(2x) = 2 sin x cos x`.
- `cos(2x) = cos^2 x - sin^2 x = 1 - 2 sin^2 x = 2 cos^2 x - 1`.
- `1 - cos(2x) = 2 sin^2 x`.
- `1 + cos(2x) = 2 cos^2 x`.

---

# Part 6: Practice map

Use this map to drill every question note against the topic.

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

Sample exams:

- `Sample Midterm Exam 1` and `Sample Midterm Exam 2` in the course folder.
- `Sample Final Exam 1` and `Sample Final Exam 2` in the course folder.
- The all-exam question bank is `MATH265-All-Exam-Questions.md`.

---

# Part 7: Weekly practice plan

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

---

# Part 8: Final checklist before exam day

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
- You have timed yourself on a full sample paper.

