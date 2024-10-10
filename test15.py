x = 5 
y = x + 3
print(x)
print(y)

x = x + 3       # statement is equal to x += 3 (statement 7)
x += 3          # statement is equal to x = x + 3 (statement 6)
print(x)

x -= 3          # statement is equal to x = x - 3
print(x)

x *= 3          # statement is equal to x = x * 3
print(x)

x /= 3          # statement is equal to x = x / 3
print(x)

x **= 2         # statement is equal to x = x ** 2
print(x)

x = 5
x &= 3          # statement is equal to x = x & 3
print(x)

x = 5           # binary representation of 5 is 0101
x &= 3          # binary representation of 3 is 0011
print(x)        # binary representation of 5 | 3 is 0001 which is 1