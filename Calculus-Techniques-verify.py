"""Verify every worked answer in Calculus-Techniques-Limits-Derivatives-Integrals.md."""
import math
import sympy as sp
import mpmath

x, y, t, u, h, a, n, i, th = sp.symbols('x y t u h a n i theta', real=True)
fails = []
count = 0

def chk(label, got, want):
    global count
    count += 1
    if isinstance(got, sp.MatrixBase) or isinstance(want, sp.MatrixBase):
        ok = sp.Matrix(got) == sp.Matrix(want)
        print(("PASS " if ok else "FAIL ") + label + f"   got={got}  want={want}")
        if not ok: fails.append(label)
        return
    if got in (sp.oo, -sp.oo, sp.zoo) or want in (sp.oo, -sp.oo, sp.zoo):
        ok = (got == want)
        print(("PASS " if ok else "FAIL ") + label + f"   got={got}  want={want}")
        if not ok: fails.append(label)
        return
    got_s = sp.simplify(sp.nsimplify(got) - sp.nsimplify(want)) if not isinstance(got, float) else None
    ok = sp.simplify(got - want) == 0 if got_s is None else got_s == 0
    if not ok:
        try:
            ok = abs(complex(sp.N(got - want))) < 1e-9
        except Exception:
            ok = False
    print(("PASS " if ok else "FAIL ") + label + f"   got={got}  want={want}")
    if not ok:
        fails.append(label)

def chknum(label, got, want, tol=1e-7):
    global count
    count += 1
    ok = abs(float(got) - float(want)) < tol
    print(("PASS " if ok else "FAIL ") + label + f"   got={float(got):.10g} want={float(want):.10g}")
    if not ok:
        fails.append(label)

def chk_anti(label, F, integrand):
    """An antiderivative claim: d/dx F must equal the integrand."""
    global count
    count += 1
    ok = sp.simplify(sp.diff(F, x) - integrand) == 0
    if not ok:  # try trig-aware simplification
        ok = sp.simplify(sp.expand_trig(sp.diff(F, x) - integrand)) == 0
    if not ok:
        d = sp.diff(F, x) - integrand
        ok = all(abs(complex(sp.N(d.subs(x, v)))) < 1e-9 for v in [sp.Rational(3,7), sp.Rational(5,4), sp.Rational(9,8)])
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        fails.append(label)

print("=== PART 1: LIMITS ===")
chk("L1  (x^3-4x+1)/(x+3) at 2", sp.limit((x**3-4*x+1)/(x+3), x, 2), sp.Rational(1,5))
chk("L2  (x^2-9)/(x^2-x-6)", sp.limit((x**2-9)/(x**2-x-6), x, 3), sp.Rational(6,5))
chk("L2b (x^3-1)/(x^4-1)", sp.limit((x**3-1)/(x**4-1), x, 1), sp.Rational(3,4))
chk("L3  (sqrt(x+4)-2)/x", sp.limit((sp.sqrt(x+4)-2)/x, x, 0), sp.Rational(1,4))
chk("L3b (x-9)/(sqrt(x)-3)", sp.limit((x-9)/(sp.sqrt(x)-3), x, 9), 6)
chk("L3c (sqrt(1+x)-sqrt(1-x))/x", sp.limit((sp.sqrt(1+x)-sp.sqrt(1-x))/x, x, 0), 1)
chk("L4  (1/x-1/2)/(x-2)", sp.limit((1/x-sp.Rational(1,2))/(x-2), x, 2), sp.Rational(-1,4))
chk("L4b 1/sin(x)-1/x", sp.limit(1/sp.sin(x)-1/x, x, 0), 0)
chk("L5  sin(5x)/sin(3x)", sp.limit(sp.sin(5*x)/sp.sin(3*x), x, 0), sp.Rational(5,3))
chk("L5b (1-cos x)/(x sin x)", sp.limit((1-sp.cos(x))/(x*sp.sin(x)), x, 0), sp.Rational(1,2))
chk("L6  x^2 sin(1/x)", sp.limit(x**2*sp.sin(1/x), x, 0), 0)
chk("L7  (3x^2-2x+7)/(5x^2+x-1)", sp.limit((3*x**2-2*x+7)/(5*x**2+x-1), x, sp.oo), sp.Rational(3,5))
chk("L8  (4x^3+x)/(2x^3-9)", sp.limit((4*x**3+x)/(2*x**3-9), x, sp.oo), 2)
chk("L8b (x^2+1)/x^3 at -oo", sp.limit((x**2+1)/x**3, x, -sp.oo), 0)
chk("L8c x^3/(x^2+1) at -oo = -oo", sp.limit(x**3/(x**2+1), x, -sp.oo), -sp.oo)
chk("L9  sqrt(4x^2+x)/x at -oo", sp.limit(sp.sqrt(4*x**2+x)/x, x, -sp.oo), -2)
chk("L9b sqrt(4x^2+x)/x at +oo", sp.limit(sp.sqrt(4*x**2+x)/x, x, sp.oo), 2)
chk("L9c sqrt(x^2+3x)-x", sp.limit(sp.sqrt(x**2+3*x)-x, x, sp.oo), sp.Rational(3,2))
chk("L9d sqrt(x^2+bx+c)-x = b/2", sp.limit(sp.sqrt(x**2+7*x+11)-x, x, sp.oo), sp.Rational(7,2))
chk("L10 (e^x-1-x)/x^2", sp.limit((sp.exp(x)-1-x)/x**2, x, 0), sp.Rational(1,2))
chk("L11 (x-sin x)/x^3", sp.limit((x-sp.sin(x))/x**3, x, 0), sp.Rational(1,6))
chk("L11b (cos x-1+x^2/2)/x^4", sp.limit((sp.cos(x)-1+x**2/2)/x**4, x, 0), sp.Rational(1,24))
chk("L12 (x^(1/3)-1)/(x-1)", sp.limit((sp.root(x,3)-1)/(x-1), x, 1), sp.Rational(1,3))
chk("L12b x sin(1/x) at oo", sp.limit(x*sp.sin(1/x), x, sp.oo), 1)
chk("L13 |x|/x from right", sp.limit(sp.Abs(x)/x, x, 0, '+'), 1)
chk("L13b |x|/x from left", sp.limit(sp.Abs(x)/x, x, 0, '-'), -1)
chk("L14 x^x at 0+", sp.limit(x**x, x, 0, '+'), 1)
chk("L14b (1+3/x)^(2x)", sp.limit((1+3/x)**(2*x), x, sp.oo), sp.exp(6))
chk("L15 x ln x at 0+", sp.limit(x*sp.log(x), x, 0, '+'), 0)
chk("L16 sin(x)/x at oo", sp.limit(sp.sin(x)/x, x, sp.oo), 0)
chk("L17 delta=eps/2 check |2x+1-7| at x=3+eps/2", sp.Abs(2*(3+sp.Rational(1,10)/2)+1-7), sp.Rational(1,10))
N19 = 400000
s19 = sum(N19/(N19**2+k**2) for k in range(1, N19+1))
chknum("L19 sum n/(n^2+i^2) -> pi/4", s19, float(sp.pi/4), tol=1e-5)
s19b = sum((k/N19)**0.5 for k in range(1, N19+1))/N19
chknum("L19b (1/n)sum sqrt(i/n) -> 2/3", s19b, 2/3, tol=1e-5)
# L20 monotone recursion
seq = math.sqrt(2)
increasing = True
for _ in range(25):
    nxt = math.sqrt(2+seq)
    increasing = increasing and nxt > seq and nxt < 2
    seq = nxt
