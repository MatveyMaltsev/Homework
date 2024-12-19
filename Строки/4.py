def transform_string(s):
    if len(s) < 4:
        condition = all(char.isupper() for char in s)
    else:
        condition = sum(1 for char in s[:4] if char.isupper()) >= 3

    return s.upper() if condition else s


input_string = input()
result = transform_string(input_string)
print(result)
