# MATH265_Review.md

# Unit 1: Fundamentals
### **Trigonometric Identities (Q1)**
For $cos(-\frac{\pi}{12})$, you need the **Difference Formula**:
* **Cosine Difference:** $cos(A - B) = cos(A)cos(B) + sin(A)sin(B)$
* **Common Angles:** You must know the exact values for $30^\circ (\frac{\pi}{6})$, $45^\circ (\frac{\pi}{4})$, and $60^\circ (\frac{\pi}{3})$.
* **Formulas to Memorize:**
    * Difference formula for cosine: $\cos(A - B) = \cos A \cos B + \sin A \sin B$
    * Basic graph transformations: $y = a f(x - h) + k$ (shift right $h$, up $k$, scale vertically by $a$).


# Unit 2: Limits and Continuity
This area focuses on evaluating the behavior of functions as they approach specific points, including handling indeterminate forms.
* **Formulas to Memorize:**
    * Difference of squares: $a^2 - b^2 = (a-b)(a+b)$
    * Special trigonometric limit: $\lim_{x\rightarrow 0} \frac{\sin(kx)}{kx} = 1$

### **Special Limits (Q4e)**
When dealing with trigonometric limits, this fundamental identity is essential:
* $\lim_{\theta \to 0} \frac{sin(\theta)}{\theta} = 1$


# Unit 3: Derivatives
This section tests your mechanical ability to apply derivative rules.
* **Formulas to Memorize:**
    * Product Rule: $\frac{d}{dx}[uv] = u'v + uv'$
    * Quotient Rule: $\frac{d}{dx}[\frac{u}{v}] = \frac{u'v - uv'}{v^2}$
    * Chain Rule: $\frac{d}{dx}[f(g(x))] = f'(g(x))g'(x)$

# Unit 4: Applications of Differentiation
### **Differentiation Rules (Q5, Q6, Q8)**
These are the "bread and butter" of Unit 3:
* **Power Rule:** $\frac{d}{dx}[x^n] = nx^{n-1}$
* **Product Rule:** $\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$
* **Quotient Rule:** $\frac{d}{dx}[\frac{f(x)}{g(x)}] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$
* **Chain Rule:** $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$

This is where calculus connects to geometry and real-world rates of change. 
* **Formulas to Memorize:**
    * Linear Approximation / Differentials: $f(x+\Delta x) \approx f(x) + f'(x)dx$ (where $dy = f'(x)dx$)
    * Newton's Method: $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
    * Volume of a Cone: $V = \frac{1}{3}\pi r^2 h$


### **Tangent Lines & Linearization (Q6, Q9)**
* **Perpendicular Slopes:** If two lines are perpendicular, their slopes $m_1$ and $m_2$ satisfy $m_1 = -\frac{1}{m_2}$.
* **Differentials:** To approximate a value, use $f(a + dx) \approx f(a) + f'(a)dx$.


# Unit 5: Integrals
Moving backward from derivatives to find antiderivatives and areas.
* **Formulas to Memorize:**
    * Power Rule for Integration: $\int x^n dx = \frac{x^{n+1}}{n+1} + C$
    * Fundamental Theorem of Calculus (Part 1): $\frac{d}{dx} \int_{a}^{g(x)} f(t) dt = f(g(x))g'(x)$


# Unit 6: Applications of Integration
### **Geometry & Related Rates (Q7)**
For problems involving physical changes, you must know standard volume formulas:
* **Volume of a Cone:** $V = \frac{1}{3}\pi r^2 h$
* **Relationship:** Since the problem states diameter equals height ($2r = h$), you need to substitute $r = \frac{h}{2}$ into the volume formula before differentiating.

Using integrals to model physical situations like area, work, and net change. 

**Formulas to Memorize:**
    
    * Area between curves: $A = \int_{a}^{b} (\text{Top Function} - \text{Bottom Function}) dx$

    * Work done lifting a cable/chain: $W = \int_{0}^{h} (\text{density})(\text{gravity})(y) dy$





# **MATH 265: Calculus I Midterm Cheat Sheet**

## **1. Fundamentals & Trigonometry**
Essential for Question 1 (Trig Values) and Question 2 (Composites/Domains).

### **Exact Trigonometric Values**
Derived from the unit circle where $\cos(\theta) = x$ and $\sin(\theta) = y$

| Angle ($\theta$) | $\sin(\theta)$ | $\cos(\theta)$ | $\tan(\theta)$ |
| :--- | :--- | :--- | :--- |
| **$0$** | $0$ | $1$ | $0$ |
| **$\pi/6$ ($30^\circ$)** | $1/2$ | $\sqrt{3}/2$ | $\sqrt{3}/3$ |
| **$\pi/4$ ($45^\circ$)** | $\sqrt{2}/2$ | $\sqrt{2}/2$ | $1$ |
| **$\pi/3$ ($60^\circ$)** | $\sqrt{3}/2$ | $1/2$ | $\sqrt{3}$ |
| **$\pi/2$ ($90^\circ$)** | $1$ | $0$ | Undefined |

> **Memory Trick:** Sine values follow the pattern $\frac{\sqrt{n}}{2}$ for $n=0, 1, 2, 3, 4$.

### **Trig Identities & Formulas**
* **Even/Odd:** $\cos(-x) = \cos(x)$ and $\sin(-x) = -\sin(x)$.
* **Sum/Difference:** $\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$.
* **Composite Domain:** For $f(g(x))$, the domain includes all $x$ in the domain of $g$ such that $g(x)$ is in the domain of $f$.

---

## **2. Limits & Continuity**
Essential for Question 4 (Evaluating Limits) and Question 10 (Curve Sketching).

### **Evaluating Limits**
1.  **Direct Substitution:** Always try this first.
2.  **Indeterminate Forms ($0/0$):**
    * **Factoring:** Cancel common terms (e.g., $(x-a)$).
    * **Conjugates:** Multiply by $\frac{\sqrt{a}+b}{\sqrt{a}+b}$ for square root limits.
3.  **Special Trig Limit:** $\lim_{x \to 0} \frac{\sin(ax)}{ax} = 1$.
4.  **Infinite Limits:** $\lim_{x \to \infty} \frac{1}{x^n} = 0$. Divide by the highest power of $x$ in the denominator.

### **Continuity & Differentiability**
* **Not Differentiable at:** Sharp corners (cusps), vertical tangents, or points of discontinuity.

---

## **3. Differentiation Rules**
Essential for Questions 5, 6, 8, and 9.

