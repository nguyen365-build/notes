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

---

*MATH 265 Exam 2 | Athabasca University | Good luck!*