from latex2sympy2 import latex2sympy, latex2latex

tex = r' \int_{a}^{b} \frac{dt}{t} '

print(f'raw_tex: {tex}')

sympy_res = latex2sympy(tex)
print(f'sympy_res: {sympy_res}')

latex_res = latex2latex(tex)
print(f'latex_res: {latex_res}')