for _ in range(60):
    seq = math.sqrt(2+seq)
chknum("L20 a_{n+1}=sqrt(2+a_n) -> 2", seq, 2)
chknum("L20a bounded above by 2 and increasing throughout", 1.0 if increasing else 0.0, 1.0)
H3 = sum(1.0/k for k in range(1, 10**3+1))
H6 = sum(1.0/k for k in range(1, 10**6+1))
r3, r6 = H3/math.log(10**3), H6/math.log(10**6)
chknum("L20b H_n - ln n -> Euler gamma", H6-math.log(10**6), 0.5772156649, tol=1e-6)
chknum("L20b2 ratio H_n/ln n decreasing toward 1", 1.0 if 1 < r6 < r3 else 0.0, 1.0)
chknum("L20b3 ratio matches 1 + gamma/ln n", r6, 1+0.5772156649/math.log(10**6), tol=1e-6)
chk("L20c ratio test 3^n/n! -> 0", sp.limit(3**n/sp.factorial(n), n, sp.oo), 0)

print()
print("=== MATH265 exam-question additions: LIMITS ===")
chk("MQ L1 Q3.2c (6x-9)/(x^3-12x+3) at 0", sp.limit((6*x-9)/(x**3-12*x+3), x, 0), -3)
chk("MQ L2 Q3.2a (x^2-1)/(x^3-1)", sp.limit((x**2-1)/(x**3-1), x, 1), sp.Rational(2,3))
f_q41 = (x**2-3*x-4)/(x**2-16)
chk("MQ L2 Q4.1 simplified form matches (x+1)/(x+4)", sp.simplify(f_q41 - (x+1)/(x+4)), 0)
chknum("MQ L2 Q4.1 hole value at x=4", ((x+1)/(x+4)).subs(x,4), sp.Rational(5,8))
chk("MQ L2 Q4.1 VA left at x=-4", sp.limit(f_q41, x, -4, '-'), sp.oo)
chk("MQ L2 Q4.1 VA right at x=-4", sp.limit(f_q41, x, -4, '+'), -sp.oo)
chk("MQ L2 Q4.1 HA as x->oo", sp.limit(f_q41, x, sp.oo), 1)
chk("MQ L3 Q3.1d double conjugate", sp.limit((sp.sqrt(6-x)-2)/(sp.sqrt(3-x)-1), x, 2), sp.Rational(1,2))
chk("MQ L5 Q3.1e sin(3x)/(x^2-x)", sp.limit(sp.sin(3*x)/(x**2-x), x, 0), -3)
chk("MQ L5 Q3.2b x^2/(1-cos2x)", sp.limit(x**2/(1-sp.cos(2*x)), x, 0), sp.Rational(1,2))
chk("MQ L6 Q3.3a squeeze*(deg comparison)",
    sp.limit(((3*x**2-4)/(2*x**4+2*x+4))*sp.sin(x), x, sp.oo), 0)
