'''
Original code:
$ cat factorial.py
#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
    return result

f = factorial(int(sys.argv[1]))
print(f)

$ ./factorial.py 2
^CTraceback (most recent call last):
  File "/private/tmp/factorial.py", line 9, in <module>
    factorial(int(sys.argv[1]))
  File "/private/tmp/factorial.py", line 5, in factorial
    while n > 1:
          ^^^^^
KeyboardInterrupt
'''

'''
It looks like your code has an infinite loop issue. The problem lies in how the factorial() function updates the value of n inside the while loop.

In the while loop, the value of n is never decremented or changed, so the loop will run indefinitely for any input greater than 1. This causes a KeyboardInterrupt because the process is stuck in the loop and cannot exit.

Here’s a corrected version of your factorial() function:
'''
#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n after each iteration
    return result

f = factorial(int(sys.argv[1]))
print(f)
