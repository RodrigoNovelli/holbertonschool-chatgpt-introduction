
It looks like there’s an issue with the indentation in your factorial function. In Python, indentation is critical, and the body of a function or loop should be indented correctly. Specifically, in your code, the return 1 line is not properly indented under the if statement.

Here’s the corrected version of your code:

python
Copiar código
#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1  # Indented correctly
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)