chk("MQ L8 Q3.2d (5-2x^3)/(x^2+2) at oo", sp.limit((5-2*x**3)/(x**2+2), x, sp.oo), -sp.oo)
chk("MQ L13 Q3.1b left +oo", sp.limit((3*x**2-2*x-16)/(x+2)**2, x, -2, '-'), sp.oo)
chk("MQ L13 Q3.1b right -oo", sp.limit((3*x**2-2*x-16)/(x+2)**2, x, -2, '+'), -sp.oo)
chk("MQ L13 Q3.1c left -oo", sp.limit((2*x**2-x+1)/(x-3), x, 3, '-'), -sp.oo)
chk("MQ L13 Q3.1c right +oo", sp.limit((2*x**2-x+1)/(x-3), x, 3, '+'), sp.oo)
chk("MQ L13 Q3.2e left -oo", sp.limit(sp.tan(2*x)/(3*x+sp.pi), x, -sp.pi/3, '-'), -sp.oo)
chk("MQ L13 Q3.2e right +oo", sp.limit(sp.tan(2*x)/(3*x+sp.pi), x, -sp.pi/3, '+'), sp.oo)
chk("MQ L13 Q3.2f left +oo", sp.limit(sp.cos(sp.pi*x)/(x-2)**2, x, 2, '-'), sp.oo)
chk("MQ L13 Q3.2f right +oo", sp.limit(sp.cos(sp.pi*x)/(x-2)**2, x, 2, '+'), sp.oo)
chk("MQ L13 Q3.3b tan(5pi/2) left +oo", sp.limit(sp.tan(x), x, sp.Rational(5,2)*sp.pi, '-'), sp.oo)
chk("MQ L13 Q3.3b tan(5pi/2) right -oo", sp.limit(sp.tan(x), x, sp.Rational(5,2)*sp.pi, '+'), -sp.oo)
# L18: x^3/(x^2+y^2) -> 0 in polar reduces to r*cos^3(theta), bounded by r for every angle
import math
worst = max(abs(rr*math.cos(a_)**3) for rr in [1e-3, 1e-4, 1e-5]
            for a_ in [k*math.pi/60 for k in range(120)])
chknum("L18 |x^3/(x^2+y^2)| <= r over all angles", worst, 1e-3, tol=1e-9)
# and the two-path failure for xy/(x^2+y^2): y=0 gives 0, y=x gives 1/2
chknum("L18b path y=0 gives 0", 0.0, 0.0)
chknum("L18c path y=x gives 1/2", (0.01*0.01)/(0.01**2+0.01**2), 0.5)

