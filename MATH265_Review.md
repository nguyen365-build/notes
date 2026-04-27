# MATH265_Review.md

# Unit 1: Fundamentals
### **Trigonometric Identities (Q1)**
For $cos(-\frac{\pi}{12})$, you need the **Difference Formula**[cite: 10]:
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
When dealing with trigonometric limits, this fundamental identity is essential[cite: 25]:
* $\lim_{\theta \to 0} \frac{sin(\theta)}{\theta} = 1$


# Unit 3: Derivatives
This section tests your mechanical ability to apply derivative rules.
* **Formulas to Memorize:**
    * Product Rule: $\frac{d}{dx}[uv] = u'v + uv'$
    * Quotient Rule: $\frac{d}{dx}[\frac{u}{v}] = \frac{u'v - uv'}{v^2}$
    * Chain Rule: $\frac{d}{dx}[f(g(x))] = f'(g(x))g'(x)$

# Unit 4: Applications of Differentiation
### **Differentiation Rules (Q5, Q6, Q8)**
These are the "bread and butter" of Unit 3[cite: 26, 32, 35]:
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
* **Perpendicular Slopes:** If two lines are perpendicular, their slopes $m_1$ and $m_2$ satisfy $m_1 = -\frac{1}{m_2}$[cite: 32].
* **Differentials:** To approximate a value, use $f(a + dx) \approx f(a) + f'(a)dx$[cite: 37].


# Unit 5: Integrals
Moving backward from derivatives to find antiderivatives and areas.
* **Formulas to Memorize:**
    * Power Rule for Integration: $\int x^n dx = \frac{x^{n+1}}{n+1} + C$
    * Fundamental Theorem of Calculus (Part 1): $\frac{d}{dx} \int_{a}^{g(x)} f(t) dt = f(g(x))g'(x)$


# Unit 6: Applications of Integration
### **Geometry & Related Rates (Q7)**
For problems involving physical changes, you must know standard volume formulas[cite: 33]:
* **Volume of a Cone:** $V = \frac{1}{3}\pi r^2 h$
* **Relationship:** Since the problem states diameter equals height ($2r = h$), you need to substitute $r = \frac{h}{2}$ into the volume formula before differentiating.

Using integrals to model physical situations like area, work, and net change. 
**Formulas to Memorize:**
    * Area between curves: $A = \int_{a}^{b} (\text{Top Function} - \text{Bottom Function}) dx$
    * Work done lifting a cable/chain: $W = \int_{0}^{h} (\text{density})(\text{gravity})(y) dy$


This comprehensive **MATH 265 Midterm Cheat Sheet** is designed to cover the specific requirements of your sample exam, combining core calculus rules with the trigonometric fundamentals you provided.

---

# **MATH 265: Calculus I Midterm Cheat Sheet**

## **1. Fundamentals & Trigonometry**
Essential for Question 1 (Trig Values) and Question 2 (Composites/Domains).

### **Exact Trigonometric Values**
Derived from the unit circle where $\cos(\theta) = x$ and $\sin(\theta) = y$[cite: 1, 2, 3, 4, 11].

| Angle ($\theta$) | $\sin(\theta)$ | $\cos(\theta)$ | $\tan(\theta)$ |
| :--- | :--- | :--- | :--- |
| **$0$** | $0$ | $1$ | $0$ |
| **$\pi/6$ ($30^\circ$)** | $1/2$ | $\sqrt{3}/2$ | $\sqrt{3}/3$ |
| **$\pi/4$ ($45^\circ$)** | $\sqrt{2}/2$ | $\sqrt{2}/2$ | $1$ |
| **$\pi/3$ ($60^\circ$)** | $\sqrt{3}/2$ | $1/2$ | $\sqrt{3}$ |
| **$\pi/2$ ($90^\circ$)** | $1$ | $0$ | Undefined |

> **Memory Trick:** Sine values follow the pattern $\frac{\sqrt{n}}{2}$ for $n=0, 1, 2, 3, 4$[cite: 1, 2, 11].

### **Trig Identities & Formulas**
* **Even/Odd:** $\cos(-x) = \cos(x)$ and $\sin(-x) = -\sin(x)$[cite: 10].
* **Sum/Difference:** $\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$[cite: 10].
* **Composite Domain:** For $f(g(x))$, the domain includes all $x$ in the domain of $g$ such that $g(x)$ is in the domain of $f$[cite: 11, 12].

---

## **2. Limits & Continuity**
Essential for Question 4 (Evaluating Limits) and Question 10 (Curve Sketching).

### **Evaluating Limits**
1.  **Direct Substitution:** Always try this first[cite: 21].
2.  **Indeterminate Forms ($0/0$):**
    * **Factoring:** Cancel common terms (e.g., $(x-a)$)[cite: 22, 23].
    * **Conjugates:** Multiply by $\frac{\sqrt{a}+b}{\sqrt{a}+b}$ for square root limits[cite: 24].
3.  **Special Trig Limit:** $\lim_{x \to 0} \frac{\sin(ax)}{ax} = 1$[cite: 25].
4.  **Infinite Limits:** $\lim_{x \to \infty} \frac{1}{x^n} = 0$. Divide by the highest power of $x$ in the denominator[cite: 41].

### **Continuity & Differentiability**
* **Not Differentiable at:** Sharp corners (cusps), vertical tangents, or points of discontinuity[cite: 42].

---

## **3. Differentiation Rules**
Essential for Questions 5, 6, 8, and 9.

### **The Big Rules**
* **Power Rule:** $\frac{d}{dx} [x^n] = nx^{n-1}$[cite: 27].
* **Product Rule:** $(fg)' = f'g + fg'$.
* **Quotient Rule:** $(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$[cite: 29].
* **Chain Rule:** $\frac{d}{dx} [f(g(x))] = f'(g(x)) \cdot g'(x)$[cite: 30, 31].

### **Special Methods**
* **Implicit Differentiation:** Differentiate both sides with respect to $x$; treat $y$ as a function of $x$ and append $\frac{dy}{dx}$ whenever $y$ is differentiated[cite: 35, 36].
* **Differentials (Linearization):** $f(x) \approx f(a) + f'(a)(x - a)$[cite: 37].

---

## **4. Applications of Derivatives**
Essential for Question 3 (Graphing), Question 6 (Tangents), and Question 7 (Related Rates).

### **Tangent & Normal Lines**
* **Slope of Tangent:** $m = f'(x_0)$[cite: 32].
* **Perpendicular (Normal) Slope:** $m_{\perp} = -\frac{1}{m}$[cite: 32].

### **Related Rates Strategy**
1.  **Identify:** List knowns (e.g., $dV/dt = 0.5$) and unknowns (e.g., $dh/dt$)[cite: 33, 34].
2.  **Equation:** Relate variables (e.g., $V = \frac{1}{3}\pi r^2 h$).
3.  **Substitute:** Use given relationships (like $d=h \Rightarrow r=h/2$) to reduce variables[cite: 33].
4.  **Differentiate:** Use the Chain Rule with respect to time ($t$).

### **Function Transformations**
* $f(x+c)$: Shift Left $c$ units[cite: 16].
* $f(x)+c$: Shift Up $c$ units.
* $a f(x)$: Vertical Stretch ($a>1$) or Compression ($a<1$)[cite: 16].

---

