import random, string
code = ''.join(random.choice(string.ascii_uppercase  + string.digits) for _ in range(8))
print(code)