### **The Big Rules**
* **Power Rule:** $\frac{d}{dx} [x^n] = nx^{n-1}$.
* **Product Rule:** $(fg)' = f'g + fg'$.
* **Quotient Rule:** $(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$.
* **Chain Rule:** $\frac{d}{dx} [f(g(x))] = f'(g(x)) \cdot g'(x)$.

### **Special Methods**
* **Implicit Differentiation:** Differentiate both sides with respect to $x$; treat $y$ as a function of $x$ and append $\frac{dy}{dx}$ whenever $y$ is differentiated.
* **Differentials (Linearization):** $f(x) \approx f(a) + f'(a)(x - a)$.

---

## **4. Applications of Derivatives**
Essential for Question 3 (Graphing), Question 6 (Tangents), and Question 7 (Related Rates).

### **Tangent & Normal Lines**
* **Slope of Tangent:** $m = f'(x_0)$[cite: 32].
* **Perpendicular (Normal) Slope:** $m_{\perp} = -\frac{1}{m}$.

### **Related Rates Strategy**
1.  **Identify:** List knowns (e.g., $dV/dt = 0.5$) and unknowns (e.g., $dh/dt$).
2.  **Equation:** Relate variables (e.g., $V = \frac{1}{3}\pi r^2 h$).
3.  **Substitute:** Use given relationships (like $d=h \Rightarrow r=h/2$) to reduce variables.
4.  **Differentiate:** Use the Chain Rule with respect to time ($t$).

### **Function Transformations**
* $f(x+c)$: Shift Left $c$ units.
* $f(x)+c$: Shift Up $c$ units.
* $a f(x)$: Vertical Stretch ($a>1$) or Compression ($a<1$).

---

This comprehensive cheat sheet is tailored specifically to the requirements of the MATH 265 Sample Midterm and the additional trigonometric foundations provided.

---

# **MATH 265: Calculus I Midterm Cheat Sheet**

## **I. Trigonometric Foundations & Identities**
*Crucial for Question 1 (Exact Values) and Question 5c (Trig Derivatives).*

### [cite_start]**Exact Values Table** [cite: 5, 10, 19, 20, 21, 22, 23]
| Angle ($\theta$) | $\sin(\theta)$ | $\cos(\theta)$ | $\tan(\theta)$ |
| :--- | :--- | :--- | :--- |
| **$0$** | $0$ | $1$ | $0$ |
| **$\pi/6$ ($30^\circ$)** | $1/2$ | $\sqrt{3}/2$ | $\sqrt{3}/3$ |
| **$\pi/4$ ($45^\circ$)** | $\sqrt{2}/2$ | $\sqrt{2}/2$ | $1$ |
| **$\pi/3$ ($60^\circ$)** | $\sqrt{3}/2$ | $1/2$ | $\sqrt{3}$ |
| **$\pi/2$ ($90^\circ$)** | $1$ | $0$ | Undefined |

### **Key Formulas to Memorize**
* [cite_start]**Sum/Difference Identities:** $\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$ [cite: 10]
* [cite_start]**Even/Odd Properties:** $\cos(-x) = \cos(x)$ and $\sin(-x) = -\sin(x)$ [cite: 10]
* [cite_start]**Special Limit:** $\lim_{\theta \to 0} \frac{\sin(\theta)}{\theta} = 1$ [cite: 25]

---

## **II. Functions & Transformations**
*Crucial for Question 2 (Composites) and Question 3 (Graphing).*

### [cite_start]**Composite Functions & Domain** [cite: 11, 12]
* [cite_start]**Composition:** $f(g(x))$ means substituting the entire expression of $g(x)$ into every $x$ in $f(x)$[cite: 14].
* [cite_start]**Domain Strategy:** The domain of $f(g(x))$ is the set of all $x$ in the domain of $g$ such that $g(x)$ is in the domain of $f$[cite: 12].

### [cite_start]**Graph Transformations ($y = a \cdot f(x - h) + k$)** [cite: 16, 17, 18]
1.  **Horizontal Shift ($h$):** $f(x+h)$ shifts **Left**; [cite_start]$f(x-h)$ shifts **Right**[cite: 16].
2.  [cite_start]**Vertical Stretch/Compression ($a$):** Multiply $y$-values by $a$[cite: 16].
3.  **Reflection:** $-f(x)$ reflects over the $x$-axis; $f(-x)$ reflects over the $y$-axis.
4.  **Vertical Shift ($k$):** $f(x)+k$ shifts **Up**; $f(x)-k$ shifts **Down**.

---

## **III. Limits & Continuity**
[cite_start]*Crucial for Question 4 (Evaluations) and Question 10 (Sketching).* [cite: 20, 38]

### [cite_start]**Evaluation Strategies** [cite: 20]
* [cite_start]**Direct Substitution:** Try this first[cite: 21].
* **Indeterminate Form ($0/0$):**
    * [cite_start]**Factoring:** Factor and cancel terms (e.g., $(x-a)$)[cite: 22].
    * [cite_start]**Conjugates:** Multiply by $\frac{\sqrt{A}+B}{\sqrt{A}+B}$ for square root limits[cite: 24].
    * [cite_start]**Trig Manipulation:** Use identities to reach the $\frac{\sin(x)}{x}$ form[cite: 25].
* [cite_start]**Infinite Limits:** $\lim_{x \to \infty} f(x) = L$ indicates a horizontal asymptote at $y=L$[cite: 41].

---

## **IV. Differentiation Rules & Methods**
*Crucial for Question 5 (Derivatives), Question 8 (Implicit), and Question 9 (Differentials).*

### [cite_start]**Derivative Rules** [cite: 26]
* [cite_start]**Power Rule:** $\frac{d}{dx} [x^n] = nx^{n-1}$[cite: 27].
* **Product Rule:** $\frac{d}{dx} [uv] = u'v + uv'$.
* [cite_start]**Quotient Rule:** $\frac{d}{dx} [\frac{u}{v}] = \frac{u'v - uv'}{v^2}$[cite: 29].
* [cite_start]**Chain Rule:** $\frac{d}{dx} [f(g(x))] = f'(g(x)) \cdot g'(x)$[cite: 30, 31].

### **Special Procedures**
* **Implicit Differentiation:** Differentiate both sides with respect to $x$. [cite_start]Treat $y$ as $y(x)$ and add a $\frac{dy}{dx}$ (or $y'$) term whenever you differentiate a $y$ variable[cite: 35, 36].
* [cite_start]**Differentials (Linearization):** To approximate $f(x)$, use $f(x) \approx f(a) + f'(a)dx$, where $a$ is a "nice" nearby number[cite: 37].

---

## **V. Applications of the Derivative**
*Crucial for Question 6 (Tangents) and Question 7 (Related Rates).*

### [cite_start]**Tangent Lines** [cite: 32]
* [cite_start]**Slope ($m$):** The derivative $f'(x)$ gives the slope of the tangent line[cite: 32].
* [cite_start]**Perpendicular Lines:** If a line is perpendicular to $y = mx+b$, its slope is $m_{\perp} = -1/m$[cite: 32].

### [cite_start]**Related Rates: The Cone Problem** [cite: 33]
1.  [cite_start]**Formula:** Volume of a cone $V = \frac{1}{3}\pi r^2 h$[cite: 33].
2.  [cite_start]**Constraint:** If diameter = height ($2r=h$), then $r = h/2$[cite: 33].
3.  [cite_start]**Substitution:** Substitute $r$ to get $V$ in terms of $h$ *before* differentiating: $V = \frac{1}{3}\pi (\frac{h}{2})^2 h = \frac{\pi}{12}h^3$[cite: 33, 34].
4.  [cite_start]**Implicit Differentiation:** Differentiate with respect to time ($t$): $\frac{dV}{dt} = \frac{\pi}{4}h^2 \frac{dh}{dt}$[cite: 34].




To excel in MATH 265, you must master the transition from algebraic manipulation to the rigorous study of change. [cite_start]This cheatsheet synthesizes the essential theorems, formulas, and strategies required to solve the problems found in your sample exams[cite: 4, 47, 118, 171].

---

## 1. Fundamentals & Trigonometry
[cite_start]Used for exact value evaluations and function compositions[cite: 10, 11, 54].

* [cite_start]**Composite Functions:** $(f \circ g)(x) = f(g(x))$[cite: 12]. [cite_start]The domain of $f(g(x))$ is the set of all $x$ in the domain of $g$ such that $g(x)$ is in the domain of $f$[cite: 12].
* **Key Identities:**
    * [cite_start]**Sum/Difference:** $\cos(\alpha \pm \beta) = \cos \alpha \cos \beta \mp \sin \alpha \sin \beta$[cite: 10].
    * [cite_start]**Pythagorean:** $\sin^2 x + \cos^2 x = 1$ and $1 + \tan^2 x = \sec^2 x$[cite: 106, 207].
    * [cite_start]**Double Angle:** $\sin(2x) = 2 \sin x \cos x$ [cite: 150] [cite_start]and $\cos(2x) = 1 - 2\sin^2 x$[cite: 91].

---

## 2. Limits and Continuity
[cite_start]Essential for evaluating behavior at boundaries and asymptotes[cite: 20, 88, 178].

* [cite_start]**Indeterminate Forms:** If you encounter $0/0$ or $\infty/\infty$, use algebraic simplification (factoring, rationalizing) or L'Hôpital's Rule[cite: 22, 24, 90].
* [cite_start]**Special Trig Limit:** $\lim_{x \to 0} \frac{\sin(ax)}{ax} = 1$[cite: 25].
* [cite_start]**Asymptotes:** * **Vertical:** Occur at $x = c$ where $\lim_{x \to c} f(x) = \pm \infty$[cite: 85, 137, 196].
    * [cite_start]**Horizontal:** Occur at $y = L$ where $\lim_{x \to \pm\infty} f(x) = L$[cite: 85, 195].

---

## 3. Differentiation Rules
[cite_start]The "toolbox" for finding rates of change[cite: 26, 101, 124].

* [cite_start]**Power Rule:** $\frac{d}{dx}[x^n] = nx^{n-1}$[cite: 27].
* [cite_start]**Product Rule:** $(fg)' = f'g + fg'$[cite: 126].
* [cite_start]**Quotient Rule:** $(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$[cite: 29, 106, 185].
* [cite_start]**Chain Rule:** $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$[cite: 30, 31, 104, 130].
* [cite_start]**Implicit Differentiation:** Differentiate both sides with respect to $x$, treating $y$ as $y(x)$ and using the chain rule (i.e., $\frac{d}{dx}[y^2] = 2y \frac{dy}{dx}$)[cite: 35, 109].

---

## 4. Applications of Differentiation
[cite_start]Connecting derivatives to geometry and real-world change[cite: 32, 137, 140, 187].

* [cite_start]**Tangent Lines:** Equation is $y - f(a) = f'(a)(x - a)$[cite: 109].
    * [cite_start]*Note:* Perpendicular lines have slopes $m_1 \cdot m_2 = -1$[cite: 32].
* [cite_start]**Related Rates:** Identify the given rate (e.g., $dV/dt$), the unknown rate (e.g., $dh/dt$), and the relating equation ($V = \frac{1}{3}\pi r^2 h$)[cite: 33, 64, 111]. Differentiate with respect to $t$.
* [cite_start]**Linearization (Differentials):** $f(x) \approx f(a) + f'(a)(x - a)$[cite: 37, 99, 131].
* **Curve Sketching:**
    * $f'(x) > 0 \implies$ Increasing; [cite_start]$f'(x) < 0 \implies$ Decreasing[cite: 197, 198].
    * $f''(x) > 0 \implies$ Concave Up; [cite_start]$f''(x) < 0 \implies$ Concave Down[cite: 199].
* **Optimization:** Find critical points by setting $f'(x) = 0$. [cite_start]Test endpoints for absolute extrema on closed intervals (Extreme Value Theorem)[cite: 140, 143, 187, 212].

---

## 5. Integration
[cite_start]The reverse process of differentiation and the study of accumulation[cite: 147, 205].

* **Fundamental Theorem of Calculus:**
    * [cite_start]Part 1: $\frac{d}{dx} \int_{a}^{x} f(t) dt = f(x)$[cite: 159].
    * [cite_start]Part 2: $\int_{a}^{b} f(x) dx = F(b) - F(a)$[cite: 151, 153].
* **Substitution Rule (u-sub):** Used for $\int f(g(x))g'(x) dx$. [cite_start]Let $u = g(x)$, then $du = g'(x) dx$[cite: 206, 207].
* **Common Integrals:**
    * [cite_start]$\int x^n dx = \frac{x^{n+1}}{n+1} + C$[cite: 148, 152].
    * [cite_start]$\int \sin x dx = -\cos x + C$[cite: 151].
    * [cite_start]$\int \sec^2 x dx = \tan x + C$[cite: 207].

---

## 6. Applications of Integration
[cite_start][cite: 157, 162, 165, 218].

* [cite_start]**Area Between Curves:** $A = \int_{a}^{b} [f_{upper}(x) - g_{lower}(x)] dx$[cite: 157, 218].
* [cite_start]**Average Value:** $f_{ave} = \frac{1}{b-a} \int_{a}^{b} f(x) dx$[cite: 165, 234].
* **Work:** $W = \int_{a}^{b} F(x) dx$. 
    * [cite_start]For springs (Hooke's Law): $F(x) = kx$[cite: 223, 224].
    * [cite_start]For lifting chains: Use the density/weight of segments[cite: 162].
* **Distance vs. Displacement:**
    * [cite_start]Displacement: $\int_{t_1}^{t_2} v(t) dt$[cite: 228].
    * [cite_start]Total Distance: $\int_{t_1}^{t_2} |v(t)| dt$[cite: 229].



Here is your **complete exam cheat sheet in Markdown**, tailored specifically to the uploaded **MATH 265 Sample Midterm Exam 2** .
It includes **all rules, formulas, identities, and strategies** needed to solve every problem.

---

# 🧠 MATH 265 – MIDTERM EXAM CHEAT SHEET (FULL COVERAGE)

---

# 🔢 1. FUNCTIONS & DEFINITIONS

## ✅ What makes a function

* Each input → exactly **one output**
* Check for:

  * Division by zero ❌
  * Square root of negative ❌

---

# 📦 2. GEOMETRIC MODELING (Cone Problem)

## Volume of a Cone

genui{"math_block_widget_always_prefetch_v2":{"content":"V=\frac{1}{3}\pi r^2 h"}}

### Special condition:

* If height = 2r → substitute:
  [
  V = \frac{1}{3}\pi r^2 (2r) = \frac{2}{3}\pi r^3
  ]

### Domain:

* (r > 0)

---

# 📊 3. INTERPRETING FUNCTIONS

## Difference Quotient Meaning

[
\frac{P(5) - P(3)}{5 - 3}
]
➡️ Average rate of change (population growth)

## Derivative Meaning

[
P'(10)
]
➡️ Instantaneous rate (growth at year 10)

---

# 📉 4. GRAPH TRANSFORMATIONS (ABSOLUTE VALUE)

## Base Function

[
y = |x|
]

## Transformations

[
f(x) = a|x - h| + k
]

* Shift right: (x - h)
* Shift left: (x + h)
* Vertical stretch: (a)
* Reflection if (a < 0)

---

# 🔍 5. LIMITS & GRAPH INTERPRETATION

## Types of Limits

* Left-hand: (x \to a^-)
* Right-hand: (x \to a^+)

## Continuity

Function is continuous if:

* Limit exists
* Function value exists
* They are equal

## Non-differentiable points

* Corners (like |x|)
* Cusps
* Vertical tangents

---

# 📐 6. ASYMPTOTES

## Vertical Asymptote

* Denominator = 0 (after simplification)

## Horizontal Asymptote

If:

* degree(top) < degree(bottom) → (y = 0)
* equal → ratio of leading coefficients
* top > bottom → none

---

# ⚡ 7. LIMIT TECHNIQUES (CORE SECTION)

## 1. Direct Substitution

Use if no indeterminate form

---

## 2. Factoring (for 0/0)

* Factor numerator & denominator
* Cancel common terms

---

## 3. Rationalizing

Multiply by conjugate:
[
\frac{1}{1 - \cos x}
]

---

## 4. Important Trig Limits

[
\lim_{x \to 0} \frac{\sin x}{x} = 1
]

[
\lim_{x \to 0} \frac{1 - \cos x}{x} = 0
]

---

## 5. Infinite Limits

* Nonzero / 0 → ±∞

---

# 📏 8. LINEARIZATION (APPROXIMATION)

## Formula

[
f(x) \approx f(a) + f'(a)(x - a)
]

## Strategy

* Convert degrees → radians if trig
* Use known angle near value

---

# ⚡ 9. DERIVATIVES (ALL RULES YOU NEED)

## Power Rule

\frac{d}{dx}(x^n)=nx^{n-1}

---

## Trig Derivatives

[
\frac{d}{dx}(\sin x) = \cos x
]
[
\frac{d}{dx}(\cos x) = -\sin x
]
[
\frac{d}{dx}(\tan x) = \sec^2 x
]
[
\frac{d}{dx}(\cot x) = -\csc^2 x
]
[
\frac{d}{dx}(\sec x) = \sec x \tan x
]

---

## Chain Rule

[
\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)
]

---

## Product Rule

[
(fg)' = f'g + fg'
]

---

## Quotient Rule

[
\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}
]

---

# 📌 10. IMPLICIT DIFFERENTIATION

Used when equation is mixed (x and y)

### Strategy:

* Differentiate both sides
* Treat y as function of x
* Multiply by (dy/dx)

---

# 📈 11. TANGENT LINE

## Formula

[
y - y_1 = m(x - x_1)
]

Where:
[
m = \frac{dy}{dx}
]

---

# 🚀 12. RELATED RATES

## Strategy

1. Write equation relating variables
2. Differentiate w.r.t time
3. Substitute known values

---

# 📐 13. TRIG EXACT VALUES (MUST MEMORIZE)

| Angle | sin  | cos  | tan       |
| ----- | ---- | ---- | --------- |
| 0     | 0    | 1    | 0         |
| π/6   | 1/2  | √3/2 | √3/3      |
| π/4   | √2/2 | √2/2 | 1         |
| π/3   | √3/2 | 1/2  | √3        |
| π/2   | 1    | 0    | undefined |

---

## 🧠 Memory Tricks

### Sine Pattern

[
\sin(\theta) = \frac{\sqrt{0,1,2,3,4}}{2}
]

### Cosine = reverse of sine

### Tangent

[
\tan = \frac{\sin}{\cos}
]

---

# ⚠️ COMMON EXAM TRAPS

* Forgetting radians vs degrees
* Missing chain rule
* Not simplifying before limits
* Division by zero in domain
* Wrong asymptote rules
* Ignoring non-differentiable points

---

# 🎯 FINAL STRATEGY

### Order to solve exam:

1. Easy definitions & interpretation
2. Algebra / geometry
3. Limits
4. Derivatives
5. Applications (tangent, related rates)


# MATH 265 — Calculus I · Exam 2 Cheat Sheet
**Time:** 3 hrs | **Passing:** 55% | **Total:** 94 pts

---

## 1. FUNCTIONS & WELL-DEFINEDNESS (Q1 — 4 pts)

A relation is a **well-defined function** of x if every input x gives **exactly one** output y.

**Test:** Solve for y. If you get two or more y-values for a single x → **not a function**.

| Equation | Strategy | Verdict |
|---|---|---|
| `2y / (x²−3|x|) = 1` | Solve → y = (x²−3|x|)/2. One y per x. | ✅ Function |
| `y² + x² = 10` | Solve → y = ±√(10−x²). Two y-values. | ❌ Not a function |

**Vertical Line Test:** a graph is a function iff no vertical line hits it more than once.

---

## 2. FUNCTIONS OF GEOMETRY / APPLIED FUNCTIONS (Q2 — 4 pts)

**Cone volume formula (given on exam):**
```
V = πr²h / 3
```

**Strategy for "express V as function of r only":**
1. Use the constraint: h = 2r (height is double the radius)
2. Substitute into V: V(r) = πr²(2r)/3 = **2πr³/3**
3. Domain: r > 0 (radius must be positive)
4. Evaluate: V(3) = 2π(27)/3 = **18π**

**General tip:** When a word problem gives a geometric formula with two variables and a relationship between them, substitute the relationship to reduce to one variable.

---

## 3. INTERPRETING DERIVATIVES & DIFFERENCE QUOTIENTS (Q3 — 4 pts)

### Average Rate of Change (Difference Quotient)
```
[f(b) − f(a)] / (b − a)  =  average rate of change of f on [a, b]
```

**In plain English:** "The average [units of f] per [units of x] between x=a and x=b"

> **Example:** [P(15) − P(2)] / 13 = 1,431
> → "The city's population grew by an average of **1,431 people per year** between year 2 and year 15."

### Instantaneous Rate of Change (Derivative)
```
f'(a)  =  instantaneous rate of change at x = a
```

> **Example:** P'(10) = 14,000
> → "In year 10, the city's population was growing at a rate of **14,000 people per year**."

**Key distinction:** difference quotient = *average* over an interval; derivative = *instantaneous* at a point.

---

## 4. ABSOLUTE VALUE — TRANSFORMATIONS (Q4 — 6 pts)

**Parent function:** y = |x|  (V-shape, vertex at origin)

### Transformation Rules (apply in this order)

| Transformation | Form | Effect |
|---|---|---|
| Horizontal shift | \|x − h\| | shift RIGHT by h |
| Horizontal shift | \|x + h\| | shift LEFT by h |
| Vertical stretch/compress | a\|x\| | multiply y-values by \|a\| |
| Reflection over x-axis | −a\|x\| | flip upside down (if a > 0) |
| Vertical shift | \|x\| + k | shift UP by k |

### Worked Example: f(x) = −3|x − 2|

1. Start with y = |x|
2. Replace x with (x−2): shift **right 2** → vertex moves to (2, 0)
3. Multiply by 3: **vertical stretch** by factor 3
4. Multiply by −1: **reflect over x-axis** (V becomes ∧-shape)

**Key points to plot:** vertex (2, 0); pick x = 0 → f(0) = −3|−2| = −6; x = 4 → f(4) = −6

---

## 5. LIMITS (expect ~16 pts)

### Techniques

**1. Direct substitution** — always try first
```
lim(x→a) f(x) = f(a)   if f is continuous at a
```

**2. Factor & cancel** — when substitution gives 0/0
```
Factor numerator and/or denominator → cancel the (x−a) term → substitute
```

**3. Rationalize** — for square root indeterminate forms
```
Multiply top & bottom by the conjugate:  √A − √B  →  use  √A + √B
Difference of squares:  (√A − √B)(√A + √B) = A − B
```

**4. Special trig limits** (must memorize)
```
lim(x→0)  sin(x)/x  = 1
lim(x→0)  [1 − cos(x)]/x  = 0
lim(x→0)  sin(kx)/x  = k       (multiply & divide by k)
lim(x→0)  sin(kx)/(kx)  = 1
```

**5. Limits at infinity** — for rational functions
```
deg(num) < deg(den)  →  limit = 0
deg(num) = deg(den)  →  limit = ratio of leading coefficients
deg(num) > deg(den)  →  limit = ±∞ (DNE)
```

**6. One-sided limits** — for absolute values or piecewise
```
|x| =  x   if x ≥ 0
|x| = −x   if x < 0
```
Check lim from left and right separately. If they differ → limit **DNE**.

### When Does a Limit Not Exist?
- Left-hand limit ≠ right-hand limit
- Function oscillates (e.g. sin(1/x) as x→0)
- Function grows without bound (→ ±∞)

---

## 6. CONTINUITY (likely tested)

A function f is **continuous at x = a** if ALL THREE hold:
1. f(a) is defined
2. lim(x→a) f(x) exists
3. lim(x→a) f(x) = f(a)

**Types of discontinuity:**

| Type | Description | Example |
|---|---|---|
| Removable | Hole in graph; limit exists but ≠ f(a) | (x²−1)/(x−1) at x=1 |
| Jump | Left & right limits exist but differ | Piecewise step function |
| Infinite | f(x) → ±∞ | 1/x at x=0 |

---

## 7. DERIVATIVES — RULES (expect ~8+ pts)

### Core Rules
```
d/dx [c]         = 0                          (Constant)
d/dx [x^n]       = n·x^(n−1)                 (Power Rule)
d/dx [cf(x)]     = c·f'(x)                   (Constant Multiple)
d/dx [f ± g]     = f' ± g'                   (Sum/Difference)
d/dx [f·g]       = f'g + fg'                  (Product Rule)
d/dx [f/g]       = (f'g − fg') / g²           (Quotient Rule)
d/dx [f(g(x))]   = f'(g(x)) · g'(x)          (Chain Rule)
```

### Trig Derivatives
```
d/dx [sin x]  = cos x         d/dx [cos x]  = −sin x
d/dx [tan x]  = sec² x        d/dx [cot x]  = −csc² x
d/dx [sec x]  = sec x tan x   d/dx [csc x]  = −csc x cot x
```

### Other Common Derivatives
```
d/dx [e^x]    = e^x
d/dx [ln x]   = 1/x
d/dx [a^x]    = a^x · ln a
d/dx [|x|]    = x/|x|  = sgn(x)   (x ≠ 0)
```

### Chain Rule — Step by Step
1. Identify outer function f and inner function g
2. Differentiate outer (leave inner unchanged): f'(g(x))
3. Multiply by derivative of inner: × g'(x)

> Example: d/dx[sin(x²)] = cos(x²) · 2x

---

## 8. DOMAIN RULES (Q1 & Q2 type questions)

| Expression | Restriction |
|---|---|
| f(x) / g(x) | g(x) ≠ 0 |
| √f(x) | f(x) ≥ 0 |
| ln(f(x)) | f(x) > 0 |
| Geometry (radius, length) | variable > 0 |

---

## 9. ABSOLUTE VALUE — LIMITS & DERIVATIVES

**Converting |x−a| for limits:**
```
|x − a| = (x−a)   when x > a
|x − a| = −(x−a)  when x < a
```

Always split into cases and evaluate one-sided limits separately.

**Derivative of |x|:**
```
d/dx[|x|] = x/|x|   for x ≠ 0   (undefined at x = 0)
d/dx[|g(x)|] = g'(x) · g(x)/|g(x)|   (chain rule version)
```

---

## 10. QUICK REFERENCE CARD

```
DIFFERENCE QUOTIENT:   [f(b)−f(a)] / (b−a)   ← average rate of change
DERIVATIVE DEFINITION: lim(h→0) [f(x+h)−f(x)] / h   ← instantaneous rate
CONE VOLUME:           V = πr²h/3
WELL-DEFINED FUNCTION: one input → exactly one output
ABSOLUTE VALUE:        splits into two cases at the "corner" point
CONTINUITY:            defined + limit exists + they match
SPECIAL LIMIT:         lim sin(x)/x = 1  as x→0
```




This comprehensive cheatsheet is designed to cover every mathematical concept, formula, and strategy required to solve the problems presented in your MATH 265 Sample Midterm and Final Exams.

---

## 1. Fundamentals & Algebra
* **Composite Functions:** $(f \circ g)(x) = f(g(x))$. To find the domain, $x$ must be in the domain of $g$, and $g(x)$ must be in the domain of $f$.
* **Trigonometric Identities:**
    * **Pythagorean:** $\sin^2 x + \cos^2 x = 1$.
    * **Double Angle:** $\sin(2x) = 2\sin x \cos x$; $\cos(2x) = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$.
    * **Sum/Difference:** $\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$.
* **Transformations:**
    * $f(x) + c$: Vertical shift.
    * $f(x - c)$: Horizontal shift.
    * $af(x)$: Vertical stretch/compression.

---

## 2. Limits and Continuity
* **Evaluation Strategies:**
    1.  **Direct Substitution:** Try this first.
    2.  **Factoring/Cancelation:** For $0/0$ indeterminate forms.
    3.  **Rationalization:** Multiply by the conjugate for square root limits.
    4.  **Infinite Limits:** Divide every term by the highest power of $x$ in the denominator.
* **Special Trig Limit:** $\lim_{x \to 0} \frac{\sin x}{x} = 1$.
* **Continuity:** A function is continuous at $a$ if $\lim_{x \to a} f(x) = f(a)$.

---

## 3. Derivatives: Rules & Methods
* **Definition of Derivative:** $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$.
* **Power Rule:** $\frac{d}{dx}[x^n] = nx^{n-1}$.
* **Product Rule:** $(uv)' = u'v + uv'$.
* **Quotient Rule:** $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$.
* **Chain Rule:** $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$.
* **Implicit Differentiation:** Differentiate both sides with respect to $x$, treating $y$ as a function of $x$ (multiply by $\frac{dy}{dx}$ whenever differentiating $y$).
* **Trig Derivatives:**
    * $(\sin x)' = \cos x$
    * $(\cos x)' = -\sin x$
    * $(\tan x)' = \sec^2 x$
    * $(\sec x)' = \sec x \tan x$
    * $(\cot x)' = -\csc^2 x$

---

## 4. Applications of Differentiation
* **Linearization/Differentials:** $L(x) = f(a) + f'(a)(x-a)$. Used to estimate values like $\sqrt{16.4}$ or $\cos(62^\circ)$.
* **Related Rates:** 1.  Identify given rates and the rate to find.
    2.  Write an equation relating the variables (e.g., $V = \frac{1}{3}\pi r^2 h$).
    3.  Differentiate with respect to time $t$.
* **Curve Sketching:**
    * $f'(x) = 0$: Critical points (Maxima/Minima).
    * $f''(x) > 0$: Concave up; $f''(x) < 0$: Concave down.
    * $f''(x) = 0$: Potential Inflection Points.
* **Optimization:** Find the objective function, differentiate, and find the absolute extremum on the given interval (Extreme Value Theorem).
* **Newton's Method:** $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$.

---

## 5. Integrals: Rules & Techniques
* **Power Rule for Integration:** $\int x^n dx = \frac{x^{n+1}}{n+1} + C$ (for $n \neq -1$).
* **Substitution Rule (u-sub):** Used for "reverse chain rule." Let $u = g(x)$, then $du = g'(x)dx$.
* **Fundamental Theorem of Calculus (Part 1):** $\frac{d}{dx} \int_a^x f(t) dt = f(x)$.
    * *Extended:* $\frac{d}{dx} \int_{g(x)}^{h(x)} f(t) dt = f(h(x))h'(x) - f(g(x))g'(x)$.
* **Fundamental Theorem of Calculus (Part 2):** $\int_a^b f(x) dx = F(b) - F(a)$.
* **Average Value:** $f_{ave} = \frac{1}{b-a} \int_a^b f(x) dx$.

---

## 6. Physics & Geometry Applications
* **Area Between Curves:** $A = \int_a^b [f_{upper}(x) - g_{lower}(x)] dx$.
* **Work:** $W = \int_a^b F(x) dx$.
    * **Springs (Hooke's Law):** $F = kx$.
    * **Lifting Chains:** Integrate the weight of the segment being moved over the distance moved.
* **Kinematics:**
    * Position $s(t) \to$ Velocity $v(t) = s'(t) \to$ Acceleration $a(t) = v'(t)$.
    * **Displacement:** $\int_{t_1}^{t_2} v(t) dt$.
    * **Distance Traveled:** $\int_{t_1}^{t_2} |v(t)| dt$.



# MATH 265 — Calculus I · Final Exam 1 Cheat Sheet
**Time:** 3.5 hrs | **Passing:** 55% | **Total:** 124 pts

---

## 1. DERIVATIVES — COMPLEX COMBINATIONS (Q1 — 20 pts)

The biggest question. Every part stacks multiple rules. Identify layers first.

### All Rules at a Glance
```
Constant:        d/dx [c]        = 0
Power:           d/dx [x^n]      = n·x^(n−1)
Constant mult:   d/dx [c·f]      = c·f'
Sum/Diff:        d/dx [f ± g]    = f' ± g'
Product:         d/dx [f·g]      = f'g + fg'
Quotient:        d/dx [f/g]      = (f'g − fg') / g²
Chain:           d/dx [f(g(x))]  = f'(g(x)) · g'(x)
```

### Trig Derivatives
```
d/dx [sin x]  =  cos x          d/dx [cos x]  = −sin x
d/dx [tan x]  =  sec² x         d/dx [cot x]  = −csc² x
d/dx [sec x]  =  sec x · tan x  d/dx [csc x]  = −csc x · cot x
```

### Chain Rule — Nested Layers (work outside → in)
```
d/dx [f(g(h(x)))] = f'(g(h(x))) · g'(h(x)) · h'(x)
```

---

### Q1 Part-by-Part Strategy

**a. y = sin x · cos(sin x²)**
- Outer structure: **Product Rule** → (sin x)' · cos(sin x²) + sin x · [cos(sin x²)]'
- Right term needs **Chain Rule twice**: outer=cos, inner=sin(x²), innermost=x²
- d/dx[cos(sin x²)] = −sin(sin x²) · cos(x²) · 2x

**b. y = [(1+x³)/(1−x²)]^(1/3)**
- **Chain Rule**: outer = u^(1/3), inner = (1+x³)/(1−x²)
- d/dx[u^(1/3)] = (1/3)u^(−2/3) · u'
- u' needs **Quotient Rule**: [(3x²)(1−x²) − (1+x³)(−2x)] / (1−x²)²

**c. y = √(1 + √(1+x))**
- Rewrite: [1 + (1+x)^(1/2)]^(1/2)
- **Chain Rule twice**: outer=√u, u = 1+(1+x)^(1/2); then inner=√(1+x)
- dy/dx = (1/2)[1+√(1+x)]^(−1/2) · (1/2)(1+x)^(−1/2)

**d. y = √(x²−1) / (x²−2x−8)**
- **Quotient Rule**: top = (x²−1)^(1/2), bottom = x²−2x−8
- Numerator derivative: (1/2)(x²−1)^(−1/2) · 2x = x/√(x²−1)
- Factor denominator: (x−4)(x+2) — useful for simplification

**e. y = sec²((x+1)/(x−2))**
- **Chain Rule twice**: outer = u², u = sec(v), v = (x+1)/(x−2)
- d/dx[sec²(v)] = 2sec(v) · sec(v)tan(v) · v'
- v' needs **Quotient Rule**: [(x−2)−(x+1)] / (x−2)² = −3/(x−2)²

---

## 2. METHOD OF DIFFERENTIALS / LINEAR APPROXIMATION (Q2 — 8 pts)

### Formula
```
f(x + Δx) ≈ f(x) + f'(x) · Δx
```
Or equivalently using differential dy = f'(x) dx:
```
Approximate value ≈ known nearby value + f'(nearby) · (small change)
```

### Strategy
1. Pick a nearby "nice" value where you know the exact answer
2. Compute f'(x) at that nice value
3. Apply the formula

**a. cos 62°**
- Convert: 62° = π/3 + π/90 · 2 ... easier: use 60° = π/3 as base, Δx = 2° = π/90
- f(x) = cos x, f'(x) = −sin x
- cos(π/3) = 1/2, sin(π/3) = √3/2
- cos 62° ≈ cos(π/3) + (−sin(π/3))(π/90) = 1/2 − (√3/2)(π/90)
- ≈ 0.5 − 0.0302 ≈ **0.4698**

**b. √16.4**
- Base: x = 16 (know √16 = 4), Δx = 0.4
- f(x) = √x, f'(x) = 1/(2√x)
- √16.4 ≈ 4 + (1/8)(0.4) = 4 + 0.05 = **4.0500**

**Key:** Always work in radians for trig approximations.

---

## 3. DERIVATIVE FROM DEFINITION — cot x (Q3 — 6 pts)

### Limit Definition
```
f'(x) = lim(h→0) [f(x+h) − f(x)] / h
```

### Strategy for cot x
```
cot x = cos x / sin x
```
1. Write [cot(x+h) − cot x] / h
2. Expand cot(x+h) = cos(x+h)/sin(x+h)
3. Combine fractions over common denominator sin(x+h)·sin x
4. Numerator becomes: cos(x+h)sin x − cos x · sin(x+h)
5. Use **sine subtraction identity**: sin(A−B) = sin A cos B − cos A sin B
   → cos(x+h)sin x − cos x sin(x+h) = −sin((x+h)−x) = −sin(h)
6. Result: [−sin h] / [h · sin(x+h) · sin x]
7. Take limit: lim sin(h)/h = 1, and sin(x+h) → sin x
8. → **−1/sin²x = −csc²x** ✓

### Key Identities Needed
```
sin(A − B) = sin A cos B − cos A sin B
lim(h→0) sin(h)/h = 1
lim(h→0) [cos(h)−1]/h = 0
```

---

## 4. CURVE SKETCHING (Q4 — 20 pts)

### Full Checklist (in order)
```
1. Domain           — where is f(x) defined?
2. Intercepts       — set x=0 (y-int), set f(x)=0 (x-int)
3. Asymptotes       — vertical (denom=0), horizontal (lim x→±∞)
4. f'(x)            — find, set = 0 → critical points
5. Inc/Dec          — sign chart of f'(x)
6. Local max/min    — first or second derivative test
7. f''(x)           — find, set = 0 → inflection point candidates
8. Concavity        — sign chart of f''(x)
9. Cusps            — where f' is undefined but f is continuous
10. Sketch
```

### First Derivative Test
- f' changes + → − at c: **local max**
- f' changes − → + at c: **local min**
- f' doesn't change sign: **neither**

### Second Derivative Test
```
f'(c) = 0 and f''(c) < 0  →  local MAX
f'(c) = 0 and f''(c) > 0  →  local MIN
f''(c) = 0                 →  inconclusive, use first derivative test
```

### Concavity
```
f''(x) > 0  →  concave UP  (∪)
f''(x) < 0  →  concave DOWN (∩)
Inflection point: f'' changes sign (even if f''=0 or undefined)
```

### Asymptotes
```
Vertical:     x = a where denominator = 0 (and num ≠ 0)
Horizontal:   lim(x→±∞) f(x) = L  →  y = L
Oblique:      do polynomial long division when deg(num) = deg(den)+1
```

**a. f(x) = x²/(x²−1)**
- Domain: x ≠ ±1
- Vertical asymptotes: x = 1, x = −1
- Horizontal asymptote: y = 1 (leading coefficients both 1)
- f'(x) = [2x(x²−1) − x²(2x)] / (x²−1)² = −2x/(x²−1)²
- Critical point: x = 0 (local max since f''(0) < 0)
- Even function (symmetric about y-axis)

**b. f(x) = x + sin x**
- Domain: all reals; no asymptotes
- f'(x) = 1 + cos x ≥ 0 always → **always increasing** (no local extrema)
- f'(x) = 0 when cos x = −1 → x = (2k+1)π (flat points, not extrema)
- f''(x) = −sin x → inflection points where sin x = 0 → x = nπ

---

## 5. ABSOLUTE EXTREMA ON CLOSED INTERVAL (Q5 — 11 pts)

### Closed Interval Method (always use for closed [a,b])
```
1. Find f'(x)
2. Solve f'(x) = 0 AND find where f'(x) is undefined → critical points
3. Evaluate f at all critical points in [a,b] AND at endpoints a, b
4. Largest value = absolute max; Smallest value = absolute min
```

**a. f(x) = 2x^(5/3) − 5x^(4/3) on [−1, 20]**
- f'(x) = (10/3)x^(2/3) − (20/3)x^(1/3)
- Factor: (10/3)x^(1/3)[x^(1/3) − 2] = 0
- Critical points: x = 0 (f' undefined) and x = 8 (f'=0)
- Evaluate at x = −1, 0, 8, 20

**b. f(x) = x + cos x on [−π, 2π]**
- f'(x) = 1 − sin x = 0 → sin x = 1 → x = π/2
- Evaluate at x = −π, π/2, 2π

**Fractional exponents tip:**
```
x^(5/3) = (x^(1/3))^5 = (∛x)^5
x^(4/3) = (∛x)^4
Negative x: ∛(−1) = −1, so (−1)^(5/3) = −1, (−1)^(4/3) = 1
```

---

## 6. OPTIMIZATION (Q6 — 6 pts)

### Strategy for Optimization Problems
```
1. Draw & label diagram
2. Write the OBJECTIVE function (what to minimize/maximize)
3. Write the CONSTRAINT equation
4. Substitute constraint → reduce objective to one variable
5. Take derivative, set = 0 → critical points
6. Verify it's a min/max (second derivative test or check endpoints)
7. Answer the question asked
```

**Rectangle with fixed area 220 cm², minimize perimeter:**
- Variables: length l, width w
- Constraint: l · w = 220  →  l = 220/w
- Objective: P = 2l + 2w = 2(220/w) + 2w = 440/w + 2w
- P'(w) = −440/w² + 2 = 0  →  w² = 220  →  w = √220
- l = 220/√220 = √220 → **l = w = √220** (it's a square!)
- P_min = 4√220 = 4√(4·55) = **8√55 cm**

**General rule:** For fixed area rectangles → **minimum perimeter = square**.

---

## 7. NEWTON'S METHOD (Q7 — 5 pts)

### Formula
```
x_(n+1) = x_n − f(x_n) / f'(x_n)
```

### Strategy
1. Rewrite equation as f(x) = 0
2. Pick starting guess x₀ (use graph or given interval)
3. Compute x₁ = x₀ − f(x₀)/f'(x₀)
4. Repeat until desired precision (usually 2–3 iterations for 4 decimal places)

**Example: solve x⁴ − 2 = 0 on [1, 2]**
- f(x) = x⁴ − 2, f'(x) = 4x³
- x₀ = 1: x₁ = 1 − (−1)/4 = 1.25
- x₁ = 1.25: x₂ = 1.25 − (1.25⁴−2)/(4·1.25³) ≈ 1.1935 ...

**Tip:** Converges fast (doubles correct digits each step) unless f'(xₙ) ≈ 0.

---

## 8. MEAN VALUE THEOREM & ROLLE'S THEOREM (Q8 — likely)

### Rolle's Theorem
**If** f is continuous on [a,b], differentiable on (a,b), and f(a) = f(b)
**Then** ∃ c ∈ (a,b) such that **f'(c) = 0**

### Mean Value Theorem (MVT)
**If** f is continuous on [a,b] and differentiable on (a,b)
**Then** ∃ c ∈ (a,b) such that:
```
f'(c) = [f(b) − f(a)] / (b − a)
```
In words: the instantaneous rate equals the average rate at some point.

### Using MVT
1. Verify continuity & differentiability (state this!)
2. Compute [f(b)−f(a)]/(b−a)
3. Set f'(c) = that value, solve for c
4. Confirm c ∈ (a,b)

---

## 9. KEY IDENTITIES & FORMULAS MASTER LIST

### Trig Identities
```
sin²x + cos²x = 1
1 + tan²x = sec²x
1 + cot²x = csc²x

sin(A ± B) = sinA cosB ± cosA sinB
cos(A ± B) = cosA cosB ∓ sinA sinB

sin(2x) = 2 sin x cos x
cos(2x) = cos²x − sin²x = 1 − 2sin²x = 2cos²x − 1

sin²x = (1 − cos 2x)/2
cos²x = (1 + cos 2x)/2
```

### Special Limits
```
lim(x→0) sin(x)/x     = 1
lim(x→0) [1−cos(x)]/x = 0
lim(x→0) (1+x)^(1/x)  = e
lim(x→∞) (1+1/n)^n    = e
```

### Unit Circle (exact values)
| θ | sin | cos | tan |
|---|-----|-----|-----|
| 0 | 0 | 1 | 0 |
| π/6 | 1/2 | √3/2 | √3/3 |
| π/4 | √2/2 | √2/2 | 1 |
| π/3 | √3/2 | 1/2 | √3 |
| π/2 | 1 | 0 | undef |
| π | 0 | −1 | 0 |
| 3π/2 | −1 | 0 | undef |

---

## 10. QUICK DECISION TREE

```
Derivative of a product?         → Product Rule
Derivative of a fraction?        → Quotient Rule
Derivative of "something inside"?→ Chain Rule (+ rule for outer function)
Function has multiple layers?    → Chain Rule repeatedly, outside → in
Limit gives 0/0?                 → Factor/cancel or L'Hôpital
Approximating a value?           → Linear approximation: f(a) + f'(a)Δx
Max/min on closed interval?      → Closed interval method (crits + endpoints)
Max/min word problem?            → Optimize: set up obj + constraint, substitute
Approximate root of equation?    → Newton's Method
Sketch a curve?                  → Domain, intercepts, asymptotes, f', f''
```



Here is your **complete, exam-focused Markdown cheat sheet** for the **MATH 265 Sample Final Exam 1** .
It is structured to cover **every question type, rule, formula, identity, and strategy** needed.

---

# 🧠 MATH 265 – FINAL EXAM CHEAT SHEET (FULL COVERAGE)

---

# ⚡ 1. DERIVATIVES (CORE SKILLS)

## Power Rule

\frac{d}{dx}(x^n)=nx^{n-1}

---

## Trigonometric Derivatives

[
\frac{d}{dx}(\sin x) = \cos x
]
[
\frac{d}{dx}(\cos x) = -\sin x
]
[
\frac{d}{dx}(\tan x) = \sec^2 x
]
[
\frac{d}{dx}(\cot x) = -\csc^2 x
]
[
\frac{d}{dx}(\sec x) = \sec x \tan x
]

---

## Chain Rule (VERY IMPORTANT)

[
\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)
]

---

## Product Rule

[
(fg)' = f'g + fg'
]

---

## Quotient Rule

[
\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}
]

---

## Strategy

* Identify structure first:

  * Inside function → Chain rule
  * Product → Product rule
  * Fraction → Quotient rule

---

# 📏 2. DIFFERENTIALS (LINEAR APPROXIMATION)

## Formula

[
f(x + dx) \approx f(x) + f'(x),dx
]

## Steps

1. Choose nearby easy value
2. Compute derivative
3. Plug into formula

⚠️ Convert degrees → radians for trig

---

# 📉 3. DEFINITION OF DERIVATIVE

[
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
]

### Strategy

* Expand numerator
* Simplify
* Cancel h
* Evaluate limit

---

# 📊 4. GRAPHING & ANALYSIS

## Critical Points

[
f'(x) = 0 \quad \text{or undefined}
]

---

## Increasing / Decreasing

* (f'(x) > 0) → increasing
* (f'(x) < 0) → decreasing

---

## Concavity

* (f''(x) > 0) → concave up
* (f''(x) < 0) → concave down

---

## Inflection Point

[
f''(x) = 0 \quad \text{and changes sign}
]

---

## Cusps / Non-differentiable

* Sharp corners
* Vertical tangent

---

## Asymptotes

### Vertical:

* Denominator = 0

### Horizontal:

* Compare degrees:

  * top < bottom → 0
  * equal → ratio
  * top > bottom → none

---

# 📈 5. OPTIMIZATION (MAX / MIN)

## Steps

1. Find derivative
2. Solve (f'(x) = 0)
3. Check endpoints
4. Plug into original

---

## Rectangle Optimization

* Area fixed → express one variable in terms of another
* Minimize perimeter

---

# 🔁 6. NEWTON’S METHOD

## Formula

[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
]

### Strategy

* Choose good initial guess
* Iterate 1–2 times

---

# 🧮 7. INTEGRALS (CORE SECTION)

## Basic Rules

### Power Rule (Reverse derivative)

[
\int x^n dx = \frac{x^{n+1}}{n+1} + C
]

---

## Trig Integrals

[
\int \sin x,dx = -\cos x + C
]
[
\int \cos x,dx = \sin x + C
]

---

## Substitution (u-sub)

### Steps

1. Let (u = g(x))
2. Compute (du)
3. Replace integral

---

## Strategy

* Inside function present → use substitution
* Polynomial → expand first

---

# 📐 8. DEFINITE INTEGRALS

## Fundamental Theorem of Calculus

[
\int_a^b f(x),dx = F(b) - F(a)
]

---

## Properties

* Reverse limits → negative
* Split intervals

---

# 📊 9. AREA BETWEEN CURVES

## Formula

[
\text{Area} = \int_a^b (\text{top} - \text{bottom}),dx
]

---

## Steps

1. Find intersection points
2. Identify top function
3. Integrate

---

# 🚰 10. ACCUMULATION / FLOW

## Total amount

[
\text{Total} = \int r(t),dt
]

---

# ⚙️ 11. WORK PROBLEMS

## Formula

[
W = \int F(x),dx
]

### Chain lifting shortcut

* Weight per length × distance lifted

---

# 🌡️ 12. AVERAGE VALUE OF FUNCTION

## Formula

[
f_{\text{avg}} = \frac{1}{b-a} \int_a^b f(x),dx
]

---

# 📐 13. TRIG VALUES (MUST MEMORIZE)

| Angle | sin  | cos  | tan       |
| ----- | ---- | ---- | --------- |
| 0     | 0    | 1    | 0         |
| π/6   | 1/2  | √3/2 | √3/3      |
| π/4   | √2/2 | √2/2 | 1         |
| π/3   | √3/2 | 1/2  | √3        |
| π/2   | 1    | 0    | undefined |

---

## Memory Trick

[
\sin = \frac{\sqrt{0,1,2,3,4}}{2}, \quad \cos = \text{reverse}
]

---

# ⚠️ COMMON EXAM TRAPS

* Forgetting chain rule
* Mixing degrees/radians
* Missing +C in integrals
* Wrong limits order
* Not checking endpoints in optimization
* Forgetting absolute value in area

---

# 🎯 FINAL EXAM STRATEGY

### Order:

1. Derivatives (fast points)
2. Integrals
3. Graphing
4. Optimization
5. Applications

---

### Time Management

* Skip hard problems early
* Show steps (partial credit!)
* Double-check signs

Here is a cheat sheet tailored to the topics and problems in your sample exam, formatted in Markdown.

---

### MATH 265 - Exam Cheat Sheet

#### 1. Limits & Continuity

- **Squeeze Theorem:** If \(g(x) \le f(x) \le h(x)\) near \(a\) (except possibly at \(a\)) and \(\lim_{x\to a} g(x) = \lim_{x\to a} h(x) = L\), then \(\lim_{x\to a} f(x) = L\).
    - *Use for \(\lim_{x\to \infty} (\text{bounded}) \cdot (\text{function} \to 0)\) or similar.*
- **Infinite Limits & Vertical Asymptotes:** \(\lim_{x \to a} f(x) = \infty\) means \(f(x)\) grows without bound. Check left/right limits to confirm sign.
- **Limits at Infinity of Rational Functions:** Divide numerator and denominator by the highest power of \(x\) in the denominator.
- **Common Trig Limits:** Know where \(\tan x\) has vertical asymptotes: \(x = \frac{\pi}{2} + k\pi\).

#### 2. Derivatives - Rules

- **Product Rule:** \((uv)' = u'v + uv'\)
- **Quotient Rule:** \(\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}\)
- **Chain Rule:** \(\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)\)
- **Derivatives of Trig Functions:**
    - \(\frac{d}{dx} \tan x = \sec^2 x\)
    - \(\frac{d}{dx} \sec x = \sec x \tan x\)
    - \(\frac{d}{dx} \cos x = -\sin x\)

#### 3. Extreme Value Theorem (EVT) & Optimization

- **EVT:** A continuous function on a closed interval \([a,b]\) has an absolute max and min.
- **Finding Absolute Extrema on \([a,b]\):**
    1. Find \(f'(x)\).
    2. Find all critical points in \((a,b)\) where \(f'(x)=0\) or DNE.
    3. Evaluate \(f\) at all critical points and endpoints \(a, b\).
    4. Largest value = absolute max, smallest = absolute min.

#### 4. Graph Interpretation

- \(f(a)=b\): Point \((a,b)\) is on the graph.
- \(\lim_{x\to\infty} f(x) = L\): Horizontal asymptote at \(y=L\).
- \(\lim_{x\to a} f(x) = \infty\): Vertical asymptote at \(x=a\).
- \(f'(x) < 0\): Function is decreasing.
- \(f''(x) > 0\): Function is concave up.

#### 5. Optimization (Box Problem)

- **Strategy:**
    1. Draw picture, assign variables (e.g., width \(w\), length \(l=2w\), height \(h\)).
    2. Write constraint (e.g., Volume \(V=lwh = 120\)).
    3. Write objective function (Cost). Differentiate cost for sides vs. lid/base.
    4. Use constraint to reduce objective to one variable.
    5. Find critical points of objective, verify minimum.

#### 6. Integration Techniques & Formulas

- **Basic Substitution:** \(\int f(g(x))g'(x) dx = \int f(u) du\).
    - *Look for a function and its derivative.*
- **Power Rule:** \(\int x^n dx = \frac{x^{n+1}}{n+1} + C\) (\(n \neq -1\)).
- **Trig Integrals:**
    - \(\int \tan x \, dx = \ln|\sec x| + C\) (or \(-\ln|\cos x|\))
    - \(\int \sec^2 x \, dx = \tan x + C\)
    - \(\int \sec x \tan x \, dx = \sec x + C\)
- **Hint from Problem 6d:** \(\sec^3x \tan x = \sec^2x (\sec x \tan x)\). Let \(u = \sec x\), \(du = \sec x \tan x dx\). Integral becomes \(\int u^2 du\).
- **Simplifying Fractions:** \(\frac{a+b}{c} = \frac{a}{c} + \frac{b}{c}\). Write \(\sqrt{5x} = \sqrt{5} x^{1/2}\).
- **Properties of Definite Integrals:**
    - \(\int_a^b f(x) dx = -\int_b^a f(x)dx\)
    - If \(m \le f(x) \le M\) on \([a,b]\), then \(m(b-a) \le \int_a^b f(x) dx \le M(b-a)\). *(Bounding an integral)*

#### 7. Absolute Extrema & Bounding Integrals

- **Absolute Extrema** (non-linear, over closed interval): Same as EVT method above.
- **Bounding an Integral:** Find max and min of the function on the interval. Use the inequality above.

#### 8. Area Between Curves

- **Formula:** Area \(= \int_a^b (\text{top function} - \text{bottom function}) dx\).
- Always integrate over the given interval, noting where curves intersect if interval is not given.
- For Problem 8: Top function is max of \(\cos x\) and \(1/\sqrt{2}\), bottom is the min. Solve intersection: \(\cos x = 1/\sqrt{2} \implies x = \pm \pi/4\).

#### 9. Work & Hooke's Law

- **Hooke's Law:** Force \(F(x) = kx\), where \(k\) is spring constant, \(x\) is distance stretched/compressed from natural length.
- **Work:** \(W = \int_a^b F(x) dx\).
- If given work to stretch *beyond* natural length, use \(a=0\) (natural length), \(b=\) stretch distance.

#### 10. Particle Motion

- Let \(v(t)\) be velocity, \(s(t)\) position.
- **Displacement** on \([t_1, t_2]\): \(\int_{t_1}^{t_2} v(t) dt\). (Net change in position)
- **Total Distance** on \([t_1, t_2]\): \(\int_{t_1}^{t_2} |v(t)| dt\).
    - *Strategy:* Find where \(v(t)=0\). Split the interval into subintervals where \(v\) is positive or negative. Integrate \(v\) on positive parts, \(-v\) on negative parts.

#### 11. Kinematics (Constant Acceleration)

- **Given:** \(a(t) = a\) (constant).
- \(v(t) = v_0 + at\)
- \(s(t) = s_0 + v_0 t + \frac{1}{2}at^2\)
- Problem 11: Two phases. Phase 1: constant acceleration. Phase 2: zero acceleration (constant velocity). Use Phase 1 to find distance covered and final velocity. Use Phase 2 with remaining distance and Phase 1's final velocity to find time for Phase 2.

#### 12. Average Value of a Function

- **Formula:** \(f_{\text{avg}} = \frac{1}{b-a} \int_a^b f(x) dx\).
- Set this equal to the given average, solve for missing boundary \(k\).



Here is a cheat sheet in Markdown covering the essential rules, formulas, and strategies needed to solve the problems in your sample exam.

---

### Derivatives Cheat Sheet

#### Basic Rules
- **Power Rule:** \(\frac{d}{dx}[x^n] = nx^{n-1}\)
- **Constant Multiple:** \(\frac{d}{dx}[c \cdot f(x)] = c \cdot f'(x)\)
- **Sum/Difference:** \(\frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)\)

#### Advanced Rules
- **Product Rule:** \(\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)\)
- **Quotient Rule:** \(\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}\)
- **Chain Rule:** \(\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)\)

#### Trigonometric Derivatives
- \(\frac{d}{dx} \sin x = \cos x\) 
- \(\frac{d}{dx} \cos x = -\sin x\)
- \(\frac{d}{dx} \tan x = \sec^2 x\) 
- \(\frac{d}{dx} \cot x = -\csc^2 x\)
- \(\frac{d}{dx} \sec x = \sec x \tan x\) 
- \(\frac{d}{dx} \csc x = -\csc x \cot x\)
- **Chain Rule Example:** \(\frac{d}{dx}[\sec^2(g(x))] = 2\sec(g(x)) \cdot [\sec(g(x))\tan(g(x))] \cdot g'(x)\)

#### Implicit/Logarithmic Differentiation
- \(y = f(x)^{g(x)} \implies \ln y = g(x) \ln[f(x)] \implies \frac{y'}{y} = g'(x) \ln[f(x)] + g(x) \frac{f'(x)}{f(x)}\)

---

### Differentials & Approximation
- **Formula:** \(f(x + \Delta x) \approx f(x) + f'(x) \cdot \Delta x\)
- **Method:**
  1.  Choose a value \(a\) close to the target where \(f(a)\) and \(f'(a)\) are easy to compute. \(\Delta x = \text{target} - a\).
  2.  Calculate \(f'(x)\).
  3.  Apply formula.
- **Radian Conversion:** For trig functions (like \(\cos 62^\circ\)), \(x\) must be in radians. \(62^\circ = \frac{62\pi}{180}\) rad. Choose \(a = 60^\circ = \frac{\pi}{3}\) rad.

---

### Definition of the Derivative
- **Limit Definition:** \(f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}\)
- **Trig Limit:** \(\lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1\)
- For \(f(x) = \cot x = \frac{\cos x}{\sin x}\), use the limit definition, trigonometric identities for \(\cos(x+h)\) and \(\sin(x+h)\), and the limit above.

---

### Curve Sketching & Analysis
- **Critical Points:** Where \(f'(x) = 0\) or \(f'(x)\) is undefined (DNE).
- **Cusps:** Points where \(f\) is continuous, but \(\lim_{x \to c^-} f'(x) = \infty\) and \(\lim_{x \to c^+} f'(x) = -\infty\) (or vice-versa).
- **Inflection Points:** Where \(f''(x)\) changes sign. Find where \(f''(x)=0\) or DNE.
- **Vertical Asymptotes:** Where denominator is 0 but numerator is not (for rational functions). Check limits on both sides.
- **Horizontal Asymptotes:** Calculate \(\lim_{x \to \pm\infty} f(x)\).
- **First Derivative Test:**
    - \(f' > 0 \implies f\) increasing.
    - \(f' < 0 \implies f\) decreasing.
- **Second Derivative Test:**
    - \(f'' > 0 \implies\) concave up.
    - \(f'' < 0 \implies\) concave down.

---

### Optimization
- **Steps:**
  1.  **Constraint:** Given equation (e.g., area \(A = xy = 220\)).
  2.  **Objective:** Function to minimize/maximize (e.g., perimeter \(P = 2x + 2y\)).
  3.  **Reduce to one variable:** Solve constraint for \(y = 220/x\). Substitute into objective: \(P(x) = 2x + \frac{440}{x}\).
  4.  **Find Critical Points:** Solve \(P'(x) = 0\). Ignore negative solutions if dimension.
  5.  **Verify min/max:** Use first or second derivative test.

---

### Newton's Method
- **Formula:** \(x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}\)
- **Purpose:** Approximate roots of \(f(x)=0\).
- **Process:** Make initial guess \(x_1\); iterate until convergence.

---

### Integration Cheat Sheet

#### Basic Rules
- **Power Rule:** \(\int x^n dx = \frac{x^{n+1}}{n+1} + C\) \((n \neq -1)\).
- **Polynomial Expansion:** Expand terms like \((x^2-4)^2\) before integrating.
- **u-Substitution:** \(\int f(g(x))g'(x) dx = \int f(u) du\), where \(u = g(x)\).

#### Common u-Substitutions (from exam)
- For \(\int x\sqrt{x-1} dx\): let \(u = x-1 \implies du = dx\) and \(x = u+1\).
- For \(\int \sin(2x)\cos x dx\): use identity \(\sin(2x) = 2\sin x \cos x\). Then integral becomes \(\int 2\sin x \cos^2 x dx\). Let \(u = \cos x\).

#### Integral Properties & Average Value
- **Bounding:** If \(m \le f(x) \le M\) on \([a,b]\), then \(m(b-a) \le \int_a^b f(x) dx \le M(b-a)\).
- **Average Value:** \(f_{avg} = \frac{1}{b-a} \int_a^b f(x) dx\)

---

### Fundamental Theorem of Calculus (FTC)
- **FTC Part 2:** \(\frac{d}{dx} \int_{a(x)}^{b(x)} f(t) dt = f(b(x)) \cdot b'(x) - f(a(x)) \cdot a'(x)\)

---

### Applications of Integration
- **Area Between Curves:** \(A = \int_a^b |f(x) - g(x)| dx\). Find bounds \(a, b\) by solving intersection points \(f(x)=g(x)\).
- **Work (Lifting Chain):**
    - Linear weight density: \(\lambda = \frac{\text{mass}}{\text{length}}\).
    - Work to lift a segment \((dy)\) at height \(y\): \(dW = \lambda \cdot g \cdot y \cdot dy\) (if mass in kg, use \(g=9.8 \text{ m/s}^2\) for Newtons, but physics context can sometimes assume weight in kg-force, check problem wording. Standard physics: force = mass \(\times\) g. If "work in Joules", multiply kg by 9.8).
    - Integrate over the length being lifted.
- **Net Change:** Amount flowed = \(\int_{t_1}^{t_2} r(t) dt\).

---

### Trigonometric Identities
- \(\sin(2x) = 2\sin x \cos x\)
- \(\cos(2x) = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x\)
- \(\sec x = \frac{1}{\cos x}\)

### Differentiation of Key Functions from Exam
- **1(a):** \(y = \sin(x) \cdot \cos(\sin(x^2))\). Needs **product rule** and **double chain rule**.
- **1(b):** \(y = \left(\frac{1+x^3}{1-x^2}\right)^{1/3}\). Needs **chain rule** and **quotient rule**.
- **1(c):** \(y = \sqrt{1+\sqrt{1+x}}\). Needs **double chain rule**.
- **1(d):** \(y = \frac{\sqrt{x^2-1}}{x^2-2x-8}\). Needs **quotient rule** and **chain rule**.
- **1(e):** \(y = \sec^2\left(\frac{x+1}{x-2}\right)\). Needs **chain rule** (\(\sec^2 u\)) and **quotient rule** for \(u'\).

### Substitutions & Setup for Specific Problems
- **Problem 8a:** \(\int (x^2 - x)\sqrt{3x} dx \implies\) write \(\sqrt{3x} = \sqrt{3}\sqrt{x}\), multiply through, integrate with power rule.
- **Problem 8e:** \(\int_2^4 x\sqrt{x-1} dx\). Use \(u = x-1\). Limits change: \(x=2 \to u=1\), \(x=4 \to u=3\). Integral \(\int_1^3 (u+1)\sqrt{u} du\).
- **Problem 13 (Work):** Chain linear density \(\lambda = 80/10 = 8\) kg/m. Lift one end to 6m. Length of chain hanging in air: if lifted to 6m, the top is at 6m, bottom is on ground. Segments lifted vary. Use \(dW = \lambda g y dy\) for segments \(dy\) at height \(y\) that are lifted. Integrate from 0 to 6. Work = \(\int_0^6 8 \cdot 9.8 \cdot y \, dy\) (Joules).



Here’s a **cheatsheet** in Markdown covering all the **rules, methods, formulas, identities, and strategies** you need to solve every problem in the attached MATH 265 Sample Midterm Exam 1.

---

# MATH 265 Exam Cheatsheet

## 1. Exact Trigonometric Values

| Angle (degrees) | Angle (radians) | sin | cos | tan |
|----------------|----------------|-----|-----|-----|
| 0° | 0 | 0 | 1 | 0 |
| 30° | π/6 | 1/2 | √3/2 | 1/√3 |
| 45° | π/4 | √2/2 | √2/2 | 1 |
| 60° | π/3 | √3/2 | 1/2 | √3 |
| 90° | π/2 | 1 | 0 | undefined |

**Even/Odd identities**:  
- cos(−θ) = cos θ  
- sin(−θ) = − sin θ  

---

## 2. Composite Functions & Domain

Given \( f(x) \) and \( g(x) \):

- \( (f \circ g)(x) = f(g(x)) \)  
- Domain of \( f \circ g \):  
  All \( x \) in domain of \( g \) such that \( g(x) \) is in domain of \( f \).

**Domain restrictions**:  
- Denominator ≠ 0  
- Radicand (even root) ≥ 0  

---

## 3. Graph Transformations

Start with \( y = x^2 \) (basic parabola).

- \( y = a(x - h)^2 + k \)  
  - \( a \): vertical stretch/compression + reflection if negative  
  - \( h \): horizontal shift (opposite sign)  
  - \( k \): vertical shift  

Example: \( g(x) = 3(x+4)^2 \)  
- Start with \( y = x^2 \)  
- Shift left 4  
- Vertical stretch by factor 3  

---

## 4. Limit Evaluation Strategies

### Direct substitution
If no division by zero, substitute directly.

### Factoring
Factor numerator/denominator, cancel common factors.

### Rationalizing
For \( \frac{\sqrt{a} - \sqrt{b}}{c} \), multiply numerator & denominator by conjugate \( \sqrt{a} + \sqrt{b} \).

### Special trig limit
\[
\lim_{x \to 0} \frac{\sin(kx)}{x} = k
\]

### One-sided limits
Check left/right separately if denominator → 0 but numerator ≠ 0.

If limit → ±∞, say “limit does not exist” (infinite).

---

## 5. Derivative Rules

- Power rule: \( \frac{d}{dx} x^n = n x^{n-1} \)  
- Sum/difference: \( (f \pm g)' = f' \pm g' \)  
- Constant multiple: \( (cf)' = c f' \)  
- Product rule: \( (fg)' = f'g + fg' \)  
- Quotient rule: \( \left( \frac{f}{g} \right)' = \frac{f'g - fg'}{g^2} \)  
- Chain rule: \( \frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x) \)  

### Common derivatives:
- \( \frac{d}{dx} \sin u = \cos u \cdot u' \)  
- \( \frac{d}{dx} \cos u = -\sin u \cdot u' \)  
- \( \frac{d}{dx} x^n = n x^{n-1} \)  
- \( \frac{d}{dx} c = 0 \)

---

## 6. Implicit Differentiation

Steps:  
1. Differentiate both sides w.r.t \( x \), treating \( y \) as \( y(x) \).  
2. Every time you differentiate \( y \), multiply by \( y' \).  
3. Collect all \( y' \) terms on one side.  
4. Solve for \( y' \).

---

## 7. Tangent Line Perpendicular Condition

Given line \( y = m_1 x + b \), slope \( m_1 \).  
Perpendicular slope \( m_2 = -\frac{1}{m_1} \).  

For curve \( f(x) \), set \( f'(x) = m_2 \) and solve for \( x \).

---

## 8. Related Rates (Cone)

Cone volume: \( V = \frac{1}{3} \pi r^2 h \)  

Given: diameter = height → \( 2r = h \) → \( r = h/2 \).  
Substitute: \( V = \frac{1}{3} \pi \left( \frac{h}{2} \right)^2 h = \frac{\pi}{12} h^3 \).  

Differentiate: \( \frac{dV}{dt} = \frac{\pi}{4} h^2 \frac{dh}{dt} \).  

Given \( \frac{dV}{dt} \) and \( h \), solve for \( \frac{dh}{dt} \).

---

## 9. Differentials (Linear Approximation)

Formula: \( f(x + dx) \approx f(x) + f'(x) \, dx \)  

Choose \( x \) near target, \( dx = \text{target} - x \).

Example: \( \sqrt{9.2} \)  
Let \( f(x) = \sqrt{x} \), \( x = 9 \), \( f'(x) = \frac{1}{2\sqrt{x}} \)  
\( f'(9) = \frac{1}{6} \), \( dx = 0.2 \)  
Approx: \( \sqrt{9.2} \approx 3 + \frac{1}{6}(0.2) = 3 + 0.0333 = 3.0333 \)

---

## 10. Sketching from Limit Conditions

- \( \lim_{x \to 0} f(x) \) DNE → jump or infinite discontinuity at \( x=0 \)  
- \( f(0) = 0 \) → point (0,0) exists but limit ≠ value or DNE.  
- \( \lim_{x \to \infty} f(x) = -1 \) → horizontal asymptote \( y = -1 \) as \( x \to \infty \)  
- Not differentiable at \( x = -2 \) → corner, cusp, vertical tangent, or discontinuity.

**Strategy**: Draw axes, plot given point, asymptote, discontinuity at 0, nondifferentiable point at -2, and ensure limit at 0 doesn’t exist (different left/right limits).

---

## 11. General Exam Strategies

- **Check domains first** for composites.  
- **Graph transformations**: identify basic function, then shifts/scale.  
- **Limits**: if 0/0, try factor, expand, or conjugate.  
- **Derivatives**: use power/quotient/chain rule.  
- **Implicit diff**: differentiate term by term, group \( y' \).  
- **Related rates**: draw diagram, find equation, differentiate, plug known values.  
- **Differentials**: choose nearby perfect square/cube to linearize.  
- **Sketching**: combine limits and continuity/differentiability info systematically.



Here is a comprehensive exam cheat sheet covering all rules, methods, strategies, formulas, and identities needed to solve the problems in the provided sample exam.

---

### 1. Functions: Definition & Vertical Line Test
- **Function Definition:** A relation where each input \(x\) has **exactly one** output \(y\).
- **Vertical Line Test:** If a vertical line intersects the graph at more than one point, \(y\) is not a function of \(x\).
- **Solving for \(y\):** If solving yields \(y = \pm \sqrt{...}\), it fails the test (not a function).

### 2. Volume of a Cone
\[
V(r) = \frac{1}{3}\pi r^2 h
\]
- **Domain:** The set of all possible inputs (\(r > 0\) for physical radius).
- **Evaluation:** Substitute the given value for the variable.

### 3. Interpreting Derivatives & Average Rate of Change
- **Average Rate of Change:** \(\frac{P(b)-P(a)}{b-a}\) is the average change in population per year over the interval \([a, b]\).
- **Instantaneous Rate of Change:** \(P'(a)\) is the rate at which the population is changing in the year \(a\).

### 4. Graph Transformations (Order of Operations)
For \(y = a f(b(x - h)) + k\):
1.  **Horizontal Shift:** \(x \to x - h\) (Right if \(h>0\), Left if \(h<0\)). *Apply to \(x\) inside the function.*
2.  **Horizontal Scaling (if any):** Multiply \(x\) by \(b\).
3.  **Reflection/Scaling in \(y\):** Multiply the function by \(a\).
    - \(a > 1\): Vertical stretch.
    - \(0 < a < 1\): Vertical compression.
    - \(a < 0\): Reflection over the \(x\)-axis.
4.  **Vertical Shift:** Add \(k\) (Up if \(k>0\), Down if \(k<0\)).

### 5. Interpreting Limits & Continuity from a Graph
- **Horizontal Asymptote:** \(\lim_{x \to \infty} f(x) = L\) means \(y = L\) is a horizontal asymptote.
- **Vertical Asymptote:** \(\lim_{x \to a} f(x) = \infty\) means \(x = a\) is a vertical asymptote.
- **Continuity at \(x=a\):** \(\lim_{x \to a} f(x) = f(a)\).
- **Not Differentiable at \(x=a\) (Corners/Cusps):** The function has a sharp point, vertical tangent, or discontinuity at \(x=a\).

### 6. Vertical & Horizontal Asymptotes
- **Vertical Asymptotes (VA):** Set the **denominator equal to zero**, but simplify the fraction first. If a factor cancels, it's a **hole**, not a VA.
- **Horizontal Asymptotes (HA):** Evaluate \(\lim_{x \to \pm \infty} f(x)\).
    - If degree(Numerator) < degree(Denominator): HA is \(y=0\).
    - If degree(Num) = degree(Den): HA is \(y = \frac{\text{leading coefficient of Num}}{\text{leading coefficient of Den}}\).
    - If degree(Num) > degree(Den): No HA (goes to \(\pm\infty\)).

### 7. Limit Evaluation Methods
- **Direct Substitution:** Try first. If you get \(\frac{0}{0}\), follow strategies below.
- **Factor & Cancel:** Factor numerator/denominator, cancel common factor.
- **Conjugate Multiplication:** For square roots, multiply numerator & denominator by the conjugate.
- **Known Limit \(\frac{1 - \cos x}{x}\) Related:**
    \[
    \lim_{x \to 0} \frac{1 - \cos x}{x} = 0 \quad \text{and} \quad \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}
    \]
    - **Identity to use:** \(\cos 2\theta = 1 - 2\sin^2\theta \implies 1 - \cos 2\theta = 2\sin^2\theta\).
    - Combined with \(\lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1\).
- **Limits at Infinity:** Divide every term by the highest power of \(x\) in the denominator.
- **Squeeze Theorem (Not heavily tested here, but useful background):** If function is bounded, e.g., \(-1 \le \cos \theta \le 1\).
- **One-Sided Limits for Asymptotes:** If denominator \(\to 0\) but numerator \(\not\to 0\), check sign (\(\pm\infty\)) from left and right.

### 8. Linear Approximation (Linearization)
- **Formula:**
    \[
    f(x) \approx f(a) + f'(a)(x - a)
    \]
- **Strategy for \(\sin 62^\circ\):**
    1.  **Choose \(a\):** The nearest value where sin/cos are known exactly. Use **radians**. \(\sin(60^\circ) = \sin(\pi/3)\), so \(a = \pi/3\).
    2.  **Convert to Radians:** \(62^\circ = 62 \times \frac{\pi}{180}\).
    3.  \(f(x) = \sin x, f'(x) = \cos x\).
    4.  Plug into formula.

### 9. Derivative Rules
- **Chain Rule:** \(\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)\).
- **Derivatives of Trig Functions:**
    - \(\frac{d}{dx} \cot x = -\csc^2 x\)
    - \(\frac{d}{dx} \sec x = \sec x \tan x\)
- **Product Rule:** \((uv)' = u'v + uv'\)
- **Quotient Rule:** \(\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}\)
- **Higher-Order Derivatives:** Differentiate the first derivative to get the second derivative.

### 10. Implicit Differentiation & Tangent Lines
- **Implicit Differentiation:** Differentiate both sides w.r.t. \(x\), treating \(y\) as a function of \(x\) (multiply by \(y'\)).
- **Finding Slope at \((x_1, y_1)\):** After differentiating, solve for \(y'\) algebraically. Then substitute \(x_1\) and \(y_1\).
- **Equation of Tangent Line:** \(y - y_1 = m(x - x_1)\), where \(m = y'\) at the point.

### 11. Related Rates
1.  **Draw & Label Picture.**
2.  **Identify Knowns/Unknowns.** \(\frac{dD}{dt}\) (rate of change of distance from radar) = 2000. Find \(\frac{dh}{dt}\) (vertical speed).
3.  **Relate Variables:** Pythagorean Theorem: \(D^2 = h^2 + x^2\), where \(x\) is the constant horizontal distance (5 miles).
    \[
    D^2 = h^2 + 5^2
    \]
4.  **Implicit Differentiation w.r.t. \(t\):**
    \[
    2D \frac{dD}{dt} = 2h \frac{dh}{dt} \implies D \cdot \frac{dD}{dt} = h \cdot \frac{dh}{dt}
    \]
5.  **Solve for Unknown Rate:** At the instant \(h = 4\), calculate \(D = \sqrt{4^2+5^2} = \sqrt{41}\). Plug in \(h, D,\) and \(\frac{dD}{dt}\).
6.  **Solve:** \(\frac{dh}{dt} = \frac{D}{h} \cdot \frac{dD}{dt} = \frac{\sqrt{41}}{4} \cdot 2000\) mi/h.

### Common Algebraic Pitfalls to Avoid
- \(\frac{x^3-1}{x^2-1}\) is **not** \(\frac{x^3}{x^2}\). Factor sum/difference of cubes/squares.
- \(\cot(2x)\) is \(\frac{\cos 2x}{\sin 2x}\), not \(\tan^{-1}(2x)\).
- Always convert degrees to radians for calculus involving trig functions.



