import latex2sympy2
import csv

test_file_name = 'latex2sympy2_test_cases.csv'

cases = [
    # A broad set of test cases: derivatives, integrals, limits, and edge cases.
    r"\frac{d}{dx} x",
    r"\frac{d}{dx} tx",
    r"\frac{d}{dx} (t x)",
    r"\frac{d}{dt} x",
    r"\frac{d}{dx} [ \tan x ]",
    r"\frac{d f(x)}{dx}",
    r"\frac{d}{dx} \sin x",
    r"\frac{d}{dx} e^{x}",
    r"\frac{d}{dx} x^2",
    r"\frac{\partial}{\partial x} f(x,y)",

    # Multiple derivatives / higher order
    r"\frac{d^2}{dx^2} x^3",
    r"\frac{d}{dx} \frac{d}{dx} x^3",

    # Integrals
    r"\int x dx",
    r"\int x d\theta",
    r"\int (x^2 - y)dx",
    r"\int_a^b x dx",
    r"\int_{a}^{b} \frac{dt}{t}",
    r"\int \frac{dz}{z}",

    # Limits
    r"\lim_{x \to 3} a",
    r"\lim_{x \to \infty} \frac{1}{x}",
    r"\lim_{x \to 0^{+}} \frac{1}{x}",

    # Tricky spacing and grouping
    r"\frac{d}{dx}    ( x  y )",
    r"\frac{d}{dx}x",
    r"d/dx x",  # intentionally malformed to see error handling

    # Edge cases
    r"\frac{d}{dx} 1",
    r"\int^{ }_{ } x dx",
    r"\int_{ }^{ } x dx",
]

# Write header once (overwrite any existing file)
with open(test_file_name, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Raw LaTeX string", "Sympy command", "LaTeX result"])

for c in cases:
    sympy_res = None
    latex_res = None
    try:
        sympy_res = latex2sympy2.latex2sympy(c)
        latex_res = latex2sympy2.latex2latex(c)
    except Exception as e:
        # Put the error text into the result columns so the CSV records failures
        err = f"ERROR: {e}"
        if sympy_res is None:
            sympy_res = err
        if latex_res is None:
            latex_res = err

    print(f'Raw LaTeX string: {c} -> Sympy command: {sympy_res} -> LaTeX result: {latex_res}')

    # Append the result row
    with open(test_file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([c, sympy_res, latex_res])