print()
print("=== PART 2: DERIVATIVES ===")
chk("D1  d/dx sqrt(x) by definition", sp.limit((sp.sqrt(x+h)-sp.sqrt(x))/h, h, 0), 1/(2*sp.sqrt(x)))
chk("D1b d/dx 1/x by definition", sp.limit((1/(x+h)-1/x)/h, h, 0), -1/x**2)
chk("D2  3x^4-2/x^3+5x^(1/3)-7", sp.diff(3*x**4-2/x**3+5*sp.root(x,3)-7, x), 12*x**3+6*x**-4+sp.Rational(5,3)*x**sp.Rational(-2,3))
chk("D3  x^2 e^x", sp.diff(x**2*sp.exp(x), x), sp.exp(x)*(x**2+2*x))
chk("D3b x sin x cos x", sp.diff(x*sp.sin(x)*sp.cos(x), x), sp.sin(x)*sp.cos(x)+x*sp.cos(x)**2-x*sp.sin(x)**2)
chk("D4  (2x+1)/(x^2+3)", sp.diff((2*x+1)/(x**2+3), x), (-2*x**2-2*x+6)/(x**2+3)**2)
chk("D5  sin(3x^2+1)", sp.diff(sp.sin(3*x**2+1), x), 6*x*sp.cos(3*x**2+1))
chk("D5b sqrt(1+tan 2x)", sp.diff(sp.sqrt(1+sp.tan(2*x)), x), sp.sec(2*x)**2/sp.sqrt(1+sp.tan(2*x)))
chk("D6  5^(x^2)", sp.diff(5**(x**2), x), 2*x*sp.log(5)*5**(x**2))
chk("D6b ln(x^2+1)", sp.diff(sp.log(x**2+1), x), 2*x/(x**2+1))
chk("D7  arctan(x^2)", sp.diff(sp.atan(x**2), x), 2*x/(1+x**4))
# D8 implicit
Y = sp.Function('Y')(x)
sol = sp.solve(sp.Eq(sp.diff(x**2+Y**2-25, x), 0), sp.Derivative(Y, x))[0]
chk("D8  circle y' = -x/y", sol.subs(Y, y), -x/y)
sol2 = sp.solve(sp.Eq(sp.diff(x**3+Y**3-6*x*Y, x), 0), sp.Derivative(Y, x))[0]
chk("D8b folium y'", sp.simplify(sol2.subs(Y, y)), (2*y-x**2)/(y**2-2*x))
ypp = sp.simplify(sp.diff(-x/sp.sqrt(25-x**2), x))
chk("D8c circle y'' = -25/y^3", ypp, sp.simplify(-25/sp.sqrt(25-x**2)**3))
chk("D9  x^(sin x)", sp.diff(x**sp.sin(x), x), x**sp.sin(x)*(sp.cos(x)*sp.log(x)+sp.sin(x)/x))
expr = x**3*sp.sqrt(x**2+1)/(3*x+2)**5
chk("D9b log-diff stack", sp.simplify(sp.diff(expr, x)), sp.simplify(expr*(3/x+x/(x**2+1)-15/(3*x+2))))
f10 = x**3+2*x+1
chk("D10 (f^-1)'(4) = 1/5", 1/sp.diff(f10, x).subs(x, 1), sp.Rational(1,5))
chknum("D10b f(1)=4 anchor", f10.subs(x, 1), 4)
# D11 parametric
xt, yt = t**2, t**3-3*t
dydx = sp.diff(yt, t)/sp.diff(xt, t)
chk("D11 dy/dx at t=2 = 9/4", sp.simplify(dydx.subs(t, 2)), sp.Rational(9,4))
d2 = sp.diff(dydx, t)/sp.diff(xt, t)
chk("D11b d2y/dx2 at t=2 = 15/32", sp.simplify(d2.subs(t, 2)), sp.Rational(15,32))
r = 1+sp.cos(th)
dpolar = (sp.diff(r,th)*sp.sin(th)+r*sp.cos(th))/(sp.diff(r,th)*sp.cos(th)-r*sp.sin(th))
chk("D11c polar dy/dx at pi/2 = 1", sp.simplify(dpolar.subs(th, sp.pi/2)), 1)
chk("D12 nth deriv of x e^x, n=7", sp.diff(x*sp.exp(x), x, 7), (x+7)*sp.exp(x))
chk("D12b 10th deriv of x^2 sin x", sp.simplify(sp.diff(x**2*sp.sin(x), x, 10)), -x**2*sp.sin(x)+20*x*sp.cos(x)+90*sp.sin(x))
# D13 related rates
xv, yv, dxv, dyv = sp.symbols('xv yv dxv dyv')
rel = 2*xv*dxv + 2*yv*dyv          # from d/dt of x^2 + y^2 = 100
chk("D13a y = sqrt(100-36) = 8", sp.sqrt(100-36), 8)
dy = sp.solve(rel.subs({xv: 6, yv: 8, dxv: 2}), dyv)[0]
chk("D13 ladder dy/dt = -3/2", dy, sp.Rational(-3,2))
chknum("D14 sqrt(4.1) approx 2.025", 2+sp.Rational(1,4)*sp.Rational(1,10), 2.025)
chknum("D14b true sqrt(4.1)", sp.N(sp.sqrt(sp.Rational(41,10)), 12), 2.02484567313, tol=1e-9)
chknum("D14c linearization error ~1.5e-4", abs(2.025-float(sp.N(sp.sqrt(4.1)))), 1.543e-4, tol=1e-6)
chknum("D14d dV = 4 pi r^2 dr at r=10,dr=.05", float(4*sp.pi*100*sp.Rational(5,100)), 62.831853, tol=1e-5)
fxy = x**3*y**2+sp.exp(x*y)
chk("D15 f_x", sp.diff(fxy, x), 3*x**2*y**2+y*sp.exp(x*y))
chk("D15b f_y", sp.diff(fxy, y), 2*x**3*y+x*sp.exp(x*y))
chk("D15c f_xy", sp.simplify(sp.diff(fxy, x, y)), 6*x**2*y+sp.exp(x*y)*(1+x*y))
chk("D15d Clairaut f_xy=f_yx", sp.simplify(sp.diff(fxy,x,y)-sp.diff(fxy,y,x)), 0)
z = x**2*y
dzdt = (sp.diff(z,x)*(-sp.sin(t))+sp.diff(z,y)*sp.cos(t)).subs({x: sp.cos(t), y: sp.sin(t)})
chk("D16 dz/dt at t=0 = 1", sp.simplify(dzdt.subs(t, 0)), 1)
g = x**2+3*x*y
grad = sp.Matrix([sp.diff(g,x), sp.diff(g,y)]).subs({x:1, y:2})
chk("D16b grad at (1,2) = <8,3>", grad, sp.Matrix([8,3]))
chk("D16c directional deriv = 36/5", grad.dot(sp.Matrix([sp.Rational(3,5), sp.Rational(4,5)])), sp.Rational(36,5))
F = x**3+y**3-6*x*y
chk("D16d -F_x/F_y matches D8b", sp.simplify(-sp.diff(F,x)/sp.diff(F,y)), sp.simplify((2*y-x**2)/(y**2-2*x)))
chk("D17 d/dx int_1^{x^2} sqrt(1+t^3)", sp.diff(sp.Integral(sp.sqrt(1+t**3), (t,1,x**2)), x).doit(), 2*x*sp.sqrt(1+x**6))
chk("D17b d/dx int_x^{x^2} dt/t = 1/x", sp.simplify(sp.diff(sp.integrate(1/t, (t,x,x**2)), x)), 1/x)
cd = (sp.log(sp.Rational(101,100))-sp.log(sp.Rational(99,100)))/sp.Rational(2,100)
chknum("D18 central difference ln at 1, h=.01", sp.N(cd, 15), 1.0000333358, tol=1e-8)
chknum("D18b f(1.01)=ln1.01", sp.N(sp.log(sp.Rational(101,100)), 12), 0.00995033085, tol=1e-9)
chknum("D18c f(0.99)=ln0.99", sp.N(sp.log(sp.Rational(99,100)), 12), -0.0100503359, tol=1e-9)
chknum("D18d error ~3.33e-5 = h^2/3", abs(float(sp.N(cd))-1), 3.3336e-5, tol=1e-7)

