x, y = map(str, input().split())
x_chars = list(x)
x_chars[0], x_chars[1] = x_chars[1], x_chars[0]
y_chars = list(y)
y_chars[0], y_chars[1] = y_chars[1], y_chars[0]
x = ''.join(x_chars)
y = ''.join(y_chars)
output = x + "-" + y
print(output)
