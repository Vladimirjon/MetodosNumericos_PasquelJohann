# Implementar el algoritmo y resolver $\frac{1}{4}(x^{3} + 3x^{2} - 6x - 8) = 0$
step = 0.1
roots = []
a = a_range

while a < b_range:
    b = a + step
    if equation(a) * equation(b) < 0:
        root_info = bisection(a, b, equation=equation, tol=tol, N=max_iter)
        if root_info:
            root, *_ = root_info
            if not any(abs(root - r) < tol for r in roots):  
                roots.append(root)
    a = b

x = np.linspace(a_range, b_range, 500)
y = equation(x)

plt.plot(x, y, label=r"$\frac{1}{4}(x^3 + 3x^2 - 6x - 8) = 0$")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of the function with identified roots')
plt.axhline(0, color='black', linewidth=0.5)
plt.scatter(roots, [0] * len(roots), color='red', marker='x', label='Roots')
plt.grid(True)
plt.legend()
plt.show()

len(roots), roots