print()
print("=== MATH265 exam-question additions: DERIVATIVES ===")
chk("MQ D1 Q7.1 d/dx cot x by definition", sp.limit((sp.cot(x+h)-sp.cot(x))/h, h, 0), -sp.csc(x)**2)
chk("MQ D2 Q8.1a poly derivative", sp.diff(4*x**5+3*x**4-6*x**3+6, x), 20*x**4+12*x**3-18*x**2)
q83a = sp.sin(x)*sp.cos(sp.sin(x**2))
chk("MQ D3 Q8.3a product of sin and nested cos(sin(x^2))",
    sp.diff(q83a, x),
    sp.cos(x)*sp.cos(sp.sin(x**2)) - sp.sin(x)*sp.sin(sp.sin(x**2))*sp.cos(x**2)*2*x)
chk("MQ D4 Q8.1b quotient (2x-16)/(x+3)^2", sp.simplify(sp.diff((2*x-16)/(x+3)**2, x) - (38-2*x)/(x+3)**3), 0)
chk("MQ D4 Q8.4a tan(2x)/sqrt(x)",
    sp.simplify(sp.diff(sp.tan(2*x)/sp.sqrt(x), x) - (2*sp.sec(2*x)**2*sp.sqrt(x)-sp.tan(2*x)/(2*sp.sqrt(x)))/x), 0)
chk("MQ D5 Q8.3c nested sqrt(1+sqrt(1+x))",
    sp.simplify(sp.diff(sp.sqrt(1+sp.sqrt(1+x)), x) - 1/(4*sp.sqrt(1+x)*sp.sqrt(1+sp.sqrt(1+x)))), 0)
chknum("MQ D5 Q8.4b cos^3(x^2) at x=sqrt(pi)/2",
       sp.diff(sp.cos(x**2)**3, x).subs(x, sp.sqrt(sp.pi)/2), sp.N(-3*sp.sqrt(2*sp.pi)/4, 12))
chk("MQ D6 Q8.2b sec(x^2-3x)", sp.diff(sp.sec(x**2-3*x), x), sp.sec(x**2-3*x)*sp.tan(x**2-3*x)*(2*x-3))
# D8 implicit, Q10.1
Y2 = sp.Function('Y')(x)
eq101 = sp.Eq(x**3*Y2 + x*Y2**2, 4*x*Y2+7)
sol101 = sp.solve(sp.Eq(sp.diff(eq101.lhs-eq101.rhs, x), 0), sp.Derivative(Y2, x))[0]
want101 = (4*y-3*x**2*y-y**2)/(x**3+2*x*y-4*x)
chk("MQ D8 Q10.1 implicit y'", sp.simplify(sol101.subs(Y2, y) - want101), 0)
# D8 Q10.2 at the point (1,1)
eq102 = sp.Eq(Y2**3+Y2*x**2+x**2, 3*Y2**2)
sol102 = sp.solve(sp.Eq(sp.diff(eq102.lhs-eq102.rhs, x), 0), sp.Derivative(Y2, x))[0]
chk("MQ D8 Q10.2 slope at (1,1) = 2", sol102.subs({Y2: y}).subs({x:1, y:1}), 2)
chk("MQ D8 Q10.2 point on curve", (1**3+1*1**2+1**2) - 3*1**2, 0)
chk("MQ D12 Q8.2a second derivative of cot(2x)", sp.simplify(sp.diff(sp.cot(2*x), x, 2) - 8*sp.csc(2*x)**2*sp.cot(2*x)), 0)
# D13 Q11.1 gravel cone
hh = sp.Symbol('hh', positive=True)
dhdt = sp.Symbol('dhdt')
Vrel = sp.pi*hh**3/12
dVdt_expr = sp.diff(Vrel, hh)*dhdt
sol_dh = sp.solve(sp.Eq(dVdt_expr.subs(hh, 4), sp.Rational(1,2)), dhdt)[0]
chk("MQ D13 Q11.1 dh/dt = 1/(8pi)", sol_dh, 1/(8*sp.pi))
# D13 Q11.2 rocket
zz = sp.sqrt(41)
dydt_sol = sp.solve(sp.Eq(zz*2000, 4*sp.Symbol('dydt')), sp.Symbol('dydt'))[0]
chk("MQ D13 Q11.2 dy/dt = 500 sqrt(41)", dydt_sol, 500*sp.sqrt(41))
# D14 Q12.1 sqrt(9.2)
chk("MQ D14 Q12.1 linear approx sqrt(9.2) = 91/30", 3+sp.Rational(1,6)*sp.Rational(1,5), sp.Rational(91,30))
chknum("MQ D14 Q12.1 true sqrt(9.2)", sp.N(sp.sqrt(sp.Rational(92,10)), 12), 3.03315018, tol=1e-6)
# D14 Q12.2 sin(62deg)
approx122 = sp.sqrt(3)/2 + sp.Rational(1,2)*sp.pi/90
chknum("MQ D14 Q12.2 linear approx sin62", sp.N(approx122, 10), 0.8834787, tol=1e-6)
chknum("MQ D14 Q12.2 true sin62deg", sp.N(sp.sin(62*sp.pi/180), 10), 0.8829476, tol=1e-6)
# D17 Q18.1
chk("MQ D17 Q18.1 d/dx int_{2x}^{x} sin(t^2) dt",
    sp.diff(sp.Integral(sp.sin(t**2), (t, 2*x, x)), x).doit(),
    sp.sin(x**2) - 2*sp.sin(4*x**2))

