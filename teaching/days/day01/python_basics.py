"""Day 1 Python experiments. Run one section at a time or the whole file.
Predict the output before running; change one thing at a time.
"""
# 1. Output: print displays the values inside its parentheses.
# Quotes enclose a string; single or double quotes work, but must match.
# print writes to the terminal, not automatically to the Pygame window.
print('Hello, Captain!')
print('My name is', 'Alice')  # Commas separate arguments; print puts spaces between them by default.

# 2. Numbers and text have different types.
print(200 + 50)  # Integer addition: prints 250.
print('200' + '50')  # String concatenation: prints 20050.
print(type(200))  # type reports the type: <class 'int'>.
print(type('200'))  # Prints <class 'str'>; quotes make it text.

# 3. Arithmetic: multiply/divide before add/subtract; parentheses go first.
print(2 + 3 * 4)  # 3*4 goes first; the result is 14.
print((2 + 3) * 4)  # Parentheses go first; the result is 20.

# 4. Assignment and updates: evaluate the right side, then store on the left.
x = 200
y = 180
# Use the old x to compute 200+40, then store 240 in x; this is assignment.
x = x + 40
print('Position:', x, y)
# A tuple groups values in order: x first, then y.
position = (x, y)
print(position)

# 5. Conditions: what prints if you change this to score = 0?
score = 10
# >= tests greater than or equal to, returning True or False.
# Indent the block after the colon by 4 spaces; else runs when the condition is false.
if score >= 10:
    print('Hit!')
else:
    print('Keep searching for a target')

# 6. Loops: this example runs once to avoid endless output.
# running is a boolean; another iteration starts only while it is True.
running = True
while running:
    print('This iteration runs once')
    running = False  # Update the condition; no next iteration.
# This unindented line runs after the loop ends.
print('Loop finished')

# Optional extension: define a function, then call it.
# def defines a function; parameters x and y receive values when it is called.
# Defining the function does not run its body yet.
def report_position(x, y):
    print('Ship position:', x, y)

# This is the call: inside this invocation, x=200 and y=180.
report_position(200, 180)

# Optional extension: repeat three times, counting from 0.
# range(3) yields 0, 1, 2; it excludes 3 and runs three times.
for number in range(3):
    print('Preparing ship', number, 'in the fleet')