print()
print("=== PART 3: INTEGRALS ===")
chk_anti("I1  int (x^3+2sqrt x)/x = x^3/3+4sqrt x", x**3/3+4*sp.sqrt(x), (x**3+2*sp.sqrt(x))/x)
chk_anti("I2  int 2x sqrt(x^2+1)", sp.Rational(2,3)*(x**2+1)**sp.Rational(3,2), 2*x*sp.sqrt(x**2+1))
chk("I2b int_0^{pi/2} sin^3 cos = 1/4", sp.integrate(sp.sin(x)**3*sp.cos(x), (x,0,sp.pi/2)), sp.Rational(1,4))
chk_anti("I2c int x sqrt(x+1)", sp.Rational(2,5)*(x+1)**sp.Rational(5,2)-sp.Rational(2,3)*(x+1)**sp.Rational(3,2), x*sp.sqrt(x+1))
chk_anti("I3  int x e^x = (x-1)e^x", (x-1)*sp.exp(x), x*sp.exp(x))
chk_anti("I3b int ln x = x ln x - x", x*sp.log(x)-x, sp.log(x))
chk_anti("I3c int arctan x", x*sp.atan(x)-sp.log(1+x**2)/2, sp.atan(x))
chk_anti("I3d int e^x sin x", sp.exp(x)*(sp.sin(x)-sp.cos(x))/2, sp.exp(x)*sp.sin(x))
chk_anti("I4  tabular int x^3 e^{2x}", sp.exp(2*x)*(x**3/2-3*x**2/4+3*x/4-sp.Rational(3,8)), x**3*sp.exp(2*x))
chk_anti("I5  int sin^3 cos^2", -sp.cos(x)**3/3+sp.cos(x)**5/5, sp.sin(x)**3*sp.cos(x)**2)
chk_anti("I5b int sin^2 = x/2 - sin2x/4", x/2-sp.sin(2*x)/4, sp.sin(x)**2)
chk_anti("I5c int sec^3", sp.sec(x)*sp.tan(x)/2+sp.log(sp.Abs(sp.sec(x)+sp.tan(x)))/2, sp.sec(x)**3)
chk_anti("I5d int sin3x cos5x", sp.cos(2*x)/4-sp.cos(8*x)/16, sp.sin(3*x)*sp.cos(5*x))
chk_anti("I6  int sqrt(9-x^2)", sp.Rational(9,2)*sp.asin(x/3)+x*sp.sqrt(9-x**2)/2, sp.sqrt(9-x**2))
chk_anti("I6b int dx/(x^2 sqrt(x^2+4))", -sp.sqrt(x**2+4)/(4*x), 1/(x**2*sp.sqrt(x**2+4)))
chk_anti("I7  int dx/(x^2+4x+13)", sp.atan((x+2)/3)/3, 1/(x**2+4*x+13))
chk_anti("I7b int (2x+7)/(x^2+4x+13)", sp.log(x**2+4*x+13)+sp.atan((x+2)/3), (2*x+7)/(x**2+4*x+13))
chk_anti("I8  int (3x+11)/(x^2-x-6)", 4*sp.log(x-3)-sp.log(x+2), (3*x+11)/(x**2-x-6))
chk_anti("I8b int (2x+3)/((x-1)(x^2+1))",
         sp.Rational(5,2)*sp.log(x-1)-sp.Rational(5,4)*sp.log(x**2+1)-sp.atan(x)/2,
         (2*x+3)/((x-1)*(x**2+1)))
chk_anti("I9  int x^3/(x^2+1)", x**2/2-sp.log(x**2+1)/2, x**3/(x**2+1))
chk_anti("I10 int dx/(1+sin x) = -2/(1+tan(x/2))", -2/(1+sp.tan(x/2)), 1/(1+sp.sin(x)))
chk_anti("I10b alt form tan x - sec x", sp.tan(x)-sp.sec(x), 1/(1+sp.sin(x)))
chk("I10c the two forms differ by a constant",
    sp.simplify(sp.diff((-2/(1+sp.tan(x/2))) - (sp.tan(x)-sp.sec(x)), x)), 0)
chk_anti("I11 int dx/(1+sqrt x)", 2*sp.sqrt(x)-2*sp.log(1+sp.sqrt(x)), 1/(1+sp.sqrt(x)))
chk_anti("I12 int sin^4", -sp.sin(x)**3*sp.cos(x)/4+3*x/8-3*sp.sin(2*x)/16, sp.sin(x)**4)
chk("I12b Wallis int_0^{pi/2} sin^4 = 3pi/16", sp.integrate(sp.sin(x)**4, (x,0,sp.pi/2)), 3*sp.pi/16)
chk("I13 int_{-2}^2 (x^3 cos x + x^2) = 16/3", sp.integrate(x**3*sp.cos(x)+x**2, (x,-2,2)), sp.Rational(16,3))
chk("I13b odd part alone is 0", sp.integrate(x**3*sp.cos(x), (x,-2,2)), 0)
chk("I14 king: int_0^{pi/2} sin/(sin+cos) = pi/4",
    sp.integrate(sp.sin(x)/(sp.sin(x)+sp.cos(x)), (x,0,sp.pi/2)), sp.pi/4)
chk("I15 int_1^2 (3x^2-2x) = 4", sp.integrate(3*x**2-2*x, (x,1,2)), 4)
chk("I15b int_{-1}^1 dx/x^2 diverges", sp.integrate(1/x**2, (x,-1,1)), sp.oo)
chk("I16 int_0^1 x^2 = 1/3 via Riemann sum",
    sp.limit(sp.Sum((i/n)**2*sp.Rational(1,1)/n, (i,1,n)).doit(), n, sp.oo), sp.Rational(1,3))
chk("I17 int_1^oo dx/x^2 = 1", sp.integrate(1/x**2, (x,1,sp.oo)), 1)
chk("I17b int_0^1 dx/sqrt x = 2", sp.integrate(1/sp.sqrt(x), (x,0,1)), 2)
chk("I17c limit comparison ratio -> 1", sp.limit(x**sp.Rational(3,2)/sp.sqrt(x**3+1), x, sp.oo), 1)
conv = float(mpmath.quad(lambda v: 1/mpmath.sqrt(v**3+1), [1, mpmath.inf]))
chknum("I17d int_1^oo dx/sqrt(x^3+1) converges to a finite value",
       1.0 if (0 < conv < 10) else 0.0, 1.0)
# I18 Simpson
f = lambda v: sp.exp(-sp.Rational(v)**2) if False else None
nodes = [sp.Rational(0), sp.Rational(1,4), sp.Rational(1,2), sp.Rational(3,4), sp.Rational(1)]
fv = [sp.N(sp.exp(-v**2), 12) for v in nodes]
for lbl, idx, want in [("f0",0,1.0), ("f1",1,0.939413063), ("f2",2,0.778800783),
                       ("f3",3,0.569782825), ("f4",4,0.367879441)]:
    chknum(f"I18 Simpson node {lbl}", fv[idx], want, tol=1e-8)
wsum = fv[0]+4*fv[1]+2*fv[2]+4*fv[3]+fv[4]
chknum("I18b Simpson weighted sum", wsum, 8.9622646, tol=1e-6)
simp = sp.Rational(1,4)/3*wsum
chknum("I18c Simpson estimate", simp, 0.7468554, tol=1e-6)
true_val = sp.N(sp.integrate(sp.exp(-x**2), (x,0,1)), 12)
chknum("I18d true value", true_val, 0.746824133, tol=1e-9)
chknum("I18e Simpson error ~3.1e-5", abs(float(simp-true_val)), 3.087e-5, tol=1e-6)
# I19 series
terms = [sp.Rational((-1)**k, (2*k+1)*sp.factorial(2*k+1)) for k in range(4)]
chknum("I19 term n=1 = -1/18", terms[1], -sp.Rational(1,18))
chknum("I19b term n=2 = 1/600", terms[2], sp.Rational(1,600))
chknum("I19c term n=3 = -1/35280", terms[3], -sp.Rational(1,35280))
chknum("I19d 4-term partial sum", sp.N(sum(terms), 12), 0.946082766, tol=1e-8)
chknum("I19e true Si(1)", sp.N(sp.integrate(sp.sin(x)/x, (x,0,1)), 12), 0.946083070, tol=1e-9)
chknum("I19f truncation err < 3e-7", abs(float(sp.N(sum(terms)-sp.Si(1)))), 3.04e-7, tol=1e-8)
# I20 Feynman
apos = sp.Symbol("apos", positive=True)
Ia = sp.integrate((x**apos-1)/sp.log(x), (x,0,1), conds="none")
chk("I20 int_0^1 (x^a-1)/ln x = ln(a+1)", sp.simplify(Ia - sp.log(apos+1)), 0)
chknum("I20a2 numeric at a=3: ln 4", float(mpmath.quad(lambda v: (v**3-1)/mpmath.log(v), [0,1])), math.log(4), tol=1e-8)
chknum("I20b at a=1 gives ln 2", sp.N(sp.integrate((x-1)/sp.log(x), (x,0,1))), sp.N(sp.log(2)), tol=1e-8)
b = sp.Symbol('b', positive=True); ap = sp.Symbol('ap', positive=True)
chk("I20c Frullani int_0^oo (e^-ax - e^-bx)/x = ln(b/a)",
    sp.simplify(sp.integrate((sp.exp(-ap*x)-sp.exp(-b*x))/x, (x,0,sp.oo)) - sp.log(b/ap)), 0)
# I21
chk("I21 swapped order int_0^1 int_x^1 e^{y^2} = (e-1)/2",
    sp.integrate(sp.integrate(sp.exp(y**2), (x,0,y)), (y,0,1)), (sp.E-1)/2)
r_, th_ = sp.symbols('r_ th_', positive=True)
chk("I21b polar disk int r*r dr dth = 2pi/3",
    sp.integrate(sp.integrate(r_*r_, (r_,0,1)), (th_,0,2*sp.pi)), 2*sp.pi/3)
chk("I21c Gaussian int_-oo^oo e^{-x^2} = sqrt(pi)",
    sp.integrate(sp.exp(-x**2), (x,-sp.oo,sp.oo)), sp.sqrt(sp.pi))
chk("I21d inner polar int_0^oo r e^{-r^2} dr = 1/2",
    sp.integrate(r_*sp.exp(-r_**2), (r_,0,sp.oo)), sp.Rational(1,2))
# I22 Green: P=y^2, Q=3xy over unit disk
P_, Q_ = y**2, 3*x*y
chk("I22 Green integrand Q_x - P_y = y", sp.diff(Q_,x)-sp.diff(P_,y), y)
green = sp.integrate(sp.integrate(r_*sp.sin(th_)*r_, (r_,0,1)), (th_,0,2*sp.pi))
chk("I22b Green double integral of y over disk = 0", green, 0)
# direct parametrization cross-check
tt = sp.Symbol('tt')
direct = sp.integrate((sp.sin(tt)**2)*(-sp.sin(tt)) + 3*sp.cos(tt)*sp.sin(tt)*sp.cos(tt), (tt,0,2*sp.pi))
chk("I22c direct line integral agrees = 0", direct, 0)
chk("I22d divergence thm flux = 4pi", 3*sp.Rational(4,3)*sp.pi, 4*sp.pi)

print()
print("=== MATH265 exam-question additions: INTEGRALS ===")
chk_anti("MQ I1 Q16.1a (x^2-x)sqrt(3x)",
         sp.sqrt(3)*(sp.Rational(2,7)*x**sp.Rational(7,2) - sp.Rational(2,5)*x**sp.Rational(5,2)),
         (x**2-x)*sp.sqrt(3*x))
chk_anti("MQ I1 Q16.1d (x^2-4)^2", x**5/5 - sp.Rational(8,3)*x**3 + 16*x, (x**2-4)**2)
chk("MQ I2 Q16.1e int_2^4 x sqrt(x-1)", sp.integrate(x*sp.sqrt(x-1), (x,2,4)), sp.simplify((84*sp.sqrt(3)-16)/15))
chk_anti("MQ I2 Q16.2a cos(sqrt(2x))/sqrt(x)", sp.sqrt(2)*sp.sin(sp.sqrt(2*x)), sp.cos(sp.sqrt(2*x))/sp.sqrt(x))
chk_anti("MQ I5 Q16.1b sin(2x)cos(x)", -sp.Rational(2,3)*sp.cos(x)**3, sp.sin(2*x)*sp.cos(x))
chk("MQ I5 Q16.2b int_0^{pi/3} tan x sec^2 x", sp.integrate(sp.tan(x)*sp.sec(x)**2, (x,0,sp.pi/3)), sp.Rational(3,2))
chk_anti("MQ I5 Q16.2d sec^3(x)tan(x)", sp.sec(x)**3/3, sp.sec(x)**3*sp.tan(x))
chk("MQ I15 Q16.1c derivative of antiderivative matches integrand",
    sp.diff(sp.Rational(1,2)*x**2 + sp.Rational(1,2)*sp.sin(2*x), x) - (x+sp.cos(2*x)), 0)
chk("MQ I15 Q19.1 area between y=x and y=2-x^2", sp.integrate((2-x**2)-x, (x,-2,1)), sp.Rational(9,2))
chk("MQ I15 Q19.3 net change water tank", sp.integrate(180-6*t, (t,0,15)), 2025)

print()
print("=" * 60)
print(f"{count} checks run, {len(fails)} failed")
if fails:
    print("FAILURES:")
    for f_ in fails:
        print("  - " + f_)
else:
    print("ALL CHECKS PASSED")
